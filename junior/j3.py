"""
Solution for problem 3: Special Event
"""

class Solution:
    def special_event(self, input: str) -> str:
        _, *people = input.splitlines()

        transposed = [
            [people[j][i] for j in range(len(people))]
            for i in range(len(people[0]))
        ]

        return ','.join([
            str(d) for d, elem in enumerate(transposed, 1)
            if elem.count('Y') == max(transposed, key=lambda a: a.count('Y'))
                .count('Y')
        ])