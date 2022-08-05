class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #print(nums.index(target))
        initial = []
        for i in range(len(nums)):
            if nums[i] == target:
                initial.append(i)
        if initial == []:
            return [-1,-1]
        #elif len(initial) == 1:
        #   return [initial[0], initial[0]]
        return [initial[0], initial[-1]]
        