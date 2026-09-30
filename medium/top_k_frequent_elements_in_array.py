#Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        # Step 1: Count how many times each number appears
        frequency = {}

        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        # Example:
        # nums = [1, 1, 1, 2, 2, 3]
        #
        # frequency = {
        #     1: 3,
        #     2: 2,
        #     3: 1
        # }

        # Step 2: Sort the numbers based on their frequency
        numbers = list(frequency.keys())

        numbers.sort(
            key=lambda num: frequency[num],
            reverse=True
        )

        # Now:
        # numbers = [1, 2, 3]

        # Step 3: Return the first k numbers
        return numbers[:k]


def main():
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    k = int(input("Enter k: "))
    result = Solution().topKFrequent(nums, k)
    print(result)


if __name__ == "__main__":
    main()