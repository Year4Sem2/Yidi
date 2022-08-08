class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        initial = {}
        for element in nums:
            if element not in initial: #this one is useful hashmap function
                initial[element] = 1
            else:
                initial[element] += 1
        #print(initial)
        sort_orders = sorted(initial.items(), key=lambda x: x[1], reverse=True)
        #print(sort_orders)
        extract = sort_orders[:k]
        initial_list = []
        for element in extract:
            initial_list.append(element[0])
            #print(element[0])
            #element = element[0]
        #print(extract)
        #print(extract)
        return initial_list
        
