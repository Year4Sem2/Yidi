from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counter = Counter(chars)
        print(counter)
        res = 0
        for word in words:
            word_counter = Counter(word)
            print(word_counter)
            print(all(word_counter[c] <= counter[c] for c in word_counter))
            if all(word_counter[c] <= counter[c] for c in word_counter):
                res += len(word)
        return res
        