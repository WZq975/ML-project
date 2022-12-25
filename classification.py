import os
import numpy as np
import json
import sklearn
import sklearn.ensemble
import sklearn.model_selection
from sklearn.linear_model import LogisticRegression
import sklearn.tree
import scipy
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import argparse


def load_dataset(data_path):
    X_train = []
    y_train = []
    X_test = []
    y_test = []
    for fold in ['HC', 'SZ']:
        path = os.path.join(data_path, fold)
        features = []
        for feature in sorted(os.listdir(path)):
            if os.path.splitext(feature)[1] == '.json':
                features.append([json.load(open(os.path.join(path, feature)))[i] for i in range(0, 13)])
        if fold == 'HC':
            labels = list(np.ones(len(features)))
        else:
            labels = list(np.zeros(len(features)))
        features_tra, features_tst, labels_tra, labels_tst = \
            sklearn.model_selection.train_test_split(features, labels, test_size=0.2, random_state=5)
        X_train = X_train + features_tra
        y_train = y_train + labels_tra
        X_test = X_test + features_tst
        y_test = y_test + labels_tst

    return np.array(X_train), np.array(y_train), np.array(X_test), np.array(y_test)


def svm(X_train, y_train, X_test, y_test):
    svm = sklearn.svm.SVC(kernel='rbf')
    param_distributions = {'C': scipy.stats.reciprocal(1.0, 1000.), 'gamma':
        scipy.stats.reciprocal(0.01, 10.)}
    RSC = sklearn.model_selection.RandomizedSearchCV(svm, param_distributions,
                                                     random_state=0, verbose=1, n_iter=32, cv=4)
    RSC.fit(X_train, y_train)
    print('validation score of the best-performing hyperparameters: %.2f%%' %
          (RSC.best_score_ * 100))
    print('best parameters: ', RSC.best_params_)
    RSC_acc_test  = sklearn.metrics.accuracy_score(y_test,
                                                   RSC.best_estimator_.predict(X_test))
    print('accuracy of testing set: %.2f%%' % (RSC_acc_test * 100))


def logistic_regression(X_train, y_train, X_test, y_test):
    LR = LogisticRegression()
    param_grid = {
        'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000],
        'penalty': ['l1', 'l2']
    }
    RSC = sklearn.model_selection.RandomizedSearchCV(LR, param_distributions=param_grid,
                                                     cv=4, n_iter=24, verbose=1, random_state=0)
    RSC.fit(X_train, y_train)
    print('validation score of the best-performing hyperparameters: %.2f%%' %
          (RSC.best_score_ * 100))
    print('best parameters: ', RSC.best_params_)
    RSC_acc_test  = sklearn.metrics.accuracy_score(y_test,
                                                   RSC.best_estimator_.predict(X_test))
    print('accuracy of testing set: %.2f%%' % (RSC_acc_test * 100))


def random_forest(X_train, y_train, X_test, y_test, args):
    RF = sklearn.ensemble.RandomForestClassifier(random_state=0)
    print('Need some minutes...')
    RSC = sklearn.model_selection.RandomizedSearchCV(RF, n_iter=36,
                                                       param_distributions={'max_depth': [3, 10, 15, 20, 25],
                                                                            'max_features': [3, 6, 8, 10, 12],
                                                                            'min_samples_leaf': [1, 4, 7, 10, 13],
                                                                            'min_samples_split': [2, 5, 9, 13, 17],
                                                                            'n_estimators': [50, 287, 525, 762,
                                                                                             1000]},
                                                       random_state=0, cv=4, verbose=1)
    RSC.fit(X_train, y_train)
    print('validation score of the best-performing hyperparameters: %.2f%%' %
          (RSC.best_score_ * 100))
    print('best parameters: ', RSC.best_params_)
    RSC_acc_test  = sklearn.metrics.accuracy_score(y_test,
                                                   RSC.best_estimator_.predict(X_test))
    print('accuracy of testing set: %.2f%%' % (RSC_acc_test * 100))
    return RSC.best_params_


def feature_importance(X_train, y_train, parameters):
    RF = sklearn.ensemble.RandomForestClassifier(random_state=0, max_depth=parameters['max_depth'],
                                                 max_features=parameters['max_features'],
                                                 min_samples_leaf=parameters['min_samples_leaf'],
                                                 min_samples_split=parameters['min_samples_split'],
                                                 n_estimators=parameters['n_estimators'])
    RF.fit(X_train, y_train)
    importances = RF.feature_importances_

    # normalized
    importances = 100.0 * (importances / importances.max())

    # rank importance
    feature_names = ['stability1', 'stability2', 'stability3', 'saccade1', 'saccade2', 'saccade3', 'saccade4',
                     'saccade5', 'saccade6', 'pursuit1', 'pursuit2', 'pursuit3', 'pursuit4']
    sorted_idx = np.argsort(importances)[::-1]
    reordered_names = [feature_names[i] for i in sorted_idx]

    # plot feature importance
    pos = np.arange(sorted_idx.shape[0]) + .5
    plt.figure()
    plt.barh(pos, importances[sorted_idx], align='center')
    plt.yticks(pos, reordered_names)
    plt.xlabel('Relative Importance')
    plt.title('Feature Importance')
    plt.show()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', default='svm', help='machine learning models: options are svm, rf (random forest), '
                                                       'and lr (logistic regression).')
    parser.add_argument('--imp', default='True', help='whether to plot feature importance in random forest, '
                                                       'True or False, require selecting random forest first if True.')
    args = parser.parse_args()

    data_path = args.fd

    X_train, y_train, X_test, y_test = load_dataset(data_path)
    scaler = sklearn.preprocessing.StandardScaler().fit(np.concatenate((X_train, X_test)))
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)
    if args.model == 'svm':
        svm(X_train, y_train, X_test, y_test)
    elif args.model == 'rf':
        best_params = random_forest(X_train, y_train, X_test, y_test, args)
        if args.imp == 'True':
            feature_importance(X_train, y_train, best_params)
    elif args.model == 'lr':
        logistic_regression(X_train, y_train, X_test, y_test)
    else:
        raise Exception('The input model name is not included. Please input svm, rf, or lr.')


if __name__ == '__main__':
    main()

