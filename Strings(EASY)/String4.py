'''Add Binary'''
def addBinary(a, b):
    output = int(a, 2) + int(b, 2)
    return (bin(output)[2:])
print(addBinary("100","101"))
