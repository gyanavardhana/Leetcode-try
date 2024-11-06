class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        swap = True
        while swap:
            swap = False
            for i in range(1,len(nums)):
                if nums[i]<nums[i-1] and nums[i].bit_count() == nums[i-1].bit_count():
                    swap = True
                    nums[i-1], nums[i] = nums[i],nums[i-1]
        return sorted(nums) == nums