class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ts = sum(nums)
        if abs(target) > ts:
            return 0 
        dp = [0] * (2 * ts + 1)
        dp[ts] = 1

        for n in nums:
            nedp = [0] * (2 * ts + 1)
            for s in range(-ts , ts+1):
                if dp[s + ts] > 0:
                    nedp[s + n + ts] += dp[s + ts]
                    nedp[s - n + ts] += dp[s + ts]
            dp = nedp
        return dp[target + ts]
        