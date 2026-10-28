# Weil-Lab — NF360: Retype the original J242 infinite Schur correction before another residual campaign

**Date:** 2026-10-27 research sequence. **Custody:** read-only local algebraic audit; no new GitHub PR, no native Arb CI, no update to canonical obligations; `W-ODD-NEG=OPEN` and RH remains open.

**Original references:** SM34 positive-energy-dual original odd Schur, `notes/RPB108_SM34_POSITIVE_ENERGY_DUAL_SCHUR_20261018.md`; #350 242-source pruning; #355 original full exterior coupling and finite Schur probes. The proposed stronger exterior floor is retained only as locally reproduced NF356, not an accepted native CI result. The previous NF359 physical form-dual decomposition is mathematically correct but not the only route to the infinite coupling.

## 1. Reuse the positive-energy-dual splitting on the smaller *same* physical complement

Let `H=L²_odd([-11/10,11/10])`, `J=J242` and `F=J^⊥`, with physical projections `P`, `Q`. Preserve the original lower-semibounded closed form `w=a_* - k_-`, where `A_*` is the positive pole-corrected operator and `K_- >=0` is the full original bounded negative-frequency operator. Conditional on the inherited realization,

- `A_* >= kappa_* I` with `kappa_*=33621/10^9`,
- `QK_-Q <= eps Q`, where `eps` is the accepted #350 leakage upper,
- `QWQ >= mu Q`, with `mu` the *locally reproduced* sharpened threshold floor from NF356.

Define the DIFFERENT finite subspace `E_A=A_*^{-1}J`. It is not the original `J` and must not be inserted into #355's physical projection formulas. Since the finite-dimensional positive definite map `T=P A_*^{-1}|_J:J->J` is invertible, every `f` uniquely decomposes `e+v`, with `e=A_*^{-1} T^{-1}Pf` in `E_A` and `v` in `F`. The map is bounded, preserves the form domain, and the positive cross vanishes:

`a_*(e,v) = <A_*e,v> = 0`.

Therefore, for this decomposition only, `w(e,v)=-<K_-e,v>`. No positive-multiplier strong action is required for this identity.

The closed signed complement `D_F` has inverse bounded above by `mu^-1 I` in its form realization. From PSD `K_-` and the complete leakage cap, for every `e in E_A`:

`||QK_-e||² <= eps * <e,K_-e>`.

Thus, **including the entire infinite complement**,

`0 <= <QK_-e,D_F^-1 QK_-e> <= (eps/mu)*<e,K_-e>`.

The full Schur is `S_A[e] = a_*(e,e) - <e,K_-e> - <QK_-e,D_F^-1 QK_-e>` and hence satisfies

`S_A[e] >= a_*(e,e) - (1+eps/mu)<e,K_-e>`.

This is SM34's original analytic decomposition, **retargeted to the accepted fixed J242 physical complement**, and not a new proof of positivity.

## 2. Entire-infinite remainder factor and finite acceptance

From the *exact* previously retained rational values `eps` and `mu`:

- `eps ≈ 0.000016767873157142093`,
- `mu ≈ 0.009981124873103065` (local, subject to native replay and form realization),
- `eps/mu ≈ 0.001679958258244802`,
- `theta = mu/(mu+eps) ≈ 0.9983228592681779`.

A convenient strict rational sufficient comparison is `theta0 = 12479/12500 = 0.99832 < theta`.

Define the *actual* fixed 242-by-242 inverse-response forms on `h,k in J`:

`G(h,k)=<h,A_*^-1 k>`, `N(h,k)=<A_*^-1 h,K_- A_*^-1 k>`.

Then the single finite matrix condition `N <= theta0 G` **on all 242 combinations** implies strict positivity of the full odd signed form in the inherited closed realization. The entire infinite `F` correction has already been paid by the factor `eps/mu` in this *new* splitting. No four-probe L² strong residual bound or full square-multiplier action enters this sufficient condition.

This test has **not been computed**. In the pinned #355 archive, `original_BS_pruned_rank_bound.json` explicitly records `actual_inverse_computed=false` and `si29_full_J_L2_normalization.json` records `inverse_response_value_certified=false` and `full_J_Astar_energy_projection_computed=false`. The accepted #354 positive signed matrix is a **different** finite matrix, not the new inverse-response pair. It is much closer to `1` than the old SM34 `51/56`, but the known near-critical original modes indicate it must not be assumed feasible. Failure of this sufficient comparison would NOT demonstrate an original Weil negative mode. `E_A` is a new finite subspace derived from the original J242, not a claim that #355's physical four-probe matrices are already its G,N.

## 3. Negative control: retained physical-probe data cannot bound the unprobed remainder

Consider two exact rational 3-by-3 signed matrices, with blocks ordered selected/probed/unprobed:

`W_t=[[1,1/250,t],[1/250,1/100,0],[t,0,1/100]]`.

Take `K=diag(2,0,0)` and `A_*=W_t+K`. For `t=1/50` and for `t=1/8`, exact rational LDL verifies `A_* >= 33621/10^9 I`; `QKQ=0`, and `QWQ=(1/100)I` in both. The finite signed selected value `1`, tested probe coupling `1/250` and tested probe energy `1/100` are identical. The probed Schur correction is `1/625 = 0.0016` in both.

However the complete Schur equals

`S_full(t)=1 - 1/625 - 100*t²`.

At `t=1/50`, `S_full=599/625>0`; at `t=1/8`, `S_full=-5641/10000<0`.

Thus finite probes + scalar complement floor + complement negative leakage **cannot logically determine the complete signed Schur sign**. This is an abstract information-boundary counterexample, NOT a Weil-negative witness; it uses none of the actual multiplier's special structure. It rules out any attempt to promote NF358's nearly zero projected strong residual to a full upper bound without additional information.

## 4. Sharpness of the relative cost

Even the upper factor `eps/mu` is optimal if one uses ONLY PSD of `K_-`, its complement scalar compression cap, and the signed complement floor. A 2x2 rank-one example takes

`K=[[1,1/100],[1/100,1/10000]]`, `A_*=diag(2, 101/10000)`, `mu=1/100`, `eps=1/10000`.

`K>=0` (determinant zero), `w|_F=mu`, `a_*(e,v)=0`, and the full Schur penalty is exactly `1/100=(eps/mu)*<e,K e>`. Improving this factor requires more operator structure, not a rearrangement of these scalar inequalities.

## 5. Decision

**Do not:** infer upper D from #355's four-probe lower approximation; repeat four-probe precision, launch arbitrary-dimensional sources, equate `E_A` with `J242`, or treat the local strengthened floor as GitHub-accepted.

**Do next, if choosing this alternative:** feasibility-preflight a *small, coupled* original positive-resolvent/negative-response sample on `E_A=A_*^-1 J242`, asking whether the sufficient `theta0=0.99832` target is plausible in the known critical region before committing to an entire 242x242 solve. An alternative remains a genuine matched energy-dual remainder bound in #355's physical splitting, but it must pay all unprobed directions, not just the four tested probes.

**Separate pending acceptance:** native independent Arb/CI floor replay; original signed form/domain matching; finite 242 inverse-response comparison (unevaluated); even sector, whole Weil and RH (open).

**Reproducibility:** `nf360_energy_dual_242_preflight.py` reads exact local NF356 rationals, verifies the retained PR355 ZIP SHA256 and accepted rank, checks the new threshold with `fractions.Fraction`, and reproduces both abstract counterexamples with exact rational LDL. Output is `nf360_energy_dual_242_report.json`. No repository file changed.
