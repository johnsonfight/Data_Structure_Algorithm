class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                for j in range(len(needle)):
                    if haystack[i+j] == needle[0+j]:
                        if j == len(needle) - 1:
                           return i
                    else:
                        break
        
        return -1