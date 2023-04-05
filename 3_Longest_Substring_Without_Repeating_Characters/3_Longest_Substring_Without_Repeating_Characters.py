class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        substr = ""
        l_substr = []
        for i in range(len(s)):
            if s[i] not in substr:
                substr += s[i]
            else:
                substr = s[i]
                j=1
                while i-j >= 0:
                    if s[i-j] not in substr:
                        substr = s[i-j] + substr
                        j+=1
                    else:
                        break
            l_substr.append(substr)
        
        return len(max(l_substr, key=len))
