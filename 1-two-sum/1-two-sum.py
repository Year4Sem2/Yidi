class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        initial = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    initial.append(i)
                    initial.append(j)
                    return initial
        if initial == []:
            return [0,0]
        