class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    def list2num(node):
        num = 0
        while node:
            num = 10 * num + node.val
            node = node.next
        return num

    num = list2num(l1) + list2num(l2)
    
    #espacially [0],[0] case
    if num == 0: return ListNode()

    cur = None
    while num > 0:
        newnode = ListNode(num % 10)
        newnode.next = cur
        cur = newnode
        num = num / 10
    return cur