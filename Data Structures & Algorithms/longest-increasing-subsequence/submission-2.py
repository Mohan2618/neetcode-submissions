class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        result = []

        for x in nums:
            left = 0
            right = len(result)
            while left < right:
                mid = (left + right) // 2

                if result[mid] < x:
                    left = mid + 1
                else:
                    right = mid

            if left == len(result):
                result.append(x)
            else:
                result[left] = x

        return len(result)

        