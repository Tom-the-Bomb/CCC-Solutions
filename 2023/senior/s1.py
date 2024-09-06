import re

c = int(input())

lines = input() + '|' + input()

print(
    lines.count('01') + lines.count('10') + lines.count('1') + lines.startswith('1') + lines.endswith('1') + ('1|' in lines) + ('|1' in lines)
)