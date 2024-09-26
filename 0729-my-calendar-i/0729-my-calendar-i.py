class MyCalendar:

    def __init__(self):
        self.res = []
        

    def book(self, start: int, end: int) -> bool:
        ress = self.res
        for s,e in ress:
            if not(end<=s or start>=e):
                return False
        ress.append([start,end])
        self.res = ress
        return True

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)