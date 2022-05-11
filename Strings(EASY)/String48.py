def prefixCount(words, pref):
    count = 0
    for word in words:
        if word.startswith(pref):
            count += 1
    return count
print(prefixCount(["pay","attention","practice","attend","rat"],"at"))