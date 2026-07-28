# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        # iterate for both two parts: nodes before and after k
        while True:
            kth = group_prev

            # checks whether k is within the range 1 <= k <= n
            for i in range(k):
                kth = kth.next
                # the linked list stays in the same order, no reverse
                if not kth:
                    return dummy.next

            group_next = kth.next

            prev, cur = group_next, group_prev.next

            # reverse
            while cur != group_next:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            # reconnect old head to becoming a tail
            new_group_head = group_prev.next
            group_prev.next = kth
            group_prev = new_group_head
            

