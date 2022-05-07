def countPoints(rings):
    lst = []
    for i in range(len(rings)):
        lst.append(rings[i:i + 2])
    res = 0
    for i in range(len(lst)):
        if (f'R{i}' in lst) and (f'G{i}' in lst) and (f'B{i}' in lst):
            res += 1
    return res
print(countPoints("B0B6G0R6R0R6G9"))
print(countPoints("G4"))
print(countPoints("B0G0R0B1G1R1"))