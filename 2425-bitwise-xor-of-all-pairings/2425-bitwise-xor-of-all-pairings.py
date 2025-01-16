class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        x1 = 0
        x2 = 0
        for i in nums1:
            x1  ^= i
        for i in nums2:
            x2 ^= i
        res = 0
        if len(nums2)%2==1:
            res ^= x1
        if len(nums1)%2==1:
            res ^= x2
        return res
        