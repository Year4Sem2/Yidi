class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr = Counter(arr)
        arrSet = set([value for key, value in arr.items()])
        #print(arr)
        #print(arrSet)
        return len(arrSet) == len(arr)
        