
class Solution:
    def magical_magnetic_marbles(self) -> int:
        N, K = map(int, input().split())
        slots = [int(marble) for marble in input()]

        for i in range(1, N):
            if slots[i] and slots[i - 1]:
                slots[i - 1] = 0

        sections = []
        curr_zeroes = 0
        ones = 0

        for slot in slots:
            if slot:
                ones += 1
                if ones >= 2:
                    # do not include leading spaces
                    # (meaning there must be at least 2 ones recorded: 1 is the left bound, 1 is the right bound that was just incremented)
                    # as a leading space means that there is 1 space to the right,
                    # meaning that inserting marbles there will end up not changing the # of 1s in that section
                    # as they will all merge towards the 1 on the right anyways
                    sections.append(curr_zeroes)
                curr_zeroes = 0
            else:
                curr_zeroes += 1

        sections.sort()

        if sections:
            for section in sections:
                if section <= K:
                    # if we can fill in the entire section
                    # we do so, and the original 2 1s that walled off the section will
                    # all become a single 1 since we connected them and merged
                    #
                    # i.e. 10001 -<fill 3>-> 11111 -> 00001
                    K -= section
                    # since those 2 became 1, we can just decrement the total count
                    ones -= 1
                else:
                    # indicating that we have ran out of marbles
                    # since `sections` is sorted, if we cant fill this section
                    # then all sections after it also cannot be filled since they can only be bigger
                    break
        else:
            # no "sections" of 0s that are walled off by 1s found
            # the answer will be 1, if k > 0 (there are marbles to place) as they will all merge into one
            # or 0 if there are none to place
            ones = 1 if K else 0

        return ones