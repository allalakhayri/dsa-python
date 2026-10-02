# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        s = set(nums)
        longest = 0

        for x in s:
            if x - 1 not in s:
                length = 1

                while x + 1 in s:
                    x += 1
                    length += 1

                longest = max(longest, length)

        return longest