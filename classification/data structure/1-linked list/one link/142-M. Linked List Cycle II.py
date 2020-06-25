#coding=utf-8

'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed)
in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
'''

#Approach 1: Hash Table
def detectCycle_hashtable(head):
    visited = set()

    node = head
    while node is not None:
        if node in visited:
            return node
        else:
            visited.add(node)
            node = node.next

    return None

#背后的原理与推导还不清楚
#Approach 2: Tortoise and Hare
def detectCycle(head):
    if not head or not head.next or not head.next.next: return None
    slow, fast = head.next, head.next.next

    while slow != fast:
        if not fast or not fast.next : return None
        slow = slow.next
        fast = fast.next.next

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow