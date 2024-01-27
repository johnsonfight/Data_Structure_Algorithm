class DynamicArray:
    
    def __init__(self, capacity: int):
        self.DA = [None] * capacity
        self.size = 0
        self.capacity = capacity

    def get(self, i: int) -> int:
        return self.DA[i]

    def set(self, i: int, n: int) -> None:
        if self.DA[i] == None:
            self.size += 1
        self.DA[i] = n
        
    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()

        self.DA[self.size] = n
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        return self.DA[self.size]

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        self.DA += [None] * self.capacity

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        print(self.DA)
        return self.capacity