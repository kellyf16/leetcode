class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum = 0
        for num in nums:
            sum += num
    
        count = 0
        while sum % k != 0:
            sum -= 1
            count += 1
    
        return count
        