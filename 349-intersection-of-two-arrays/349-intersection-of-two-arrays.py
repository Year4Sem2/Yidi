class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        initial = []
        if len(nums1) < len(nums2):
            for element in nums1:
                if element in nums2:
                    initial.append(element)
            return list(set(initial))
        else:
            for element in nums2:
                if element in nums1:
                    initial.append(element)
            return list(set(initial))
        