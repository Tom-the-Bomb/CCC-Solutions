"""
Solution for problem 3: Palindrome Poster
"""

class Solution:
    def palindrome_poster(self, input: str) -> str:
        n, m, r, c = map(int, input.splitlines())

        poster = [['b'] * m for _ in range(n)]
        
        if r == 1 and c == 1:
            poster[0] = ['a'] * c
            for i in range(r):
                poster[0][i] = 'a'
        else:
            ...
        
        return '\n'.join(' '.join(row) for row in poster)