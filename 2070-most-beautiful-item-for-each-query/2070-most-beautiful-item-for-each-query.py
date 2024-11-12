class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        beuties = [0]*len(queries)
        items = sorted(items, key = lambda x : (x[1], x[0]), reverse=True)
        for x in range(len(queries)):
            for y in range(len(items)):
                if queries[x] >= items[y][0]:
                    beuties[x] = items[y][1]
                    break            
        return beuties  
        