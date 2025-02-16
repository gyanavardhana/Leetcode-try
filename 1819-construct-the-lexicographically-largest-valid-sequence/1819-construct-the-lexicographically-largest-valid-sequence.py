class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        res = [0]*(2*n-1)
        nums = [0]*(n+1)
        nums[0]=1
        def helper(i):
            if all(nums):
                return True
            for i in range(i, 2*n-1):
                for num in range(n, 0, -1):
                    if nums[num]:
                        continue
                    if num>1 and i+num>=2*n-1:
                        continue
                    if res[i]==0 and res[i+(num if num>1 else 0)]==0:
                        res[i] = res[i+(num if num>1 else 0)] = num
                        nums[num]=1
                        if helper(i+1):
                            return True
                        else:
                            res[i] = res[i+(num if num>1 else 0)] = 0
                            nums[num]=0
            return False
        helper(0)
        return res
        