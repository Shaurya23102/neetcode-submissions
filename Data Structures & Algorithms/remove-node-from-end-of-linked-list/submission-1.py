class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        a = []
        cur = head

        # Copy linked list values into array
        while cur:
            a.append(cur.val)
            cur = cur.next

        # Remove nth node from the end
        a.pop(len(a) - n)

        # Convert array back into linked list
        dummy = ListNode(0)
        cur = dummy

        for x in a:
            cur.next = ListNode(x)
            cur = cur.next

        return dummy.next