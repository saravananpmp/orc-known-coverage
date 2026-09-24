# ORACLE FIXTURE — do not "improve" this file. Its shape is the test.
#
# Built so that coverage is an exact, hand-countable number:
#   statements  28 of 35 covered  = 80.0%
#   branches     4 of  8 covered  = 50.0%
#
# add/subtract/label/tally and the two module constants are fully exercised.
# classify and bucket are exercised on BOTH paths (4 branch arcs).
# parity and scale are never called at all (7 statements, 4 arcs, all missed).

DEFAULT_LABEL = "unnamed"
MAX_ITEMS = 100


def add(a, b):
    total = a + b
    return total


def subtract(a, b):
    diff = a - b
    return diff


def classify(n):
    if n > 0:
        return "positive"
    return "non-positive"


def bucket(n):
    if n < 10:
        return "small"
    return "large"


def parity(n):
    if n % 2 == 0:
        return "even"
    return "odd"


def scale(n):
    if n > 100:
        doubled = n * 2
        return doubled
    return n


def label(name):
    cleaned = name.strip()
    lowered = cleaned.lower()
    prefixed = "item-" + lowered
    trimmed = prefixed[:32]
    return trimmed


def tally(first, second):
    running = first + second
    capped = min(running, MAX_ITEMS)
    return capped
