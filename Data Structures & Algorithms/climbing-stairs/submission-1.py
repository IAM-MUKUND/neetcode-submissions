class Solution:
    def climbStairs(self, n: int) -> int:
        a = 0
        b = 1
        curr = 0
        for _ in range(n):
            curr = a + b
            a = b
            b = curr
        return curr