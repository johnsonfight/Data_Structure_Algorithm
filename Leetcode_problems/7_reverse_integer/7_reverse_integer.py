class Solution:
    def reverse(self, x: int) -> int:
        # Check input is in range of signed 32-bit integer
        if x > 2**31 - 1 or x < -2**31:
            return 0
        
        # Handle negative sign
        output = 0
        if x > 0 :
            isNeg = False
        elif x == 0:
            return 0
        else:
            isNeg = True
            x = -x

        # Do reversing
        while x != 0 :
            output = output*10 + x%10
            x = x//10

        # Handle negative sign
        if isNeg:
            output = -output

        # Check output is in range of signed 32-bit integer
        if output > 2**31 - 1 or output < -2**31:
            return 0

        return output
            