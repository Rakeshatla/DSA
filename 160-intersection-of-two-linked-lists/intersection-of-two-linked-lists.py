class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        n1 = n2 = 0
        p1, p2 = headA, headB
        while p1:
            n1 += 1
            p1 = p1.next
        while p2:
            n2 += 1
            p2 = p2.next
        p1, p2 = headA, headB
        if n1 > n2:
            for _ in range(n1 - n2):
                p1 = p1.next
        else:
            for _ in range(n2 - n1):
                p2 = p2.next
        while p1 and p2:
            if p1 is p2:
                return p1
            p1 = p1.next
            p2 = p2.next
        return None
