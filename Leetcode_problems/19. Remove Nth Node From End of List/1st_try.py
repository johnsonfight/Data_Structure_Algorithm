# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getListLen(self, head: Optional[ListNode]):
        curr = head.next
        len = 1
        while curr:
            curr = curr.next
            len += 1
        return len

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len = self.getListLen(head)
        curr = head

        if len == 1:
            return None

        if len == n:
            return head.next

        for i in range(len - n - 1):
            curr = curr.next
        if curr.next:
            if curr.next.next:
                curr.next = curr.next.next
            else:
                curr.next = None
        return head
