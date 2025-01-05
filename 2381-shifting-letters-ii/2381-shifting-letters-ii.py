class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        arr = [0] * n
        for l,r,d in shifts:
            if d==1:
                arr[l] += 1
                if r+1<n:
                    arr[r+1] -= 1
            else:
                arr[l] -= 1
                if r+1<n:
                    arr[r+1] += 1
        for i in range(1, n):
            arr[i] += arr[i-1]
        res = []
        for i in range(n):
            sh = (arr[i] % 26 + 26) % 26
            ch = (ord(s[i]) - ord('a') + sh) % 26
            res.append(chr(ord('a') + ch))
        return "".join(res)
        