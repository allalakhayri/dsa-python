# You are given an array of integers nums and an integer target.
# Return the indices of the two numbers that add up to target.
# Each input will have exactly one valid solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        m = {}

        for i in range(len(nums)):
            needed = target - nums[i]

            if needed in m:
                return [m[needed], i]

            m[nums[i]] = i


if __name__ == "__main__":
    result = Solution().twoSum([2, 7, 11, 15], 9)
    print(result)