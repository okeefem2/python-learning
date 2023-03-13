from sklearn.datasets import load_breast_cancer
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


def load_and_explore_data():
    bc_data = load_breast_cancer()
    target_names = bc_data.target_names
    target_counts = np.bincount(bc_data.target)
    print('Target names: ', target_names)
    print('Target counts: ', target_counts)
    # names and counts are both iterable and can be zipped together into pairs
    # (tuples) since the indexes match each other
    # then turned into a dict for nice printing
    target_name_count_pairs = zip(target_names, target_counts)
    print('Sample counts per class: \n', dict(target_name_count_pairs))
    # unrelated but I need to right this down, dict.update looks relly cool,
    # basically able to update/add new fields to a dict from another dict
    # almost like spread operator? but no new object created
    feature_names = bc_data.feature_names
    print('Feature names:\n', feature_names)
    return bc_data


def evaluate_model(X_train, y_train, X_test, y_test):
    # Evaluate the accuracy of the model based on different values of k for nearest neighbors
    training_accuracy = []
    test_accuracy = []
    neighbor_values = range(1, 11)

    for n in neighbor_values:
        knn = KNeighborsClassifier(n_neighbors=n)
        knn.fit(X_train, y_train)
        # How closely does it match the test data
        training_accuracy.append(knn.score(X_train, y_train))
        # How well does it generalize
        test_accuracy.append(knn.score(X_test, y_test))
        # Theory before running, these will have a somewhat inverse relationship

    plt.plot(neighbor_values, training_accuracy, label='Training Accuracy')
    plt.plot(neighbor_values, test_accuracy, label='Testing Accuracy')
    plt.ylabel('knn Accuracy')
    plt.xlabel('k neighbors')
    plt.legend()
    plt.show()
    # Observation, inverse for smaller n, but converge as n increases
    # Lower n is an example of over-fitting in this case


def create_and_train_model():
    bc_data = load_and_explore_data()
    X_train, X_test, y_train, y_test = train_test_split(bc_data.data, bc_data.target, stratify=bc_data.target, random_state=66)
    evaluate_model(X_train, y_train, X_test, y_test)
