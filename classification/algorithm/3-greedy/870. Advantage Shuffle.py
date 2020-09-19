'''
Given two arrays A and B of equal size, the advantage of A with respect to B is the number of indices i for which A[i] > B[i].
Return any permutation of A that maximizes its advantage with respect to B.

Example 1:
Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]
'''

def advantageCount(A, B):
    sortedA = sorted(A)
    sortedB = sorted(B)

    # assigned[b] = list of a that are assigned to beat b
    # remaining = list of a that are not assigned to any b
    assigned = {b: [] for b in B}
    remaining = []

    # populate (assigned, remaining) appropriately
    # sortedB[j] is always the smallest unassigned element in B
    j = 0
    for a in sortedA:
        #a greedy approach
        if a > sortedB[j]:
            assigned[sortedB[j]].append(a)
            j += 1
        else:
            remaining.append(a)

    # Reconstruct the answer from annotations (assigned, remaining)
    return [assigned[b].pop() if assigned[b] else remaining.pop()
            for b in B]
