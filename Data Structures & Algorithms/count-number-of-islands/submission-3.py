class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        
        def water(r, c):
            if r >= len(grid) or r < 0 or c >= len(grid[0]) or c < 0 or grid[r][c] == "0":
                return
            else:
                grid[r][c] = "0"
            
            water(r+1, c)
            water(r-1, c)
            water(r, c+1)
            water(r, c-1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    count += 1
                    water(r, c)

        return count