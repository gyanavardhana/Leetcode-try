class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        dire = [(0,1),(1,0),(0,-1),(-1,0)]
        que = deque([(0,0,0)])
        vis = [[False] * n for _ in range(m)]
        vis[0][0] = True
        while que:
            x,y, obsr = que.popleft()
            if x==m-1 and y==n-1:
                return obsr
            for dx,dy in dire:
                nx,ny = x+dx, y+dy
                if 0<=nx<m and 0<=ny<n and not vis[nx][ny]:
                    vis[nx][ny] = True
                    if grid[nx][ny] == 0:
                        que.appendleft((nx,ny,obsr))
                    else:
                        que.append((nx,ny,obsr + 1))
        return -1