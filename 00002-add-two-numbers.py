from typing import Optional
from common import ListNode, createLinkedList, printLinkedList

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        firstNode = None
        prevNode = None
        carry = 0
        while l1 or l2:
            resNode = ListNode()
            if not l1:
                resNode.val = l2.val + carry
            elif not l2:
                resNode.val = l1.val + carry
            else:
                resNode.val = l1.val + l2.val + carry

            if resNode.val >= 10:
                resNode.val = resNode.val - 10
                carry = 1
            else:
                carry = 0
            
            if prevNode:
                prevNode.next = resNode
            else:
                firstNode = resNode
            prevNode = resNode

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            resNode = ListNode()
            resNode.val = carry
            prevNode.next = resNode
    
        return firstNode

# Main
list1 = [2, 4, 3]
list2 = [5, 6, 4]
l1 = createLinkedList(list1)
l2 = createLinkedList(list2)
printLinkedList(Solution().addTwoNumbers(l1, l2))
