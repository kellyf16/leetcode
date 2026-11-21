class Solution(object):
    def findDegrees(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        for i in matrix:
            sum = 0
            for j in i:
                if j == 1:
                    sum += 1
            ans.append(sum)
        return ans