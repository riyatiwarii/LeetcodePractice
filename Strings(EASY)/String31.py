'''Check If Two String Arrays are Equivalent'''
def arrayStringsAreEqual(word1, word2):
    return ''.join(word1) == ''.join(word2)
print(arrayStringsAreEqual(["ab", "c"],["a", "bc"]))

