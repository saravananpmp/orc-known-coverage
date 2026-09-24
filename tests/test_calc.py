# ORACLE FIXTURE — a GENUINE zero.
# These tests run and pass, but deliberately never import or call application
# code. Real coverage is therefore 0%. The platform must report 0 WITH evidence
# that the suite ran — not "not measured", and not a false PASS on the
# lower-is-better leaves.


def test_arithmetic_only():
    assert 2 + 3 == 5


def test_string_only():
    assert "widget".upper() == "WIDGET"
