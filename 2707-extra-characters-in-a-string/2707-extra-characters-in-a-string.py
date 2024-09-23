class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        Set = set(dictionary)
        dp = [0] * (len(s)+1)
        n = len(s)
        for i in range(n-1,-1,-1):
            dp[i] = dp[i+1]+1
            for l in range(1,n-i+1):
                if s[i:i+l] in Set:
                    print(dp[i],dp[i+l])
                    dp[i] = min(dp[i],dp[i+l])
                    print(dp[i],dp[i+l],'after')
        print(dp)
        return dp[0]
        
        