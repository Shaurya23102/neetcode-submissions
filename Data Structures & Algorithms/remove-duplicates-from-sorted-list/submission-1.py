# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        a = []

        while cur:
            if not a or a[-1] != cur.val:
                a.append(cur.val)
            cur = cur.next

        d = ListNode(0)
        cur = d

        for val in a:
            cur.next = ListNode(val)
            cur = cur.next

        return d.next      