'''Find First Palindromic String in the Array'''
def firstPalindrome(words):
    for i in words:
        if i == i[::-1]:
            return i
    return ""
print(firstPalindrome(["abc","car","ada","racecar","cool"]))


