class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        neededValue = {}

        for i, num in enumerate(nums):
            if num in neededValue:
                return [neededValue[num], i]
            neededValue[target - num] = i
        