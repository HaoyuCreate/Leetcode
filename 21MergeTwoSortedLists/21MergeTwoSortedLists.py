# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Node():
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

# at least two pointerx c1 and c2
# co = min(c1,c2)
# O(m+n)
# l1 and l2 do not share the same length --> where not (c1 and c2 are None)
class Solution:
    def mergeTwoLists(self, l1_head, l2_head):
        c1 = l1_head
        c2 = l2_head
        dummy = Node(None)
        cout = dummy
        while c1 and c2:
            if c1.data <= c2.data:
                cout.next = Node(c1.data)
                c1 = c1.next
            else:
                cout.next = Node(c2.data)
                c2 = c2.next
            cout = cout.next
        cout.next = c1 if c1 else c2
        return dummy.next

    def Array2SingleList(self, array):
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

if __name__ == '__main__':
    solution = Solution()
    i1 = []#[1, 2, 4]
    i2 = []#[1, 3, 4]
    l1 = solution.Array2SingleList(i1)
    l2 = solution.Array2SingleList(i2)

    head = solution.mergeTwoLists(l1,l2)
    output = solution.SingleList2Arrary(head)
    print(output)