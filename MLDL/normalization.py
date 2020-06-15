from sklearn import preprocessing #標準化的函數
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets #產生隨機資料
from sklearn.svm import SVC #用SVC分類法
import matplotlib.pyplot as plt

x,y = datasets.make_classification(n_samples=300,n_features=2,n_redundant=0,n_informative=2,random_state=3,scale=100,n_clusters_per_class=1)

xTrain,xTest,yTrain,yTest = train_test_split(x,y,test_size= 0.2)
clf = SVC()
clfFit = clf.fit(xTrain,yTrain)
clfSc=clfFit.score(xTest,yTest)
print(clfSc)

x = preprocessing.scale(x)
xTrain,xTest,yTrain,yTest = train_test_split(x,y,test_size= 0.2)
clf = SVC()
clfFit = clf.fit(xTrain,yTrain)
clfSc=clfFit.score(xTest,yTest)
print(clfSc)

#plt.scatter(x[:,0],x[:,1],c=y)
#plt.show()