from typing import Callable

import click

MergeSignature = Callable[[list[int], tuple[int, int], int], list[int]]


def test_merge(func_merge: MergeSignature):
    """Test de la fonction merge."""

    test_cases = ((([1, 2, 3, 1, 2, 3, 4], (2, 3), 5), [1, 5, 1, 5, 4]),)

    for i, (arg, expected) in enumerate(test_cases):
        if func_merge(*arg) != expected:
            click.secho(f"❌ TEST {i: >2}", fg="red")
        else:
            click.secho(f"✅ TEST {i: >2}", fg="green")
