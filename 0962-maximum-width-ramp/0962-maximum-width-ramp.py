class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        st = []
        n = len(nums)
        for i in range(n):
            if not st or nums[i]<nums[st[-1]]:
                st.append(i)
        m = 0
        for i in range(n-1,-1,-1):
            while st and nums[i]>=nums[st[-1]]:
                m = max(m, i-st.pop())
        return m
        
