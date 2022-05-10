def freqAlphabets(s):
    for i in range(26, 0, -1): s = s.replace(str(i)+"#"*(i>9),chr(96+i))
    return s
print(freqAlphabets("10#11#12"))

