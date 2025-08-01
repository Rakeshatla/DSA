class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        
        preRows = self.generate(numRows - 1)
        newRow = [1] * numRows
        
        for r in range(1, numRows - 1):
            newRow[r] = preRows[-1][r - 1] + preRows[-1][r]
        
        preRows.append(newRow)
        return preRows