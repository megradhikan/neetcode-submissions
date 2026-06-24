class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights: return []
        
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visited, prev_height):
            # Base cases: out of bounds, already visited, or too low (cannot flow "up")
            if (r < 0 or c < 0 or r == ROWS or c == COLS or 
                (r, c) in visited or heights[r][c] < prev_height):
                return
            
            visited.add((r, c))
            # Check all 4 directions
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])

        # Start DFS from Top and Bottom rows
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])            # Top (Pacific)
            dfs(ROWS - 1, c, atl, heights[ROWS-1][c]) # Bottom (Atlantic)

        # Start DFS from Left and Right columns
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])            # Left (Pacific)
            dfs(r, COLS - 1, atl, heights[r][COLS-1]) # Right (Atlantic)

        # Return cells that are in both sets
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res