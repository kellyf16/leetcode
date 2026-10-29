# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        while curr and curr.next:
            nxt = curr.next
            while nxt is not None and curr.val == nxt.val:
                nxt = nxt.next
                curr.next = nxt
            curr = curr.next
    
        return head
            


        