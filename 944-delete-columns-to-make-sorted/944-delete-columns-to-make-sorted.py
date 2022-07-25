class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        counter=0
    
        for x in zip(*strs):
            if list(x) != sorted(x):
                counter+=1
        return counter
        #print(sorted(strs)[::-1])
        