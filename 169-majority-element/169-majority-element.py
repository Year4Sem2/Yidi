class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mylist = list(dict.fromkeys(nums))
        for key in mylist:
            if nums.count(key) > len(nums)/2:
                return key
        