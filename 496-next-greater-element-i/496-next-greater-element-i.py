class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer=[]
        for i in nums1:
            x=nums2.index(i)
            m=-1
            for j in range(x,len(nums2)):
                if(nums2[j]>i):
                    m=nums2[j]
                    break
                    
            if(m>i):
                answer.append(m)
            else:
                answer.append(-1)
        return answer
        
                
            
                