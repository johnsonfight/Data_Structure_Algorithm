class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Count the number of zeros
        count_zeros = nums.count(0)

        # Remove all zeros from the list
        nums[:] = [num for num in nums if num != 0]

        # Append the zeros at the end of the list
        nums.extend([0] * count_zeros)