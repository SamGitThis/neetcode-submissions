class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        nr = len(grid)
        nc = len(grid[0])
        q = deque()
        visited = set()
        dist = 0

        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))

        def adds(r, c):
            if r < 0 or r == nr or c < 0 or c == nc or (r, c) in visited or grid[r][c] == -1:
                return
            visited.add((r, c))
            q.append((r, c))

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                adds(r+1, c)
                adds(r, c+1)
                adds(r-1, c)
                adds(r, c-1)
            dist += 1