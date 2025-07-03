class Solution:
    def kthCharacter(self, k: int) -> str:
        word='a'
        while(len(word)<k):
            for i in word:
                word+=chr(ord(i)+1)
        return word[k-1]