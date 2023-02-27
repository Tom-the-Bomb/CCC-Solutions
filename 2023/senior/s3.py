"""
Solution for problem 3: Palindrome Poster
"""

class Solution:
    def palindrome_poster(self, input: str) -> str:
        n, m, r, c = map(int, input.splitlines())

        poster = [['a'] * m for _ in range(n)]
        for i in range(r):
            poster[i]