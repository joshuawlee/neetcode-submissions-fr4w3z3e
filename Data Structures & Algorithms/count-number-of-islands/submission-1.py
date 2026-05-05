from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #define directions
        directions = [[1,0], [0,1], [-1, 0], [0, -1]]

        rows = len(grid)
        cols = len(grid[0])

        islands = 0

        def bfs(r, c):
            q = deque()
            q.append([r, c])
            grid[r][c] = "0"

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == "0":
                        continue
                    
                    q.append([nr, nc])
                    grid[nr][nc] = "0"

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    bfs(r, c)
        
        return islands