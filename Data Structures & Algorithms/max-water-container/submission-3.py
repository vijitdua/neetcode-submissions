# Two pointer versionO(n)
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_volume = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            is_left_smaller_pointer = (heights[left] == min(heights[left], heights[right]))
            smaller_pointer = left if is_left_smaller_pointer else right
            max_volume = max(max_volume, heights[smaller_pointer] * (right-left))
            left += (1 if is_left_smaller_pointer else 0)
            right -= (1 if not is_left_smaller_pointer else 0)
        return max_volume