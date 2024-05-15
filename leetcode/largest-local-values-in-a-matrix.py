class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        result = [[0] * (n - 2) for _ in range(n - 2)]

        for i in range(1, n - 1):
            for j in range(1, n - 1):
                max_value = 0
                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                        max_value = max(max_value, grid[x][y])
                result[i - 1][j - 1] = max_value

        return result
