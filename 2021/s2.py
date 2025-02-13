
from collections import defaultdict

N = int(input())
M = int(input())
K = int(input())

rows = defaultdict(int)
cols = defaultdict(int)

for _ in range(K):
    typ, idx = input().split()

    idx = int(idx) - 1

    if typ == 'R':
        rows[idx] += 1
    else:
        cols[idx] += 1

print(sum(
    (rows[i] + cols[j]) % 2
    for i in range(N)
    for j in range(M)
))