class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        pocket=[]
        for i in bills:
            if(i==5):
                pocket.append(i)
            if(i==10):
                if(5 in pocket):
                    pocket.append(10)
                    pocket.remove(5)
                else:
                    return False
            if(i==20):
                if(10 in pocket and 5 in pocket ):
                    pocket.remove(10)
                    pocket.remove(5)
                elif(sum(pocket)==15 or sum(pocket)>20):
                    pocket.remove(5)
                    pocket.remove(5)
                    pocket.remove(5)
                else:
                    return False
        return True
