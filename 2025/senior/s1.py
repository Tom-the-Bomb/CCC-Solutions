import sys
input = sys.stdin.readline

A, B, X, Y = map(int, input().split())

print(min(
    2 * (A + X + max(B, Y)),
    2 * (max(A, X) + B + Y),
))