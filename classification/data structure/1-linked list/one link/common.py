class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def constructlist(values):
    prevNode,head = None, None
    for v in values:
        if not prevNode:
            head = prevNode = ListNode(v)
        else:
            prevNode.next = ListNode(v)
            prevNode = prevNode.next

    return head

def printList(pHead):
    while pHead:
        print(pHead.val)
        pHead = pHead.next
    print("\n")