# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# Compute how much water it can trap after raining.



class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        max_left = [0] * n
        max_right = [0] * n

        max_left[0] = height[0]

        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], height[i])

        max_right[n - 1] = height[n - 1]

        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i])

        water = 0

        for i in range(n):
            water_level = min(max_left[i], max_right[i])
            water += water_level - height[i]

        return water


if __name__ == "__main__":
    height = list(map(int, input("Enter bar heights separated by spaces: ").split()))
    print("Trapped rain water:", Solution().trap(height))