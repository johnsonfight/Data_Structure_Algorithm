class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] *= -1

        heapq.heapify(nums)
        a = heapq.heappop(nums)
        b = heapq.heappop(nums)
        return (-a-1) * (-b-1)