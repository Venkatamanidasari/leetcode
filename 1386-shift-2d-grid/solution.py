class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        k %= total

        # Flatten the grid
        a = [num for row in grid for num in row]

        # Rotate the flattened list
        a = a[-k:] + a[:-k]

        # Reconstruct the 2D grid
        new_grid = []
        for i in range(m):
            new_grid.append(a[i * n:(i + 1) * n])

        return new_grid
