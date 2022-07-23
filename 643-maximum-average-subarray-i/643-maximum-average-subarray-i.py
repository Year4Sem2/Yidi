class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        temp=nums[:k]
        s=sum(temp)
        
        avg=s/k
        for i in range(1,len(nums)-k+1):
            s-=nums[i-1]
            s+=nums[i+k-1]
            avg=max(avg,s/k)
        #print(temp)
        return avg
        