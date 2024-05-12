from sklearn.preprocessing import  MinMaxScaler
import pandas as pd
from sklearn.model_selection import train_test_split

class Preprocessor:
    '''Preprocessor class for the customer dataset
    '''

    def __init__(self):
        self.scaler = MinMaxScaler()

    def get_raw_data(self):
        '''Get the full raw, unhandled data set
        
        Returns
        -------
        pandas.DataFrame
            raw dataframe retrieved from `ucimlrepo` library
        '''
        return pd.read_csv("customer_data_large.csv")
    
    def get_data(self, test_size=0.25, random_state=42, aggregate_features=False, remove_outliers=True):
        '''Prepare data for preprocessing
        
        Parameters
        ----------
        test_size : float
            Proportion of data to be used as test set. If `test_size` is outside of the range [0,1], the entire dataset is returned
        random_state : int
            Random state to be used as random seed. Defaults to 42.
        aggregate_features : bool
            Should aggregate new features; TotalSpend, AvgSpendPerPurchase, TotalPurchases.
        remove_outliers : bool
            Should remove outliers. 

        Returns
        -------
        np.ndArray
            Prepared training data.
        np.ndArray
            Prepared test data. If test_size is out of range, returns `None`.
        '''

        data = self.get_raw_data()

        split_target = (test_size < 0 or test_size > 1)
        if (aggregate_features):
            data['TotalSpend'] = data[['MntWines', 'MntFruits', 'MntSweetProducts', 'MntGoldProds', 'NumWebVisitsMonth']].sum(axis=1)
            data['AvgSpendPerPurchase'] = data['TotalSpend'] / (data['NumWebPurchases'] + data['NumStorePurchases'] + 1)
            data['TotalPurchases'] = data[['NumWebPurchases', 'NumStorePurchases']].sum(axis=1)
        
        if (remove_outliers):         
            data = self.__remove_outliers(data)            

        self.scaler = MinMaxScaler()

        if split_target:

            train, test = train_test_split(data, test_size=0.25, random_state=random_state)

            train_scaled = self.scaler.fit_transform(train)
            test_scaled = self.scaler.transform(test)

            train_scaled = pd.DataFrame(data=train_scaled, columns=data.columns) 
            test_scaled = pd.DataFrame(data=test_scaled, columns=data.columns) 
        else:
            train_scaled = self.scaler.fit_transform(data)
            train_scaled = pd.DataFrame(data=train_scaled, columns=data.columns) 
            
            test_scaled = None


        return train_scaled, test_scaled    
    

    def get_scaler(self):
        return self.scaler


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
        _, bound_fruit = self.__IQR_bounds(df, 'MntFruits', should_print=False)
        _, bound_web = self.__IQR_bounds(df, 'NumWebPurchases', should_print=False)

        outliers_wine = df[(df['MntWines'] > 1400)].index
        print(f'Removing {len(outliers_wine)} wine outliers')
        df = df.drop(outliers_wine)
        
        outliers_fruit = df[(df['MntFruits'] > bound_fruit * 2)].index
        print(f'Removing {len(outliers_fruit)} fruit outliers')
        df = df.drop(outliers_fruit)
        
        outliers_sweets = df[(df['MntSweetProducts'] > 200)].index
        print(f'Removing {len(outliers_sweets)} sweets outliers')
        df = df.drop(outliers_sweets)

        outliers_gold = df[(df['MntGoldProds'] > 250)].index
        print(f'Removing {len(outliers_gold)} gold outliers')
        df = df.drop(outliers_gold)

        outliers_web_1 = df[(df['NumWebPurchases'] > bound_web)].index
        outliers_web_2 = df[(df['NumWebPurchases'] > 20)].index
        # print(f'Removing {len(outliers_web_1)} web purchase outliers')
        # df = df.drop(outliers_web_1)
        print(f'Removing {len(outliers_web_2)} web purchase outliers')
        df = df.drop(outliers_web_2)

        outliers_fish_meat = df[(df['MntFishMeatProdcts'] > 1250)].index
        print(f'Removing {len(outliers_fish_meat)} fish_meat outliers')
        df = df.drop(outliers_fish_meat)

        return df
    

    def aggregate_features(df):
        df['TotalSpend'] = df[['MntWines', 'MntFruits', 'MntSweetProducts', 'MntGoldProds', 'NumWebVisitsMonth']].sum(axis=1)
        df['AvgSpendPerPurchase'] = df['TotalSpend'] / (df['NumWebPurchases'] + df['NumStorePurchases'] + 1)
        df['TotalPurchases'] = df[['NumWebPurchases', 'NumStorePurchases']].sum(axis=1)

        return df
