class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        fresh, count = 0, -1
        rotten = deque()

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotten.append((i,j))

        if fresh == 0:
            return 0
            
        moves = [[0,1], [0,-1], [1,0], [-1,0]]

        while rotten:
            count += 1
            l = len(rotten)
            for _ in range(l):
                rw, cl = rotten.popleft()
                for mov in moves:
                    row, col = rw + mov[0], cl + mov[1]
                    if (row >= 0 and row < r) and (col >= 0 and col < c):
                        if grid[row][col] == 1:
                            fresh -= 1
                            grid[row][col] = 2
                            rotten.append((row,col))

        print(fresh, count)
        if fresh == 0:
            return count

        return -1