# Time_Series-Hello-World
This Repo has various approaches for a time series problem encountered in deep learning.  
## File : Helper_function.py
- This file contains two python functions to convert time-series to supervised learning dataset.(Function Name = series_to_supervised)    
  and to create test dataset for the case of univariate time-series.(Function name = create_test_lag)  
  -**About: series_to_supervised() :-**
    -converts Time-seires data (multivariate/univariate) to supervised learning dataset
    - data = DataFrame, train dataset
    - n_in = int, lag window for each instance
    - n_out = int, no. of future predictions
    - dropnan = Boolean, default : True, when True will drop rows having nan values

    -**About: create_test_lag() :-**
      -In most of cases of univariate time-series, you have to predict upon the new dates , with nothing provided except dates, this function creates dataset to predict upon dates provided for prediction
      - len_test = int, size of  test dataset (dataset for prediction)
      - train_wd = DataFrame, dataset for training (**NOTE: It must not be date parsed.**)
      - lag = int, lag window for each test case. (**NOTE: Must be same as n_in in above function**)
  
*Author:series_to_supervised()* (Jason Brownie [https://machinelearningmastery.com/about/])  
*Author:create_test_lag()* (@that_danish [https://https://github.com/thatdanish/])   


*This Space will be regularly updated*  
**This is me learning various different ways of time series**
