class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need not in d:
                d[nums[i]] = i
            else:
                return [d[need], i]