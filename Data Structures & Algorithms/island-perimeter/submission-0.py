class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        visit=set()
        def dfs(r,c):
            if r<0 or c<0 or r==rows or c==cols:
                return 1
            if grid[r][c]==0:
                return 1
            if (r,c) in visit:
                return 0
            else:
                visit.add((r,c))
                p=dfs(r-1,c)+dfs(r,c-1)+dfs(r+1,c)+dfs(r,c+1)
            return p
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    return dfs(i,j)
