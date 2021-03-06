# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# O(2n) --> O(n)
# initial idea is going through the linked list first and get the length
# length - n = order in ACSE
#########
# n can be larger than the length
# length can be zero
# length - n can be zero

class Node():
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        position = length - n + 1

        if position > 1 and position< length+1:
            # move to the index-1th node
            curr = head
            i = 1
            while i < position -1 and curr.next is not None:
                curr = curr.next
                i += 1

            # remove the index-th node
            # length should larger than 2
            if curr.next.next:
                curr.next = curr.next.next
            else:
                curr.next = None
            return head
        elif position == 1:
            curr = head.next
            head = curr
            return head
        else:
            return None

    def _removeNthFromEnd(self,head,n):
        '''two path method'''
        length = 1
        dummy = Node(None,head) # real lenth l = length - 1
        curr = dummy
        while curr:
            length += 1
            curr = curr.next

        position = length - n
        i = 1
        curr = dummy
        while i < position-1 and curr.next:
            i += 1
            curr = curr.next
        if curr.next:
            curr.next = curr.next.next
            return dummy.next
        else:
            return None

    def removeNthFromEnd2(self, head, n):
        dummy = Node(None,None)
        dummy.next = head
        curr = dummy
        first = curr # the first pointer
        second = curr # the second pointer
        i = 1
        j = 1
        while first:
            first = first.next
            i += 1
            if i-n>2:
                second = second.next
        curr = second
        if curr.next:
            curr.next = curr.next.next
            return dummy.next # not the head, it is very important!!!!
        else:
            return None



    def Array2SingleList(self,array):
        head = Node(array[0])
        currentNode = head
        for item in array[1:]:
            currentNode.next = Node(item)
            currentNode = currentNode.next
        return head

    def SingleList2Arrary(self,head):
        output = []
        currentNode = head
        while currentNode != None:
            output.append(currentNode.data)
            currentNode = currentNode.next
        return output

if __name__=='__main__':
    solution = Solution()
    input = [1,2]
    n = 1

    head = solution.Array2SingleList(input)
    singlelist = solution._removeNthFromEnd(head,n)
    output = solution.SingleList2Arrary(singlelist)
    print(output)