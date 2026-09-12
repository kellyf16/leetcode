class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []
        triangle.append([1])
        for i in range(1, numRows):
            row = []
            row.append(1)

            for j in range(1, i):
                sum = triangle[i-1][j-1] + triangle[i-1][j]
                row.append(sum)    

            row.append(1)            
            triangle.append(row)
        
        return triangle

        