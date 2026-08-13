# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        count = 0 
        cur = head
        while cur:
            count+=1
            cur = cur.next
        k = count//2
        if count == 1:
            return head  

        cur = head
        for i in range(k-1):
            cur = cur.next
            
        return cur.next
            
            
