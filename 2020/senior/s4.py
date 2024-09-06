from collections import Counter

seats = input()
n = len(seats)

cycle = seats * 2

seats_counter = Counter(seats)
n_A = seats_counter['A']
n_B = seats_counter['B']
n_C = seats_counter['C']

A_counter = Counter(seats[:n_A])
# if `B`s were placed after `A` => ABC -> BCA -> CAB
B_counter = Counter(seats[n_A:n_A + n_B])
# if `C`s were placed after `A` => ACB -> CBA -> BAC
C_counter = Counter(seats[n_A:n_A + n_C])

swaps = float('inf')

for i in range(n):
    seats = cycle[i:i + n]

    if i > 0:
        A_counter[cycle[i - 1]] -= 1
        A_counter[cycle[i + n_A - 1]] += 1

        B_counter[cycle[i + n_A - 1]] -= 1
        B_counter[cycle[i + n_A + n_B - 1]] += 1

        C_counter[cycle[i + n_A - 1]] -= 1
        C_counter[cycle[i + n_A + n_C - 1]] += 1

    swaps = min(
        swaps,
        A_counter['B'] + A_counter['C'] + B_counter['A'] + B_counter['C'] - min(A_counter['B'], B_counter['A']),
        A_counter['B'] + A_counter['C'] + C_counter['A'] + C_counter['B'] - min(A_counter['C'], C_counter['A']),
    )

print(swaps)