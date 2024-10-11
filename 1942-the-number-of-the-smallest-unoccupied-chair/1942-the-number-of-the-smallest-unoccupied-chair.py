class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        e = []
        n = len(times)
        for idd,(a,d) in enumerate(times):
            e.append((a,idd,'arrive'))
            e.append((d,idd,'leave'))
        e.sort(key=lambda x:(x[0],x[2]=='arrive'))
        ac = []
        oc = {}
        cc = 0
        for t,idd,et in e:
            if et == 'arrive':
                if ac:
                    c = heappop(ac)
                else:
                    c = cc
                    cc += 1
                oc[idd] = c
                if idd == targetFriend:
                    return c
            else:
                c = oc[idd]
                heapq.heappush(ac,c)


        