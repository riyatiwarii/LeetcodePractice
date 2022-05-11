def prefixCount(words, pref):
    return sum(word.startswith(pref) for word in words)
print(prefixCount(["pay","attention","practice","attend","rat"],"at"))