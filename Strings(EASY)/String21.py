'''Defanging an IP Address'''
def defangIPaddr(address):
    while "." in address:
        return address.replace(".","[.]")
print(defangIPaddr("1.1.1.1"))

def defangIPaddr(address):
    return '[.]'.join(address.split('.'))
print(defangIPaddr("1.1.1.1"))