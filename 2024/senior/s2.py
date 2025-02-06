from collections import Counter

T, N = map(int, input().split())
strings = [input() for _ in range(T)]

for string in strings:
    counter = Counter(string)

    for i in range(1, N):
        if (counter.get(string[i]) > 1) == (counter.get(string[i - 1]) > 1):
            print('F')
            break
    else:
        print('T')