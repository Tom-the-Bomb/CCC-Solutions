cities, roads = map(int, input().split())

graph = {
    int((road := input().split())[0]): int(road[1])
    for _ in range(roads)
}
new_roads = [f'{i} {i + 1}' for i in range(1, roads + 1) if not graph.get(i)]

print(len(new_roads))
print(*new_roads, sep='\n')