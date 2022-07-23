class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        total1=nums[-1]*nums[-2]*nums[-3]
        total2=nums[0]*nums[1]*nums[-1]
        return max(total1,total2)
        