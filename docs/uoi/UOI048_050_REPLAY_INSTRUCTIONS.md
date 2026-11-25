# UOI048–UOI050 exact elementary checker replay

**Purpose:** Re-run three narrow symbolic/rational receipts. This is not a Lean/Mathlib verification, not a proof of the PNT error estimate, not an original source/native form equivalence, and not full Gamma or prime operator certification.

From the repository root, with Python 3.11+ and network/package access:

```sh
python -m pip install -r scripts/uoi/requirements-uoi048-050.txt
python scripts/uoi/check_uoi048.py
python scripts/uoi/UOI049_prime_resonance_checker.py
python scripts/uoi/UOI050_discrepancy_checker.py
```

The scripts write, respectively:

```
research/unified/receipts/UOI048_exact_constant_receipt.json
research/unified/receipts/UOI049_prime_resonance_receipt.json
research/unified/receipts/UOI050_discrepancy_receipt.json
```

Review changes with `git diff -- research/unified/receipts/` after replay; checked-in receipts must not silently change. `sympy==1.14.0` is the version used for the UOI050 local replay. The other two scripts use only the Python standard library. No GitHub Actions workflow was added or triggered by these instructions.

**Limits and missing gates:**

- UOI048 verifies exact rational majorants, not the digamma kernel derivation or the source Gamma lower bound.
- UOI049 verifies isolation of the exact `n=8^M` prime-power shift under stated 8-adic geometry, not its identification with the actual collar sources or the Gamma-normalized operator norm.
- UOI050 verifies symbolic derivative/moment identities and geometric scaling; its test precursor is finitely differentiable after zero extension and is not a Schwartz source. Classical prime-number-theorem error, completed-space tail compactness and original prime normalization remain externally unverified.
- The completed family still lacks a certified positive infinite-tail margin `tau_M`, a sufficiently small `beta_M`, and exact source-to-native proof. No original Weil positivity or RH follows.

**Provenance:** Original UOI048 recovered as an exact checker/JSON receipt plus a summary-only intake, not a full analytic proof; UOI049/050 original artifacts were imported and their scripts adapted solely to output repository-relative paths. Historical earlier commits preserve the initial imported scripts.
