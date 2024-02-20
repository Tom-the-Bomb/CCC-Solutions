"""
Problem 1. Shell Game

http://www.usaco.org/index.php?page=viewproblem2&cpid=891
"""

class Solution:
    def shell_game(self, inp: str) -> int:
        shells = [1, 2, 3]
        _, *lines = inp.splitlines()

        scores = [0, 0, 0]
        for line in lines:
            a, b, g = [int(x) for x in line.split()]
            shells[a - 1], shells[b - 1] = shells[b - 1], shells[a - 1]
            scores[shells[g - 1] - 1] += 1
        return max(scores)