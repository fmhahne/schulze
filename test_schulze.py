from collections import defaultdict

from schulze import add_ballot, schulze


def test_example_1():
    example1 = defaultdict(int)
    add_ballot(example1, "A>C>D>B", 8)
    add_ballot(example1, "B>A>D>C", 2)
    add_ballot(example1, "C>D>B>A", 4)
    add_ballot(example1, "D>B>A>C", 4)
    add_ballot(example1, "D>C>B>A", 3)

    result1 = schulze(example1)

    assert result1.strengths == {
        ("A", "B"): 14,
        ("A", "C"): 14,
        ("A", "D"): 12,
        ("B", "A"): 13,
        ("B", "C"): 13,
        ("B", "D"): 12,
        ("C", "A"): 13,
        ("C", "B"): 15,
        ("C", "D"): 12,
        ("D", "A"): 13,
        ("D", "B"): 19,
        ("D", "C"): 13,
    }

    assert result1.winners == {"D"}


def test_example_4():
    example4 = defaultdict(int)
    add_ballot(example4, "A>B>C>D", 3)
    add_ballot(example4, "C>B>D>A", 2)
    add_ballot(example4, "D>A>B>C", 2)
    add_ballot(example4, "D>B>C>A", 2)

    result4 = schulze(example4)

    assert result4.strengths == {
        ("A", "B"): 5,
        ("A", "C"): 5,
        ("A", "D"): 5,
        ("B", "A"): 5,
        ("B", "C"): 7,
        ("B", "D"): 5,
        ("C", "A"): 5,
        ("C", "B"): 5,
        ("C", "D"): 5,
        ("D", "A"): 6,
        ("D", "B"): 5,
        ("D", "C"): 5,
    }

    assert result4.winners == {"B", "D"}


def test_example_10():
    example10 = defaultdict(int)
    add_ballot(example10, "A>B>C>D", 6)
    add_ballot(example10, "A=B>C=D", 8)
    add_ballot(example10, "A=C>B=D", 8)
    add_ballot(example10, "A=C>D>B", 18)
    add_ballot(example10, "A=C=D>B", 8)
    add_ballot(example10, "B>A=C=D", 40)
    add_ballot(example10, "C>B>D>A", 4)
    add_ballot(example10, "C>D>A>B", 9)
    add_ballot(example10, "C=D>A=B", 8)
    add_ballot(example10, "D>A>B>C", 14)
    add_ballot(example10, "D>B>C>A", 11)
    add_ballot(example10, "D>C>A>B", 4)

    result10 = schulze(example10)

    assert result10.strengths == {
        ("A", "B"): 67,
        ("A", "C"): 67,
        ("A", "D"): 45,
        ("B", "A"): 45,
        ("B", "C"): 79,
        ("B", "D"): 45,
        ("C", "A"): 45,
        ("C", "B"): 45,
        ("C", "D"): 45,
        ("D", "A"): 50,
        ("D", "B"): 72,
        ("D", "C"): 72,
    }

    assert result10.winners == {"D"}
