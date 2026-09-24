# ORACLE FIXTURE — the set of tests here is calibrated.
# Adding a test for parity() or scale() will change the expected numbers.
from app.calc import add, subtract, classify, bucket, label, tally


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_classify_both_paths():
    assert classify(1) == "positive"
    assert classify(-1) == "non-positive"


def test_bucket_both_paths():
    assert bucket(1) == "small"
    assert bucket(99) == "large"


def test_label():
    assert label("  Widget ") == "item-widget"


def test_tally():
    assert tally(2, 4) == 6
