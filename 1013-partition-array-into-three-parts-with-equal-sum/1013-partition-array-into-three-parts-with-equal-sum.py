class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        N = len(arr)

        total_sum = 0

        for val in arr:
            total_sum += val
            
        if total_sum % 3 != 0:
            return False
        
        target = total_sum // 3
        count = 0
        curr_sum = 0
        
        for val in arr:
            curr_sum += val
            
            if curr_sum == target:
                count += 1
                curr_sum = 0
            
            if count == 3:
                return True

        return False
        