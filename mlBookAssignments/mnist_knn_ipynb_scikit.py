# -*- coding: utf-8 -*-
"""mnist-knn.ipynb-scikit

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1l6LifJ_LyM_QabEJQatlCGU4e-iTKk_y
"""

from sklearn.datasets import fetch_openml

mnist = fetch_openml('mnist_784', version=1)

X,y = mnist['data'], mnist['target']

X_train, y_train, X_test, y_test = X[:60000], y[:60000], X[60000:], y[60000:]

from sklearn.neighbors import KNeighborsClassifier
knn_clf_1 = KNeighborsClassifier(n_neighbors=11)
knn_clf_1.fit(X_train, y_train)

y_pred = knn_clf_1.predict(X_test)

n_correct = sum(y_pred==y_test)
print(n_correct/len(y_pred))

from sklearn.base import clone
knn_clf_2 = clone(knn_clf_1)

from sklearn.model_selection import StratifiedKFold

skfolds = StratifiedKFold(n_splits=3, random_state=42)

for train_index, test_index in skfolds.split(X_train, y_train):
  X_train_folds = X_train[train_index]
  y_train_folds = y_train[train_index]
  X_test_fold = X_train[test_index]
  y_test_fold = y_train[test_index]

  knn_clf_2.fit(X_train_folds, y_train_folds)
  y_pred1 = knn_clf_2.predict(X_test_fold)
  n_correct = sum(y_pred1==y_test_fold)
  print(n_correct/len(y_pred1))

from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
param_grid = {'n_neighbors':[5,11,17],'weights':['uniform', 'distance'],'metric':['euclidean']}
grid_search_knn = GridSearchCV(KNeighborsClassifier(), param_grid, cv=2, n_jobs=-1)

grid_search_knn.fit(X_train, y_train)

grid_search_knn.best_params_

grid_search_predict  = grid_search_knn.predict(X_test)
n_correct = sum(grid_search_predict==y_test)
print(n_correct/len(y_test))