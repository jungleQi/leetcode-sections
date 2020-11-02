class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

def oddEvenList_clear(head):
    if not head: return None

    odd_dummy = ListNode()
    even_dummy = ListNode()

    odd_dummy.next = odd_head = head
    head = head.next
    even_dummy.next = even_head = head

    i = 3
    while head:
        if(i%2) == 0:
            odd_head.next = head
            odd_head = odd_head.next
        else:
            even_head.next = head
            even_head = even_head.next
        i += 1
        head = head.next
    odd_head.next = even_dummy.next
    return odd_dummy.next