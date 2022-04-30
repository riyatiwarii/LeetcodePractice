'''Ransom Note'''
def canConstruct(ransomNote, magazine):
    for i in set(ransomNote):
        if magazine.count(i) < ransomNote.count(i):
            return False
    return True
print(canConstruct("name","rename"))