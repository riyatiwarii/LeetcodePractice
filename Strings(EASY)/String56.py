'''Remove All Adjacent Duplicates In String'''
def removeDuplicates(s):
    stack = []
    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    return "".join(stack)
print(removeDuplicates("abbaca"))