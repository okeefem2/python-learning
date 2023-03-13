import mglearn
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression


def load_and_explore_data():
    # Data is loaded in a dict like object (Bunch)
    X, y = mglearn.datasets.make_wave(n_samples=40)
    plt.plot(X, y, 'o')
    plt.ylim(-3, 3)
    plt.xlabel('Feature')
    plt.ylabel('Target')
    # plt.show()
    return X, y


def evaluate_knn_regression(X_train, y_train, X_test, y_test):
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    # Create 1k data pts, evenly spaced between -3 and 3
    line = np.linspace(-3, 3, 1000).reshape(-1, 1)
    for n_neighbors, ax in zip([1, 3, 9], axes):
        knn = KNeighborsRegressor(n_neighbors=n_neighbors)
        knn.fit(X_train, y_train)
        ax.plot(line, knn.predict(line))
        ax.plot(X_train, y_train, '^', c=mglearn.cm2(0), markersize=8)
        ax.plot(X_test, y_test, 'v', c=mglearn.cm2(1), markersize=8)
        test_score = knn.score(X_test, y_test)
        train_score = knn.score(X_train, y_train)

        ax.set_title(f'{n_neighbors} neighbors\n train score {train_score:.2} \n test score {test_score:.2}')
        ax.set_xlabel('Feature')
        ax.set_ylabel('Target')
    axes[0].legend(['Model predictions', 'Trainingdata/target', 'Test data/target'], loc='best')
    plt.show()


def evaluate_linear_regression(X_train, y_train, X_test, y_test):
    model = LinearRegression().fit(X_train, y_train)
    print(f'slope by feature: {model.coef_} \n intercept: {model.intercept_}')
    print(f'test score: {model.score(X_test, y_test)} \n train score: {model.score(X_train, y_train)}')


def create_and_train_model():
    X, y = load_and_explore_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    # knn_reg = KNeighborsRegressor(n_neighbors=3)
    # knn_reg.fit(X_train, y_train)
    # print('Test set R^2: {:.2f}'.format(knn_reg.score(X_test, y_test)))

    evaluate_linear_regression(X_train, y_train, X_test, y_test)



