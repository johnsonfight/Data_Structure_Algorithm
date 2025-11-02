class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0 or len(nums)== 0:
            return 0

        l = 0
        r = 0
        prod = 1
        count = 0
        for r in range(len(nums)):
            prod *= nums[r]
            while prod >= k and l<=r:
                prod /= nums[l]
                l += 1
            count += r-l+1
        return count
