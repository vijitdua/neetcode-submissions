class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not len(nums): return 0
        seen_value_set = set()
        longest_cons_streak_ending_at = dict()
        longest_cons_current = 1
        longest_cons_max = 1
        for num in nums:
            seen_value_set.add(num)
        for num in nums:
            longest_cons_current = 1
            i = num - 1
            while True:
                if i in longest_cons_streak_ending_at:
                    longest_cons_current += longest_cons_streak_ending_at[i]
                    break
                elif i in seen_value_set:
                    longest_cons_current += 1
                    i -= 1
                else:
                    break
            longest_cons_max = max(longest_cons_max, longest_cons_current)
            longest_cons_streak_ending_at[num] = longest_cons_current
        return longest_cons_max
        