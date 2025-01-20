class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n = len(arr)
        row, col = len(mat), len(mat[0])
        index = 0
        m1 = {}
        pos = [[0, 0] for _ in range(row * col + 1)]
        
        for i in range(row):
            for j in range(col):
                pos[mat[i][j]] = [i, j]
        
        while index < n:
            i, j = pos[arr[index]]
            m1['R' + str(i)] = m1.get('R' + str(i), 0) + 1
            m1['C' + str(j)] = m1.get('C' + str(j), 0) + 1
            if m1['R' + str(i)] == col or m1['C' + str(j)] == row:
                return index
            index += 1
        
        return -1
        