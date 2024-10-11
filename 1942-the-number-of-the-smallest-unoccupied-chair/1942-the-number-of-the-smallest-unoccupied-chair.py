class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        e = []
        for i,(a,d) in enumerate(times):
            e.append((a,0,i))
            e.append((d,1,i))
        e.sort(key=lambda x:(x[0],x[1]=='0'))
        ac = []
        for i in range(len(times)):
            heapq.heappush(ac,i)
        d = {}
        for t,e,idd in e:
            if e==0:
                c = heapq.heappop(ac)
                d[idd] = c
                if idd == targetFriend:
                    return c
            else:
                c = d[idd]
                heapq.heappush(ac,c)


        