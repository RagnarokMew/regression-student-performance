import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

################################################
## Loading datasets and splitting the targets ##
################################################

X_train = pd.read_csv("../../data/train.csv")
y_train = X_train['exam_score']
X_train.drop(columns='exam_score')

X_test = pd.read_csv("../../data/test.csv")
y_test = X_test['exam_score']
X_test.drop(columns='exam_score')

##########################################
## Model for regression train + predict ##
##########################################

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"Root mean squared error: {rmse}")

#############################################
## Plotting error graph and residual graph ##
#############################################

plt.scatter(y_test, y_pred, s=2, color='red', label='Model prediction')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--', color='lightgrey', label='Real values')
plt.title('Error graph')
plt.legend()
plt.savefig("../../raw/error_graph.png")
plt.close()

residual = y_test - y_pred
plt.scatter(y_pred, residual, alpha=0.5)
plt.axhline(y=0, color='black', linestyle='--')
plt.xlabel('Model predictions')
plt.ylabel('Residuals')
plt.title('Residual predictions')
plt.savefig("../../raw/residual_graph.png")
plt.close()