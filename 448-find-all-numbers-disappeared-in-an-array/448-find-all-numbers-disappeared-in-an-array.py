class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s={x for x in range(1,len(nums)+1)}
        print(s)
        s=s-set(nums)
        return s
        