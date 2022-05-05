'''Jewels and Stones'''
def numJewelsInStones(jewels, stones):
    return sum(i in jewels for i in stones)
print(numJewelsInStones("zz","zZzz"))