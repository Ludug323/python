def isLeapYear(n):
    n = int(n)
    return n%4 == 0 and n%100 != 0 or n %400 == 0
ylist = [1999,2000,2001,2002]

isLeapList =[(x,isLeapYear(x)) for x in ylist]
print(isLeapList)