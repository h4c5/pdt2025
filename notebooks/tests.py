from typing import Any, Callable, Iterable

BASE_VOCAB = {idx: bytes([idx]) for idx in range(256)}


class FunctionNotFound(Exception):
    """La fonction n'a pas été trouvée dans les fonctions à tester."""


class TestFailures(Exception):
    """Des cas de tests sont en erreur."""


def test_func(func: Callable, test_cases: Iterable[tuple[tuple, Any]]):
    """Test générique d'une fonction à partir d'une liste de cas de test."""

    failures = 0

    for i, (args, expected) in enumerate(test_cases):
        # Cas où la fonction doit renvoyer une exception
        if isinstance(expected, type) and issubclass(expected, Exception):
            try:
                func(*args)
            except expected:
                print(f"✅ TEST {i}")
            except Exception as e:
                print(
                    f"❌ TEST {i} | arguments : {args} | "
                    f"exception attendue : {expected} | exception obtenue : {e}"
                )
                failures += 1

        # Cas où la fonction ne renvoie pas la bonne sortie
        elif (result := func(*args)) != expected:
            print(
                f"❌ TEST {i} | arguments : {args} | "
                f"attendu : {expected} | obtenu : {result}"
            )

            failures += 1

        # Cas où tout roule
        else:
            print(f"✅ TEST {i}")

    if failures > 0:
        raise TestFailures(f"{failures} tests en erreur")


def test(func: Callable, keyword: str | None = None):
    """Test automatique à partir du nom de la fonction."""

    # Cas de tests des différentes fonctions
    TESTCASES_TOP_PAIR = (
        (([1, 2, 1, 2, 3],), ((1, 2), 2)),
        (([],), None),
        (([1],), None),
    )

    TESTCASES_MERGE = (
        (([1, 2, 3, 1, 2, 3, 4], (2, 3), 5), [1, 5, 1, 5, 4]),
        (([1, 2, 3, 1, 2, 3, 4], (1, 3), 5), [1, 2, 3, 1, 2, 3, 4]),
        (([], (1, 2), 3), []),
        (([1], (1, 2), 3), [1]),
    )

    TESTCASES_TRAIN = (
        (
            ("ploc, ploc, la pluie pleut", 266),
            {
                (112, 108): 256,
                (32, 256): 257,
                (111, 99): 258,
                (258, 44): 259,
                (256, 259): 260,
                (260, 257): 261,
                (261, 259): 262,
                (262, 32): 263,
                (263, 108): 264,
                (264, 97): 265,
            },
        ),
        (("", 266), {}),
        (("", 100), ValueError),
    )

    TESTCASES_ENCODE = (
        (
            (
                "ploc, ploc",
                {(112, 108): 256, (32, 256): 257, (111, 99): 258, (258, 44): 259},
            ),
            [256, 259, 257, 258],
        ),
        (("ploc, ploc", {}), [112, 108, 111, 99, 44, 32, 112, 108, 111, 99]),
        (("", {}), []),
    )

    TESTCASES_VOCAB = (
        (
            ({(112, 108): 256, (32, 256): 257, (111, 99): 258},),
            {**BASE_VOCAB, 256: b"pl", 257: b" pl", 258: b"oc"},
        ),
        (({},), {**BASE_VOCAB}),
    )

    TESTCASES_DECODE = (
        (
            ([112, 108, 111, 99, 44, 32, 112, 108, 111, 99], BASE_VOCAB),
            "ploc, ploc",
        ),
        (
            (
                [256, 259, 257, 258],
                {**BASE_VOCAB, 256: b"pl", 257: b" pl", 258: b"oc", 259: b"oc,"},
            ),
            "ploc, ploc",
        ),
        (([], BASE_VOCAB), ""),
        (([256], BASE_VOCAB), Exception),  # Cas où le token n'existe pas
    )

    # Association des cas de tests aux fonctions
    TEST_FUNCS = {
        "merge": TESTCASES_MERGE,
        "pair": TESTCASES_TOP_PAIR,
        "train": TESTCASES_TRAIN,
        "encode": TESTCASES_ENCODE,
        "vocab": TESTCASES_VOCAB,
        "decode": TESTCASES_DECODE,
    }

    # Si le mot clé est passé en entrée, on invoque les cas de test directement.
    if keyword:
        return test_func(func, TEST_FUNCS[keyword])

    # Sinon on recherche les cas de test à invoquer.
    found = False

    for func_keyword, func_testcases in TEST_FUNCS.items():
        if func_keyword in func.__name__.lower():
            found = True

            test_func(func, func_testcases)
            break

    if not found:
        raise FunctionNotFound(
            f"Aucun test trouvé pour la fonction {func.__name__}. Les cas de tests "
            f"sont basés sur les mots clés suivants : '{"', '".join(TEST_FUNCS)}'. "
            f"Vous pouvez invoquer directement les cas de test d'un mot clé. Exemple : "
            f"test(func, 'encode')"
        )
