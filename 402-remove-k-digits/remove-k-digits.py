class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if(len(num)==k):
            return '0'
        st=[]
        for i in num:
            while(st and k>0 and st[-1]>i):
                st.pop()
                k-=1
            st.append(i)
        st=st[:-k] if k>0 else st
        result=''.join(st).lstrip('0')
        return result if result else '0'
