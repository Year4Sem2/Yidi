class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        #list(set(list1).intersection(list2))
        initial = []
        initial_dict = {}
        common = list(set(list1).intersection(list2))
        for element in common:
            #initial_dict[list1.index(element) + list2.index(element)] = element 
            initial_dict[element] = list1.index(element) + list2.index(element)
        #print(initial_dict)
        minimum_value = min(initial_dict.values())

#get keys with minimal value using list comprehension
        minimum_keys = [key for key in initial_dict if initial_dict[key]==minimum_value]
        return minimum_keys
        #initial.append(initial_dict[min(initial_dict)])
        #return initial
        
        