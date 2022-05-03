'''addStrings'''
def addStrings(num1, num2):
    res = []
    carry, p1, p2 = 0, len(num1)-1, len(num2)-1
    while p1>=0 and p2>=0:
        x1, x2 = ord(num1[p1]) - ord("0"),ord(num2[p2]) - ord("0")
        x = x1+x2+carry
        carry, rem = divmod(x,10)
        res.append(rem)
        p1 -= 1
        p2 -= 1
    if carry:
        res.append(carry)
    return "".join(str(i) for i in res[::-1])
print(addStrings("119","22"))
