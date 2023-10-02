"""
Solution for problem 1: Cupcake Party
"""

class Solution:
    def cupcake_party(self, input: str) -> int:
        r, s = input.splitlines()
        return int(r) * 8 + int(s) * 3 - 28