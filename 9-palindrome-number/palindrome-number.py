class Solution:
    def isPalindrome(self, x: int) -> bool:
        n=list(str(x))
        l=0
        h=len(n)-1
        while(l<=h):
            if(n[l]!=n[h]):
                return False
            l+=1
            h-=1
        return True