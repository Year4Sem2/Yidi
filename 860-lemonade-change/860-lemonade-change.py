class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic={}
        dic[5]=dic[10]=dic[20]=0
        
        for i  in bills:

            dic[i]+=1
        
            if i==10 and dic[5]>0:
                dic[5]-=1
            elif i==20 and dic[10]>0 and dic[5]>0:
                dic[5]-=1
                dic[10]-=1
            elif i==20 and dic[10]==0 and dic[5]>2:
                dic[5]-=3
            elif i==5:
                continue
            else:
                return 0
        return 1
        