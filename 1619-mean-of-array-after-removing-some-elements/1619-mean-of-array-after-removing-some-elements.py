class Solution:
    def trimMean(self, arr: List[int]) -> float:
        sorted_arr = sorted(arr)
        small = int(len(arr) * 0.05)
        big = int(len(arr) * 0.95)
        chopped = sorted_arr[small:big]
        return sum(chopped)/len(chopped)
        #print(chopped)
        #print(small)
        #print(big)
        