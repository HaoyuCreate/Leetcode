# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #         slow = head
        #         if head:
        #             fast = head.next
        #         else:
        #             return False
        #         curr = head

        #         while slow != fast:
        #             if not fast or not fast.next:
        #                 return False
        #             slow = slow.next
        #             fast = fast.next.next
        #         return True

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

        # return the start of the loop
        # while slow != curr:
        #     slow = slow.next
        #     curr = curr.next
        # return curr