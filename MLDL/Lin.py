from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

def reshape(nArr):
    return np.reshape(nArr,(len(nArr),1))

temp = np.array([29, 28, 34, 31, 25, 29, 32, 31, 24, 33, 25, 31, 26, 30])#np.array 方便整理元素
iceTea = np.array([77, 62, 93, 84, 59, 64, 80, 75, 58, 91, 51, 73, 65, 84])
lm = LinearRegression()#宣告lm 為一線性回歸

tempResh = reshape(temp)#利用np.reshape 重新將元素分割開來
iceTeaResh = reshape(iceTea) 
lmFit = lm.fit(tempResh,iceTeaResh)#lm.fit將資料逐一配對，且紀錄資料

lmPrec = lm.predict(tempResh) #利用empResh(溫度)資料,來預測iceTea所需要的資料 (注意,使用多個元素以利做預測)
print(lmPrec) #每一次所需要的iceTea.value

todayTemp = np.array([35])
todayTemp = reshape(todayTemp)

todayPrec = lm.predict(todayTemp)
print(todayPrec)
plt.scatter(todayTemp,todayPrec,color="red")
plt.scatter(tempResh,iceTeaResh,color='blue') #利用plt(matplotlib.pyplot) 將(x(tempResh),y(iceTeaResh)) 標記在圖形上(座標)
plt.plot(tempResh,lmPrec) # .plot(x,y) (溫度,預測出來所需要的iceTea)
plt.show() #視覺化出來