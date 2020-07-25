from pandas import DataFrame
from pandas import concat
 
def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
	"""
	Frame a time series as a supervised learning dataset.
	Arguments:
		data: Sequence of observations as a list or NumPy array.
		n_in: Number of lag observations as input (X).
		n_out: Number of observations as output (y).
		dropnan: Boolean whether or not to drop rows with NaN values.
	Returns:
		Pandas DataFrame of series framed for supervised learning.
	"""
	n_vars = 1 if type(data) is list else data.shape[1]
	df = DataFrame(data)
	cols, names = list(), list()
	# input sequence (t-n, ... t-1)
	for i in range(n_in, 0, -1):
		cols.append(df.shift(i))
		names += [('var%d(t-%d)' % (j+1, i)) for j in range(n_vars)]
	# forecast sequence (t, t+1, ... t+n)
	for i in range(0, n_out):
		cols.append(df.shift(-i))
		if i == 0:
			names += [('var%d(t)' % (j+1)) for j in range(n_vars)]
		else:
			names += [('var%d(t+%d)' % (j+1, i)) for j in range(n_vars)]
	# put it all together
	agg = concat(cols, axis=1)
	agg.columns = names
	# drop rows with NaN values
	if dropnan:
		agg.dropna(inplace=True)
	return agg

# Work of Jason Brownie -- Read the documentation (README.md)
########################################################################################################################################################################################



def create_lag_test(len_test,train_wd,lag=1):
    test_lag = pd.DataFrame()
    cols,names = [],[]
    for i in tqdm(range(lag,0,-1)):
        T_hist = train_wd['Count'].shift(i-1) #Change the column name according to the dataset
        T_hist = pd.DataFrame(T_hist)
        T_hist = T_hist.iloc[-len_test:]
        cols.append(T_hist)
        names.append('t-'+str(i))

    test_lag = pd.concat(cols,axis=1)
    test_lag.columns = names
    
    return test_lag      

# Work of Mohd Danish Khurseed -- Read the documentation (README.md)
########################################################################################################################################################################################

# create a differenced series
def difference(dataset, interval=1):
	diff = list()
	for i in range(interval, len(dataset)):
		value = dataset[i] - dataset[i - interval]
		diff.append(value)
	return Series(diff)

diff_series = difference(raw_values, 1)
diff_values = diff_series.values
diff_values = diff_values.reshape(len(diff_values), 1)