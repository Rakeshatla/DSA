# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        res=0
        arr=[]
        n=head
        temp=head
        while n:
            res=res*2+n.val
            n=n.next
        return res
        