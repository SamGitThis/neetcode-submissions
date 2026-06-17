class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        dc = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        curs = ""
        n = len(digits)

        def backtrack(i, curs):
            if len(curs) == n:
                res.append(curs)
                return

            for c in dc[digits[i]]:
                backtrack(i+1, curs+c)

        if digits:
            backtrack(0, "")

        return res