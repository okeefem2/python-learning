import mglearn
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np


def load_and_explore_data():
    # Data is loaded in a dict like object (Bunch)
    X, y = mglearn.datasets.make_forge()
    mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
    plt.legend(['Class 0', 'Class 1'], loc=4)
    plt.xlabel('First feature')
    plt.ylabel('Second feature')
    # plt.show()
    print('X Shape: ', X.shape)
    return X, y


def build_model(X_train, y_train):
    knn = KNeighborsClassifier(n_neighbors=1)
    return knn.fit(X_train, y_train)


def evaluate_model(model: KNeighborsClassifier, X_test, y_test):
    y_pred = model.predict(X_test)
    print('Test set predictions: \n', y_pred)
    # These basically seem to do the same thing, just showing the two methods the book has used so far
    print('Test set score: {:.2f}'.format(np.mean(y_pred == y_test)))
    print('Test set accuracy: {:.2f}'.format(model.score(X_test, y_test)))


def visualize_decision_boundary(X, y):
    fig, axes = plt.subplots(1, 3, figsize=(10, 3))
    for n_neighbors, ax in zip([1, 3, 9], axes):
        knn = KNeighborsClassifier(n_neighbors=n_neighbors).fit(X, y)
        mglearn.plots.plot_2d_separator(knn, X, fill=True, eps=0.5, ax=ax, alpha=0.4)
        mglearn.discrete_scatter(X[:, 0], X[:, 1], y, ax=ax)
        ax.set_title(f'{n_neighbors} neighbors(s)')
        ax.set_xlabel('Feature 0')
        ax.set_ylabel('Feature 1')

    axes[0].legend(loc=3)
    plt.show()


# KNN
def create_and_train_model():
    X, y = load_and_explore_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    knn = build_model(X_train, y_train)
    evaluate_model(knn, X_test, y_test)
    visualize_decision_boundary(X, y)
