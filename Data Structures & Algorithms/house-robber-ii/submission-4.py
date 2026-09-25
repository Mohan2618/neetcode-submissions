class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        prev1 = 0
        prev2 = 0
        for i in range(1, len(nums)):
            cur = max(prev1, nums[i] + prev2)
            prev2 = prev1
            prev1 = cur

        prev11 = 0
        prev22 = 0
        for i in range(len(nums) - 1):
            cur = max(prev11, nums[i] + prev22)
            prev22 = prev11
            prev11 = cur

        return max(prev1, prev11)