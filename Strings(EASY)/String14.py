def firstUniqChar(str):
    freq = {}
    for char in range(0, len(str)):
        if str[char] not in freq:
            freq[str[char]] = True
        else:
            freq[str[char]] = False
    for char in range(0, len(str)):
        if freq[str[char]]:
            return char
    return -1
print(firstUniqChar("test"))
