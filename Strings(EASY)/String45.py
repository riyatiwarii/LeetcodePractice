'''Reverse Prefix of Word'''
def reversePrefix(word, ch):
    index = word.find(ch)
    return word[:index+1][::-1]+word[index+1:]
print(reversePrefix("abcdefd","d"))


