# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow, fast = head, head

        # 1. find the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 2. reverese the second half

        second = slow.next
        slow.next = None

        prev = None
        curr = second

        while curr:
            tmp = curr.next
            curr.next = prev

            prev = curr
            curr = tmp
        
        second = prev
        
        #3. append alternatively
        first = head

        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1
            
            first = tmp1
            second = tmp2



            



