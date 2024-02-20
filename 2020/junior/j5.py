"""
Solution for problem 5: Escape Room
"""

from collections import deque, defaultdict
import sys

sys.setrecursionlimit(999_999_999)

class Solution:
    def escape_room_bfs_bf(self) -> str:
        # BFS implementation
        # brute force by finding factors using double for-loop

        M = int(input())
        N = int(input())
        grid = [[int(x) for x in input().split()] for _ in range(M)]

        seen = set()
        queue: deque[tuple[int, int]] = deque([(1, 1)])

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

    def escape_room(self) -> str:
        # [best solution]: BFS + mapping table

        M = int(input())
        N = int(input())

        # maps <K = tile value> -> all <tile value>s of location (a, b) where a * b = K
        #
        # we can use this as a lookup table to find all locations we can jump to at any given tile, `K`
        grid = defaultdict(list[int])

        for i in range(1, M + 1):
            for j, tile in enumerate(input().split(), 1):
                grid[i * j].append(int(tile))

        seen = set()
        # a tile of value `1` doesn't physically exist
        # but it will get us mapped to the tile at (1, 1) since only 1 * 1 = 1
        queue = deque([1])

        while queue:
            tile = queue.popleft()

            # we know we can get to the end if we are a tile K, where K = M * N,
            # meaning that we can reach (M, N) which is the end tile
            if tile == M * N:
                return 'yes'

            for tile in grid[tile]:
                if tile not in seen:
                    queue.append(tile)
                    seen.add(tile)
        return 'no'

    def escape_room_dfs(self):
        # DFS + mapping table

        M = int(input())
        N = int(input())

        # maps <K = tile value> -> all <tile value>s of location (a, b) where a * b = K
        #
        # we can use this as a lookup table to find all locations we can jump to at any given tile, `K`
        grid = defaultdict(list[int])

        for i in range(1, M + 1):
            for j, tile in enumerate(input().split(), 1):
                grid[i * j].append(int(tile))

        seen = set()

        def _dfs(tile: int) -> str:
            if tile not in seen:
                if tile == M * N:
                    return 'yes'

                seen.add(tile)

                for tile in grid[tile]:
                    result = _dfs(tile)

                    if result == 'yes':
                        return result
            return 'no'

        return _dfs(1)