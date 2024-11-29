class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        dire = [(0,1),(1,0),(-1,0),(0,-1)]
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        rows,cols = len(grid), len(grid[0])
        heap = [(0,0,0)]
        vis = [[False] * cols for _ in range(rows)]
        while heap:
            t,r,c = heapq.heappop(heap)
            if r == rows - 1 and c == cols - 1:
                return t
            if vis[r][c]:
                continue
            vis[r][c] = True
            for dr,dc in dire:
                nr,nc = r + dr, c + dc
                if 0<=nr<rows and 0<=nc<cols and not vis[nr][nc]:
                    if grid[nr][nc] <= t + 1:
                        heapq.heappush(heap, (t+1,nr,nc))
                    else:
                        diff = grid[nr][nc] - t
                        if diff %2 == 1:
                            heapq.heappush(heap, (grid[nr][nc],nr,nc))
                        else:
                            heapq.heappush(heap, (grid[nr][nc] +1, nr, nc))
        return -1

    
        