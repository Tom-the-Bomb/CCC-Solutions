from math import ceil

n = int(input())
mtns = [int(mtn) for mtn in input().split()]

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
print(out)