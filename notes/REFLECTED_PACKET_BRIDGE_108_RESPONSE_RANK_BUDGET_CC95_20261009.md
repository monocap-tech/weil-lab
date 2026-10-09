# RPB108 — CC95: current response has a certified rank budget

2026-10-09 UTC. CC parent 779aec35c365e36fbc98b24499a3e6bbe4ec4855; Native Source read only at 6658ff2837838ab00b9b9c605fdd200d473c3293. Definitions precede use in [CC95 terminology](../docs/TERMINOLOGY_RPB108_RESPONSE_RANK_BUDGET_CC95.md).

CC94 recovered all 106 remaining retained coordinates. CC95 now quantifies the leverage of the already-paid high inverse-response construction on that full integration problem. It checks exact outward interval determinants of the signed packet response Dv, authenticates the current producer certificates, verifies the high inverse residual, and reconstructs the actual NF37 selected scalar-floor block from its native and complete-source Grams.

| Exact integration constraint | Even | Odd |
| --- | ---: | ---: |
| Existing paid high columns | 8 | 7 |
| Certified packet response rank | 3 | 3 |
| Additional response profile rank, at most | 5 | 4 |
| Full retained correction-kernel dimension, at least | 48 | 49 |
| Actual packet scalar-floor negative index | 1 | 1 |
| Full scalar-floor negative index repairable, at most | 8 | 7 |

The same three high-column indices (zero-based 1,2,3) give a nonzero response minor in each parity. Its determinant lies in (6.2861,6.4447)e-50 even and (-1.2294,-1.2291)e-44 odd. Thirty-five even and twenty odd minors independently exclude zero. This proves rank three, rather than inferring it from a floating-point singular-value calculation.

The selected scalar-floor packet has positive first principal entry and leading two-by-two determinant, but negative three-by-three determinant in both parities. Hence its exact inertia is (2,1,0). The response correction already repairs this one negative direction per parity; a full completion with too many further negative directions cannot be repaired by the same eight/seven columns.

At least 97 dimensions of the full retained family belong to the correction kernel. They are generally mixtures of packet and remaining coordinates. On those vectors the current correction vanishes exactly, so the full scalar-floor form itself must be positive. Completing the remaining source Gram and signed response rows will locate this kernel and allow its sign to be tested. The existing numerical packet pass alone cannot establish that condition.

This yields two useful rejection tests for a future common full certificate: a nonpositive scalar-floor vector annihilating D-star, or a scalar-floor negative index above eight/seven. Neither test has yet been triggered for the actual full Weil family. No claim that more high columns are required follows from the rank count alone.

Exact controls cover genuine negative/null/positive joint crossings at scales 1 and 1e-18, with both individual high-Schur diagonals and the finite native matrix positive throughout. The correction kernel is also positive throughout those crossings, demonstrating that its positivity is not sufficient. Further controls use a non-coordinate rank-one update with a preserved negative kernel vector and nine negative directions against a rank-eight correction.

Reproduction:

```sh
python3 scripts/certify_cc95_response_rank_budget.py notes/cc92-source notes/cc91-source notes/cc87-source --output notes/data/RPB108_CC95_RESPONSE_RANK_BUDGET_20261009.json
```

PASS. No new native integration or full remaining source computation is claimed. CC93's conditional six-direction-plus-all-F physical gap and CC94's finite 106-direction lifted gap remain standing. The high floor, original attachments, full retained Schur sign and transport remain open; whole aperture remains 21/20=1.05. Whole 53/50, RH, F4 and Lean remain open. Historical wording and other branches remain unchanged.
