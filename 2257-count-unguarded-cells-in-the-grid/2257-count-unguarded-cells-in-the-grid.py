class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0]*n for i in range(m)]
        for i,j in guards:
            grid[i][j] = 1
        for i,j in walls:
            grid[i][j] = 1
        dire = [(-1,0),(1,0),(0,-1),(0,1)]
        for r,c in guards:
            for dr, dc in dire:
                nr, nc = r+dr, c+dc
                while 0<=nr<m and 0<=nc<n:
                    if grid[nr][nc] == 1:
                        break
                    if grid[nr][nc] == 0:
                        grid[nr][nc] = 2
                    nr += dr
                    nc += dc
        c = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    c += 1

        return c
        