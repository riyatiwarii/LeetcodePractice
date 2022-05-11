def squareIsWhite(coordinates):
    a = int(ord(coordinates[:-1])+int(coordinates[1:]))
    if a%2 != 0:
        return True
    return False
print(squareIsWhite("d2"))