"""
Solution for problem 2: Fergusonball Ratings
"""

class Solution:
    def fergusonball_ratings(self, input: str) -> int:
        n, *data = input.splitlines()
        data = [data[i:i + 2] for i in range(0, len(data), 2)]

        gold = sum(1 for score, foul in data if int(score) * 12 - int(foul) * 3 > 40)
        return f"{gold}{'+' if gold == int(n) else ''}"