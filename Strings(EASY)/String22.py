''' Maximum Number of Words Found in Sentences'''
def mostWordsFound(sentences):
    return max(len(word.split()) for word in sentences)
print(mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))