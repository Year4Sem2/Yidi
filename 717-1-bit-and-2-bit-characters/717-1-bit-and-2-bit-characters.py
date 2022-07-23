class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if(len(bits)==1 or bits[-2]==0):
            return True
        i=len(bits)-2
        while(i>=0 and bits[i]!=0):
            i-=1
            print(i)
        return ((len(bits)-2-i)%2)==0