class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}

        for num in nums:
            if num not in count_dict:
                count_dict[num] = 1
            else:
                count_dict[num] += 1

        nums_sorted = {num: count for num, count in sorted(count_dict.items(), key=lambda item: item[1], reverse=True)}

        return list(nums_sorted.keys())[:k]