class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans=0
        min1=1111111111111
     
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            low=i+1
            high=len(nums)-1
            #print(low, high)
            #print(nums)
       
            while(low<high):
                sum1=nums[low]+nums[high]+nums[i]
                #print(sum1)
                if abs(target-sum1)<min1:
                    min1=abs(target-sum1)
                    #print(min1)
                    ans=sum1
                if sum1<target:
                    low+=1
                elif sum1>target:
                    high-=1    
                else:
                    return target
            #break
        return ans
        