class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = []
        k=len(nums1)
        for i in range(k):
            if(nums1[i] in nums2):
                a.append(nums1[i])
                ind = nums2.index(nums1[i])
                nums2[ind]= '_'

        return a
        