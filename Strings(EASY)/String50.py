''' DI String Match'''
def diStringMatch(s):
    res = []
    low, high = 0, len(s)
    for i in s:
        if i == "I":
            res.append(low)
            low += 1
        else:
            res.append(high)
            high -= 1
    res.append(low)
    return res
print(diStringMatch("IDID"))