class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_keys = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        res = []

        def backtrack(n = 0, curstr = ''):
            if len(curstr) == len(digits):
                res.append(curstr)
                return

            for c in digit_keys[digits[n]]:
                backtrack(n + 1, curstr + c)

        if digits:
            backtrack()
        return res