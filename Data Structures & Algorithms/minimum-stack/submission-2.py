class MinStack:

    def __init__(self):
        self.arr = []
        self.min = float('inf')
        

    def push(self, val: int) -> None:
        if not self.arr:
            self.arr.append(val)
            self.min = val
        else:
            if val < self.min:
                push = (2 * val - self.min)
                self.arr.append(push)
                self.min = val
            else:
                self.arr.append(val)

    def pop(self) -> None:
        if self.arr[-1] < self.min:
            ## encoded val
            self.min = 2*self.min - self.arr[-1] ## for previous min
        
        self.arr.pop()
        

    def top(self) -> int:
        top_element = self.arr[-1]
        if self.arr[-1] < self.min:
            ## encoded val
            top_element = self.min ## for current min
        
        return top_element

    def getMin(self) -> int:
        return self.min

        
