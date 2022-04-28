'''Excel Sheet Column Title'''

def convertToTitle(num):
    s = ""
    while num > 0:
        num, rem = divmod(num - 1, 26)
        s += chr(65 + rem)
    return s[::-1]
print(convertToTitle(29))

def convertToTitle(columnNumber):
    capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
    result = []
    while columnNumber>0:
        result.append(capitals[(columnNumber-1)%26])
        columnNumber = (columnNumber-1)//26
    result.reverse()
    return "".join(result)
print(convertToTitle(28))