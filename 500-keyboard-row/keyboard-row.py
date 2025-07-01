class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        a='qwertyuiop'
        b='asdfghjkl'
        c='zxcvbnm'
        res=[]
        def check(s):
            if all(x.lower() in a for x in s):
                return True
            elif all(x.lower() in b for x in s):
                return True
            elif all(x.lower() in c for x in s):
                return True
            else:
                return False
        for i in words:
            ch=check(i)
            if(ch):
                res.append(i)
        return res