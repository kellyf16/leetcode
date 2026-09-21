class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """

        max = 0
        for x in n:
            if x > max:
                max = x
        return int(max)
        