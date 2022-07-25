class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        initial = {}
        list_to_set = set(nums)
        #print(len(list_to_set))
        n = len(list_to_set) - 1
        for element in nums:
            if element not in initial:
                initial[element] = 1
            else:
                initial[element] += 1
        #print(initial)
        for big in initial.items():
            #print(big)
            #print(big[1])
            if big[1] == n:
                return big[0]