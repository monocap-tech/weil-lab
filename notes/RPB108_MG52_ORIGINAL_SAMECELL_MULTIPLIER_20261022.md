## MG52 independently verified: strict but small same-cell PSD upper improvement

[MG52 Actions #39813976498](https://github.com/monocap-tech/weil-lab/actions/runs/39813976498) **PASSED**, original 32-cell source multiplier cancellation and independent four-case exact rational 24D full-frequency PSD replays. Artifact `mg52-original-samecell-vector-multiplier-24D-PSD-gain` ID **12444906442**.

| Original case | MG50 Gersh | MG52 improved Gersh | PSD full-upper reduction trace | same MG43 witness-ray gain | selected valid method |
|---|---:|---:|---:|---:|---|
| 16/k12 | −24.1887384404 | −24.1886299849 | 0.002577290072 | 0.000425399653 | MG43 whole |
| 16/k16 | −24.8340174120 | −24.8339180584 | 0.002247307280 | 0.000394432295 | MG43 whole |
| 32/k12 | −23.9413516473 | −23.9409059127 | 0.009751036932 | 0.000878869968 | MG43 whole |
| 32/k16 | −24.7512065036 | −24.7508113164 | 0.008601657072 | 0.000784260253 | MG43 whole |

The same-cell source-vector cancellation is a rigorously valid tightening and the PSD difference survives exact outward-rational compaction, but its benefit is very small compared with the accepted complete-source deficits. **0 original source 24D contractions.**

**MG53 next:** audit an exact fixed-method **direct-measured-band zero ceiling** on MG43's rational witness for MG52. Since any valid original direct covariance upper must be PSD, if the *optimistic* source lower with the entire direct [4,8] upper set to ZERO remains exactly negative on a known rational witness, refining **only** that direct-band upper cannot establish full original source contraction with all other MG52 terms held fixed. Also test hypothetically deleting both measured bands to classify the remaining source deficit. Zero-band diagnostics are NEVER valid original residual uppers; this is a restricted method-family obstruction, not a negative original operator mode or a universal impossibility theorem.

---

# MG52 — Genuine original 24D same-cell source-vector multiplier cancellation

**Status: independently verified exact rational original-source PSD upper tightening with no source contraction.** Stacked on independently verified MG51 PR #300, MG50 #299.

## Verified motivation

MG50 independently added a genuine 32-cell original physical Fourier source measurement on [4,8], and reconstructed 864 original complete-frequency 24x24 residual upper matrices, yet its best complete bound worsened relative to MG48 and MG43. MG51 independently identified the largest positive charge on the accepted MG43 conservative-certificate witness rays as MG50's *direct [4,8] residual upper*, not the source-tail subtraction or Young parameter selection.

MG52 attempts a strictly stronger SAME source-cell physical inequality **without collecting new Fourier data or changing any response matrix**.

## New analytic same-cell cancellation

For an original positive frequency cell `I=[left,right]` of width `h`, midpoint `xi0`, and local coordinate `s=xi-xi0`, write the **original** transformed source as

```
t(xi) = v+s*d+e(xi),    |e_i(xi)| <= r_i,    |s|<=h/2
a(xi) = ac + delta_a(xi),  |delta_a(xi)|<= da
C(ac) = I-ac*B+2 e_p bmid^T B
```

Retain the rank-one original sinh pole coefficient uncertainty:
`|delta_b_i|<=brad_i`. The physical original residual is exactly

```
q(xi) = t(xi) C(ac) - delta_a(xi) t(xi) B
        + 2 t_p(xi) delta_b^T B.
```

MG32/MG50 bounded each residual channel j by the affine centered
`(v C(ac))_j+s(d C(ac))_j` plus a radius

```
Rold_j = sum_i |C_ij| r_i
       + da sum_i |B_ij| (|v_i|+(h/2)|d_i|+r_i)
       + 2 (|v_p|+(h/2)|d_p|+r_p) sum_i |B_ij| brad_i.
```

The multiplier uncertainty `delta_a(xi)` is a **single common
scalar** across all original source coordinates; it cannot independently
change sign per coordinate. Thus it is valid to sum the source vector
before taking the absolute:

```
Rnew_j = sum_i |C_ij| r_i
       + da (|sum_i B_ij v_i|+(h/2)|sum_i B_ij d_i|
             +sum_i |B_ij| r_i)
       + 2 (|v_p|+(h/2)|d_p|+r_p) sum_i |B_ij| brad_i.
```

By the triangle inequality, `0<=Rnew_j<=Rold_j`
for **every source channel on every real-frequency point in the cell**.
This retains true multiplier-source correlations and does not assert that
two independently extremized whole source moments are realized together.

Reuse MG50's SAME accepted rational physical 32 source cells and all
exact midpoint affine source vectors; retain the EXACT SAME original
MG50 per-cell positive Young tau. For the accepted outward-rounded
matrix-cell upper `2h[(1+tau)(vv^T+h² dd^T/12)
 +(1+1/tau)*diag(sum(R)*R)]`, monotonicity in nonnegative `R`
gives an exact **positive-semidefinite diagonal improvement**.
Reconstruct and verify the complete original 24D old/new compacted
matrix inequalities exactly; do not rely solely on nominal radii.

## Complete-frequency acceptance standard

Take the independently accepted MG50 **complete** original full
24x24 residual upper for each of four original mesh/cutoff cases,
subtract ONLY the exact PSD diagonal improvement on the new physical
[4,8] direct source upper, and leave the accepted original [0,4]
direct residual, all `|xi|>8` multiplier/moment and strong tail
bounds, original seven-prime/digamma multiplier, true sinh pole and
response `B` untouched. The result is itself a valid original
complete-frequency Loewner upper, now proved no larger than MG50's
winner. Compare exact rational Gersh sufficient margins and full
24D rational inertia against the independently accepted MG43
fallback. MG50's selected 864 candidate trial is not silently
reclassified without rebuilding each candidate; this is a
**four-case fixed-candidate proof-valid sharpening**, not a new
864-case full parameter search.

The separate independent verification regenerates original [4,8]
physical Fourier source cells with MG50's separately authored
independent algorithm, derives both radii in a different order,
checks frozen original taus, exact old MG50 new-source residual
matrix equality and every exact PSD matrix difference, and replays
full original 24D source-lower witness signs.

Any positive results concern the ORIGINAL SOURCE CERTIFICATE only.
Even a new positive 24D source lower does not settle original 470D
inverse, signed odd 51/56, independent original Fourier/form/domain,
even/Weil/CC27/RH. Those remain OPEN.
