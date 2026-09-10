class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start != end:
            mid_index = (end + start)//2
            middle = nums[mid_index]

            if target == middle:
                return mid_index
            elif target < nums[start]:
                return start
            elif target > nums[end]:
                return end + 1
            elif target < middle:
                end = mid_index - 1
            else:
                start = mid_index + 1

        if target <= nums[start]:
            return start
        else:
            return end + 1