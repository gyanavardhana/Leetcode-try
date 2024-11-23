class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        r,c = len(box),len(box[0])
        res = [['.' for _ in range(r)] for _ in range(c)]
        for i in range(r):
            ep = c - 1
            for j in range(c -1, -1, -1):
                if box[i][j] == "*":
                    res[j][r - i -1] = '*'
                    ep = j-1
                elif box[i][j] == "#":
                    res[ep][r - i -1] = "#"
                    ep -= 1
        return res

        