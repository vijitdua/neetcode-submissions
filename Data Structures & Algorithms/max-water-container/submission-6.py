# Two pointer versionO(n)
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_volume = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            width = right - left
            if heights[left] <= heights[right]:
                area = heights[left] * width
                left += 1
            else:
                area = heights[right] * width
                right -= 1
            max_volume = max(max_volume, area)
        return max_volume