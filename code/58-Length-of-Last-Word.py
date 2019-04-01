class Solution:

    def lengthOfLastWord(self, s: str) -> int:
        if not s.strip():
            return 0

        return len(s.split()[-1])
