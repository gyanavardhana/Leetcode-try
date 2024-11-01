class Solution:
    def makeFancyString(self, s: str) -> str:
        res = ""
        ls = ""
        c = 0
        for i in range(len(s)):
            if(s[i] == ls):
                c += 1
            else:
                c = 1
                ls = s[i]
            if c>2:
                continue
            res += s[i]
        return res
        

            

