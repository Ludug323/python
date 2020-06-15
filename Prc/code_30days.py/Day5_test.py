def hidePassword(psd):
    return "*"*len(psd)

psd = input("輸入 : psd = ")
print("輸出 : {}".format(hidePassword(psd)))