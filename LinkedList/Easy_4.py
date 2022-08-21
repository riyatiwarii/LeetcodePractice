'''Design a HashSet'''
class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashSet:
    def __init__(self):
        self.size = 1000
        self.table = [None]*1000

    def add(self, key: int) -> None:
        index = key % self.size
        if self.table[index] == None:
            self.table[index] = ListNode(key, True)
        else:
            temp = self.table[index]
            self.table[index] = ListNode(key, True)
            self.table[index].next = temp

    def remove(self, key: int) -> None:
        index = key % self.size
        temp = self.table[index]
        while temp != None:
            if temp.key == key:
                temp.val = False
                break
            temp = temp.next

    def contains(self, key: int) -> bool:
        index = key % self.size
        temp = self.table[index]
        while temp != None:
            if temp.key == key:
                if temp.val == True:
                    return True
                else:
                    return False
            temp = temp.next
        return False


