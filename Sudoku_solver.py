class Solution:
    
    def solve(self, board: List[List[str]]) -> bool:

        for i in range(9):

            for j in range(9):

                if board[i][j] == ".":

                    for c in "123456789":

                        if self.is_valid(board, i, j, c):

                            board[i][j] = c

                            if self.solve(board):

                                return 1
                            else:

                                board[i][j] = "."
                    return 0
        return 1

    def is_valid(self, board: List[List[str]], row: int, col: int, c: str) -> bool:

        for i in range(9):

            if(board[i][col] == c):   
                return 0
            if(board[row][i] == c):   
                return 0
            if(board[row//3  *3 +  i//3][col//3 *3  +  i%3]   ==   c): 
                return 0

        return 1

    def solveSudoku(self, board: List[List[str]]) -> None:
        self.solve(board)
        
        # Test case here: Uncomment to test it
        
        # [["5","3",".",".","7",".",".",".","."],
        #  ["6",".",".","1","9","5",".",".","."],
        #  [".","9","8",".",".",".",".","6","."],
        #  ["8",".",".",".","6",".",".",".","3"],
        #  ["4",".",".","8",".","3",".",".","1"],
        #  ["7",".",".",".","2",".",".",".","6"],
        #  [".","6",".",".",".",".","2","8","."],
        #  [".",".",".","4","1","9",".",".","5"],
        #  [".",".",".",".","8",".",".","7","9"]]
        