class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head

        for i in range(k):
            if not curr:
                return head
            curr = curr.next

        curr, prev = head, None
        for i in range(k):
            curr_next = curr.next
            curr.next = prev

            prev = curr
            curr = curr_next

        head.next = self.reverseKGroup(curr, k)
        return prev