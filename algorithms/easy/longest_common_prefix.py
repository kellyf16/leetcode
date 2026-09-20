class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]

        prefix = ""
        for i, x in enumerate(strs[0]):
            for j in range(1, len(strs)):
                if len(strs[j]) <= i or strs[j][i] != x:
                    return prefix
            prefix = prefix + x   

        return prefix   
        