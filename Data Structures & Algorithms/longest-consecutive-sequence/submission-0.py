class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = {}    # num = True
        for num in nums:
            seen[num] = True

        sequenceStarter = {}
        for num in nums:
            if num - 1 not in seen:
                sequenceStarter[num] = True
        longest = 0
        for starter in sequenceStarter.keys():
            counter = 0
            nextNum = starter
            while nextNum in seen:
                counter += 1
                nextNum += 1
            if counter > longest:
                longest = counter
        return longest

        