'''Valid Anagram'''
def isAnagram(s,t):
    d = {}
    for i in s:
        if i in d: d[i] +=1
        else: d[i] = 1
    for i in t:
        if i in d: d[i] -=1
    for k, v in d.items():
        if v!=0: return False
        return True
print(isAnagram('car','rat'))
