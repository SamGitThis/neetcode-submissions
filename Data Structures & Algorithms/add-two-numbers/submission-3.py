class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        answer = dummy
        carry = 0

        while l1 or l2:
            if l1 and l2:
                s = carry + l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
                
            elif l1 and not l2:
                s = carry + l1.val
                l1 = l1.next
                
            elif l2 and not l1:
                s = carry + l2.val
                l2 = l2.next
            
            if s >= 10:
                s =s%10
                carry = 1
            else:
                carry = 0
            
            dummy.next = ListNode(s)
            dummy = dummy.next

        if carry == 1:
            dummy.next = ListNode(1)

        return answer.next