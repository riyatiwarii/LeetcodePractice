'''Check if All Characters Have Equal Number of Occurrences.'''
def areOccurrencesEqual(s):
    freq = {}
    for item in s:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    count = sum(freq.values()) / len(freq)
    for key, value in freq.items():
        return value == count
print(areOccurrencesEqual("abacbc"))
'''Another way'''
from collections import Counter
def areOccurrencesEqual(s):
    return len(set(Counter(s).values())) == 1
print(areOccurrencesEqual("abacbc"))


