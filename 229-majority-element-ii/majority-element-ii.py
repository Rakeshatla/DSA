class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        co1=0
        co2=0
        ele1=0
        ele2=0
        n=len(nums)
        res=[]
        for i in nums:
            if(co1==0 and i!=ele2):
                co1=1
                ele1=i
            elif(co2==0 and i!=ele1):
                co2=1
                ele2=i
            elif(i==ele1):
                co1+=1
            elif(i==ele2):
                co2+=1
            else:
                co1-=1
                co2-=1
            # print(ele1,ele2,co1,co2)
        co1=0
        co2=0
        for i in nums:
            if(i==ele1):
                co1+=1
            elif(i==ele2):
                co2+=1
        # print(co1,co2)
        if(co1>(n//3)):
            res.append(ele1)
        if(co2>(n//3)):
            res.append(ele2)
        return res
