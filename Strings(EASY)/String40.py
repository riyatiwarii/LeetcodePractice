'''Number of Strings That Appear as Substrings in Word'''
def numOfStrings(patterns, word):
    return len([p for p in patterns if p in word])
print(numOfStrings(["a","abc","bc","d"],"abc"))


