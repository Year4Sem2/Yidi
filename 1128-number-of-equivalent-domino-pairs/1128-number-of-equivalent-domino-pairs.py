class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        #sum concept 
        #dictionary concept
        #iterate through .items()
        dict1, total = defaultdict(int), 0
        #print(dict1)
        for i, j in dominoes:
            min_val = min(i, j)
            max_val = max(i, j)
            dict1[(min_val, max_val)] += 1
            #print(dict1)

        for i in dict1:
            #print(i)
            total += dict1[i]*(dict1[i]-1)//2

        return total
        
        
        