class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        a = []

        while cur:
            a.append(cur.val)
            cur = cur.next

        b = []
        mx = float('-inf')

        for i in range(len(a) - 1, -1, -1):
            if a[i] >= mx:
                b.append(a[i])
                mx = a[i]

        b.reverse()

        d = ListNode(0)
        cur = d

        for val in b:
            cur.next = ListNode(val)
            cur = cur.next

        return d.next