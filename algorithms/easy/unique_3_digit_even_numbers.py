class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        nums = []
        length = len(digits)
        for i in range(length):
            if digits[i] == 0:
                continue
            for j in range(length):
                if i == j:
                    continue
                for k in range(length):
                    if i == k or j == k or digits[k] % 2 != 0:
                        continue
                    num = str(digits[i])+str(digits[j])+str(digits[k])
                    nums.append(int(num))

        return len(set(nums))
        