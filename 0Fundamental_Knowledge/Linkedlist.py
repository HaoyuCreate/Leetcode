import math
import random

class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None


class SingleLinkList:
    def __init__(self,head=Node()):
        self.head = head

    def __len__(self):
        length = 0
        currentNode = self.head
        while currentNode.next is not None:
            length += 1
            currentNode = currentNode.next
        return length

    def PrintLList(self):
        currentNode = self.head
        result = []
        while currentNode.next is not None:
            result.append(currentNode.data)
            currentNode = currentNode.next
        print(result)

    def RandomCreate(self,length):
        currentNode = self.head
        for i in range(length):
            currentNode.data = random.randint(0,9)
            currentNode.next = Node()
            currentNode = currentNode.next
        return self.head

    def CreatefromArray(self,array):
        currentNode = self.head
        for item in array:
            currentNode.data = item
            currentNode.next = Node()
            currentNode = currentNode.next

# test case: index<1 || index>length
#            LListHead = None
def InsertOneElementBefore(LList,index,data):
    '''
    insert a new element before the index-th element
    '''
    currentNode = LList.head
    for i in range(index-2): # index = 10, length = 10, insert in 9-th as required
        currentNode = currentNode.next # currentNode = 8
    # print(currentNode.data)
    # print(currentNode.next.data)
    newNode = Node(data)
    newNode.next = currentNode.next
    currentNode.next = newNode
    return LList

def InserOneElementAfter(LList,index,data):
    '''
    insert a new element after the index-th element
    '''
    currentNode = LList.head
    for i in range(index-1):
        currentNode = currentNode.next
    newNode = Node(data)
    newNode.next = currentNode.next
    currentNode.next = newNode
    return LList



if __name__ =='__main__':
    singlelinklist = SingleLinkList()
    array = [0,1,2,3,4,5,6,7,8,9,10,12]
    singlelinklist.CreatefromArray(array)
    singlelinklist.PrintLList()
    # head_after_add = InsertOneElementBefore(singlelinklist,10,9)
    # head_after_add.PrintLList()
    head_after_add = InserOneElementAfter(singlelinklist,12,13)
    head_after_add.PrintLList()




