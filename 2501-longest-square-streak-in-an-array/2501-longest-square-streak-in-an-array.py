class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        s = set(nums)
        m = -1
        for i in nums:
            c = 0
            curr = i
            while curr in s:
                c += 1
                curr = curr ** 2
            if c >= 2:
                m = max(c,m)
        return m