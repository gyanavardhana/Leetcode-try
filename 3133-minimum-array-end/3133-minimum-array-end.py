class Solution:
    def minEnd(self, n: int, x: int) -> int:
        ans = x
        n -= 1
        
        v = []
        for i in range(32):
            if not (1 << i) & x:
                v.append(i)
        
        while len(v) < 64:
            v.append(v[-1] + 1)
        
        curr = 0
        j = 0
        while curr != n:
            if (1 << j) & n:
                ans += (1 << v[j])
                curr += (1 << j)
            j += 1
        
        return ans
        