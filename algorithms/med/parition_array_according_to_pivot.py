class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        before = []
        between = []
        after = []

        for num in nums:
            if num < pivot:
                before.append(num)
            elif num == pivot:
                between.append(num)
            else:
                after.append(num)
        return before + between + after

        