
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mylist = list(dict.fromkeys(nums))
        for key in mylist:
            if nums.count(key) == 1:
                return key
        
        