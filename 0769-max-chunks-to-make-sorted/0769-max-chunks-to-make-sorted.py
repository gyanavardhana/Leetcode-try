class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        maxi, cnt = 0, 0
        for i in range(len(arr)):
            maxi = max(maxi, arr[i])
            if maxi == i:
                cnt += 1
        return cnt
        