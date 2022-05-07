'''Maximum Nesting Depth of the Parentheses'''
def maxDepth(s):
    count = 0
    maxnum = 0
    for i in s:
        if i == "(":
            count += 1
            if maxnum < count:
                maxnum = count
        if i == ")":
            count -= 1
    return maxnum
print(maxDepth("(1)+((2))+(((3)))"))
