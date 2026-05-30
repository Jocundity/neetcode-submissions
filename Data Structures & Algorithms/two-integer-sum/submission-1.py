class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        second_num_indices = {} # Store as num : index

        for index, num in enumerate(nums):
            # Find second number
            difference = target - num

            if difference in second_num_indices:
                i = index
                j = second_num_indices[difference]

                result = sorted([i, j])
                return result

            else:
                second_num_indices[num] = index