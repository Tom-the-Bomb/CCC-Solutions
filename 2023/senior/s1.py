
c = int(input())

tiles = [
    [int(t) for t in input().split()],
    [int(t) for t in input().split()],
]
meters = 0

for y, row in enumerate(tiles):
    for x, tile in enumerate(row):
        if tile == 1:
            beside = (
                (y, x - 1),
                (y, x + 1),
            )
            if y == 0:
                beside += (1, x),
            else:
                beside += (0, x),

            meters += [
                tiles[i][j] == 0 if i in range(2) and j in range(c) else True
                for i, j in beside
            ].count(True)
print(meters)