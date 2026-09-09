import math 

class Solution(object):
    def countingSameBitIntegers(self, n):
        """
        :type n: int
        :rtype: int
        """
        bit_length = len(bin(n)) - 2
        ones = bin(n).count("1")

        count = math.comb(bit_length, ones) - 1

        return count % (10**9 + 7)