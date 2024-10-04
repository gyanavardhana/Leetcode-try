class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        l = skill
        l.sort()
        ts = l[0]+l[-1]
        cs = 0
        for i in range(len(l)//2):
            if l[i]+l[-i-1] != ts:
                return -1
            else:
                cs+=(l[i]*l[-i-1])
        return cs
        
        