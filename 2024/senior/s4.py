from collections import defaultdict
from typing import Literal
from sys import setrecursionlimit
setrecursionlimit(300_000)

_, M = map(int, input().split())

graph = defaultdict(list)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, i))
    graph[b].append((a, i))

seen = set()
paint = ['G'] * M

def dfs(node: int, color: Literal['R', 'B']) -> None:
    for neighbor, edge in graph[node]:
        if neighbor not in seen:
            seen.add(neighbor)
            paint[edge] = color
            dfs(neighbor, 'B' if color == 'R' else 'R')

for node in graph:
    if node not in seen:
        dfs(node, 'R')

print(''.join(paint))