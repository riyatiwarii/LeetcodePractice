'''Reverse Linked List II'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummynode = ListNode(0, head)
        Prevleft, curr = dummynode, head

        for i in range(left - 1):
            Prevleft, curr = curr, curr.next

        prev = None
        for i in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp

        Prevleft.next.next = curr
        Prevleft.next = prev
        return dummynode.next