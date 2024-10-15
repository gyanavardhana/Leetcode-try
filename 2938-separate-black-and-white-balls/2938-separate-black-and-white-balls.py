class Solution:
    def minimumSteps(self, s: str) -> int:
        sw, b = 0, 0
        for i in s:
            if i=='0':
                sw += b
            else:
                b += 1
        return sw
        
        