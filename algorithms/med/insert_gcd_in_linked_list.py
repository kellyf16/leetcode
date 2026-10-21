# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def gcd(self, a, b):
        if b == 0:
            return a
        r = a % b
        while r:
            a = b
            b = r
            r = a % b
        return b

    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        while curr.next is not None:
            val = self.gcd(curr.val, curr.next.val)
            new_node = ListNode(val, curr.next)
            temp = curr.next
            curr.next = new_node
            curr = temp

        return head        