class Solution:

    def traversal(self, board: list[list[str]], sr: int, er: int, sc: int, ec: int) -> bool:
        st = set()

        for i in range(sr, er+1):
            for j in range(sc, ec+1):
                if board[i][j] == ".": 
                    continue
                if board[i][j] in st:
                    return False
                
                st.add(board[i][j])
        return True

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # for row
        for row in range(9):
            if not self.traversal(board, row, row, 0, 8):
                return False
    

        # for col
        for col in range(9):
            if not self.traversal(board, 0, 8, col, col):
                return False

        # for 3x3 box
        for sr in range(0, 9, 3):
            for sc in range(0, 9, 3):
               if not self.traversal(board, sr, sr +2, sc, sc+2):
                return False
            
        return True
