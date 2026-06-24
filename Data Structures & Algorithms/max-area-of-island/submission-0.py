class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        count=0
        rows=len(grid)
        cols=len(grid[0])
        maxa=0
        def dfs(i,j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]==0:
             return 0
            else:
                grid[i][j]=0
                return (1+dfs(i-1,j)+dfs(i+1,j)+dfs(i,j-1)+dfs(i,j+1))
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    a=dfs(i,j)
                    maxa=max(a,maxa)
        return maxa