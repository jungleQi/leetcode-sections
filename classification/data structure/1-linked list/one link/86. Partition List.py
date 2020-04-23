#coding=utf-8

'''
Given a linked list and a value x,
partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:
Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
'''

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







