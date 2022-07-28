class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        initial = {}
        for element in arr:
            if element not in initial:
                initial[element] = 1
            else:
                initial[element] += 1
        #print(initial)
        proportion = 0.25 * len(arr)
        #print(proportion)
        for k, v in initial.items():
            if v > proportion:
                return k
        