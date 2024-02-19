class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createLinkedList(lst: list[int]) -> ListNode:
    firstNode = None
    prevNode = None
    for n in lst:
        node = ListNode(val=n)
        if prevNode:
            prevNode.next = node
        else:
            firstNode = node
        prevNode = node
    return firstNode

def printLinkedList(ll: ListNode) -> None:
    node = ll
    llStr = ""
    while node:
        llStr += str(node.val)
        node = node.next
        if node:
            llStr += " -> "
    print(llStr)

# Main
ll = createLinkedList([1, 2, 3])
printLinkedList(ll)
