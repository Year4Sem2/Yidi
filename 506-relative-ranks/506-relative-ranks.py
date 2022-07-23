class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        if len(score)==1:
            return ["Gold Medal"]
        elif len(score)==2:
            if score[1]>score[0]:
                return ["Silver Medal","Gold Medal"]
            else:
                return ["Gold Medal","Silver Medal"]
        else:
            d={}
            a=sorted(score,reverse=True)
            d[a[0]]="Gold Medal"
            d[a[1]]="Silver Medal"
            d[a[2]]="Bronze Medal"
            for i in range(3,len(a)):
                d[a[i]]=str(i+1)
            for i in range(0,len(score)):
                score[i]=d[score[i]]
            return score
            
        