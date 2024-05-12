## Task description

1. Load the resulting files from the 1st part of the project

2. Train, evaluate and compare these algorithms (note that some of them work exclusively with classification or regression problems and you may not be able to use them) from the sklearn library:

   - k Nearest Neighbours
   - Logistic/Linear regression
   - Polynomial regression
   - Decision/Regression Trees
   - Gaussian Naive Bayes
   - SVM
   - Bagging
   - Adaboost
   - Gradient boost
   - Random Forest

3. Explore different values of the hyperparameters, analyze the results

## Guide from teacher

Here are the aspects you need to focus on for the second part of the project:

- Make a quick review of the -already prepared- datasets used in this part of the project: which features are included and which is the class/target variable. If multiple datasets are used to validate hypotheses (e.g., comparing models' performance with and without outliers), clearly specify the method for testing these hypothesis (Are you going to use all the datasets throughout the entire project? Are you going to to use only some algorithms to test the hypothesis and then use the selected dataset for the project?).

- Specify the performance metrics to be used for model evaluation. Choose appropriate metrics based on the nature of the problem (e.g., accuracy, precision, recall, F1-score, precision/recall curves for classification; RMSE, MAE, R-squared for regression). Justify the choice of performance metric in relation to the problem being addressed. Take into account that you can choose more than one metric because each can be useful for different goals or indicate different aspects of performance.
  Experiment with the following algorithms from the sklearn library (note that a few of them are only eligible for classification problems while others only work with regression): Linear Regression, Polynomial Regression, Logistic Regression, Gaussian Naive Bayes, k-Nearest Neighbors, Decision/Regression Trees, SVM, Bagging, Random Forests, AdaBoost, Gradient Boosting, Multi Layer Perceptron.

- For each algorithm, specify which hyperparameters will be tuned and use grid search to find the best values according to the chosen metrics. Don't immediately accept the best result from grid search. Analyze other results to see if there are alternative hyperparameter values that provide almost the same performance but are more desirable for some reason (e.g., simpler models). Plot and study the effect of different hyperparameter values on performance.
  Analyze model performance in the context of bias and variance. Consider whether each model exhibit high bias or high variance. Analyze how changes in hyperparameters affect model complexity and, hence, the tradeoff between bias (underfitting) and variance (overfitting).

- At the end, show a summary table comparing the performance of different algorithms on the train and on the test sets based on the chosen evaluation metrics and draw some conclusions. Compare the performance on training and test sets and check for overfitting or underfitting.

- Remember that the most relevant aspect of your lab reports are not the programming but the comments, analysis, and conclusions. Programming is a means to an end. You have to get insights from your data, justify your decisions and try to explain the strengths and weaknesses of the methods you are applying for your particular problem.
  Pay also attention to the correctness of the methodological approach, the rationale used for choosing the hyperparameters and the clarity of the expositions as they can significantly influence the grade.
