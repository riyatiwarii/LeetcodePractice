def longestCommonPrefix(strs):
    l = len(strs[0])
    res = ""
    for i in range(l):
        for word in strs:
            if len(word) > i:
                if word[i] != strs[0][i]:
                    return res
            else:
                return res
        res += strs[0][i]
    return res
print(longestCommonPrefix(['flower','flow','flight']))