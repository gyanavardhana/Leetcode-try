class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def gsb(num):
            c = 0
            while num:
                c += 1
                num &= num -1
            return c
        sbc = []
        for i in nums:
            sbc.append(gsb(i))
        swap = True
        while swap:
            swap = False
            for i in range(1,len(nums)):
                if nums[i]<nums[i-1] and sbc[i] == sbc[i-1]:
                    swap = True
                    nums[i-1], nums[i] = nums[i],nums[i-1]
        return sorted(nums) == nums