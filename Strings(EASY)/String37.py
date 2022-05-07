'''Replace All Digits with Characters.'''
def replaceDigits(s):
    result = ""
    for ind, val in enumerate(s):
        if ind % 2 == 0:
            result += val
            previous = val
        else:
            result += (chr(ord(previous) + int(val)))
    return result
print(replaceDigits("a1c1e2"))


