# Given an integer array nums of unique elements, return all possible subsets
# (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in any
# order.
#
# This approach uses bitmasks: each subset is represented by a binary mask from
# 0 to (2^n)-1. A bit set to 1 means the corresponding element is included in the
# current subset.

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        result = []

        # Iterate through every bitmask from 0 to 2^n - 1.
        for mask in range(1 << n):
            subset = []

            # Build the subset based on which bits are set in the mask.
            for i in range(n):
                if mask & (1 << i):
                    subset.append(nums[i])

            result.append(subset)

        return result


# Example usage:
if __name__ == "__main__":
    nums = [1, 2, 3]
    solution = Solution()
    print(solution.subsets(nums))