# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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