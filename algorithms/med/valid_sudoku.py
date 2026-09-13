class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = {}
        cols = {}
        boxes = {}

        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == ".":
                    continue
                    
                row_key = str(i) + "_" + str(cell)
                col_key = str(j) + "_" + str(cell)
                box_key = str(j//3) + "x" + str(i//3) + "_" + str(cell)

                if row_key in rows or col_key in cols or box_key in boxes:
                    return False
                else:
                    cols.update({col_key: 1})
                    rows.update({row_key: 1})
                    boxes.update({box_key: 1})
        
        return True

        