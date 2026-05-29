class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_num_set = set(nums)

        if len(nums) != len(unique_num_set):
            return True
        else:
            return False