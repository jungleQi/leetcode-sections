def getIntersectionNode(headA, headB):
    if headA and headB:
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A

