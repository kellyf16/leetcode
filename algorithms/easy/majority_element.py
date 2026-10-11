class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        m = -1
        for i in nums:
            if count == 0:
                m = i
                count = 1
            elif m == i:
                count += 1
            else:
                count -= 1
        return m