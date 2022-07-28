class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        #print(sorted(arr))
        initial = {}
        count = 0
        sorted_arr = sorted(arr)
        #for i in range(1, len(arr)+1):
            #if sorted_arr[i] == sorted_
        for element in sorted_arr:
            if element not in initial:
                count += 1
                initial[element] = count
            else:
                initial[element] = count
        #print(initial)
        
        initial_list = []
        for element in arr:
            initial_list.append(initial[element])
        return initial_list
        
        