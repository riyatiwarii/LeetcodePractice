def squareIsWhite(coordinates):
    return True if ((ord(coordinates[0])) + int(coordinates[1])) % 2 else False
print(squareIsWhite("d2"))