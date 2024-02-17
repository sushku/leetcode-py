from common import *

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head
        lead_ptr = head
        cur_ptr = head
        prev_ptr = None
        count = 0
        while lead_ptr:
            count += 1
            lead_ptr = lead_ptr.next
            if count > n:
                prev_ptr = cur_ptr
                cur_ptr = cur_ptr.next
        if prev_ptr:
            prev_ptr.next = cur_ptr.next
            return head
        else:
            return cur_ptr.next

s = Solution()
head = create_ll([1, 2, 3, 4, 5])
res = s.removeNthFromEnd(head, 2)
print_ll(res)
