'''Truncate Sentence'''
def truncateSentence(s, k):
    return " ".join(s.split()[:k])
print(truncateSentence("Hello, how are you doing?", 4))


