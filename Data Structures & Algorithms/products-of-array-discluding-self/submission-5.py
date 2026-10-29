# O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right_side_product_upto_index = [None] * len(nums)
        left_side_product_upto_index = [None] * len(nums)
        right_side_product_upto_index[len(nums)-1] = nums[len(nums)-1]
        left_side_product_upto_index[0] = nums[0]
        for i in range(1, len(nums)):
            left_side_product_upto_index[i] = left_side_product_upto_index[i-1] * nums[i]
            right_side_product_upto_index[len(nums)-1-i] = right_side_product_upto_index[len(nums)-i] * nums[len(nums)-1-i]
        result = []
        result.append(right_side_product_upto_index[1])
        for i in range(1, len(nums)-1):
            result.append(left_side_product_upto_index[i-1] * right_side_product_upto_index[i+1])
        result.append(left_side_product_upto_index[len(nums)-2])
        return result