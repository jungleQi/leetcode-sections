from common import *


class Solution(object):
    lnode = None

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next: return True

        self.lnode = head
        return self._helper(head)

    def _helper(self, nod):
        if not nod.next:
            return self.lnode.val == nod.val

        res = self._helper(nod.next)
        self.lnode = self.lnode.next
        return res and self.lnode.val == nod.val