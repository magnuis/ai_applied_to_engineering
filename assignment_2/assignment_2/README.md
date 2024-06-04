# Time series forecasting

We will use Mean Absolute Error (MAE) and Mean Squared Error (MSE) to evaluate the performance of the different methods. MAE gives us the average magnitude of the errors, while MSE highlights larger errors by squaring the differences between actual and predicted values.

In addition, we will use Mean Absolute Scaled Error (MASE) to compare the performance of the methods across different datasets. MASE is helpful because it normalizes the error, making it easier to compare results from datasets with different scales.

## The tavg forecasting

| Method                    | MSE   | MAE   | MASE  |
| ------------------------- | ----- | ----- | ----- |
| ARIMA without seasonality | 2.573 | 1.377 | 0.494 |
| ARIMA with seasonality    | 1.266 | 1.005 | 0.361 |
| Exponential smoothing     | 1.104 | 0.947 | 0.340 |
| CatBoostRegressor         | 1.525 | 0.983 | 0.355 |

### Overall Performance

Exponential smoothing performs the best across all metrics (MSE, MAE, and MASE), indicating it is the most accurate method for this predicting the average montlhly temperate.

### Impact of Seasonality

Including seasonality in the ARIMA model significantly improves its performance. The ARIMA model with seasonality has lower MSE, MAE, and MASE compared to the ARIMA model without seasonality, demonstrating the importance of considering seasonal patterns in the data.

### Machine Learning Method

The CatBoostRegressor performs reasonably well compared to the others, but it is not as accurate as Exponential Smoothing or ARIMA with seasonality.

### Error Sensitivity

The differences in MASE values reinforce the findings from MSE and MAE. Since MASE normalizes the error, it confirms that Exponential Smoothing and ARIMA with seasonality provide more reliable tavg forecasts compared to the naive forecast.

## The prcp forecasting

| Method                        | MSE     | MAE    | MASE  |
| ----------------------------- | ------- | ------ | ----- |
| ARIMA unseasonal              | 859.824 | 27.374 | 0.684 |
| ARIMA seasonal                | 990.113 | 28.331 | 0.708 |
| Exponential smoothing         | 979.253 | 27.903 | 0.698 |
| CatBoostRegressor (wout/pres) | 871.276 | 26.126 | 0.654 |
| CatBoostRegressor (w/pres)    | 830.266 | 23.468 | 0.588 |

### Overall Performance

The CatBoostRegressor with pressure data (w/pres) outperforms all other methods across all metrics (MSE, MAE, and MASE). This indicates that using atmospheric pressure as an external feature enhances the model's accuracy.

### Impact of Seasonality

The ARIMA model without seasonality performs better than the ARIMA model with seasonality, as indicated by its lower MSE, MAE, and MASE. This suggests that seasonality may not be as crucial for predicting monthly precipitaion.

### Machine Learning Methods

Both CatBoostRegressor models (with and without pres) show strong performance, with the model incorporating pres data performing the best. This suggests that machine learning methods can be highly effective for forecasting precipitation.

### Error Sensitivity

The MASE values align with the findings from MSE and MAE, confirming that the CatBoostRegressor with pressure data is the most reliable method.

## Conclusions

### Overall Model Performance

For tavg forecasting, Exponential Smoothing has the best performance across all metrics. For prcp forecasting it is the CatBoostRegressor without pressure that performs best.

### Impact of Seasonality

We expected ARIMA to perform better with seasonality for both prcp and tavg, as both data are expected to be follow the seasons of the year. This expectation was strengthened by the observation of seasonality from the decomposition. It was however only the ARIMA model for tavg data that performed better with seasonality, whereas the prcp model became worse.

### Error Sensitivity

The MASE values confirm the findings from MSE and MAE, with the best models having the lowest MASE, indicating more reliable forecasts relative to the naive forecast.

### Conclusion

Overall, Exponential Smoothing is the best method for forecasting average temperature (tavg), effectively capturing seasonal patterns. For precipitation (prcp), the CatBoostRegressor with pressure performs best, highlighting the need for careful feature selection and model tuning. These results show the importance of model selection and parameter tuning in achieving accurate time series forecasts.
