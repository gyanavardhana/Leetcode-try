from collections import deque
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        dire = {
            1:[0,1],
            2:[0,-1],
            3:[1,0], 
            4:[-1,0]
        }
        deq = deque([(0,0,0)])
        vis = [[False] * n for i in range(m)]
        while deq:
            cost,x,y = deq.popleft()
            if(x,y) == (m-1, n-1):
                return cost
            if vis[x][y]:
                continue
            vis[x][y] = True
            for direc, [dx,dy] in dire.items():
                nx,ny = x+dx,y+dy
                if 0<=nx<m and 0<=ny<n and not vis[nx][ny]:
                    if grid[x][y] == direc:
                        deq.appendleft((cost,nx,ny))
                    else:
                        deq.append((cost+1,nx,ny))
        return -1