# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = [None]
        def helper(prev, curr):

            if not curr:
                new_head[0] = prev
                return
            helper(curr, curr.next)
            curr.next = prev

        helper(None, head)
        return new_head[0]

        