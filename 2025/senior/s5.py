# PARTIAL SOLUTION: TIME LIMIT EXCEEDED

Q = int(input())

ans = 0

tasks = []
stasks = []

for _ in range(Q):
    typ, *ints = input().split()

    if typ == 'A':
        s, t = map(int, ints)

        s = (s + ans) % 1_000_003
        t = (t + ans) % 1_000_003

        task = [s, t, True]
        tasks.append(task)
        stasks.append(task)

        for j in range(len(stasks) - 2, -1, -1):
            if stasks[j] < stasks[j + 1]:
                break
            stasks[j], stasks[j + 1] = stasks[j + 1], stasks[j]
    else:
        i = int(ints[0])

        i = (i + ans) % 1_000_003
        tasks[i - 1][-1] = False

    time = 0

    for start, duration, exists in stasks:
        if exists:
            if time < start:
                time = start + duration - 1
            else:
                time += duration

    ans = time
    print(ans)