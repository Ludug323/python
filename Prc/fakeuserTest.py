from fake_useragent import UserAgent
ua = UserAgent()

for i in range(5):
    print(ua.random)
    print("")