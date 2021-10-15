# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# at least two pointers lo and lk
# co = min(lo,lk)
# O(m*N_k), m is the length of the list, N_k is the length of the k-th linked list

class Solution:
    def mergeKLists(self, lists):
        for i in range(len(lists)):
            head = self.Array2SingleList(lists[i])
            if head:
                lo = head # lo is the head of linked list i
                for item in lists[i+1:]:
                    head2 = self.Array2SingleList(item)
                    if head2:
                        l_tmp = head2 # l_tep is the head of liked list from i+1 to final
                        lo = self.mergeTwoLists(lo,l_tmp)
                return lo
        return []

    def mergeTwoLists(self,l1,l2):
        dummy = ListNode(None)
        curr = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = ListNode(l1.val)
                l1 = l1.next
            else:
                curr.next = ListNode(l2.val)
                l2 = l2.next
            curr = curr.next
        curr.next = l1 if l1 else l2
        return dummy.next

    def Array2SingleList(self, array):
        if len(array)>0:
            head = ListNode(array[0])
            currentNode = head
            for item in array[1:]:
                currentNode.next = ListNode(item)
                currentNode = currentNode.next
        else:
            head = None
        return head

    def SingleList2Arrary(self,head):
        output = []
        if head:
            currentNode = head
            while currentNode != None:
                output.append(currentNode.val)
                currentNode = currentNode.next
        return output

if __name__ == '__main__':
    solution = Solution()
    lists = [[],[1,2,3],[]]

    head = solution.mergeKLists(lists)
    output = solution.SingleList2Arrary(head)
    print(output)