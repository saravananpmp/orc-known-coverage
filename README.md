# orc-known-coverage — the calibration repo

A test repository whose coverage is **known by construction**. You do not need to
read code or run anything to use it: open the platform's report and compare the
numbers below. A difference is a platform defect, full stop.

Think of it as the test claim with a known expected payment. If the engine says
something else, the engine is wrong — no investigation needed to establish that.

## How it is built

`app/calc.py` has 35 statements and 8 branch arcs, all hand-countable:

* `add`, `subtract`, `label`, `tally` and the two module constants — fully exercised.
* `classify` and `bucket` — exercised on **both** paths (4 of the 8 arcs).
* `parity` and `scale` — **never called at all** (7 statements and 4 arcs, all missed).

7 missed of 35 is exactly 20%. 4 arcs of 8 is exactly 50%. Nothing rounds.

> Do not "improve" these files. Adding a test for `parity()` or `scale()`, or
> adding a loop or an `if`, changes the expected numbers and breaks the oracle.

## Expected values — branch `cov-80` (the everyday check)

| Measure | Expected | coverage.py key |
|---|---|---|
| **Statement coverage** | **80.00%** (28 of 35) | `percent_statements_covered` |
| **Branch coverage** | **50.00%** (4 of 8) | `percent_branches_covered` |
| Missed statements | 7 | `missing_lines` |
| Partial branches | 0 | `num_partial_branches` |
| Combined lines+branches | 74.42% | `percent_covered` |
| Tests | 6, all passing | — |

## Expected values — branch `cov-100`

| Measure | Expected |
|---|---|
| Statement coverage | **100.00%** (35 of 35) |
| Branch coverage | **100.00%** (8 of 8) |
| Tests | 8, all passing |

Catches the opposite error: a tool that under-reports when everything is covered.

## Expected values — branch `cov-genuine-zero`

Tests run and pass but never import application code, so the coverage is a **real
zero**, not a measurement failure.

| Measure | Expected |
|---|---|
| Statement coverage | **0.00%** (0 of 35) |
| Tests | 2, all passing |
| Branch totals | **absent from coverage.json entirely** |

Two things must be true in the report:

1. Statement coverage shows **0 with evidence that the suite ran** — never "not measured".
2. Branch coverage shows **N/A**, because coverage.py emitted no branch data at all.
   Reporting branch coverage as 0 here is the "no denominator became a real zero"
   defect, and this branch is its permanent regression test.

Lower-is-better leaves (Dead Code Detection, Partial Path Coverage) must **FAIL**
on this branch, not PASS. A false 100 there means the empty-stub bug is back.

## A defect this repo exposes immediately

`coverage.py` reports `percent_covered` as a **combined** lines+branches figure when
`--cov-branch` is on. For `cov-80` that is **74.42%**, not 80%.

`backend/wb-cpu-worker/app/parsers/python/coverage_py_parser.py` (lines 243-247) reads
`totals["percent_covered"]` into `line_pct`, and `coverage.line_percent` is bound to the
**"Statement Coverage %"** leaf. So the platform will report **74.42%**
where the true statement coverage is **80.00%** — a 5.58 point error,
with a mislabelled metric underneath it.

The fix is one line: use `percent_statements_covered` for the statement leaf and
`percent_branches_covered` for the branch leaf.

## Running it yourself (30 seconds, optional)

```bash
cd branches/cov-80
python3 -m pytest -q --cov=app --cov-branch --cov-report=term
```

<!-- demo run 2026-09-24T21:45:17Z -->
