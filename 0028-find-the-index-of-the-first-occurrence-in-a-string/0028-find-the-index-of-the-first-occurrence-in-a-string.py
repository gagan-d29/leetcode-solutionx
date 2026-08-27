class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        while haystack:
            if needle in haystack:
                return haystack.index(needle)
            else:
                return -1