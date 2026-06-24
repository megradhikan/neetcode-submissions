class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count=0
        rows=len(grid)
        cols=len(grid[0])
        def dfs(i,j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]=="0":
             return
            else:
                grid[i][j]="0"
                dfs(i-1,j)
                dfs(i+1,j)
                dfs(i,j-1)
                dfs(i,j+1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1":
                    count+=1
                    dfs(i,j)
        return count
    
    
        
