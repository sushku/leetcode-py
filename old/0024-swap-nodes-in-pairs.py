from common import *

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        prev = None
        node1 = head
        node2 = head.next
        new_head = node2
        while node1 and node2:
            node3 = node2.next
            # swap node1 and node2
            node2.next = node1
            node1.next = node3
            if prev:
                prev.next = node2
            # increment loop variables
            prev = node1
            node1 = node3
            if node3:
                node2 = node3.next
        return new_head

s = Solution()
head = create_ll([1, 2, 3, 4])
res = s.swapPairs(head)
print_ll(res)
