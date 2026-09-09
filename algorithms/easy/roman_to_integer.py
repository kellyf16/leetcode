class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000
        }

        sum = 0
        for i, x in enumerate(s):
            if i != 0 and s[i-1] + x in roman_map:
                sum = sum + roman_map[s[i-1] + x] - roman_map[s[i-1]]
            else:
                sum = sum + roman_map[x]
        return sum
        