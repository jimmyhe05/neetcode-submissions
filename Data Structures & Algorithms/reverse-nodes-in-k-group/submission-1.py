class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            # check if there are k nodes left to reverse
            kth = group_prev
            for i in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next  # node right after this group

            # reverse the k nodes in this group
            prev, cur = group_next, group_prev.next
            while cur != group_next:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            # reconnect: old head is now the tail, attach it forward
            new_group_head = group_prev.next
            group_prev.next = kth
            group_prev = new_group_head