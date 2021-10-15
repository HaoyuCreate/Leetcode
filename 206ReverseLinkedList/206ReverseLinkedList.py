# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Node():
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class Solution:
    def reverseList(self, head):
        curr = head
        pre = None
        while curr:
            post = curr.next
            curr.next = pre
            pre = curr
            curr = post
        head = pre
        return head

    def Array2SingleList(self, array):
        head = Node(array[0])
        currentNode = head
        for item in array[1:]:
            currentNode.next = Node(item)
            currentNode = currentNode.next
        return head

    def SingleList2Arrary(self, head):
        output = []
        currentNode = head
        while currentNode != None:
            output.append(currentNode.data)
            currentNode = currentNode.next
        return output

if __name__ == '__main__':
    solution = Solution()
    input = [1, 2, 3, 4, 5]
    head = solution.Array2SingleList(input)
    singlelist = solution.reverseList(head)
    output = solution.SingleList2Arrary(singlelist)
    print(output)