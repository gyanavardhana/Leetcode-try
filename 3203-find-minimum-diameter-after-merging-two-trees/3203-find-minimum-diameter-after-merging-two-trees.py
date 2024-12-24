class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        
        def calc(edges):

            if len(edges) == 0: return 0
            elif len(edges) == 1: return 1
            graph = defaultdict(list)

            for x,y in edges:
                graph[x].append(y)
                graph[y].append(x)

            d = 0
            visited = set()
            visited.add(edges[0][0])
            
            def path(node):
                
                nonlocal d
                top_two = []
                
                for nei in graph[node]:
                    if nei in visited: continue
                    visited.add(nei)
                    x = path(nei)
                    heapq.heappush(top_two, x)
                    if len(top_two) > 2:
                        heapq.heappop(top_two)

                d = max(d, sum(top_two))

                return max(top_two)+1 if len(top_two) != 0 else 1
            
            path(edges[0][0])

            return d

        d1 = calc(edges1)
        d2 = calc(edges2)
        ans = (d1 // 2) + (d1 % 2)
        ans += (d2 // 2) + (d2 % 2)

        return max(ans+1, d1, d2)
        