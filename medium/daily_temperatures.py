# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead.


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            t = temperatures[i]
            while stack and t > stack[-1][0]:
                _, stackIndex = stack.pop()
                res[stackIndex] = i - stackIndex
            stack.append([t, i])
        return res


def main():
    sol = Solution()
    tests = [
        [73, 74, 75, 71, 69, 72, 76, 73],
        [30, 40, 50, 60],
        [30, 60, 90],
    ]

    for temperatures in tests:
        print(temperatures, "->", sol.dailyTemperatures(temperatures))


if __name__ == "__main__":
    main()

           