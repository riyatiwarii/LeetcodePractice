'''Cells in a Range on an Excel Sheet'''
def cellsInRange(s):
    res = []
    for i in range(ord(s[0]), ord(s[3])+1):
        for j in range(int(s[1]), int(s[4])+1):
            res.append(chr(i) + str(j))
    return res
print(cellsInRange("A2:F2"))

