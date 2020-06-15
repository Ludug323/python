from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt

iris = datasets.load_iris()
x = iris.data
y = iris.target
#knn = KNeighborsClassifier(n_neighbors=10)#尋找附近10個鄰居

k_range = range(1,25)
k_scores = list()
for k_number in k_range:
    knn = KNeighborsClassifier(n_neighbors=k_number)
    scores = cross_val_score(knn,x,y,cv=10,scoring='accuracy')#cv=10 分成10組,accuracy為一種方法 顯示準確度高不高的方法
    k_scores.append(scores.mean())
    
plt.plot(k_range,k_scores)
plt.xlabel('Value ok k for KNN')
plt.ylabel('Cross-Validated Accuracy')
plt.show()