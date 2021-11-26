class Stack:
    def __init__(self) -> None:
        self.li = []

    def append(self,data):
        self.li.append(data)
    
    def pop(self):
        if self.getSize() > 0:
            return self.li.pop()

    def getSize(self):
        return len(self.li)

class Queue:
    def __init__(self) -> None:
        self.li = []

    def enqueue(self,data):
        self.li.append(data)

    def pop(self):
        if self.getSize() > 0:
            return self.li.pop(0)

    def getSize(self):
        return len(self.li)

    def clear(self):
        self.li.clear()