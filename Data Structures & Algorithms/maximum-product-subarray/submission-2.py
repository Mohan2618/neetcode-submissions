class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = nums[0]
        cur_min = nums[0]
        max_p = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]
            temp_max = max(x, cur_max * x, cur_min * x)
            temp_min = min(x, cur_max * x, cur_min * x)
            cur_max = temp_max
            cur_min = temp_min

            max_p = max(max_p, cur_max)

        return max_p