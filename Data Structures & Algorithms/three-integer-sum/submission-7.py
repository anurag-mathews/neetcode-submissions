class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        # -4, -1, -1, 0, 1, 2
        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1
            while j < k:
                target = -nums[i]
                if nums[j] + nums[k] == target:
                    res.add(tuple([nums[i], nums[j], nums[k]]))
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    j += 1
        
        return [list(i) for i in res]