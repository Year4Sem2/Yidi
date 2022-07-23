class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        #count = 0 
        #counter = [count = count + 1 for i in range(1,len(nums)+1)]
        #print(counter)
        hashmap = {}
        dup = -1
        missing = 1
        for n in nums:
            if n not in hashmap:
                hashmap[n] = 1
            else:
                hashmap[n] +=1
        print(hashmap)
        for i in range(1, len(nums)+1):
            if i in hashmap:
                if hashmap[i] == 2:
                    dup = i
            else:
                missing = i
        return [dup, missing]

                
                
        