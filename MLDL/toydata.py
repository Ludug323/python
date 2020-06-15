from sklearn import datasets
import pandas as pd

iris = datasets.load_iris()
print(type(iris))

iris_df = pd.DataFrame(iris.data,columns= iris.feature_names)
print(iris_df.columns)

iris_df.insert(4,column="species",value=iris.target)
print(iris_df)