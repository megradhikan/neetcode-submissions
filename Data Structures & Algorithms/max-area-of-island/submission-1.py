class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        count=0
        biggest=0
        def sink(i,j):
            if (i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]==0):
                return 0
            grid[i][j]=0
            return(1+sink(i-1,j)+sink(i+1,j)+sink(i,j-1)+sink(i,j+1))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    count+=1
                    size=sink(i,j)
                    biggest=max(biggest,size)
        return biggest