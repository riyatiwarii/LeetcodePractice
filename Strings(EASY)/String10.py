'''Word Pattern'''
def wordPattern(pattern, s):
    words = s.split(" ")
    if len(pattern) != len(words):
        return False
    wordinChar = {}
    charinWord = {}
    for c, w in zip(pattern, words):
        if c in charinWord and charinWord[c] != w:
            return False
        if w in wordinChar and wordinChar[w] != c:
            return False
        charinWord[c] = w
        wordinChar[w] = c
    return True
print(wordPattern("aab","cat cat dog"))

