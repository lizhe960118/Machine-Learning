# from numpy import loadtxt
# from xgboost import XGBClassifier
# from sklearn.cross_validation import train_test_split
# from sklearn.metrics import accuracy_score
#
# # load Data
# dataset = loadtxt('pima-indians-diabetes.csv', delimiter=',')
#
# # split dataset into X and Y
# X = dataset[:, 0: 8]
# Y = dataset[:, 8]
#
# # split data into train and test sets
# seed = 7
# test_size = 0.33
# X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)
#
# # fit model no training data
# model = XGBClassifier()
# model.fit(X_train, y_train)
# print(model)
#
# # make predictions for test data
# y_pred = model.predict(X_test)
# predictions = [round(value) for value in y_pred]
#
# # evaluate predictions
# accuracy = accuracy_score(y_test, predictions)
# print("Accuracy:%.2f%%" % (accuracy * 100.0))

# # -----------------------------------------------------
# from pandas import read_csv
# from xgboost import XGBClassifier
# from sklearn import cross_validation
# from sklearn.metrics import accuracy_score
# from sklearn.preprocessing import LabelEncoder
#
# data = read_csv('iris.csv', header=None)
# dataset = data.values
#
# X = dataset[:, 0:4]
# Y = dataset[:, 4]
#
# label_encoder = LabelEncoder()
# label_encoder = label_encoder.fit(Y)
# label_encoded_y = label_encoder.transform(Y)
# # The three class values (Iris-setosa, Iris-versicolor, Iris-virginica) are mapped to the integer values (0, 1, 2).
#
# seed = 7
# test_size = 0.33
#
# X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, label_encoded_y, test_size=test_size, random_state=seed)
#
# model = XGBClassifier()
# model.fit(X_train, y_train)
# print(model)
#
# y_pred = model.predict(X_test)
# predictions = [round(value) for value in y_pred]
#
# accuracy = accuracy_score(y_test, predictions)
# print("Accuracy : %.2f%%" % (accuracy * 100.0))

# # -----------------------------------------------------
# ONE HOT Encode catagorical data
import numpy
from pandas import read_csv
from xgboost import XGBClassifier
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

data = read_csv('datasets-uci-breast-cancer.csv', header=None)
dataset = data.values

X = data[:, 0:9]
Y = data[:, 9]
# encode string input values as integers
columns = []
for i in range(0, X.shape[1]):
    label_encoder = LabelEncoder()
    feature = label_encoder.fit_transform(X[:, i])
    feature = feature.reshape(X.shape[0], 1)
    onehot_encoder = OneHotEncoder(sparse=False)
    feature = onehot_encoder.fit_transform(feature)
    columns.append(feature)
# collaspe columns into array
encoded_x = numpy.column_stack(columns)
print("X shape::", encoded_x.shape)

label_encoder = LabelEncoder()
label_encoder = label_encoder.fit(Y)
label_encoded_y = label_encoder.fit_transform(Y)

seed = 7
test_size = 0.33

X_train, X_test, y_train, y_test = train_test_split(encoded_x, label_encoded_y, test_size=test_size, random_state=seed)

model = XGBClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
predictions = [round(value) for value in y_pred]

accuracy = accuracy_score(y_test, predictions)
print("Accuracy : %.2f%%" % (accuracy * 100.0))