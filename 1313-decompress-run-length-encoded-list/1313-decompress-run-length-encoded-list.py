class Solution:
    def loopit(self,nums,i,result):
        obj = Solution()
        n = len(nums)
       
        for j in range(nums[i]):
            result.append(nums[i+1])
            #print(result)
        i+=2
        if(i<n):
            return obj.loopit(nums,i,result)
        else:
            return result
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        #n = len(nums)
        #result = []   
        obj = Solution()
        i = 0
        result = []
        return obj.loopit(nums,i,result)
        