
N = int(input())
coach, *burgers, josh = [int(burger) for burger in input().split()]

if josh == coach:
    print(1)
    exit()

dp = [1] + [1 if burger == coach else 0 if burger == josh else None for burger in burgers] + [0]

values = {}

for i in range(N - 1, -1, -1):
    if dp[i] is None:
        burger = burgers[i - 1]

        if seen := values.get(burger):
            dp[i] = seen
        else:
            values[burger] = dp[i] = (sum(dp[i + 1:N]) + 1) / (N - i) # type: ignore

print(dp)
print(sum(dp) / N) # type: ignore