class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        moves = []

        for i, box in enumerate(boxes):
            move = 0
            for j, bx in enumerate(boxes):
                if j == i:
                    continue
                elif bx == '1':
                    move += abs(j-i)
            moves.append(move)

        return moves