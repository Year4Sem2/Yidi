class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        count_top = [0]
        count_btm = [0]

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[:])
                my_str = "res: {}"
                print(my_str.format(res))
                return

            # All subsets that include nums[i]
            subset.append(nums[i])
            subset_top = "subset_top: {}"
            print(subset_top.format(subset))
            count_top[0] += 1
            print("into the recursion(top): {}".format(count_top))
            backtrack(i + 1, subset)
            count_top[0] -= 1
            print("recursions left(top): {}".format(count_top))
            subset.pop()
            subset_btm = "subset_btm: {}"
            print(subset_btm.format(subset))
            # All subsets that don't include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            count_btm[0] += 1
            print("into the recursion(btm): {}".format(count_btm))
            backtrack(i + 1, subset)
            count_btm[0] -= 1
            print("recursions left(btm): {}".format(count_btm))

        backtrack(0, [])
        return res
        