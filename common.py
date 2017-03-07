# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def create_ll(val_list):
    prev = None
    for val in val_list:
        node = ListNode(val)
        if prev:
            prev.next = node
        else:
            ll = node
        prev = node
    return ll

def print_ll(ll):
    while ll:
        print(ll.val, end="")
        ll = ll.next
        if ll:
            print("->", end="")
        else:
            print("\n", end="")

# Main
if __name__ == "__main__":
    val_list = [3, 4, 0, 4, 2, 7, 6]
    print_ll(create_ll(val_list))
