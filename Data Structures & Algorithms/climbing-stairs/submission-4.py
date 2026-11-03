# O(n) bottom-up (safer, no recursion)
class Solution:
    def climbStairs(self, n: int) -> int:
        number_of_distinct_ways_to_reach_i = [None] * (n+1)
        number_of_distinct_ways_to_reach_i[0] = 0
        for i in range(1, n + 1):
            if i < 3:
                number_of_distinct_ways_to_reach_i[i] = i
                continue
            number_of_distinct_ways_to_reach_i[i] = number_of_distinct_ways_to_reach_i[i-1] + number_of_distinct_ways_to_reach_i[i-2]
        return number_of_distinct_ways_to_reach_i[n]
