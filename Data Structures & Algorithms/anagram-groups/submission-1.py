class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for string in strs:
            sortedString = "".join(sorted(string))
            if sortedString in anagrams:
                anagrams[sortedString].append(string)
            else:
                anagrams[sortedString] = [string]

        return list(anagrams.values())