class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        key=lambda x:arr2.index(x) if x in arr2 else len(arr2)+x
        #print(key(7))
        
        return sorted(arr1,key=lambda x:arr2.index(x) if x in arr2 else len(arr2)+x)
        