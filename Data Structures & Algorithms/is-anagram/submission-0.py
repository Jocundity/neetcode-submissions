class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check length
        if len(s) != len(t):
            return False

        # Check letter frequency
        s_letter_frequencies = {}
        t_letter_frequencies = {}

        def addLettersToFrequencyDict(x: str, d: dict):
            for char in x:
                if char in d:
                    d[char] += 1
                else:
                    d[char] = 1

        addLettersToFrequencyDict(s, s_letter_frequencies)
        addLettersToFrequencyDict(t, t_letter_frequencies)

        # Check if letter appears in each string
        # and how many times the letter appears
        for letter in s_letter_frequencies:
            if letter not in t_letter_frequencies:
                return False

            if s_letter_frequencies[letter] != t_letter_frequencies[letter]:
                return False
            
        return True

        

        