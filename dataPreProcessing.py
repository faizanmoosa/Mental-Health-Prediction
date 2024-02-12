import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('survey.csv')

# dropped this column, as it has large number of missing values
# data = data.drop('comments', axis=1)
# data.to_csv('survey.csv', index=False)

# let's check mean value of missing values in each feature
# print(data.isna().mean())

# let's print uniques values in the given feature
# print(data['work_interfere'].unique()) 

# filling missing values in this column, with most occuring value i.e., mode is 'No'
# data['self_employed'].fillna('No', inplace=True)
# data.to_csv('survey.csv', index=False)

# filling missing values in this column, with most occuring value i.e., mode is 'Sometimes'
# data['work_interfere'] = data['work_interfere'].fillna('Sometimes')
# data.to_csv('survey.csv', index=False)

# converting this column, to this format 'YYYY-MM-DD HH:MM:SS' from 'DD-MM-YYYY HH:MM'
# data['Timestamp'] = pd.to_datetime(data['Timestamp'], format='%d/%m/%y %H:%M')
# data.to_csv('survey.csv', index=False)

# dropped the rows containing such impractical values in 'Age' column
# data.drop(data[(data['Age'] > 60) | (data['Age'] < 18)].index, inplace=True)
# data.to_csv('survey.csv', index=False)

# dropped this column, as it was no more useful, after feature engineering
# data = data.drop('Timestamp', axis=1)
# data.to_csv('survey.csv', index=False)

value_counts = data['treatment'].value_counts()
print(value_counts)