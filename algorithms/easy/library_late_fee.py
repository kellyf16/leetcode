class Solution(object):
    def lateFee(self, daysLate):
        """
        :type daysLate: List[int]
        :rtype: int
        """
        sum = 0
        for days in daysLate:
            if days == 1:
                sum += 1
            elif 2 <= days and days <= 5:
                sum += 2 * days
            else:
                sum += 3 * days

        return sum
        