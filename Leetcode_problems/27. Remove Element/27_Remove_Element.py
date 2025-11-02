class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while(1):
            try:
                nums.remove(val)
            except:
                return len(nums)
        return len(nums)