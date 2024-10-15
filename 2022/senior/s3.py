
N, M, K = [int(n) for n in input().split()]

ans = []

for i in range(N):
    rem = N - i - 1
    cur = min(K - rem, M)

    if cur <= 0:
        break
    if cur > i:
        cur = val = min(M, i + 1)
    else:
        val = ans[i - cur]

    ans.append(val)
    K -= cur

if K == 0 and len(ans) == N:
    print(' '.join(map(str, ans)))
else:
    print(-1)