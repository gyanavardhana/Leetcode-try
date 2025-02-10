class Solution:
    def clearDigits(self, s: str) -> str:
        s1 = []
        s2 = []
        for i in s:
            if not i.isalpha():
                s1.append(i)
            else:
                s2.append(i)
        if not s1:
            return s
        else:
            while len(s1) != 0:
                s1.pop(0)
                s2.pop(0)
        return "".join(s2)
        