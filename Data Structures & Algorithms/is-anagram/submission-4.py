class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        count = [0] * 26
        for ind in range(len(s)):
            count[ord(t[ind]) - ord('a')] += 1
            count[ord(s[ind]) - ord('a')] -= 1
        for c in count:
            if c != 0:
                return False
        return True
        