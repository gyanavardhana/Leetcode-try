class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        memo = [[-1] * m for _ in range(n)]

        def maxMovesInGrid(i, j, prev, count):
            # Boundary check and comparison with previous cell value
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] <= prev:
                return count

            # Check memoized result
            if memo[i][j] != -1:
                return memo[i][j]

            # Store current cell's value and mark as visited
            temp = grid[i][j]
            grid[i][j] = -1  # Mark as visited

            # Recursive calls in three directions
            moves = max(
                maxMovesInGrid(i - 1, j + 1, temp, count + 1),
                maxMovesInGrid(i, j + 1, temp, count + 1),
                maxMovesInGrid(i + 1, j + 1, temp, count + 1)
            )
            memo[i][j] = moves  # Store result in memo

            # Restore cell's value after recursion
            grid[i][j] = temp
            return moves

        ans = 0
        for i in range(n):
            ans = max(ans, maxMovesInGrid(i, 0, -1, -1))

        return ans
        