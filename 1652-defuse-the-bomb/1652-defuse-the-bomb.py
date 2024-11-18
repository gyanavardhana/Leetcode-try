class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k==0:
            return [0]*n
        out = []
        if k>0:
            f = sum(code[:k])
            for i in range(n):
                f = f - code[i]+code[(k+i)%n]
                out.append(f)
        elif k<0:
            f = sum(code[k:])
            for i in range(n):
                out.append(f)
                f = f+code[i]-code[(k+i)%n]
        return out

        