'''
Given a singly linked list, group all odd nodes together followed by the even nodes.
Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place.
The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

Example 2:
Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL

Constraints:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
'''
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def oddEvenList_clear(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    oddDummy, evenDummy = ListNode(), ListNode()
    oddHead = oddDummy
    evenHead = evenDummy

    idx = 0
    while head:
        if idx % 2 == 0:
            evenHead.next = head
            evenHead = evenHead.next
        else:
            oddHead.next = head
            oddHead = oddHead.next

        head = head.next
        idx += 1

    #关键收尾，不然形成circle
    oddHead.next = None
    evenHead.next = oddDummy.next

    return evenDummy.next

def oddEvenList_concise(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head: return None

    odd = head
    even = head.next
    evenHead = even

    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = even.next.next
        even = even.next

    odd.next = evenHead

    return head