# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = head
        curr = head
        curr = curr.next
        while curr is not None:
            total = 0
            while curr.next is not None and curr.val != 0:
                total += curr.val
                curr = curr.next
            prev.val = total
            if curr is not None and curr.next is not None:
                prev.next = curr
                prev = curr
                curr = curr.next
            else:
                prev.next = None
                break
        return head

        