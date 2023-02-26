"""
Solution for problem 3: Palindrome Poster
"""

class Solution:
    def palindrome_poster(self, input: str) -> str:
        n, m, r, c = [int(x.strip()) for x in input.split()]

        poster = [['a'] * m for _ in range(n)]