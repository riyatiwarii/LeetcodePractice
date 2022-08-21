'''Middle of the Linked List'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        '''Approach one'''
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        temp = head
        while temp.next is not None:
            temp = temp.next
            count += 1
        if (count % 2) == 1:
            mid = count // 2
        else:
            mid = count+1 // 2
        for i in range(mid):
            head = head.next
        return head
        '''Appproach second'''
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
