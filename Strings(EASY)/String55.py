'''Maximum Number of Words You Can Type'''
def canBeTypedWords(text, brokenLetters):
    text = text.split()
    count = len(text)
    for i in text:
        for j in i:
            if j in brokenLetters:
                count -= 1
                break
    return count
print(canBeTypedWords("hello world","ad"))
print(canBeTypedWords("leet code","e"))
print(canBeTypedWords("leet code","lt"))
