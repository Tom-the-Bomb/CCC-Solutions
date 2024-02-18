"""
Solution for problem 4: Good Groups
"""

class Solution:
    def good_groups_bf(self) -> int:
        X = int(input())
        same = [frozenset(input().split()) for _ in range(X)]
        Y = int(input())
        not_same = [frozenset(input().split()) for _ in range(Y)]
        G = int(input())
        groups = [frozenset(input().split() for _ in range(G))]

        violated = 0
        for condition in same:
            violated += not any(condition.issubset(group) for group in groups)

        for condition in not_same:
            violated += any(condition.issubset(group) for group in groups)

        return violated

    def good_groups(self) -> int:
        X = int(input())
        same = [input().split() for _ in range(X)]
        Y = int(input())
        not_same = [input().split() for _ in range(Y)]

        group_map = {}
        for i in range(int(input())):
            for name in input().split():
                group_map[name] = i

        violated = 0
        for a, b in same:
            violated += group_map[a] != group_map[b]

        for a, b in not_same:
            violated += group_map[a] == group_map[b]

        return violated