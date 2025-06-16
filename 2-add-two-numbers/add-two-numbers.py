# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        curr=dummy
        t1=l1
        t2=l2
        carry=0
        while(t1 or t2):
            summ=carry
            print(summ)
            if(t1):
                summ+=t1.val
            if(t2):
                summ+=t2.val
            nn=ListNode(summ%10)
            carry=summ//10
            curr.next=nn
            curr=curr.next
            if(t1):
                t1=t1.next
            if(t2):
                t2=t2.next
        if(carry==1):
            nn=ListNode(1)
            curr.next=nn
        return dummy.next


