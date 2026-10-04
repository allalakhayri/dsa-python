# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.


class Solution:
    def maxArea(self, height: list[int]) -> int:
        i = 0
        j = len(height) - 1
        max_area = 0

        while i < j:
            area = min(height[i], height[j]) * (j - i)
            max_area = max(max_area, area)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area


def main() -> None:
    user_input = input("Enter heights as space-separated integers: ").strip()
    if not user_input:
        print("No input provided.")
        return

    try:
        height = [int(value) for value in user_input.split()]
    except ValueError:
        print("Please enter valid integers separated by spaces.")
        return

    solution = Solution()
    print(f"height = {height} -> max area = {solution.maxArea(height)}")


if __name__ == "__main__":
    main()