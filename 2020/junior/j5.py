from collections import deque


class Solution:
    def escape_room(self):
        M = int(input())
        N = int(input())
        grid = [[int(x) for x in input().split()] for _ in range(M)]

        seen = set()
        queue = deque([(1, 1)])

        while queue:
            row, col = queue.popleft()

            for i in range(1, M + 1):
                for j in range(1, N + 1):
                    if i * j == grid[row - 1][col - 1] and (i, j) not in seen:
                        if i == M and j == M:
                            return 'yes'

                        queue.append((i, j))
                        seen.add((i, j))
        return 'no'

    def escape_room_dfs(self):
        M = int(input())
        N = int(input())
        grid = [[int(x) for x in input().split()] for _ in range(M)]

        seen = set()

        def dfs(row, col):
            if row == M and col == M:
                return True

            if (row, col) in seen:
                return False

            return dfs()
