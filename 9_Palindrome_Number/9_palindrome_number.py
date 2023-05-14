class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reverse = 0
        origin = x
        while x > 0:
            reverse = (x%10) + reverse*10
            x = x//10

        return reverse == origin