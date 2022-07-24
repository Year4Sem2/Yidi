class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even, odd = [], []
        for n in nums:
            if n % 2 == 0:
                even.append(n)
            else:
                odd.append(n)
                
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = even.pop()
            else:
                nums[i] = odd.pop()
        return nums
        