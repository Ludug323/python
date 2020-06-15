from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier#導入KNN演算法
from sklearn.model_selection import train_test_split#做資料訓練的模組
import numpy as np

iris = datasets.load_iris()
irisData = iris.data
irisLabel = iris.target
print(irisLabel)
print(irisData[:3])

trainData, testData, trainLabel, testLabel = train_test_split(irisData, irisLabel,test_size= 0.2)#分別為訓練資料跟測試資料,給電腦訓練=0.8
knn = KNeighborsClassifier()
knn.fit(trainData, trainLabel)#將訓練資料做配對
print(knn.predict(testData))#印出 利用KNN演算法將testData所預測出來的testLabel
print(testLabel)#比對我們原本的testLabel是否跟預測出來的標籤相同