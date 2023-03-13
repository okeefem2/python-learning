from sklearn.datasets import load_iris
from sklearn.utils import Bunch
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import pandas as pd
import mglearn
import matplotlib.pyplot as plt


def load_and_explore_data() -> Bunch:
    # Data is loaded in a dict like object (Bunch)
    iris_data: Bunch = load_iris()
    print('Keys of iris data:\n ', iris_data.keys())

    # These are the potential labels of the data
    print('Target names (species): \n', iris_data['target_names'])

    # The features used by the algorithm for clustering
    print('Feature names: \n', iris_data['feature_names'])

    # Data is a 2d numpy array where the rows (inner arrays) are flowers and their measurements
    # and the columns (items in the inner arrays) are measurements
    # The shape gives us the number of rows/columns - 150 rows, 4 columns or 150 samples x 4 features
    print('Data shape: \n', iris_data['data'].shape)
    # print the first 5 rows
    print('Data sample: \n', iris_data['data'][:5])

    # Target array has the species for all the flowers in data and is a 1d numpy array
    print('Target shape: \n', iris_data['target'].shape)
    # Get all the possible results for the target - [0, 1, 2]
    print('Target distinct values: \n', np.unique(iris_data['target']))
    # The target values correspond to the index in the target meanings array
    print('Target meanings: \n', iris_data['target_names'])
    # print the first 5 rows
    print('Target sample: \n', iris_data['target'][:5])
    return iris_data


def visualize_data(iris_data, iris_targets, columns):
    iris_dataframe = pd.DataFrame(iris_data, columns=columns)
    # pair plot with histograms of features on the diagonal
    # the histograms give the distribution of each feature individually
    # the scatter plots show the relationship on x and y of each pair of features
    # Look for separation of the features
    pd.plotting.scatter_matrix(iris_dataframe, c=iris_targets, figsize=(15, 15), marker='o',
                               hist_kwds={'bins': 20}, s=60, alpha=0.8, cmap=mglearn.cm3)
    plt.show()


def build_model(X_train, y_train):
    knn = KNeighborsClassifier(n_neighbors=1)
    return knn.fit(X_train, y_train)


def evaluate_model(model: KNeighborsClassifier, X_test, y_test):
    y_pred = model.predict(X_test)
    print('Test set predictions: \n', y_pred)
    print('Test set score: {:.2f}'.format(np.mean(y_pred == y_test)))


def iris_create_and_train_model():
    iris_data: Bunch = load_and_explore_data()
    # Each of these are numpy arrays, X being the data, and y being the targets
    # The train arrays should contain a random 75% of the data and the test arrays a random 25% of the data
    # the random state is fixed to make this split deterministic
    X_train, X_test, y_train, y_test = train_test_split(iris_data['data'], iris_data['target'], random_state=0)
    # visualize_data(X_train, y_train, iris_data.feature_names)
    knn = build_model(X_train, y_train)
    evaluate_model(knn, X_test, y_test)
    # Numpy arrays are still used for prediction so a 2d in this case with the one sample as a row works
    X_new = [[5, 2.9, 1, 0.2]]
    prediction = knn.predict(X_new)
    print('Prediction: ', prediction)
    # The prediction is the label from iris_data['target'] which is an index for iris_data['target_names'] in this data
    print('Predicted Target Name: ', iris_data['target_names'][prediction])

