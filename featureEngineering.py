import pandas as pd
import numpy as np
data = pd.read_csv('survey.csv')

# making new features of int64 datatype, with only 'year', 'month', 'day', 'hour', 'minute', 'second' values
# 0:4 implies taking only first four characters of the feature
data['Year'] = data['Timestamp'].apply(lambda x: np.int64(x[0:4]))
data['Month'] = data['Timestamp'].apply(lambda x: np.int64(x[5:7]))
data['Day'] = data['Timestamp'].apply(lambda x: np.int64(x[8:10]))
data['Hour'] = data['Timestamp'].apply(lambda x: np.int64(x[11:13]))
data['Minute'] = data['Timestamp'].apply(lambda x: np.int64(x[14:16]))
data['Second'] = data['Timestamp'].apply(lambda x: np.int64(x[17:19]))
data.to_csv('survey.csv', index=False)