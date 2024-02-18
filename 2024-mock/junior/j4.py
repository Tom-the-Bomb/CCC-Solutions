from collections import deque

N, K = map(int, input().split())
marbles = input()

marbles_arr = ''
for i in range(len(marbles) - 1, -1, -1):
    try:
        if marbles[i + 1] == '1':
            marbles_arr = '0' + marbles_arr
        else:
            marbles_arr = marbles[i] + marbles_arr
    except IndexError:
        marbles_arr = marbles[i] + marbles_arr

print(marbles_arr)

zeroes = [len(s) for s in marbles_arr.split('1') if s]
zeroes.sort()

ones = marbles_arr.count('1')
print(zeroes, ones)
for space in zeroes:
    if space <= K:
        K -= space
        ones -= 1

print(ones)