class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        myset = set(bobSizes)
        sA = sum(aliceSizes)
        sB = sum(bobSizes)
        
        for i in aliceSizes:
            x = i
            y = x + (sB - sA) / 2
            
            if y in myset:
                return [x, y]
                
            
        