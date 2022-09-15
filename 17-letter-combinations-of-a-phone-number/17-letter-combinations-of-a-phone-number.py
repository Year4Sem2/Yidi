class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                print("if len(curStr) == len(digits), res: {}".format(res))
                return
            for c in digitToChar[digits[i]]:
                print("backtrack({},{})".format(i+1, curStr + c))
                backtrack(i + 1, curStr + c)
                print("backtrack({},{}), getting out".format(i,curStr))

        if digits:
            backtrack(0, "")

        return res
        