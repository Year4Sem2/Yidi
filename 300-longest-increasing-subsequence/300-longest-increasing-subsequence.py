class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)
        #print(LIS)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                #print("i:{},j:{}".format(i,j))
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
                    #print("LIS:{}".format(LIS))
        return max(LIS)