'''Reverse Words in a String III'''
def reverseWords(s):
    split_list = s.split(" ")
    split_list = [i[::-1] for i in split_list]
    return " ".join(split_list)
print(reverseWords("Let's take LeetCode contest"))