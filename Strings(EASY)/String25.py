'''Shuffle String'''
def restoreString(s, indices):
    return "".join([i for (j, i) in sorted(zip(indices, s))])
print(restoreString("codeleet",[4,5,6,7,0,2,1,3]))