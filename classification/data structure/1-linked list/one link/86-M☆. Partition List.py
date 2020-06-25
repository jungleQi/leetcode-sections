#coding=utf-8

'''
Given a linked list and a value x,
partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:
Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
'''

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#这道题正是可以利用List调整数据的优势，避开数组移动数据的劣势
#而list -> arr -> list的套路，虽然在某些情况下比较好使，但是在这里很不优雅，就是"扬arr短，避list长"
def partition(head, x):
    """
    :type head: ListNode
    :type x: int
    :rtype: ListNode
    """
    def _partition(nums, x):
        i, j, N = 0, 0, len(nums)
        while j < N:
            while i < N and nums[i] < x:
                i += 1
                if j <= i: j = i + 1
            while j < N and nums[j] >= x:
                j += 1
            if j >= N:
                break

            target = nums[j]
            nums[i + 1:j + 1] = nums[i:j]
            nums[i] = target

    nums = []
    curHead = head
    while curHead:
        nums.append(curHead.val)
        curHead = curHead.next

    _partition(nums, x)
    curHead = head
    for num in nums:
        curHead.val = num
        curHead = curHead.next

    return head

# 核心为：将node[j]调整为node[i]的next (i<j)
# 产生了3次提交错误，才有下面这个正确的提交，这里面陷阱很多
# 容易出错的地方在于line81-86 ，需要正确控制 head 和 cur在不同情形下的移动
def partition_II(head, x):
    if not head: return head

    dummy = ListNode(-1)
    dummy.next = head

    cur = head
    if head.val >= x:
        head = dummy

    while cur and cur.next and head:
        #这种情况下才需要做调整
        if cur.val >= x and cur.next.val < x:
            hNext = head.next
            cNext = cur.next

            head.next = cNext
            cur.next = cur.next.next

            cNext.next = hNext
            head = head.next
        #如果没有采用else判断，会出现问题：
        # [3,1,2] 3 ，[1,3,2]× ，[1,2,3]√
        else:
            cur = cur.next

        #如果不对head进行后续移动判断，会导致 the original relative order 被破坏
        if head and head.next and head.next.val < x:
            head = head.next

    return dummy.next


#用smaller和bigger 分别 指向比x小 和 大于等于的节点，将它们串成两个独立的链表
#最后将两个链表连接成一个整体
def partition_grace(head, x):
    bigger = biggerHead = ListNode()
    smaller = smallerHead = ListNode()

    while head:
        if head.val >= x:
            bigger.next = head
            bigger = head
        else:
            smaller.next = head
            smaller = head
        head = head.next

    bigger.next = None
    smaller.next = biggerHead.next
    return smallerHead.next



