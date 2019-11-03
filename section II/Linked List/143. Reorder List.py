from common import *

def reorderList(head):
    if not head : return None

    global leftNode
    leftNode = head
    def _helper(node):
        global leftNode
        if node.next == None:
            return

        _helper(node.next)
        if leftNode.next == None or leftNode.next.next == None:
            return

        next = leftNode.next
        leftNode.next = node.next
        node.next.next = next
        node.next = None

        leftNode = next
        return

    _helper(head)
values = [1]
head = constructlist(values)
reorderList(head)
printList(head)


