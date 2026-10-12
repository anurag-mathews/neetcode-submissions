class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        library = {}
        for c in list(s):
            if c in library:
                library[c] += 1
            else:
                library[c] = 1
        
        print(library)
        for c in list(t):
            if c in library:
                library[c] -= 1
            if c not in library or library[c] < 0:
                return False
        
        return True
