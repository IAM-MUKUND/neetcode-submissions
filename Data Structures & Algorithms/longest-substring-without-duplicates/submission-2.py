class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        entry = set()
        res = 0

        for r in range(len(s)):
            while s[r] in entry:
                entry.remove(s[l])
                l += 1
            entry.add(s[r])
            res = max(res, r - l + 1)
        return res