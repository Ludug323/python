from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

x,y= datasets.make_regression(n_samples=20000,n_features=1,n_targets=1,noise=10)
lm = LinearRegression()
print(x,y)
lmFit = lm.fit(x,y)
predictValue = lmFit.predict(x)

plt.scatter(x,y)
plt.plot(x,predictValue,c="red")
plt.show()

#---------------second condition---------

a,b = datasets.make_regression(n_samples=200,n_features=2,n_targets=1,noise=10)
lmScd = LinearRegression()
lmScd_fit = lmScd.fit(a,b)
lmScd_pre = lmScd_fit.predict(a)
print(lmScd_pre)
print(b)