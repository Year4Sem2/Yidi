class Solution:
    def calPoints(self, ops: List[str]) -> int:
        lst=[]
        for i in ops:
            if i != "C" and i!="D" and i!="+":
                lst.append(int(i))
            if i=="C":
                lst.remove(lst[len(lst)-1])
            if i=="D":
                lst.append(2*lst[len(lst)-1])
            if i=="+":
                lst.append(lst[len(lst)-1] + lst[len(lst)-2] )
        print(lst)
            
        return sum(lst)
        