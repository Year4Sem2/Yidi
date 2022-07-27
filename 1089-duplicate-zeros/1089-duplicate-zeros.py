class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i = 0 
        while i < len(arr):
            if arr[i] == 0: 
                for q in range(len(arr)-1,i,-1):
                    arr[q] = arr[q-1]
                i+=1 
            i+= 1
        """
        Do not return anything, modify arr in-place instead.
        """
        