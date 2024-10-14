class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        res = 0
        maxheap  = []
        for i in nums:
            maxheap.append(-i)
        heapq.heapify(maxheap)
        while k:
            s = -heapq.heappop(maxheap)
            res += s
            k -= 1
            p = -ceil(s / 3)
            heapq.heappush(maxheap, p)
        return res
        

        