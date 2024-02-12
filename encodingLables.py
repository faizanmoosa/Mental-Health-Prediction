import pandas as pd
data = pd.read_csv('survey.csv')

# positive_values specify which value is considered as the "positive" or "1" value in the binary representation
def binary_encode(data_frame, columns, positive_values):
    data_frame = data_frame.copy() # ensures that modifications made to new DataFrame, do not affect the original
    for column, positive_value in zip(columns, positive_values): # it iterates over a set of columns in data_frame
        data_frame[column] = data_frame[column].apply(lambda x: 1 if x == positive_value else 0)
        # modifies values of each column by applying the given binary values
    return data_frame

# encoding the 'treatment' feature with positive_values
# data = binary_encode(data, columns=['treatment'], positive_values=['Yes'])
# data.to_csv('survey.csv', index=False)

# print("Number of non-numeric columns: ", len(data.select_dtypes('object').columns))
# print("Number of missing values in all columns: ", data.isna().sum().sum())