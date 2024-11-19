class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        d = defaultdict(int)
        curr = 0
        for i in range(len(nums)):
            d[nums[i]] += 1
            curr += nums[i]

            if i>=k:
                d[nums[i-k]] -= 1
                if d[nums[i-k]] == 0:
                    del d[nums[i-k]]
                curr -= nums[i-k]
            if len(d) == k:
                res = max(res, curr)
        return res
