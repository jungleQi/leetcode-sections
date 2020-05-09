#coding=utf-8

'''
Given a non-empty, singly 1-linked list with head node head, return a middle node of 1-linked list.

If there are two middle nodes, return the second middle node.
'''

#确定link list的中间节点或者是否有环，可以采用slow和fast，为了使处理简单：
#1.从同一个head节点出发，循环判断 fast and fast.next，循环体里进行各自的移动

def middleNode(head):
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

#递归返回节点对象
# 如果返回值为None，说明目前已经得到结果，可用于中断归中后续判断
# 如果返回值非None，这是归中下一个需要用于处理的目标节点
def middleNode_recursive(head):
    def travel(node):
        if not node: return head

        ret = travel(node.next)
        if not ret: return None

        if ret == node or ret.next == node:
            ans[0] = node
            return None

        return ret.next

    ans = [None]
    travel(head)
    return ans[0]