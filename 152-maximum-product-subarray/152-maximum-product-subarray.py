class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:

            tmp = curMax * n
            #print("tmp: {}".format(tmp))
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)
            #print("curMax: {}, curMin: {}, res: {}".format(curMax, curMin, res))
        return res
        