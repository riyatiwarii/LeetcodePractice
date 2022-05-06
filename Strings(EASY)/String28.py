'''Sorting the Sentence'''
def sortSentence(s):
    slist = s.split()
    sdic = {}
    for i in slist:
        sdic[i[-1]] = i[:-1]
    return " ".join(sdic[j] for j in sorted(sdic))
print(sortSentence("is2 sentence4 This1 a3"))
