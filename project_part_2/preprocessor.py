from sklearn.preprocessing import  MinMaxScaler, StandardScaler
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import KNNImputer

# Get rid of future deprecation warning
pd.set_option('future.no_silent_downcasting', True)

class Preprocessor:
    '''Preprocessor class for the Heart Disease dataset: https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset'''

    def get_raw_data(self):
        '''Get the full raw, unhandled data set
        
        Returns
        -------
        pandas.DataFrame
            raw dataframe from ./hearts.csv
        '''
        return pd.read_csv("heart.csv")
    

    def get_data(self, 
                 test_size=0.25, 
                 random_state=42, 
                 impute_method='knn', 
                 remove_outliers=True, 
                 scaling_method=None
        ):
        '''Prepare data for preprocessing
        
        Parameters
        ----------
        test_size : float
            Proportion of data to be used as test set. If `test_size` is outside of the range [0,1], the entire dataset is returned
        random_state : int
            Random state to be used as random seed. Defaults to 42.
        impute_method : str
            Method to impute the zero-values of `Cholesterol`; 'knn' or 'median'. Defaults to 'knn'.
        remove_outliers : bool
            Should remove outliers. 
        scaling

        Returns
        -------
        np.ndArray
            Prepared training data.
        np.ndArray
            Prepared test data. If test_size is out of range, returns `None`.
        '''
        data = self.get_raw_data()

        # Transform categorical features
        data = self.__transform_objects(data)

        # Impute the zero-values of cholesterol
        data = self.__impute_cholesterol(data, impute_method)

        # Remove outliers
        if (remove_outliers):         
            data = self.__remove_outliers(data)            

        # Set scaler
        if (scaling_method == None):
            self.scaler = None
        elif (scaling_method.lower() == 'standard'):
            self.scaler = StandardScaler()
        else:
            self.scaler = MinMaxScaler()

        # Split target from features
        y = data['HeartDisease']
        X = data.drop('HeartDisease', axis=1)

        # If test_size is out of range the data should not be split
        if (test_size < 0 or test_size > 1):

            if (self.scaler == None):
                X_train = X
            else:
                # Scale data
                X_train = self.scaler.fit_transform(X)
                X_train = pd.DataFrame(data=X_train, columns=X.columns)

            X_test = None
            y_train = y
            y_test = None
        
        else:
            # Split into train and test
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
            
            if (self.scaler == None):
                X_train = X_train
                X_test = X_test

            else:
                # Scale data
                X_train = self.scaler.fit_transform(X_train)
                X_test = self.scaler.transform(X_test)

                X_train = pd.DataFrame(data=X_train, columns=X.columns) 
                X_test = pd.DataFrame(data=X_test, columns=X.columns) 

        return X_train, X_test, y_train, y_test
    

    def get_scaler(self):
        if (self.scaler == None):
            raise AttributeError('Scaler not initialized')
        return self.scaler
    

    def __transform_objects(self, df):
        # Transform numerical
        if ('Sex' in df.columns.tolist()):
            df['Sex'] = df['Sex'].replace({'F': 0, 'M': 1})
            df['Sex'] = df['Sex'].astype('int')
        
        if ('ExerciseAngina' in df.columns.tolist()):
            df['ExerciseAngina'] = df['ExerciseAngina'].replace({'Y': 0, 'N': 1}).astype('int')
        
        if ('ST_Slope' in df.columns.tolist()):
            df['ST_Slope'] = df['ST_Slope'].replace({'Down': 0, 'Flat': 1, 'Up': 2}).astype('int')

        # Apply one-hot encoding
        df = pd.get_dummies(df, columns=['ChestPainType', 'RestingECG'], dtype='int')
        
        return df


    def __IQR_bounds(self, df, column, lower_quantile=0.25, upper_quantile=0.75, should_print=True):
        Q1, Q3 = df[column].quantile([lower_quantile, upper_quantile])

        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        low_outliers = (df[column] < lower_bound).sum()
        high_outliers = (df[column] > upper_bound).sum()

        if should_print:
            print(f'{column} has {low_outliers} low outliers (below {lower_bound}) and {high_outliers} high outliers (above {upper_bound})')

        return lower_bound, upper_bound


    def __remove_outliers(self, df):
        # Find lower and upper bound for RestingBP, and remove
        restingbp_lower, restingbp_upper = self.__IQR_bounds(df, 'RestingBP', should_print=True)
        df = df[(df['RestingBP'] >= restingbp_lower) & (df['RestingBP'] <= restingbp_upper)]
        
        # Find upper bound for Cholesterol, and remove
        _, cholesterol_upper = self.__IQR_bounds(df, 'Cholesterol', should_print=True)
        df = df[(df['Cholesterol'] <= cholesterol_upper)]
        
        # Find lower and upper bound for MaxHR, and remove
        maxhr_lower, maxhr_upper = self.__IQR_bounds(df, 'MaxHR', should_print=True)
        df = df[(df['MaxHR'] >= maxhr_lower) & (df['MaxHR'] <= maxhr_upper)]
        
        # Find lower and upper bound for Oldpeak, and remove
        oldpeak_lower, oldpeak_upper = self.__IQR_bounds(df, 'Oldpeak', should_print=True)
        df = df[(df['Oldpeak'] >= oldpeak_lower) & (df['Oldpeak'] <= oldpeak_upper)]
        
        return df


    def __impute_cholesterol(self, df, method):
        column = 'Cholesterol'
        if (method == None):
            method == 'knn'

        if (method.lower() == 'median'):
            median = df[column].median()
            df[column] = df[column].replace(to_replace=0, value=median)

        else:
            imputer = KNNImputer(missing_values=0)
            imputed = imputer.fit_transform(df)
            imputed_df = pd.DataFrame(imputed, columns=df.columns)
            df[column] = imputed_df[column]
        
        return df
    
