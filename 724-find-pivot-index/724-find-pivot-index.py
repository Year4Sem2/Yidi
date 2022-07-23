class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        
        right = sum(nums)
        left = 0
        # now we try to check each index, if this index could be the pivot
        # note that pivot point is neither a elem of left not right
        i = 0
        while i < len(nums):
            # i is the candidate pivot index, so we remove nums[i] from right
            right -= nums[i]
            # if current index makes left==right, then this index is pivot
            if left == right:
                return i
            # if it's not like that, we add this number into left, and move i forward
            print(right)
            print(left)
            left += nums[i]
            i += 1
            
        # return -1 if no pivot point 
        return -1