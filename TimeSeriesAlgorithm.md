# Time Series Algorithms in AWS and Azure

## AWS 

Forecast is a fully managed service for time-series forecasting by Amazon. Amazon Forecast provides the following predefined algorithms:
 
* Autoregressive Integrated Moving Average (ARIMA) Algorithm 

It is useful for datasets that can be mapped to stationary time series.Datasets with stationary time series usually contain a combination of signal and noise. 
ARIMA acts like a filter and separate the signal from the noise,and then extrapolates the signal in the future to make predictions.

* DeepAR+ Algorithm 

DeepAR+ is a supervised learning algorithm for forecasting scalar (one-dimensional) time series using recurrent neural networks (RNNs). 
This algorithm is beneficial when the data has many similar time series across a set of cross-sectional units so that a single model 
can be trained jointly over all of the time series. 

* Exponential Smoothing (ETS) Algorithm 

Exponential Smoothing (ETS) calls the ets function in the Package 'forecast' of the Comprehensive R Archive Network (CRAN).
The ETS algorithm is useful for datasets with seasonality and other prior assumptions about the data. 

* Non-Parametric Time Series (NPTS) Algorithm 

NPTS algorithm is a scalable, probabilistic baseline forecaster. It predicts the future value distribution of a given time series by 
sampling from past observations. The predictions are bounded by the observed values. NPTS is especially useful when the
time series is intermittent (or sparse, containing many 0s) and bursty. Amazon Forecast NPTS forecasters have the following variants: 

NPTS, seasonal NPTS, climatological forecaster, and seasonal climatological forecaster

* Prophet Algorithm 

Prophet algorithm  uses the Prophet class of the Python implementation of Prophet and is useful for datasets that:

• Contain an extended time period (months or years) of detailed historical observations (hourly, daily, or weekly)

• Have multiple strong seasonalities

• Include previously known important, but irregular, events

• Have missing data points or large outliers

• Have non-linear growth trends that are approaching a limit


## Azure 

Automated ML provides users with both native time-series and deep learning models as part of the recommendation system. These learners include:

• Prophet

• Auto-ARIMA

• ForecastTCN

Automated ML's deep learning allows for forecasting univariate and multivariate time series data. Deep learning models have three intrinsic capabilities:

• learn from arbitrary mappings from inputs to outputs

• support multiple inputs and outputs

• automatically extract patterns in input data that spans over long sequences


### Reference

<https://docs.aws.amazon.com/forecast/latest/dg/forecast.dg.pdf>

<https://docs.microsoft.com/en-us/azure/machine-learning/how-to-auto-train-forecast>
