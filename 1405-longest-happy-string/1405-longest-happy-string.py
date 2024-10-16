class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        res = []
        if a>0:
            heapq.heappush(heap, (-a, "a"))
        if b>0:
            heapq.heappush(heap, (-b, "b"))
        if c>0:
            heapq.heappush(heap, (-c, "c"))
        while heap:
            c1, ch1 = heapq.heappop(heap)
            if len(res)>=2 and res[-1]==ch1 and res[-2]==ch1:
                if not heap:
                    break
                c2, ch2 = heapq.heappop(heap)
                res.append(ch2)
                c2 += 1
                if c2<0:
                    heapq.heappush(heap, (c2, ch2))
                heapq.heappush(heap, (c1, ch1))
            else:
                res.append(ch1)
                c1+=1
                if c1<0:
                    heapq.heappush(heap, (c1,ch1))
        return ''.join(res)
        

        