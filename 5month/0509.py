from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

temp = np.array([18,16,25,34,35,36,27,24,28,16,36,32,22,24])
time = np.array([0.8,0.4,3.5,8,10,14,5,2,7,0.4,13.5,9.8,1.2,2.7])

tempRes = np.reshape(temp,(len(temp),1))
timeRes = np.reshape(time,(len(time),1))
lm = LinearRegression()

lmFit = lm.fit(tempRes,timeRes)
lmPre = lmFit.predict(tempRes)
print(lmPre)

plt.scatter(tempRes,timeRes)
plt.plot(tempRes,lmPre)
plt.show()