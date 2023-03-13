from sklearn.datasets import load_boston
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, PolynomialFeatures
from sklearn.utils import Bunch
from sklearn.linear_model import LinearRegression, Ridge


def load_and_explore_data():
    boston_data = load_boston()
    return boston_data


# Taken and adapted from https://github.com/amueller/mglearn/blob/master/mglearn/datasets.py for the purpose of
# Seeing how feature engineering works
def load_extended_boston(boston: Bunch):
    X = MinMaxScaler().fit_transform(boston.data)
    X = PolynomialFeatures(degree=2, include_bias=False).fit_transform(X)
    return X, boston.target


def evaluate_linear_regression(X_train, y_train, X_test, y_test):
    model = LinearRegression().fit(X_train, y_train)
    print(f'linear \n test score: {model.score(X_test, y_test)} \n train score: {model.score(X_train, y_train)}')


def evaluate_ridge_regression(X_train, y_train, X_test, y_test):
    model_1 = Ridge().fit(X_train, y_train)
    print(f'ridge \n test score: {model_1.score(X_test, y_test)} \n train score: {model_1.score(X_train, y_train)}')

    # a higher value for the alpha parameter forces the coefficients to be smaller,
    #  this will decrease train perf but might generalize better.
    model_10 = Ridge(alpha=10).fit(X_train, y_train)
    print(
        f'ridge alpha 10 \n test score: {model_10.score(X_test, y_test)} \n train score: {model_10.score(X_train, y_train)}'
    )
    # a lower value for the alpha parameter loosens the restrictions on coefficients
    # bringing us closer to a linear model
    model_0_1 = Ridge(alpha=0.1).fit(X_train, y_train)
    print(
        f'ridge alpha 0.1 \n test score: {model_0_1.score(X_test, y_test)} \n train score: {model_0_1.score(X_train, y_train)}'
    )

    plt.plot()

def evaluate_ridge_coef():



def create_and_train_model():
    boston_data = load_and_explore_data()
    X, y = load_extended_boston(boston_data)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    # In this case, ridge is better, because it generalizes better with the data
    # Linear shows signs of overfitting in this case (train score is near perfect, test score is not good)
    evaluate_linear_regression(X_train, y_train, X_test, y_test)
    evaluate_ridge_regression(X_train, y_train, X_test, y_test)

