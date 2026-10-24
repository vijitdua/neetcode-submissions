class Solution:
    def stripNonAlphaNumericChars(self, s: str) -> str:
        output = []
        for char in s:
            lower_case_char = char.lower()
            if (ord('0') <= ord(lower_case_char) <= ord('9')) or (ord('a') <= ord(lower_case_char) <= ord('z')):
                output.append(lower_case_char)
        return "".join(output)

    def isPalindrome(self, s: str) -> bool:
        strippedString = self.stripNonAlphaNumericChars(s)
        for i in range (0, len(strippedString)//2, 1):
            if not strippedString[i] == strippedString[len(strippedString)-1-i]:
                return False
        return True
