class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        #if "e" in "bella":
        #    print("Yay")
        d = {}
        for s in set(words[0]):
            d[s] = min([word.count(s) for word in words])
            print(d)
        #print(d)
        result = []
        for k, v in d.items():
            result += [k] * v
        return result
        
        