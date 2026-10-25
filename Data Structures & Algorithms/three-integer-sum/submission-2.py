class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution_set = set()
        integer_location_map = dict()
        for i in range(len(nums)):
            integer_location_map[nums[i]] = i
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                k = integer_location_map.get(-(nums[i] + nums[j]), None)
                if not (k == None) and not ((k == i) or (k ==j)):
                    solution_set.add(tuple(sorted([nums[i],nums[j],nums[k]])))
        return [list(x) for x in solution_set]