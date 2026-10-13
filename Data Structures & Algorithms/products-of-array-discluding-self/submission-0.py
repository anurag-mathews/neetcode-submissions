class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        total = 1
        zeros = 0
        index = 0
        for i, num in enumerate(nums):
            if num == 0:
                zeros += 1
                index = i
            else:
                total *= num


        if zeros > 1:
            return [0 for num in nums]
        elif zeros == 1:
            res = [0 for num in nums]
            res[index] = total
            return res
        else:
            return [int(total / num) for num in nums]

        
        # res = [1 for num in nums]
        # print(res)
        # for i, num in enumerate(nums):
        #     for j in range(len(res)):
        #         if i != j:
        #             res[j] *= num

        # return res
        