class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.array = [0] * capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n


    def pushback(self, n: int) -> None:
        if(self.length >= self.capacity):
            self.resize()
        self.array[self.length] = n
        self.length += 1


    def popback(self) -> int:
        popped_element = self.array[self.length-1]
        self.array[self.length-1] = 0
        self.length -= 1
        return popped_element
 

    def resize(self) -> None:
        old_capacity = self.capacity
        self.capacity *= 2
        self.array[old_capacity:self.capacity] = list(range(0,old_capacity,1))

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity
