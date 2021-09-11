Schulze method implementation in Python.

## Example

```python
>>> from collections import defaultdict
>>> from schulze import add_ballot, schulze
>>>
>>> winning_votes = defaultdict(int)
>>> add_ballot(winning_votes, "A>C>D>B", 8)
>>> add_ballot(winning_votes, "B>A>D>C", 2)
>>> add_ballot(winning_votes, "C>D>B>A", 4)
>>> add_ballot(winning_votes, "D>B>A>C", 4)
>>> add_ballot(winning_votes, "D>C>B>A", 3)
>>>
>>> result = schulze(winning_votes)
>>> result.strengths
{('B', 'A'): 13, ('B', 'C'): 13, ('B', 'D'): 12, ('A', 'B'): 14, ('A', 'C'): 14, ('A', 'D'): 12, ('C', 'B'): 15, ('C', 'A'): 13, ('C', 'D'): 12, ('D', 'B'): 19, ('D', 'A'): 13, ('D', 'C'): 13}
>>> result.winners
{'D'}
```
