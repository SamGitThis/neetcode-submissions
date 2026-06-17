class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        nr, nc = len(grid), len(grid[0])
        a = 0
        isa = [0]
        
        def dfs(r, c):
            nonlocal a
            if r < 0 or r >= nr or c < 0 or c >= nc or grid[r][c] == 0:
                return
            
            a += 1
            grid[r][c] = 0
            dfs(r, c+1)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r-1, c)
        
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == 1:
                    dfs(r, c)
                    isa.append(a)
                    a = 0
        
        return max(isa)