class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #print(len([]))
        #print(stones.index(8))
        
        while len(stones) > 1:
            max1 = max(stones)
            index1 = stones.index(max1)
            stones.pop(index1)

            max2 = max(stones)
            index2 = stones.index(max2)
            stones.pop(index2)

            sum = max1 - max2

            stones.append(sum)

        return stones[0]