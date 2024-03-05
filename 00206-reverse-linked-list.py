from typing import Optional
from common import ListNode, createLinkedList, printLinkedList

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prevNode = None
        prevPrevNode = None
        while node:
            if prevNode:
                prevNode.next = prevPrevNode
                prevPrevNode = prevNode
            prevNode = node
            if node.next:
                node = node.next
            else:
                node.next = prevPrevNode
                break
        return node

# Main
nums = [1, 2, 3, 4, 5]
head = createLinkedList(nums) 
printLinkedList(Solution().reverseList(head))