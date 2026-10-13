class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += "["
            for char in list(string):
                res += str(ord(char)) + ","
            res = res + "]"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        cur = ""
        ascii = ""
        for char in list(s):
            if char == "[":
                ascii = ""
                cur = ""
            elif char == "]":
                res.append(cur)
            elif char == ",":
                cur += chr(int(ascii))
                ascii = ""
            else:
                ascii += char
        print(res)

        return res
