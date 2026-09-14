class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            result += str(len(string)) + "#" + string
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        left = 0
        while left < len(s):
            right = left
            while s[right] != '#':
                right += 1
            length = int(s[left: right])
            result.append(s[right + 1: right + length + 1])
            left = right + length + 1
        return result