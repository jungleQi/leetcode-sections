#coding=utf-8
from utils import Node
from utils import ListNode
import heapq
import collections

# "abc3[cd]xyz"
class node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def constructLinkList(arr):
    dummy = head = node(0)
    i,N = 0, len(arr)

    while i<N:
        cur = node(arr[i])
        head.next= cur
        head = cur
        i += 1
    return dummy.next


def printList(node):
    while node:
        print node.val,
        node = node.next
    print "\n"


#功能，打印链表首位
def travel(head):
    def helper(node):
        if not node: return head
        newHead = helper(node.next)

        #首位相向打印，相遇后退出递归
        if not newHead or newHead == node or node.next == newHead:
            #如果list node 个数为奇数，打印最中间的
            if newHead and newHead == node:
                print newHead.val
            return None
        #打印首、尾
        print newHead.val,node.val,
        return newHead.next

    helper(head)

'''
Node* helper(Node* head, Node* node)
{
    if (node == NULL)
    {
        return head;
    }
    Node* newHead = helper(head, node->next);

    if(newHead == NULL || newHead == node || node->next == newHead)
    {
        if(newHead and newHead == node)
        {
            printf("%d", newHead->val);
        }
        return NULL;
    }
    printf("%d,%d", newHead->val,node->val);
    return newHead->next;
}

void travel(Node* head)
{
    helper(head, head);
}
'''

arr = [1,2,3,4,5,6,7]
head = constructLinkList(arr)
print "原始链表: "
printList(head)
print "打印结果："
travel(head)