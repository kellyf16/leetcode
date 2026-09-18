class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        total = 0
        for jewel in jewels:
            if jewel not in stones:
                continue
            else:
                total += stones.count(jewel)

        return total