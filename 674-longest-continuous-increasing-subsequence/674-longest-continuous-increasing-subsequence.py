class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_subsequence = 1
        count = 1 
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                count += 1
                max_subsequence = max(max_subsequence, count)
            else:
                count = 1
        return max_subsequence