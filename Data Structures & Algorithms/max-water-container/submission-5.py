# Two pointer versionO(n)
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_volume = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            width = right - left
            area = min(heights[left], heights[right]) * width
            max_volume = max(max_volume, area)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return max_volume