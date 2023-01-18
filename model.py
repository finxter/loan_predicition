from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import RidgeClassifier
from sklearn.metrics import accuracy_score
import pickle
import pandas as pd

# load the data
data = pd.read_csv('LoanApprovalPrediction.csv')
# Drop Loan_ID column
data.drop(['Loan_ID'], axis=1, inplace=True)
# convert to int datatype
label_encoder = LabelEncoder()
obj = (data.dtypes == 'object')
for col in list(obj[obj].index):
    data[col] = label_encoder.fit_transform(data[col])

# fill in missing rows
for col in data.columns:
    data[col] = data[col].fillna(data[col].mean())
# divide model into features and target variable
x = data.drop(['Loan_Status'], axis=1)
y = data.Loan_Status

# divide into training and testing data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=7)
# define the model
model = RidgeClassifier()
# fit the model on the training data
model.fit(x_train, y_train)

#save the train model
with open('train_model.pkl', mode='wb') as pkl:
    pickle.dump(model, pkl)

