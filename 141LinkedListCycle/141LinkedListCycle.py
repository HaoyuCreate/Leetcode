# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        #1. check if head is None
        if not head:
            return False
        curr = slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def detectCycle(self, head: ListNode) -> ListNode:
        start = None
        # 1. check if head is None
        if not head:
            return start
        curr = slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        # 2. check is the iteration stops by finding an end or finding a loop
        if not fast or not fast.next:
            return start

        # 3. return the start of the loop
        while slow != curr:
            slow = slow.next
            curr = curr.next
        return curr

    def detectCycle2(self, head: ListNode) -> ListNode:
        '''A better grammer by while{}else{}'''
        start = None
        # 1. check if head is None
        if not head:
            return start
        curr = slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            # 2. check is the iteration stops by finding an end or finding a loop
            return start

        # 3. return the start of the loop
        while slow != curr:
            slow = slow.next
            curr = curr.next
        return curr