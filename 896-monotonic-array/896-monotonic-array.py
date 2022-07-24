class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = sorted(nums)
        decreasing = sorted(nums)[::-1]
        if nums == increasing or nums == decreasing:
            return True
        else:
            return False