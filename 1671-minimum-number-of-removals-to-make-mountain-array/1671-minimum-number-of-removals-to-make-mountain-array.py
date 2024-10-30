class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        left, right = [1] * len(nums), [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    left[i] = max(left[i], left[j] + 1)
        for i in range(len(nums)-1,-1,-1):
            for j in range(len(nums)-1,i,-1):
                if nums[i]>nums[j]:
                    right[i] = max(right[i], right[j] + 1)
        ans = 0
        for i in range(len(nums)):
            if (left[i] !=1 and right[i] != 1):
                ans = max(ans, left[i]+right[i])
        
        return len(nums) - ans + 1