class CustomStack:

    def __init__(self, maxSize: int):
        self.res = []
        self.k = maxSize
        
    def push(self, x: int) -> None:
        if len(self.res)<self.k:
            self.res.append(x)
            
    def pop(self) -> int:
        if not self.res==[]:
            return self.res.pop()
        return -1
    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.res))):
            self.res[i] += val


    

        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
