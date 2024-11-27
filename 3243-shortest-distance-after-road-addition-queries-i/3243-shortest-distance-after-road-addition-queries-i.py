class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def djs(n,adj,src,dest):
            d = [float('inf')] * n
            d[src] = 0
            pq = [(0,src)]
            while pq:
                de,u = heapq.heappop(pq)
                for v, w in adj[u]:
                    if d[u] + w < d[v]:
                        d[v] = d[u] + w
                        heapq.heappush(pq,(d[v],v))
            if d[dest] == float('inf'):
                return -1
            else:
                return d[dest]
        adj = defaultdict(list)
        for i in range(n-1):
            adj[i].append((i+1,1))
        ans = []
        for u,v in queries:
            adj[u].append((v,1))
            ans.append(djs(n,adj,0,n-1))
        return ans
        