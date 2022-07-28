class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            if arr[i] % 2 == 0:
                continue
            else:
                if len(arr) - i > 2:
                    if arr[i+1] % 2 != 0 and arr[i+2] % 2 !=0:
                        return True
                else:
                    return False
        return False
            
        