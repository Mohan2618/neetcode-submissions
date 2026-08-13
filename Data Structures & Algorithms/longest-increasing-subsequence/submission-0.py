class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            j = 0
            while j < i:
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                j += 1
        
        return max(dp)