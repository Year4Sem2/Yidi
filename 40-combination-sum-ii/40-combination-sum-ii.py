class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        #print("sorted candidates: {}.".format(candidates))

        res = []

        def backtrack(cur, pos, target):
            if target == 0:
                res.append(cur.copy())
                print("if target == 0, res: {}.".format(res))
            if target <= 0:
                return

            prev = -1
            for i in range(pos, len(candidates)):
                print("value of i: {}".format(i))
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                print("cur after appending: {}.".format(cur))
                print("backtrack({},{},{})".format(cur,i+1, target - candidates[i]))
                backtrack(cur, i + 1, target - candidates[i])
                print("backtrack({},{},{}), getting out, i: {}".format(cur[:-1],pos, target,i))
                cur.pop()
                print("cur after popping: {}.".format(cur))
                prev = candidates[i]
                print("prev: {}".format(prev))

        backtrack([], 0, target)
        return res
        