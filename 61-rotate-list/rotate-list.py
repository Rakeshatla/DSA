# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n,s,f=head,head,head
        if(head==None):
            return None
        le=1
        while(n.next!=None):
            le+=1
            n=n.next
        # print(le)
        k=k%le
        # print(k)
        if(k==0):
            return head
        while(k>0):
            f=f.next
            k-=1
        while(f!=None and f.next!=None):
            s=s.next
            f=f.next
        n.next=head
        head=s.next
        s.next=None
        return head
        

        
        