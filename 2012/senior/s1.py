"""
Solution for problem 1: Don't pass me the ball
"""
from math import factorial

class Solution:
    def dont_pass_me_the_ball(self) -> int:
        N = int(input())

        if N < 4:
            # negative factorial values are not defined
            #
            # in the context of the problem, 4 players is a required minimum to play too
            return 0
        else:
            # [(n - 1) choose 3] -> [(n- 1)! / (3! - ((n - 1) - 3)!)]
            return int(
                factorial(N - 1)
                / (6 * factorial(N - 4))
            )