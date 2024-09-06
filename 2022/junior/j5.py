"""
Solution for problem 5: Square Pool
"""

class Solution:
    def square_pool_bf(self) -> int: # type: ignore
        N = int(input())

        trees = []
        for _ in range(int(input())):
            y, x = input().split()
            trees.append((int(x), int(y)))

        for n in range(N, 0, -1):
            for left in range(1, N - n + 2):
                for top in range(1, N - n + 2):
                    if any(left <= x <= left + n - 1 and top <= y <= top + n - 1 for x, y in trees):
                        continue
                    return n

    def square_pool(self) -> int:
        N = int(input())

        x_coords = [0]
        y_coords = [0]

        for _ in range(int(input())):
            x, y = input().split()

            x_coords.append(int(x))
            y_coords.append(int(y))

        ans = 1

        for x in x_coords:
            for y in y_coords:
                size = min(N - x, N - y)

                for tree_x, tree_y in zip(x_coords, y_coords):
                    if x < tree_x <= x + size and y < tree_y <= y + size:
                        size = max(tree_x - x - 1, tree_y - y - 1)
                ans = max(ans, size)
        return ans