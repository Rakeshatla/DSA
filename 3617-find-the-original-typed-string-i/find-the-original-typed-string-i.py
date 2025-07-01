from collections import Counter
class Solution:
    def possibleStringCount(self, word: str) -> int:
        res=0
        co=1
        for i in range(len(word)-1):
            if(word[i]==word[i+1]):
                co+=1
            else:
                res+=co-1
                co=1
        res+=co-1
        return res+1