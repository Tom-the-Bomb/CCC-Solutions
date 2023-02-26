"""
Solution for problem 4: Minimum Cost Roads
"""

class Solution:
    def minimum_cost_roads(self, input: str) -> int:
        n_m, *roads = input.splitlines()
        n, m = map(int, n_m.split())

        for u, v, l, c in roads:
            ...