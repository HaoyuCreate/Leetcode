# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, node):
        if not node:
            return

        pre = None
        curr = node

        while curr:
            post = curr.next
            curr.next = pre
            pre = curr
            curr = post

        return pre

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
            # split the list
        nNode = 0
        curr = head

        while curr:
            nNode += 1
            curr = curr.next

        mid = ceil(nNode / 2.0)
        curr = head
        post = None
        while mid > 1:
            post = curr.next
            curr = post
            mid -= 1
        l1 = head
        l2 = post

        curr1 = l1
        curr2 = l2

        # reverse the second list
        new_l2 = self.reverseList(l2)
        curr1 = l1
        curr2 = new_l2

        # merge two list
        while curr1 and curr2:
            post1 = curr1.next
            post2 = curr2.next

            curr1.next = curr2
            curr2.next = post1

            curr1 = post1
            curr2 = post2
        return l1
