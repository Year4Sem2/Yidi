class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        increasing = None
        
        for i in range(len(arr) - 1):
            if (increasing == None or increasing == True) and arr[i] < arr[i + 1]:
                increasing = True
            elif increasing != None and arr[i] > arr[i + 1]:
                increasing = False
            else:
                return False
            
        #CHECK JUST IN CASE len(arr) = 1 such as [2], since it should return False
        return True if increasing == False else False
        