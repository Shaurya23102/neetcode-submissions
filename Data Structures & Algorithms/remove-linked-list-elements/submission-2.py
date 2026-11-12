class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        a = []
        cur = head
        # Step 1: Copy linked list values into array
        while cur:
            a.append(cur.val)
            cur = cur.next

        # Step 2: Remove all occurrences of val from array
        a = [x for x in a if x != val]

        # Step 3: Convert array back into linked list
        dummy = ListNode(0)
        cur = dummy
        for x in a:
            cur.next = ListNode(x)
            cur = cur.next

        return dummy.next
