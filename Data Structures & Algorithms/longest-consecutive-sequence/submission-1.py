class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sorted_nums = sorted(set(nums))
        sequences = []

        sequence_length = 1
        for i in range(len(sorted_nums) - 1):
            if sorted_nums[i] == sorted_nums[i + 1] - 1:
                sequence_length += 1
            else:
                sequences.append(sequence_length)
                sequence_length = 1

        sequences.append(sequence_length)

        return max(sequences)