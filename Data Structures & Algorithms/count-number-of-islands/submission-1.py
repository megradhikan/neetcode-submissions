class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count=0
        def sink(i,j):
            if (i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]=="0"):
                return
            grid[i][j]="0"
            sink(i-1,j)
            sink(i+1,j)
            sink(i,j-1)
            sink(i,j+1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    count+=1
                    sink(i,j)
        return count
    
    

