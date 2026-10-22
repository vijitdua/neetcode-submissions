class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right_side_product_upto_index = [nums[0]]
        left_side_product_upto_index = [None] * len(nums)
        left_side_product_upto_index[len(nums)-1] = nums[len(nums)-1]
        result = []
        # Build products arrays
        for i in range(1, len(nums)-1):
            right_side_product_upto_index.append(right_side_product_upto_index[i-1] * nums[i])
        for i in range(len(nums)-2, 0, -1):
            left_side_product_upto_index[i] = left_side_product_upto_index[i+1] * nums[i]

        result.append(left_side_product_upto_index[1])
        for i in range(1, len(nums)-1):
            result.append(right_side_product_upto_index[i-1] * left_side_product_upto_index[i+1])
        result.append(right_side_product_upto_index[len(nums)-2])
        return result