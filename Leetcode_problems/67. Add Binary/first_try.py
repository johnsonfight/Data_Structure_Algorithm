class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 1. get max length of a and b
        # 2. pad heading 0 to short length one
        # 3. for range(0, max(a, b)), add each number of a[len(a)] and b[len(b)]
        # 4. if sum >= 2, carry 1 to the next sum

        sum = 0
        carry = 0
        ans = ""

        # padding 0
        if len(a) < len(b):
            a = "0" * (len(b) - len(a)) + a
        else:
            b = "0" * (len(a) - len(b)) + b

        # calcuate
        for i in range(0, max(len(a), len(b))):
            sum = int(a[len(a) - 1 - i]) + int(b[len(b) - 1 - i]) + carry
            carry = 0
            if sum >= 2:
                carry = 1
                ans = str(sum - 2) + ans
                sum = 0
            else:
                ans = str(sum) + ans
                sum = 0
                
        if carry == 1:
            ans = "1" + ans
        
        return ans