class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        value = 0
        for operation in operations:
            if "--" in operation:
                value -= 1
            else:
                value += 1
        return value
        