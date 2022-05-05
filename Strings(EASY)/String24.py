def interpret(s):
    mapped = {'G':'G','()':'o','(al)':'al'}
    tmp = ''
    res = ''
    for i in s:
        tmp += i
        if tmp in mapped:
            res += mapped[tmp]
            tmp = ''
    return res
print(interpret("G()(al)"))