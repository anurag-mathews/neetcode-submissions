class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        for i in range(0, len(nums) - 2):
            #2 pointers for remainders
            target = -nums[i]            
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] == target:
                    res.add(tuple([nums[i], nums[j], nums[k]]))
                    j += 1
                    k -= 1
                    
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    k -= 1
        return [list(i) for i in res]