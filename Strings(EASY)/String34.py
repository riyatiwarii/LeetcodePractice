'''Check if the Sentence Is Pangram'''
def checkIfPangram(sentence):
    return len(set(sentence)) == 26
print(checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
print(checkIfPangram("thequickbrownfox"))