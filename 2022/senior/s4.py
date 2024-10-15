from math import comb

def s4_nCr() -> None:
    N, C = map(int, input().split())
    semi_C = C // 2

    points = {}

    for name, pos in enumerate(input().split(), 1):
        pos = int(pos)
        if pos not in points:
            points[pos] = 0
        points[pos] += 1

    total = comb(N, 3)

    rest = sum(points.get(i % C, 0) for i in range(1, semi_C + 1))

    for start in range(C):

        first_point = points.get(start, 0)
        if start != 0:
            rest -= points.get(start % C, 0)
            rest += points.get((start + semi_C) % C, 0)

        total -= first_point * comb(rest, 2) + comb(first_point, 2) * rest + comb(first_point, 3)

    if C % 2 == 0:
        for start in range(semi_C):
            first_point = points.get(start, 0)
            last_point = points.get(start + semi_C, 0)

            total += first_point * comb(last_point, 2) + comb(first_point, 2) * last_point

    print(total)

def s4_no_nCr() -> None:
    N, C = map(int, input().split())
    semi_C = C // 2

    points = {}

    for name, pos in enumerate(input().split(), 1):
        pos = int(pos)
        if pos not in points:
            points[pos] = 0
        points[pos] += 1

    total = N * (N-1) * (N-2) // 6

    rest = sum(points.get(i % C, 0) for i in range(1, semi_C + 1))

    for start in range(C):

        first_point = points.get(start, 0)
        if start != 0:
            rest -= points.get(start % C, 0)
            rest += points.get((start + semi_C) % C, 0)

        total -= (
            (first_point * rest * (rest - 1)) // 2
            + (first_point * (first_point - 1) * rest) // 2
            + (first_point * (first_point - 1) * (first_point - 2)) // 6
        )

    if C % 2 == 0:
        for start in range(semi_C):
            first_point = points.get(start, 0)
            last_point = points.get(start + semi_C, 0)

            total += (
                first_point * last_point * (last_point - 1) // 2
                + first_point * (first_point - 1) * last_point // 2
            )

    print(total)

if __name__ == '__main__':
    s4_nCr()