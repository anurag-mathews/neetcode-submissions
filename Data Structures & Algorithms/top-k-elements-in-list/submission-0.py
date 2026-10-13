class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        numItems = list(freq.items())
        numItemsTuple = []
        # sort
        for item in numItems:
            numItemsTuple.append((item[1], item[0]))
        sortedNumItems = sorted(numItemsTuple)
        sortedNumItems.reverse()

        ret = []
        for i in range(k):
            ret.append(sortedNumItems[i][1])
        return ret