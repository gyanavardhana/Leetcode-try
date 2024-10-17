
class Solution:
    def maximumSwap(self, num: int) -> int:
        heap = [] 
        l = list(str(num))
        for i, v in enumerate(l):
            heapq.heappush(heap, (-int(v),-i))
        end = 0
        while heap and end != 1:
            mele, mind = heapq.heappop(heap)
            mele *= -1
            mind *= -1
            for i,v in enumerate(l):
                if mele > int(v):
                    temp = l[i]
                    l[i] = str(mele)
                    l[mind] = temp
                    end = 1
                    break
                elif mind == i:
                    break
        return int(''.join(l))
        