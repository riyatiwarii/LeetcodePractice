'''Remove Outermost Parentheses'''
def removeOuterParentheses(S):
    res, stack = [], []
    for i, c in enumerate(S):
        if c == '(':
            if stack:
                res.append(c)
            stack.append(c)
        else:
            stack.pop()
            if stack:
                res.append(c)
    return ''.join(res)
print(removeOuterParentheses("(()())(())"))

