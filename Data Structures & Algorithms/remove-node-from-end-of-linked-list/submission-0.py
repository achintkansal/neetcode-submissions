# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = 0
        curr = head
        while curr:
            sz += 1
            curr = curr.next
        cnt = 0
        dummy = ListNode(next = head)
        curr = dummy
        while curr:
            if cnt == (sz - n):
                curr.next = curr.next.next
            
            cnt += 1
            curr = curr.next
        
        return dummy.next
        