# O(n) top-down
class Solution:
    def climbStairs(self, n: int) -> int:
        number_of_distinct_ways_to_reach_i = [None] * (n+1)
        def climbStairsDynamic(n: int):
            if not number_of_distinct_ways_to_reach_i[n] == None:
                return number_of_distinct_ways_to_reach_i[n]
            elif n == 0:
                return 0
            elif n == 1:
                return 1
            elif n == 2:
                return 2
            number_of_distinct_ways_to_reach_i[n] = climbStairsDynamic(n-1) + climbStairsDynamic(n-2)
            return number_of_distinct_ways_to_reach_i[n]
        return climbStairsDynamic(n)
