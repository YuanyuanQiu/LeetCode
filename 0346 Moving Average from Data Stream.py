class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.ls = [0] * self.size
        self.num = 0
        

    def next(self, val: int) -> float:
        self.num = min(self.size,self.num + 1)
        self.ls.append(val)
        del self.ls[0]
        return sum(self.ls)/self.num
