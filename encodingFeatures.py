import pandas as pd
data = pd.read_csv('survey.csv')

# let's get a sense of length of unique values, in each categorical feature
# for this, let's create a dictionary by mapping each column to the length of unique values in the column
# print({column: len(data[column].unique()) for column in data.select_dtypes('int').columns})

# we've specified the type as object which corresponds to string 
# print(data.select_dtypes('object').columns)

# let's get a sense of list of unique values, in each categorical feature
# for this, let's create a dictionary by mapping each column to the list of unique values in the column
# print({column: list(data[column].unique()) for column in data.select_dtypes('object').columns})

# creating our own function first for encoding this feature
def encode_gender(x): # x gets the values of 'gender' feature
    if x.lower()[0] == 'f':
        return 0
    elif x.lower()[0] == 'm':
        return 1
    else:
        return 2

# here, this feature has 49 unique values, making it to 3 values i.e., female=0, male=1, non-binary=2
# data['Gender'] = data['Gender'].apply(encode_gender)
# data.to_csv('survey.csv', index=False)
    
# target feature
target = 'treatment'

# let's create 3 lists, for dividing the features according to their characteristics
binary_features = [
    'self_employed',
    'family_history',
    'remote_work',
    'tech_company',
    'obs_consequence',
]
# values of ordinal features has a meaningful progression between them, and a clear rank or order
ordinal_features = [
    'work_interfere',
    'no_employees',
    'leave',
]
# they represent distinct categories without a natural order or ranking, also known as one-hot
nominal_features = [
    'Country',
    'state',
    'benefits',
    'care_options',
    'wellness_program',
    'seek_help',
    'anonymity',
    'mental_health_consequence',
    'phys_health_consequence',
    'coworkers',
    'supervisor',
    'mental_health_interview',
    'phys_health_interview',
    'mental_vs_physical',
]

# let's create some functions to encode the categorical features
# positive_values specify which value is considered as the "positive" or "1" value in the binary representation
def binary_encode(data_frame, columns, positive_values):
    data_frame = data_frame.copy() # ensures that modifications made to new DataFrame, do not affect the original
    for column, positive_value in zip(columns, positive_values): # it iterates over a set of columns in data_frame
        data_frame[column] = data_frame[column].apply(lambda x: 1 if x == positive_value else 0)
        # modifies values of each column by applying the given binary values
    return data_frame

# orderings are used to specify the unique values that each ordinal feature can take
def ordinal_encode(data_frame, columns, orderings):
    data_frame = data_frame.copy() # ensures that modifications made to new DataFrame, do not affect the original
    for column, ordering in zip(columns, orderings):
        data_frame[column] = data_frame[column].apply(lambda x: ordering.index(x))
        # modifies values of each column by applying the index value of each element 'x' in the ordering list
    return data_frame

# prefixes are used to specify the unique values that each nominal feature can take
def nominal_encode(data_frame, columns, prefixes):
    data_frame = data_frame.copy() # ensures that modifications made to new DataFrame, do not affect the original
    for column, prefix in zip(columns, prefixes): 
        dummies = pd.get_dummies(data_frame[column], prefix) # creates dummy_variables for each value in the column
        data_frame = pd.concat([data_frame, dummies], axis=1) # adds dummy_variables to the data_frame
        data_frame = data_frame.drop(column, axis=1) # column for which dummy_variables were created is dropped
    return data_frame

# let's create some positive_values
binary_positive_values = ['Yes' for feature in binary_features]

# let's create some orderings
ordinal_orderings = [
    ['Never', 'Rarely', 'Sometimes', 'Often'],
    ['1-5', '6-25', '26-100', '100-500', '500-1000', 'More than 1000'],
    ["Don't know", 'Somewhat difficult', 'Somewhat easy', 'Very difficult', 'Very easy']
]

# let's create some prefixes by taking the first two letters of each nominal feature like 'co' for country 
nominal_prefixes = [
    'co',
    'st',
    'be',
    'ca',
    'we',
    'se',
    'an',
    'mc',
    'pc',
    'cw',
    'su',
    'mi',
    'pi',
    'mp',
]

# encoding the binary_features with only binary_positive_values
# data = binary_encode(data, binary_features, binary_positive_values)
# data.to_csv('survey.csv', index=False)

# data['no_employees'] = data['no_employees'].replace('01-May', '1-5')
# data.to_csv('survey.csv', index=False)

# encoding the ordinal_features with the indices of ordinal_orderings
# data = ordinal_encode(data, ordinal_features, ordinal_orderings)
# data.to_csv('survey.csv', index=False)

# encoding the new features, out of nominal_features. the dataset will have 143 columns
# data = nominal_encode(data, nominal_features, nominal_prefixes)
# data.to_csv('survey.csv', index=False)