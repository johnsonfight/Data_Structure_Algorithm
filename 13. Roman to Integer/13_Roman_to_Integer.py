roman = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
}

class Solution:
    def romanToInt(self, s: str) -> int:
        if len(s) < 1 or len(s) > 15 :
            return 0

        output = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                output -= roman[s[i]]
            else:
                output += roman[s[i]] 

        return output

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         if 1 > len(s) or len(s) > 15 :
#             return 0

#         output = 0
#         for i in range(len(s)):
#             output += roman[s[i]]
#             if (roman[s[i-1]] < roman[s[i]]) and (i != 0):
#                 output -= 2*roman[s[i-1]]

#         return output