class Solution:
    def check(self, nums: List[int], queries: List[List[int]], limit: int) -> bool:
        arr = [0] * (len(nums)+1)
        for i in range(0, limit):
            arr[queries[i][0]] -= queries[i][2]
            arr[queries[i][1]+1]+=queries[i][2]

        dec = 0
        Sum = 0
        for i in range(0, len(nums)):
            dec += arr[i]
            if nums[i]+dec>0: Sum += nums[i]
        
        return Sum==0

    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        Sum = 0
        for i in range(0, len(nums)):
            Sum+=nums[i]
        
        if Sum == 0: return 0
        n = len(nums)
        
        l, r = 1, len(queries)
        res = -1

        while l <= r: 
            mid = (l+r)//2
            if self.check(nums, queries, mid): 
                res = mid
                r = mid-1
            else: 
                l = mid+1
        
        return res