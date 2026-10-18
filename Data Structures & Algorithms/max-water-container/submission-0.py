class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) -1
        maxVol = 0
        while l < r:
            vol = min(heights[l], heights[r]) * (r - l)
            if vol > maxVol:
                maxVol = vol
            if heights[l] > heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else:
                if r - l < 3:
                    l += 1
                    continue
                if heights[l+1] > heights[r-1]:
                    l += 1
                else:
                    r -= 1
        return maxVol
        