def checkRepeat(plays):
    return len(set(plays))<len(plays)
plays = [80, 11, 86, 45, 54, 31, 46, 11, 61, 42]
print(f"True or False : {checkRepeat(plays)}")

plays= [54, 35, 69, 52, 29, 5, 4, 45, 23, 84]
print(f"True or False : {checkRepeat(plays)}")