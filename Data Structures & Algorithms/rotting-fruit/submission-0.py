class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshcount=0
        q=deque()
        rows=len(grid)
        cols=len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    freshcount+=1
                elif grid[i][j]==2:
                    q.append((i,j))
        minute=0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and freshcount>0:
            for i in range(len(q)):
                r,c=q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        q.append((row, col))
                        freshcount-= 1
            minute+=1
        return minute if freshcount==0 else -1

            
        