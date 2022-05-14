'''Kth Distinct String in an Array'''
def kthDistinct(arr, k):
    from collections import Counter
    l=[]
    c=Counter(arr)
    for i in arr:
        if c[i] == 1:
            l.append(i)
    if k > len(l):
        return ""
    else:
        return l[k-1]
print(kthDistinct(["d", "b", "c", "b", "c", "a"], 2))
print(kthDistinct(["aaa","aa","a"], 2))
print(kthDistinct(["a","b","a"], 2))



