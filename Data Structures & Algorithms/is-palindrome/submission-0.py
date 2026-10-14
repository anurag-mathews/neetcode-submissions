class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1_list = []
        for char in list(s):
            ascii = ord(char)
            if (ascii >= 48 and ascii <= 57) or (ascii >= 65 and ascii <= 90) or (ascii >= 97 and ascii <= 122):
                s1_list.append(char)

        s1 = "".join(s1_list)

        s2_list = s1_list
        s2_list.reverse()
        s2 = "".join(s2_list)
        return s1.lower() == s2.lower()
        