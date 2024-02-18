N, K = map(int, input().split())
slots = [int(marble) for marble in input()]

for i in range(N):
    if i > 0:
        if slots[i] and slots[i - 1]:
            slots[i - 1] = 0

print(slots)

groups, amount, ones = [], 0, 0

for i in range(N):
    if slots[i]: # slot[i] = 1
        if ones:
            ones += 1
            groups.append(amount)
        else:
            ones += 1
        amount = 0
    else: # slots[i] = 0
        amount += 1

groups.sort()

print(groups)
print(ones)

if groups:
    for group in groups:
        if group <= K:
            K -= group
            ones -= 1
        else:
            break
else:
    if K:
        ones = 1
    else:
        ones = 0

print(ones)