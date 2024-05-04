import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

print('Start: model preparation')

df_train = pd.read_csv('train/train_result.csv')

X_train = df_train[['temp']]
y_train = df_train['is_noize']

model = LogisticRegression()
model.fit(X_train, y_train)

pickle.dump(model, open('models/model.pkl', 'wb'))

print('Finish: model preparation')