"""
Solution for problem 1: Deliv-e-droid
"""

class Solution:
    def deliv_e_droid(self, input: str) -> int:
        p, c = [int(x.strip()) for x in input.splitlines()]

        score = p * 50 - c * 10
        if p > c:
            score += 500
        return score