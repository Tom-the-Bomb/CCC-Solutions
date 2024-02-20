"""
Solution for problem 5: Choose Your Own Path
"""

from itertools import chain

class Solution:
    def choose_your_own_path(self) -> str:
        N = int(input())
        pages = [input() for _ in range(N)]

        path_lengths = []

        def find(page: str, length: int, visited: list[int]) -> None:
            M, *targets = page.split()
            if M == '0':
                return path_lengths.append(length)

            for i in targets:
                i = int(i)
                if i in visited:
                    return
                find(pages[i - 1], length + 1, visited + [i])

        find(pages[0], 1, [1])
        not_accessed = set(chain(*[page.split()[1:] for page in pages])) == set(range(2, N + 1))
        return f'{("Y", "N")[not_accessed]}\n{min(path_lengths)}'

    # Alternative implementations below ...:
    #
    # (WIP)
    def choose_your_own_path_2(self) -> str:
        N = int(input())
        pages = {
            i: [int(j) for j in input().split()[1:]]
            for i in range(1, N + 1)
        }
        all_paths = []
        other_paths = [
            [1, [1]]
        ]

        while other_paths:
            curr_page, dest_pages = other_paths.pop(0)
            if not pages[curr_page]:
                all_paths.append(dest_pages)

            for dest_page in pages[curr_page]:
                if dest_page in dest_pages:
                    continue
                else:
                    other_paths.append([dest_page, dest_pages + [dest_page]])

        print(f'{pages}\n\n')
        for path in all_paths:
            print(path)
        return ''

    def choose_your_own_path_bfs(self) -> str:
        N = int(input())
        pages = {
            i: [int(j) for j in input().split()[1:]]
            for i in range(1, N + 1)
        }

        frontier = [1]
        visited = []

        add, step = True, 0

        while frontier:
            if add:
                step += 1
            for _ in range(len(frontier)):
                cur = frontier.pop(0)
                for child in pages[cur]:
                    frontier.append(child)

                visited.append(cur)
                if not pages[cur]:
                    add = False

        all_accessed = set(range(1, int(N) + 1)) == set(visited)
        return f'{("N", "Y")[all_accessed]}\n{step}'