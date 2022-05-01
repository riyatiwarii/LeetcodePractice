'''isSubsequence'''
def isSubsequence(s,t):
    i,j = 0, 0
    while i<len(s) and j<len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return True if i == len(s) else False
print(isSubsequence("abc","abcde"))