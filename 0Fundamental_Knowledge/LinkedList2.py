import random

class Node():
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next


class SingleList():
    def __init__(self, head=None):
        self.head = head

    def __len__(self):
        length = 0
        currentnode = self.head
        while currentnode != None:
            currentnode = currentnode.next
            length += 1
        return length


    def PrintLList(self):
        currentnode = self.head
        while currentnode != None:
            print(currentnode.data)
            currentnode = currentnode.next

    def SingleList2Arrary(self):
        output = []
        currentNode = self.head
        while currentNode != None:
            output.append(currentNode.data)
            currentNode = currentNode.next
        return output

    def RandomCreate(self, length):
        self.head = Node(random.int(0,length))
        currentNode = self.head
        for i in range(length-1):
            currentNode.next = Node(random.int(0,length))
            currentNode = currentNode.next
        return self.head

    def Array2SingleList(self, array):
        self.head = Node(array[0])
        currentNode = self.head
        for item in array[1:]:
            currentNode.next = Node(item)
            currentNode = currentNode.next
        return self.head

    @staticmethod
    def InsertOneElementBefore(LList, index, data):
        currentNode = LList.head
        i = 1
        while i < index-1 and currentNode.next is not None:
            i += 1
            currentNode = currentNode.next
        newNode = Node(data)
        newNode.next = currentNode.next
        currentNode.next = newNode
        return LList

    @staticmethod
    def InserOneElementAfter(LList,index,data):
        currentNode = LList.head
        i = 1
        while i < index and currentNode.next is not None:
            i += 1
            currentNode = currentNode.next
        newNode = Node(data)
        newNode.next = currentNode.next
        currentNode.next = newNode
        return LList

    def __reverse__(self):
        currentNode = self.head
        pre = None
        while currentNode:
            post = currentNode.next
            currentNode.next = pre
            pre = currentNode
            currentNode = post
        return SingleList(pre)

if __name__ == '__main__':
    singlelinklist = SingleList()
    array = [0,1,2,3,4,5,6,7,8,9,10,11,12]
    singlelinklist.Array2SingleList(array)
    output = singlelinklist.__reverse__().SingleList2Arrary()
    # head_after_add = singlelinklist.InsertOneElementBefore(singlelinklist,0,100)
    # head_after_add.PrintLList()
    # head_after_add = singlelinklist.InserOneElementAfter(singlelinklist,0,100)
    # print(head_after_add.__len__())
    # output = head_after_add.SingleList2Arrary()
    print(output)