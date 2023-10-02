"""
Solution for problem 3: Harp Tuning
"""

import re

class Solution:
    def harp_tuning(self, input: str) -> int:
        parsed = re.split(r'([+-]\d+)', input)

        output = ''
        for element in parsed:
            if element.isalpha():
                output += element
            elif element:
                output += f" {'tighten' if element.startswith('+') else 'loosen'} {element[1:]}\n"
        return output.strip('\n')