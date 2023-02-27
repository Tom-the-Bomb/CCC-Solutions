"""
Solution for problem 2: Chili Peppers
"""

class Solution:
    mapping: dict[str, int] = {
        'poblano': 1500,
        'mirasol': 6000,
        'serrano': 15500,
        'cayenne': 40000,
        'thai': 75000,
        'habanero': 125000,
    }

    def chili_peppers(self, input: str) -> int:
        _, *chilis = input.splitlines()

        return sum(self.mapping.get(chili.lower(), 0) for chili in chilis)