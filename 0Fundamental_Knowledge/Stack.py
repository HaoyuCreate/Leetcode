class Node:
    def __init__(self,val=None,next=None):
        self.val = val
        self.next = next


class Stack:
    def __init__(self,maxsize:int=None):
        self.array = []
        self.top = -1
        self.maxsize = maxsize

    def Push(self,value):
        self.array.append(value)
        self.top += 1

    def Pop(self):
        if self.top > -1:
            self.top -= 1
            return self.array.pop()
        else:
            return None

    def Clear(self):
        pass

if __name__=="__main__":
    stack = Stack(5)