class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st = []
        a = 0
        b = 0
        for i in s:
            if i=='(':
                a+=1
            elif a:
                a-=1
            else:
                b+=1
        return a+b
        