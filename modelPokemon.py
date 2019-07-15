# Soal 3 - Pokemon Battle
# =========================

import pandas as pd
from sklearn.linear_model import LogisticRegression

dataTrain = pd.read_csv('datasetTrainPokemon.csv')

dataX = dataTrain.drop(['Unnamed: 0', 'idPoke1', 'idPoke2', 'winner'], axis='columns')
# print(dataX.columns.values)
dataY = dataTrain['winner']

# splitting for training and testing
from sklearn.model_selection import train_test_split

xtrain, xtest, ytrain, ytest = train_test_split(
    dataX,
    dataY,
    test_size = 0.1
)

model = LogisticRegression(solver='liblinear', multi_class='auto')
model.fit(xtrain,ytrain)
# print(model.score(xtest,ytest))

import joblib
joblib.dump(model,'modelPokemon')