from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

featuresName = ["high","age","ID"]
data = [[170,18,110],[155,19,111],[180,35,112],[135,10,45],[165,45,113],[155,56,200],[135,35,15],[189,15,1],[245,200,2000],[167,32,166]]
ramData = [[171,30,35],[175,15,21],[172,45,116],[163,55,200],[188,68,40],[55,55,2000]]

#data_df = pd.DataFrame(data,columns= featuresName)
#ramData_df = pd.DataFrame(ramData,columns= featuresName)
#print(data_df)
#print(testData_df)

features = data
labels = [1,1,1,0,1,1,0,0,1,1]
ramLabels = [0,0,1,1,0,1]

trainData, testData, trainLabels, testLabels = train_test_split(data, labels,test_size=0.12)
knn = KNeighborsClassifier()
knn.fit(trainData,trainLabels)
predictNum = knn.predict(ramData)
print(predictNum)
print(ramLabels)