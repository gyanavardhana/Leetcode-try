class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        tr = sum(nums)%p
        if tr == 0:
            return 0
        pr = 0
        ml = len(nums)
        rm = {0: -1}
        for i , num in enumerate(nums):
            pr = (pr + num) % p
            nr = (pr - tr) % p
            if nr in rm:
                ml = min(ml, i-rm[nr])
            rm[pr] = i
        print(rm)
        if ml < len(nums):
            return ml
        else:
            return -1