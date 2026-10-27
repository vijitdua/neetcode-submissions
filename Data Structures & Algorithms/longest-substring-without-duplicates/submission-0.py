class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right = 0
        left = 0
        max_len = 0
        seen_set = set()
        while right < len(s):
            while s[right] in seen_set:
                seen_set.remove(s[left])
                left += 1
            seen_set.add(s[right])
            max_len = max(max_len, right-left+1)
            right += 1
        return max_len