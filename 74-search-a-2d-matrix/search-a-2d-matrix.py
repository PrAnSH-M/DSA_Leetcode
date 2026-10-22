class Solution:

    def bs(self, matrix: list[list[int]], target: int, row: int) -> bool:
        m = len(matrix[0])
        l = 0
        r = m - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if target == matrix[row][m]:
                return True
            elif target > matrix[row][m]:
                l = m + 1
            else: 
                r = m - 1
            
        return False


    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        n = len(matrix)
        c = len(matrix[0])

        l = 0
        r = n - 1

        while l <= r:
            m = l + ((r-l)//2)

            if target >= matrix[m][0] and target <= matrix[m][c-1]:
                return self.bs(matrix, target, m)
            
            elif target > matrix[m][c-1]:
                l = m + 1
            
            else:
                r = m - 1

        
        return False