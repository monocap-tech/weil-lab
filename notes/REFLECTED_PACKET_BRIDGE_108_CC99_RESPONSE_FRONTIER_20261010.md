# RPB108 — CC99: response method versus the current collective source bound

Parent: CC98, `d1bf34dcef2a0bdbf49517e2d14bd94aefbb18f4`.
Read-only source: DNE36, `b45a73dd626380d87940d72fcee22208c1ff182f`.
Definitions: `docs/TERMINOLOGY_RPB108_CC99_RESPONSE_FRONTIER.md`.

The source-response method is a strictly stronger sufficient collective positivity criterion when rebased to DNE's current original high floor 11/25. Its implemented complete-Gram version is not computationally cheaper by construction. The literal historical CC93 certificate, using floor 207/1000, does not dominate DNE's current bound; CC96 already established that those two historical choices are incomparable. The useful next comparison is the response method at the common floor 11/25.

## Same-floor dominance and strict separation

For the objects defined above, let D=Gamma/kappa-R*A^-1 R. Spectral calculus gives

    D = kappa^-1 R*(A-kappa I)A^-1 R >= 0.

Put T=A^(1/2)(A-kappa I)^(1/2)Y. Then T*T=kappa N and the finite projection onto range(T) lies between zero and the identity. Applying that projection to A^(-1/2)(A-kappa I)^(1/2)R gives

    D >= kappa^-2 W N^-1 W* >= 0.

Thus the true original Schur form is bounded below by SY, which is bounded below by S0. This is a collective matrix inequality, with every mixed term retained. The finite paid moments and their error ledger must justify N and W on the original domain; a floating-point or partially measured response does not suffice.

Strict separation has an exact one-dimensional admissible control: kappa=11/25, A=1, R=1, Q=3/2, Y=1. Then S0=-17/22, N=14/11, W=14/25, and the corrected lower bound SY=1/2 equals the true Schur value. This control can be embedded as a block in larger collective packets. It proves strictness in principle, not a rescue of DNE36's particular packet. If W vanishes on a failed trial, this paid family cannot rescue it. Correction rank is at most r; finite rank alone does not prove success or failure of a particular full packet.

## Actual frontier: the floor bound now fails

CC99 independently authenticates DNE36 custody, reconstructs all 800 replay projected-source entries and their physical error payments, and evaluates fresh rational outward congruences for the native controls and positive signed prefixes. It independently evaluates both full and first-prefix negative rational trials. Retained-rank proofs and the underlying analytic source construction are inherited from DNE36; original source integrations were not freshly rerun in CC.

| Quantity | Even | Odd |
|---|---:|---:|
| Complete source packet | 20 | 20 |
| Positive prefix plus all F112 | 18 | 17 |
| First failing prefix | 19 | 18 |
| First failing signed trial, approximate paid upper bound | -0.008645556418 | -0.01165563150 |
| Necessary response gain on that stored trial, approximate | >0.01964899186 | >0.02649007159 |

The exact rational thresholds and sign enclosures are recorded in `notes/data/RPB108_CC99_RESPONSE_FRONTIER_20261010.json`; decimal displays are diagnostic. These thresholds use the stored, unnormalized trial vectors. They are necessary scalar tests only: a complete corrected collective matrix must still be certified positive.

The independently checked enlarged span contains 35 retained directions and every original infinite high vector, with common physical guard 1e-38. Seventy-seven retained directions remain uncovered. The negative signed trials prove that the uniform-floor comparison cannot close the full frozen 56-column parity packets containing them. They do not prove negativity of the true original Schur form or an original null. Invertible coordinate changes cannot remove this obstruction.

## Cost and concrete missing inputs

Both implemented methods need the same complete Gamma: m(m+1)/2 unique source moments per parity. The response method additionally needs m r signed trial-to-high source crosses, m r native crosses, and the paid high moments defining N. CC96 already checked that the inherited eight-even/seven-odd paid high denominators remain positive at floor 11/25, so those self moments can be reused. They do not supply the crosses for the new DNE36 trial frame.

For the first failing packets, that existing family requires 19*8+18*7=278 additional mixed source entries and the same number of native entries. For both complete twenty-column packets, the count is 300 of each. These entries must be attached to the actual frozen DNE36 physical columns; CC93's old six-direction response data cannot be substituted. No such complete mixed block is supplied by the inspected DNE36 packet, so an actual response rescue is not yet proved.

With dense arithmetic, forming the response correction adds an r-by-r certified solve and O(m r^2+m^2 r) work to the same m-by-m positivity check. Selecting one failing witness can screen the paid high family with only r aggregated crosses per parity (15 total for the existing family), but a scalar screen is not a cheaper collective certificate. Entry counts do not establish wall-clock source integration costs; no timing benchmark is claimed.

A future implementation could certify a directional source bound on the residual after paid response projection, avoiding formation of the entire original Gamma. That would require a new certified residual-source ledger. CC93's implemented complete-Gram method and the current imported source data do not establish such a saving.

Decision: use a same-floor paid response test on the first failing DNE36 packets. Its potential strength is proved; its rescue of this frontier and any computational saving remain open. Whole 1.06 positivity, RH/F4/full transport and Lean remain open.

## Reproduction

Run `python scripts/certify_cc99_response_frontier.py notes/cc99-source --output notes/data/RPB108_CC99_RESPONSE_FRONTIER_20261010.json`.
This is an independent consumer of authenticated original-source interval data, not a fresh analytic integration or Lean proof.
