# Task Description

1. Download the weather_bcn.csv dataset from the Example datasets section in Atenea.

2. Make sure the date column is an index and it is of datetime type. Select only the tavg (average temperature) column to obtain a one-column time series format. Split the data leaving out 2022 as the test set. Select some metrics to evaluate the results when applying the different methods. Plot the series and obtain a decomposition.

3. Apply auto_arima with and without seasonality.

4. Apply the ExponentialSmoothing method from the statsmodel library.

5. Convert the data into a classical tabular format by using lag features, create a regression model (do not use a very simple model) and check the performance.

6. Repeat the same procedure (steps 2-5) to forecast the pcrp (precipitation) column. When using lag features, try an additional model using 'pres' as an additional external feature of the model.

7. Draw some conclusions about the results.
