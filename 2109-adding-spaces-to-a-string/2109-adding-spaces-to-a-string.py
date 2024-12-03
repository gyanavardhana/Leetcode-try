class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        pi = 0
        for si in spaces:
            res.append(s[pi: si])
            res.append(" ")
            pi = si
        res.append(s[pi:])
        return "".join(res)
        