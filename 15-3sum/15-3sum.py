class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        #print(nums)
        
        for i in range(len(nums)):
            if nums[i] > 0: break  # after sorting, if the min > 0, we couldn't find such three values
            if i > 0 and nums[i] == nums[i - 1]:  # ensure that nums[i] is not duplicated
                continue               
            l, r = i + 1, len(nums) - 1
            #print(l, r)
            while l < r:
                if nums[l] + nums[r] > -nums[i]:
                    r -= 1
                    #print(l, r)
                elif nums[l] + nums[r] < -nums[i]:
                    l += 1
                    #print(l, r)
                else:
                    ans.append([nums[i], nums[l], nums[r]])
					# update l to get a different sum
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return ans

        