class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        c,l=0,[]
        for i in nums:
            c=(c*2+i)%5
            print(c)
            l.append(c==0)
        return l
        