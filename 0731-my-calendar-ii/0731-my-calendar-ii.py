class MyCalendarTwo:

    def __init__(self):
        self.res = []
        self.track = []
        
        
    def book(self, start: int, end: int) -> bool:
        for s,e in self.track:
            if not(end<=s or start>=e):
                return False
        for s,e in self.res:
            if not(end<=s or start>=e):
                self.track.append([max(start,s), min(end,e)])
        self.res.append([start,end])
        return True
        
        
        
        

        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)