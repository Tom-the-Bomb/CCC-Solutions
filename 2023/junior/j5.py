"""
Solution for problem 5: Word Hunt
"""

class Solution:
    increments: set[tuple[int, ...]] = {
        (1,), (-1,),
        (0, 1), (0, -1),
        (1, 1), (-1, -1),
        (1, -1), (-1, 1),
    }

    def word_hunt(self, input: str) -> int:
        word, r, c, *arr = input.splitlines()
        r, c = int(r), int(c)
        amount = 0

        def recursive_search(
            row: int, col: int,
            index: int = 0,
            x_incr: int = 0, y_incr: int = 0,
            *,
            has_turned: bool = False,
        ) -> None:
            if len(word) == index:
                nonlocal amount
                amount += 1

            elif row in range(r) and col in range(c):
                if word[index] == arr[row][col]:
                    recursive_search(
                        row=row + x_incr,
                        col=col + y_incr,
                        index=index + 1,
                        x_incr=x_incr,
                        y_incr=y_incr,
                    )
                elif not has_turned and index > 1:
                    if x_incr == 0:
                        turns = {(1, 0), (-1, 0)}
                    elif y_incr == 0:
                        turns = {(0, 1), (0, -1)}
                    else:
                        turns = {(-x_incr, y_incr), (x_incr, -y_incr)}

                    for (x_incr, y_incr) in turns:
                        recursive_search(
                            row=row + x_incr,
                            col=col + y_incr,
                            index=index + 1,
                            x_incr=x_incr,
                            y_incr=y_incr,
                            has_turned=True,
                        )

        for i in range(r):
            for j in range(c):
                for increments in self.increments:
                    recursive_search(
                        i, j, 0,
                        *increments,
                    )
        return amount