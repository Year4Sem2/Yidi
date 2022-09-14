class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                #print("if i == len(nums), res: {}.".format(res))
                return

            # All subsets that include nums[i]
            subset.append(nums[i])
            #print("subset after appending: {}.".format(subset))
            #print("backtrack({},{})".format(i+1, subset))
            backtrack(i + 1, subset)
            #print("backtrack({},{}),getting out(top)".format(i, subset[:-1]))
            subset.pop()
            #print("subset after popping: {}.".format(subset))
            # All subsets that don't include nums[i]
            i_store = i
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
                #print("value of i: {}.".format(i))
            #print("backtrack({},{})".format(i+1, subset))
            backtrack(i + 1, subset)
            #print("backtrack({},{}),getting out(btm)".format(i_store, subset))

        backtrack(0, [])
        return res
        