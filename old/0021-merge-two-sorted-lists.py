from common import *

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            head = l1
        else:
            head = l2
        prev = None
        while l1 and l2:
            if l1.val <= l2.val:
                if prev:
                    prev.next = l1
                prev = l1
                l1 = l1.next
            else:
                if prev:
                    prev.next = l2
                prev = l2
                l2 = l2.next
        if l1:
            prev.next = l1
        if l2:
            prev.next = l2
        return head

s = Solution()
l1 = create_ll([1, 2, 5, 7, 10, 11, 12])
l2 = create_ll([1, 3, 4, 6, 8, 9])
print_ll(s.mergeTwoLists(l1, l2))
