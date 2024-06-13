# Project part 2

Part 2 of the course project in _Artificial intelligence applied to engineering_ at ETSEIB, UPC, spring 2024. The team members contributing to the deliverable is

- Lise Jakobsen
- Julie Sørlie Lund
- Magnus Ingnes Sagmo

The dataset used in this deliverable can be retrieved from [Kaggle](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset).

## Data set review

#### Target class

The target class, `HeartDisease`, is a boolean class telling whether the patient has a heart disease. Subsequently, this is a classification problem.

#### Features

The data set has 11 features. Two of these, `ChestPainType` and `RestingECG`, are one-hot encoded.

#### Preprocessing method

The preprocessing done in the project part 1 was in some aspects insufficient, and in others executed poorly. We have therefore revised the preprocessing, that can now be found in the `preprocessor.py` file. To summarize, these are the preprocessing methods applied to the data:

- zero values of `Cholesterol` are imputed using `sklearn.impute.KNNImputer`.
- outliers are removed (28 from _RestingBP_, 21 from _Cholesterol_, 2 from _MaxHR_ and 13 from _Oldpeak_).
- the data is split into train and test set using `sklearn.model_selection.train_test_split`.
- the data is normalized using `sklearn.preprocessing.StandardScaler`.

## Performance metrics

Below are the performance metrics we will evaluate the methods based on.

#### Recall

In the case of detecting heart diseases it is crucial to minimize the number of false negatives (people with a heart disease going unnoticed). We will therefore focus on minimizing recall.

#### F1-score

By solely focusing on recall, we can end with a too high number of false positives (by choosing a model that classifies everything as heart disease). We will therefore also look at the F1-score, as it offers a balance between precision and recall.

#### Precision-recall curve

The precision-recall curve is a good way to visualize how well the model balances precision and recall.

## Results

All the models perform fairly well on our dataset. The highest performer in terms of recall is bagging, closely followed by decision trees. Bagging also has the highest F1-score, telling us that it has a good precision.

| model                  | Recall | F1-score | Precision-recall AUC |
| ---------------------- | ------ | -------- | -------------------- |
| adaboost               | 0.850  | 0.879    | 0.940                |
| bagging                | 0.879  | 0.892    | 0.937                |
| decision tree          | 0.872  | 0.889    | 0.948                |
| gaussian naive bayes   | 0.857  | 0.877    | 0.942                |
| gradient boosting      | 0.857  | 0.877    | 0.954                |
| knn                    | 0.850  | 0.879    | 0.942                |
| support vector machine | 0.857  | 0.891    | 0.939                |
