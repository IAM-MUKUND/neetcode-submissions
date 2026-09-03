class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        s = ""
        valid = []
        def brackets(op = n, cl = n, s = ""):
            if op == 0 and cl == 0:
                valid.append(s)
                return
            if op > 0:
                brackets(op - 1, cl, s + '(')
            if cl > 0 and op < cl:
                brackets(op, cl - 1, s + ')')
        brackets()
        return valid