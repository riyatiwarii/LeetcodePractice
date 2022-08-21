class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("linkedlist is empty.")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.ref

    def get_length(self):
        n = self.head
        count = 0
        while n is not None:
            count += 1
            n = n.ref
        return count

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def insert_at(self, data, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_start(data)
            return

        new_node = Node(data)
        n = self.head
        i = 1
        while i < index:
            n = n.ref
            i = i+1
        new_node.ref = n.ref
        n.ref = new_node


LL1 = LinkedList()
LL1.insert_at_start(30)
LL1.insert_at_start(10)
LL1.insert_at_end(50)
LL1.insert_at(40,0 )
LL1.print_LL()



