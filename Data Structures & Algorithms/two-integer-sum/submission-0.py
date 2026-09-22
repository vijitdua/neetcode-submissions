class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenNumberToIndex: dict[int, int] = {}
        for i in range(0, len(nums), 1):
            number = nums[i]
            diff = target - number
            if seenNumberToIndex.get(diff,-1) != -1:
                return [seenNumberToIndex[diff],i]
            seenNumberToIndex[number] = i if seenNumberToIndex.get(number,-1) == -1 else seenNumberToIndex[number]
        return [-1,-1]
