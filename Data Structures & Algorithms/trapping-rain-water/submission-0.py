class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        i, j = 0, len(height) - 1
        leftMax, rightMax = height[i], height[j]
        while i < j:
            if leftMax < rightMax:
                i += 1
                if leftMax - height[i] >= 0: 
                    res += leftMax - height[i]
                else:
                    leftMax = height[i]
            else:
                j -= 1
                if rightMax - height[j] >= 0:
                    res += rightMax - height[j]
                else:
                    rightMax = height[j]

        return res
