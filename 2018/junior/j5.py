from itertools import chain

def choose_your_own_path(input: str) -> str:
    N, *pages = input.splitlines()
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
    not_accessed = set(chain(*[page.split()[1:] for page in pages])) == set(range(2, int(N) + 1))
    return f'{("Y", "N")[not_accessed]}\n{min(path_lengths)}'