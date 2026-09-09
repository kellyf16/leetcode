class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if abs(x) != x:
            return False

        temp = x
        digits = []

        while (temp != 0):
            digit = temp % 10
            temp = temp // 10
            digits.append(digit)

        reverse = 0
        for y in digits:
            reverse = reverse * 10 + y

        return reverse == x