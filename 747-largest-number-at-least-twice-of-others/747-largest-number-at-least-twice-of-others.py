class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_val = sorted(nums)
        #if max_val[-2] == 0:
        #    return -1
        if max_val[-2] == 0 or max_val[-1] / max_val[-2] >= 2:
            return nums.index(max_val[-1])
        else:
            return -1
        