from sklearn import tree
features = [[120,0],[130,0],[170,1],[180,1]]
label = [1,1,0,0]

clf = tree.DecisionTreeClassifier()

clf = clf.fit(features,label)
predictData = [[120,1]]
wantPredict = clf.predict(predictData)

if wantPredict == [1]:
    print("This is an orange")
else:
    print("This is an apple")