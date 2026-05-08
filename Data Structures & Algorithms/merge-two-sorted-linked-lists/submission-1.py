# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head_sorted = None
        curr = None
        l1 = list1
        l2 = list2
        while l1 and l2:
            if l1.val <= l2.val:
                if head_sorted:
                    curr.next = l1
                    curr = curr.next
                else:
                    curr = l1
                    head_sorted = l1
                l1 = l1.next
            else:
                if head_sorted:
                    curr.next = l2
                    curr = curr.next
                else:
                    curr = l2
                    head_sorted = l2
                l2 = l2.next
        if l1:
            if head_sorted:
                curr.next = l1
            else:
                head_sorted = l1
        if l2:
            if head_sorted:
                curr.next = l2
            else:
                head_sorted = l2

        return head_sorted    
            


        