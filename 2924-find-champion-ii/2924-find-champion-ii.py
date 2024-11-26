class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        d = defaultdict(int)
        for u,v in edges:
            d[v] += 1
        ans , pc = 0,0
        for i in range(n):
            if not d[i]:
                ans = i
                pc += 1
            if pc == 2:
                return -1
        return ans

        