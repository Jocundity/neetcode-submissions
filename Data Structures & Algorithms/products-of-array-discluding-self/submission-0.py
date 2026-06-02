class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        i = 0

        while i < len(nums):
            product = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    product *= nums[j]

            result.append(product)
            i += 1


        return result