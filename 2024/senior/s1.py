N = int(input())

circle = [int(input()) for _ in range(N)]
offset = len(circle) // 2
count = 0

for i, person in enumerate(circle[:offset]):
    if person == circle[i + offset]:
        count += 2
print(count)