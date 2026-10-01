class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        words = s.strip().split(" ")

        return len(words[len(words) - 1])