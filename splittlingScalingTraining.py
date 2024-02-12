import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

from sklearn.model_selection import GridSearchCV

import pickle

data = pd.read_csv('survey.csv')

# we considered the target feature, to split it away from rest of the data
y = data['treatment'].copy()
# this will take the rest of the columns, except 'treatment' column
X = data.drop('treatment', axis=1).copy()

# this will give every column's mean and unit variance
scaler = StandardScaler()
X = scaler.fit_transform(X)

# we are splitting horizontally i.e., splitting rows
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=100)

# we are considering various models that are mentioned in IEEE paper and we will choose the best performance one
# model_dict = {}
# model_dict['Logistic Regression'] = LogisticRegression(solver='liblinear', random_state=100)
# model_dict['K Neighbors Classifier'] = KNeighborsClassifier()
# model_dict['Decision Tree Classifier'] = DecisionTreeClassifier(random_state=100)
# model_dict['Random Forest Classifier'] = RandomForestClassifier(random_state=100)

# we are defining a function for testing the aforementioned models, that accepts various model related parameters
# def model_test(X_train, X_test, y_train, y_test, model, model_name):
#     model.fit(X_train, y_train)
#     y_pred = model.predict(X_test)
#     accuracy = accuracy_score(y_test, y_pred)
#     print("Accuracy of", model_name, "is:", accuracy)

# we are calculating the accuracy, by iterating through the dictionary
# for model_name, model in model_dict.items():
#     model_test(X_train, X_test, y_train, y_test, model, model_name)

# from the results, it is clear that Random Forest Classifier is providing a good accuracy i.e., 73%
# we are doing the hyper-parameter tuning of the aforementioned model, in order to improve the performance
# abc = RandomForestClassifier(random_state=1)
# params_abc = {
#     'n_estimators': [50, 100, 200],
#     'max_depth': [None, 10, 20, 30],
#     'min_samples_split': [2, 5, 10],
#     'min_samples_leaf': [1, 2, 4, 8],
# }
# abc_random = GridSearchCV(estimator=abc, param_grid=params_abc, cv=5)
# the_abc_random = abc_random.fit(X_train, y_train)
# print(the_abc_random.best_params_)

# we are doing the hyper-parameter tuning of the aforementioned model, in order to improve the performance
model = RandomForestClassifier(max_depth = None, min_samples_leaf=8, min_samples_split=2, n_estimators = 20, random_state = 1)
my_model = model.fit(X_train, y_train)

new_model = RandomForestClassifier(criterion='entropy', max_depth = 10, random_state=42, n_estimators=100)
my_new_model = new_model.fit(X_train, y_train)

# we are saving the models
# with open('model.pkl', 'wb') as files:
#     pickle.dump(my_model, files)

# with open('new_model.pkl', 'wb') as files:
#     pickle.dump(my_new_model, files)
