# Brute force version, O(n^2)
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_volume = 0
        for i, height_i in enumerate(heights):
            for j in range(i, len(heights)):
                distance = j-i
                max_height = min(height_i, heights[j])
                max_volume = max(max_volume, max_height * distance)
        return max_volume
