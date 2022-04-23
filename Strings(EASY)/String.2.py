'''Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".'''

#My preferred way
def longestCommonPrefix(self, strs):
    if len(strs) == 0:
        return ""
    s1, s2 = min(strs), max(strs)
    i = 0
    while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
        i += 1
    return s1[:i]
print(commonprefix(['far', 'farm', 'farming']))

# Another way
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
print(longestCommonPrefix(['winner','windown','wink']))