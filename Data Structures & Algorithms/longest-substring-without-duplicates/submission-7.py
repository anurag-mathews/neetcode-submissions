class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = j = 0
        res = 0
        temp = 0
        chars = list(s)
        seen = {}
        while j < len(chars):
            #print(chars[i:j], i, j)
            char = chars[j]
            if char not in seen:
                temp += 1
                seen[char] = j
            else:
                res = max(res, temp)
                while chars[i] != char:
                    if chars[i] in seen:
                        seen.pop(chars[i])
                    i += 1
                seen.pop(chars[i])
                i += 1
                temp = j - i + 1
                seen[char] = j
            j += 1
        #print(chars[i:j], i, j)
        res = max(res, temp)

        return res