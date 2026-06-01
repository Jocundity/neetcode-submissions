class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strings = {}

        for s in strs:
            s_sorted = "".join(sorted(s))
            if s_sorted not in sorted_strings:
                sorted_strings[s_sorted] = []
                sorted_strings[s_sorted].append(s)
            else:
                sorted_strings[s_sorted].append(s)

        return list(sorted_strings.values())
        



