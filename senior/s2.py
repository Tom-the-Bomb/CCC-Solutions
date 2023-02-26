"""
Solution for problem 2: Symmetric mountains
"""

from math import ceil

class Solution:
    def symmetric_mountains(self, input: str) -> str:
        n, mtns = input.splitlines()
        n = int(n.strip())
        mtns = [int(m) for m in mtns.split()]

        out = '0'

        for length in range(2, len(mtns) + 1):
            syms = []
            for i in range(len(mtns)):
                slice = mtns[i:i + length]
                if len(slice) == length:
                    syms.append(sum(
                        abs(slice[i] - slice[-i - 1]) for i in range(ceil(len(slice) / 2))
                    ))
            out += f' {min(syms)}'
        return out