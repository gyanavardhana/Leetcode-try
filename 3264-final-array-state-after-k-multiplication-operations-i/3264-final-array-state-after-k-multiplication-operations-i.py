class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        l = []
        for i,num in enumerate(nums):
            heappush(l,(num, i))
        while(k):
            x,i = heappop(l)
            x *= multiplier
            heappush(l,(x,i))
            k-=1
        for x,i in l:
            nums[i] = x
        return nums
        