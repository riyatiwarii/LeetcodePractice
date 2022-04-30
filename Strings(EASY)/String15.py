def findTheDifference(s, t):
    for i in s:
        if s.count(i) != t.count(i):
            return i
print(findTheDifference("abcdef","abcde"))
