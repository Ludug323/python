from class0521 import Account 


acct1 = Account('123-456-789', 'Justin')
deposit1 = acct1.deposit #balance = 0
withdraw1 = acct1.withdraw #balance = 0
deposit1(100) # balance = 100
withdraw1(50) #balance = 50
print(acct1.balance)

acct2 = Account('987-654-321', 'Momor')
deposit2 = acct2.deposit 
withdraw2 = acct2.withdraw
deposit2(200) #balance = 200
withdraw2(100) #balance = 100
print(acct2.balance) #balance = 100

acct1.deposit = acct2.deposit
acct1.deposit(1000)      # 你其實是將錢存到 acct2 去
print(acct1.balance)     # 50
print(acct2.balance)     # 1100