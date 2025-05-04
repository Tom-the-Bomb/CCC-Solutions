# PARTIAL SOLUTION: TIME LIMIT EXCEEDED

from heapq import heappush, heappop

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = {}

for _ in range(M):
    a, b, c = map(int, input().split())

    if a not in graph:
        graph[a] = [(b, c)]
    else:
        graph[a].append((b, c))

    if b not in graph:
        graph[b] = [(a, c)]
    else:
        graph[b].append((a, c))

heap = []
heappush(heap, (0, 0, 1))

seen = {}

while heap:
    cost, chilling, node = heappop(heap)

    if node == N:
        print(cost)
        break

    for next_node, next_temp in graph[node]:
        next_cost = cost + abs(next_temp - chilling)
        key = (next_node, next_temp)

        if key not in seen or seen[key] > next_cost:
            seen[key] = next_cost
            heappush(heap, (next_cost, next_temp, next_node))