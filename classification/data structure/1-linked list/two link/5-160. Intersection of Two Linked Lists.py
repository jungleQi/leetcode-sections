'''
Write a program to find the node at which the intersection of two singly linked lists begins.
Notes:
    If the two linked lists have no intersection at all, return null.
    The linked lists must retain their original structure after the function returns.
    You may assume there are no cycles anywhere in the entire linked structure.
    Your code should preferably run in O(n) time and use only O(1) memory.
'''

def getIntersectionNode(headA, headB):
    def getLength(head):
        nlen = 0
        while head:
            nlen += 1
            head = head.next
        return nlen

    Alen, Blen = getLength(headA), getLength(headB)
    if Alen > Blen:
        while Alen != Blen:
            headA = headA.next
            Alen -= 1
    elif Alen < Blen:
        while Alen != Blen:
            headB = headB.next
            Blen -= 1

    while headA != headB:
        headA = headA.next
        headB = headB.next
    return headA
