def reorderList(head):
    """
    :type head: ListNode
    :rtype: None Do not return anything, modify head in-place instead.
    """

    def helper(node):
        if not node or not node.next: return head

        retNode = helper(node.next)

        #key point: the three  conditions
        if not retNode or retNode == node or not retNode.next:
            return None

        nextNode = retNode.next
        retNode.next = node.next
        node.next.next = nextNode
        node.next = None

        return nextNode

    helper(head)