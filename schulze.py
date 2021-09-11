"""Calculate Schulze winner from winning votes table"""

from itertools import chain, permutations
from typing import NamedTuple


def add_ballot(
    winning_votes: dict[tuple[str, str], int], ballot: str, votes: int = 1
) -> None:
    """Add votes from ballot to winning votes table"""

    ranks = {}
    for i, group in enumerate(ballot.split(">"), 1):
        for candidate in group.split("="):
            ranks[candidate.strip()] = i

    for a, b in permutations(ranks, 2):
        if ranks[a] < ranks[b]:
            winning_votes[a, b] += votes


class SchulzeResult(NamedTuple):
    """Holds result of a Schulze method election"""

    winners: set[str]
    strengths: dict[tuple[str, str], int]


def schulze(winning_votes: dict[tuple[str, str], int]) -> SchulzeResult:
    """Use Schulze method to find winners and strength of strongest path"""

    candidates = set(chain.from_iterable(winning_votes))
    strengths = {}

    for a, b in permutations(candidates, 2):
        if winning_votes[a, b] > winning_votes[b, a]:
            strengths[a, b] = winning_votes[a, b]
        else:
            strengths[a, b] = 0

    # Floyd-Warshall algorithm to find strength strengths[a, b] of strongest
    # path from candidate a to candidate b
    for a, b, c in permutations(candidates, 3):
        strengths[b, c] = max(strengths[b, c], min(strengths[b, a], strengths[a, c]))

    check_winner = lambda a: all(
        strengths[a, b] >= strengths[b, a] for b in candidates.difference([a])
    )
    winners = set(filter(check_winner, candidates))

    return SchulzeResult(winners, strengths)
