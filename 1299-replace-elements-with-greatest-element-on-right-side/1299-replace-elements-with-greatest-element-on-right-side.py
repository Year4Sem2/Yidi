class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        initial = []
        for i in range(len(arr)):
            if i != len(arr) - 1:
                initial.append(max(arr[i+1:]))
            else:
                initial.append(-1)
        return initial
        