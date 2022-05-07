'''Count the Number of Consistent Strings'''
def countConsistentStrings(allowed, words):
    count = 0
    for word in words:
        for char in word:
            if char not in allowed:
                count += 1
                break
    return len(words) - count
print(countConsistentStrings("ab",["ad","bd","aaab","baa","badab"]))

