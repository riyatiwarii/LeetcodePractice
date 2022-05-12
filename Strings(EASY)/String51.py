'''Merge Strings Alternately'''
def mergeAlternately(word1, word2):
    res = ""
    for i in range(min(len(word1), len(word2))):
        res += word1[i] + word2[i]
    return res + word1[i+1:] + word2[i+1:]
print(mergeAlternately("abc","pqr"))




