class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                #print("if i >= len(nums), res: {}.".format(res))
                return
            # decision to include nums[i]
            subset.append(nums[i])
            #print("subset after appending: {}.".format(subset))
            #print("dfs({})".format(i+1))
            dfs(i + 1)
            #print("dfs({}),getting out(top)".format(i))
            # decision NOT to include nums[i]
            subset.pop()
            #print("subset after popping: {}.".format(subset))
            #print("dfs({})".format(i+1))
            dfs(i + 1)
            #print("dfs({}),getting out(btm)".format(i))

        dfs(0)
        return res