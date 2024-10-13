class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        maxval = float('-inf')
        for i in range(len(nums)):
            maxval = max(maxval,nums[i][0])
            heappush(heap, (nums[i][0], i, 0))
        res = [heap[0][0], maxval]
        ans = maxval - heap[0][0]
        while True:
            num,row,col = heappop(heap)
            col += 1
            if len(nums[row]) == col:
                return res
            heappush(heap, (nums[row][col],row,col))
            maxval = max(maxval, nums[row][col])
            diff = maxval - heap[0][0]
            if ans>diff:
                ans = diff
                res = [heap[0][0], maxval]
        return res

        

        
        