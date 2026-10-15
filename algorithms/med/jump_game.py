class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        jump = [False] * len(nums)
        if len(nums) == 1:
            return True

        jump[0] = True
        for i, num in enumerate(nums):
            if num == 0 or jump[i] is False:
                continue
            
            for j in range(num):
                if i+j+1 >= len(nums):
                    break
                jump[i+j+1] = True
                if jump[-1] == True:
                    return True

        return jump[-1]