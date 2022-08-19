class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        #print(dp)
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                print("(i, w): ({},{})".format(i,w))
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                    #print(dp)
                if dp[i]:
                    #print("What is this?")
                    break

        return dp[0]
        