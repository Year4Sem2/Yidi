class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minDiff = arr[1] - arr[0]
        for i in range(len(arr)-1):
            minDiff = min(minDiff,arr[i+1]-arr[i])
        print(minDiff)
        
        ls=[]
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] == minDiff:
                ls.append([arr[i],arr[i+1]])
        
        return ls