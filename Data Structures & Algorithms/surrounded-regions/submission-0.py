class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows=len(board)
        cols=len(board[0])
        def capture(r, c):
            if (r < 0 or c < 0 or r == rows or
                c == cols or board[r][c] != "O"
            ):
                return
            board[r][c] = "S"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)
        for i in range(cols):
            if board[0][i]=="O":
                capture(0,i)
            if board[rows-1][i]=="O":
                capture(rows-1,i)
        for i in range(rows):
            if board[i][0]=="O":
                capture(i,0) 
            if board[i][cols-1]=="O":
                capture(i,cols-1)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"