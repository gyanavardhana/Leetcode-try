class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxi,res=values[0],0
        for i in range(1,len(values)):
            maxi-=1
            res=max(res,maxi+values[i])
            maxi=max(maxi,values[i])
        return res
        