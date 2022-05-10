'''Determine if String Halves Are Alike'''
def halvesAreAlike(s):
    count, half = 0, len(s)/2
    for i, c in enumerate(s):
        if c in "aeiouAEIOU":
            count += 1 if i < half else -1
    return count == 0
print(halvesAreAlike("riya"))
