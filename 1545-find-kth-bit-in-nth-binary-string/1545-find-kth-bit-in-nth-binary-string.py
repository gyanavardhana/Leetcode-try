class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        for _ in range(n-1):
            newb = "1"
            nn = len(s)
            for i in range(nn-1,-1,-1):
                if s[i] == '1':
                    newb += '0'
                else:
                    newb += '1'
            s += newb
        return s[k-1]
        