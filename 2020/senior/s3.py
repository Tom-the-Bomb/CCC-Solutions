from collections import Counter

needle = input()
haystack = input()

n = len(needle)

needle_counter = Counter(needle)
cand_counter = Counter()

seen = set()
count = 0

for i in range(len(haystack) - n + 1):
    candidate = haystack[i:i + n]
    if i == 0:
        cand_counter = Counter(candidate)
    else:
        cand_counter[haystack[i - 1]] -= 1
        cand_counter[haystack[i + n - 1]] += 1

    if cand_counter == needle_counter and candidate not in seen:
        count += 1
        seen.add(candidate)

print(count)