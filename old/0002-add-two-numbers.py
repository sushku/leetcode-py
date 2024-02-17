from common import *

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        prev = None
        while l1 or l2:
            if not l1:
                sum = l2.val + carry
                l2 = l2.next
            elif not l2:
                sum = l1.val + carry
                l1 = l1.next
            else:
                sum = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next

            if sum >= 10:
                digit = sum - 10
                carry = 1
            else:
                digit = sum
                carry = 0

            node = ListNode(digit)

            if prev:
                prev.next = node
            else:
                res = node

            prev = node

        if carry == 1:
            node = ListNode(carry)
            prev.next = node

        return res

s = Solution()
l1 = create_ll([2, 4, 3])
l2 = create_ll([5, 6, 4])
res = s.addTwoNumbers(l1, l2)
print_ll(res)
