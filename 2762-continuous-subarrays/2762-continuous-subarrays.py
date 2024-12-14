class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        def sl(arr):
            c = 0
            n = len(arr)
            result = []
            for window_size in range(1, n + 1):
                for i in range(n - window_size + 1):
                    subarray = arr[i:i + window_size]
                    if check(subarray):
                        c+=1
            return c
        def check(l):
            if len(l) == 1:
                return True
            for i in range(len(l)):
                for j in range(i+1,len(l)):
                    if abs(l[i] - l[j])>2:
                        return False
            return True
        return sl(nums)
        