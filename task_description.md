1. Check the dimensions of the dataset (number of rows and columns).g

2. Peek at the first few rows to understand the data structure

3. Examine the types of data present in each column (numerical, categorical, datetime,...). Verify that the data types assigned to each column align with the actual nature of the data. Convert data types if necessary.

4. Filter the data by removing variables that are not relevant for the analysis.

5. Univariate analysis: Summary statistics for numerical variables and frequency distribution for categorical ones. Create visualizations (histograms, box plots, bar plots, etc).

6. Identify outliers and decide whether to remove, transform, or keep them.

7. Identify variables that provide little to no information and remove them.

8. Bivariate analysis: Examine correlations and dependencies between variables to identify potential relationships. Create visualizations to explore these relationships. A particularly significant case involves assessing the relationship of each variable with the class/target variable you want to predict.

9. Create new features from existing ones if necessary (e.g., extracting date components, ratios between variables, etc.).

10. Divide the dataset into training and test sets.

11. Scale numerical features to a similar range in order to improve model performance on some models.

12. Encode categorical variables.

13. Identify missing data and decide how to handle them (remove, impute).
