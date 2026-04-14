class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #define directions for bfs
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        #define rows and cols for traverse
        rows = len(grid)
        cols = len(grid[0])
        #define counter for islands
        islands = 0
        #define bfs func
        def bfs(r, c):
            q = deque()
            grid[r][c] = "0"
            q.append((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr >= rows or 
                    nc >= cols or grid[nr][nc] == "0"):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = "0"
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
            
        return islands
        #search for island


