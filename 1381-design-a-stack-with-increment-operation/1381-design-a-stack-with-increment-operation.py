class CustomStack:

    def __init__(self, maxSize: int):
        self.res = []
        self.k = maxSize
        

    def push(self, x: int) -> None:
        if not self.isFull():
            self.res.append(x)

    def pop(self) -> int:
        if not self.isEmpty():
            return self.res.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(len(self.res)):
            if i<=k-1:
                self.res[i] = self.res[i] + val

    def isEmpty(self) -> bool:
        if len(self.res)==0:
            return True
        return False

    def isFull(self) -> bool:
        if len(self.res)==self.k:
            return True
        return False

        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)