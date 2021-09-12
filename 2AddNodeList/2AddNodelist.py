#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LList():
    def __init__(self, head:ListNode = None):
        self.head = head

    def PrintLList(self):
        currentNode = self.head
        result = []
        while currentNode.next is not None:
            result.append(currentNode.val)
            currentNode = currentNode.next
        print(result)

# test cases:
# l1 is None, SOLVED
# l1 and l2 share the same length, l1 = [1,2,6], l2 = [2,3,4], result = [3,5,0,1]
# l1 != l2 in length, l1 = [1,2,6], l2 = [2,3,4,5], result = [3,5,0,6]
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode() # LList.head = None
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        l1_currentNode = l1
        l2_currentNode = l2
        result_currentNode = result
        carry = 0
        while l1_currentNode.next is not None or l2_currentNode.next is not None:
            sum = l1_currentNode.val + l2_currentNode.val + carry
            carry = int(sum / 10)
            rest = int(sum % 10)
            if result_currentNode is None:
                result_currentNode = ListNode(rest)
            result_currentNode.val = rest
            result_currentNode.next = ListNode()

            if l1_currentNode.next is None:
                l1_currentNode.next = ListNode()
            if l2_currentNode.next is None:
                l2_currentNode.next = ListNode()

            l1_currentNode = l1_currentNode.next
            l2_currentNode = l2_currentNode.next
            result_currentNode = result_currentNode.next

        sum = l1_currentNode.val + l2_currentNode.val + carry
        carry = int(sum / 10)
        rest = int(sum % 10)
        result_currentNode.val = rest
        if carry >= 1:
            result_currentNode.next = ListNode(carry)
        return result


class OtherPeopleSolution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        result_tail = result
        carry = 0

        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry, out = divmod(val1 + val2 + carry, 10)

            result_tail.next = ListNode(out)
            result_tail = result_tail.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return result.next


if __name__=='__main__':


    def LListfromArray(array):
        head = ListNode()
        currentNode = head
        for val in array:
            currentNode.val = val
            newNode = ListNode()
            currentNode.next = newNode
            currentNode = currentNode.next
        linkedllist = LList(head)
        return linkedllist

    l1 = [1,2,6]
    l2 = [2,3,4,5]
    LinkedList_1 = LListfromArray(l1)
    LinkedList_2 = LListfromArray(l2)
    LinkedList_1.PrintLList()
    LinkedList_2.PrintLList()


    solution = Solution()
    Head = solution.addTwoNumbers(LinkedList_1.head,LinkedList_2.head)
    while Head.next != None:
        print(Head.val)
        Head = Head.next
