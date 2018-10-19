#       GRUPO 88       #
# Rodrigo Lima - 83559 #
# Tiago Soares - 78658 #

import numpy as np
from sklearn import neighbors, datasets, tree, linear_model
from sklearn.externals import joblib
import timeit
from sklearn.model_selection import cross_val_score

def features(X):
    
    F = np.zeros((len(X),5))
    for x in range(0,len(X)):
        F[x,0] = len(X[x])
        F[x,1] = nvogais(X[x])
        F[x,2] = nconsoantes(X[x])
        F[x,3] = na(X[x])
        F[x,4] = naccents(X[x])

    return F     

def mytraining(f,Y):
    n_neighbors = 3
    weights = 'distance'
    clfKNNC = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
    clfKNNC = clfKNNC.fit(f, Y)
    return clfKNNC

def myprediction(f, clf):
    Ypred = clf.predict(f)
    return Ypred

#Conta o numero de vogais numa palavra
def nvogais(x):
    count = 0

    for char in x:
        if char in "aeiou":
            count = count + 1

    return count

#Conta o numero de consoantes numa palavra
def nconsoantes(x):
    count = 0

    for char in x:
        if char not in "aeiou":
            count = count + 1 

    return count

#Conta o numero de a's numa palavra
def na(x):
    count = 0

    for char in x:
        if char in "a":
            count = count + 1

    return count

#Conta o numero de letras com acentos numa palavra
def naccents(x):
    count = 0

    for char in x:
        if char in "áàãâçéèêíìóôú":
            count = count + 1

    return count