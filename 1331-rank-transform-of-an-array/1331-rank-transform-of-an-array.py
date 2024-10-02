class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr1 = sorted(list(set(arr)))
        d = {}
        for i in range(len(arr1)):
            d[arr1[i]] = i+1
        res = []
        for i in range(len(arr)):
            res.append(d[arr[i]])
        return res
        
        
        