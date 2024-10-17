import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap, res = [], []
        for x, ch in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if x: heapq.heappush(heap, (x, ch))
        
        while heap:
            c1, ch1 = heapq.heappop(heap)
            if len(res) > 1 and res[-1] == res[-2] == ch1:
                if not heap: break
                c1, ch1, (c2, ch2) = c2, ch2, heapq.heappop(heap)
                res.append(ch2)
                if c2 + 1: heapq.heappush(heap, (c2 + 1, ch2))
            res.append(ch1)
            if c1 + 1: heapq.heappush(heap, (c1 + 1, ch1))
        
        return ''.join(res)
