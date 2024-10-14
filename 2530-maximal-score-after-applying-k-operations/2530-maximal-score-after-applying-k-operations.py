class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        res = 0
        maxi = []
        for i in nums:
            maxi.append(-i)
        heapq.heapify(maxi)
        while k:
            n = -heapq.heappop(maxi)
            res += n
            k -= 1
            p = -ceil(n/3)
            heapq.heappush(maxi, p)
        return res

        