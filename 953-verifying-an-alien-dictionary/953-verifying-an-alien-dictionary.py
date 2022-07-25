class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {v: k for k, v in enumerate(order)}
        for i in range(len(words) - 1): 
            a, b = words[i], words[i+1]
            L = min(len(a), len(b))
            for j in range(L): 
                if d[a[j]] < d[b[j]]: 
                    break
                elif d[a[j]] > d[b[j]]: 
                    return False
            if len(a) > len(b) and a[:L] == b:
                return False
        return True
        