class Solution:
    def isValid(self, s: str) -> bool:
        opening_brackets = []

        for char in s:
            if char in ["(", "{", "["]:
                open = char
                opening_brackets.append(open)
            else:
                if not opening_brackets:
                    return False

                if char == ")":
                    match = opening_brackets.pop()
                    if match != "(":
                        return False

                if char == "]":
                    match = opening_brackets.pop()
                    if match != "[":
                        return False

                if char == "}":
                    match = opening_brackets.pop()
                    if match != "{":
                        return False
    

        if not opening_brackets:
            return True
        else:
            return False