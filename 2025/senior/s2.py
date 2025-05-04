import re

import sys
input = sys.stdin.readline

cipher = input()
c = int(input())

n = len(cipher)

length = 0
breakpoints = []

for char, count in re.findall(r'([a-z])([0-9]+)', cipher):
    count = int(count)
    length += count

    # OLD IMPLEMENTATION:
    #
    # if not breakpoints:
    #     breakpoints.append((count, char))
    # else:
    #     breakpoints.append((breakpoints[-1][0] + count, char))
    #
    # OPTIMIZED IMPLEMENTATION:
    #
    breakpoints.append((length, char))

c %= length

for breakpoint, char in breakpoints:
    if c < breakpoint:
        print(char)
        sys.exit(0)