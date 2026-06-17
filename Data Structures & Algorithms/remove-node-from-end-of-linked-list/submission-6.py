class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head
        prev = None
        i = 0

        while i != n:
            fast = fast.next
            i += 1

        while fast:
            prev = slow
            fast = fast.next
            slow = slow.next
        
        if prev:
            prev.next = slow.next
            return head

        if i == 1:
            return None

        head = head.next
        return head