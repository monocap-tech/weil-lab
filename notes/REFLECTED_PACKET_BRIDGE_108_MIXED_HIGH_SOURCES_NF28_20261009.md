# RPB108 — NF28: original mixed high-source Gram and retained-background obstruction

2026-10-09 UTC. Aperture a=53/50. Phase Geometry continues NF27 at
`a446275d4ba9a6c71599c310c35e81d2e439de95`. Coupled CC69 was recovered
read-only at `43661c39489f33f7fb0ad45c1573ff12a0973eeb`. No integration
or paused branch is modified.

Read the additive [NF28 definitions](../docs/TERMINOLOGY_RPB108_MIXED_HIGH_SOURCES_NF28.md).

## Result

NF28 certifies the complete original mixed high-source Gram of NF26's
corrected critical trial v and NF27's exact retained response w, separately
in both parities. The signed physical source cross terms are now bounded
rigorously, with all arch/prime/pole crosses and endpoint logarithms.

The two-direction coarse collective matrix is rigorously indefinite in
both parities. The decisive obstruction already appears on w alone:

| Strict original source quantity | Even | Odd |
| --- | ---: | ---: |
| ||P_F Lw||² / Q(w,w) | **(0.69827, 0.69829)** | **(0.80553, 0.80554)** |
| Coarse high-floor budget | 0.207 | 0.207 |
| Signed mixed high covariance <P_F Lv,P_F Lw> | $(-4.355,-4.275)\times10^{-38}$ | $(7.3385,7.3392)\times10^{-34}$ |
| w diagonal of sufficient collective matrix | $(-1.11662,-1.11661)\times10^{-36}$ | $(-7.83220,-7.83218)\times10^{-33}$ |

The corresponding coarse correction loss is more than 3.37 times native
w energy even and more than 3.89 times native w energy odd. The original
native form on (v,w) is positive definite; the sufficient collective
matrix has a strictly negative determinant. NF26's v diagonal stays
strictly positive, and its original source-square enclosure is reproduced.

This rejects the **sufficient estimator**, not the original Schur sign.
No actual inverse response, negative Weil vector, contact, RH consequence
or nonimplication from all Weil identities is asserted.

## 1. The complete original object

Let E be the original E112 retained space and F=E-perp. NF26's fixed trial
v has retained component x, while NF27's exact rational w lies in E and
satisfies x*w=0. Define

\[
r_v=P_F L_a v,\qquad r_w=P_F L_a w,\qquad
\Gamma=\begin{pmatrix}\|r_v\|^2&\langle r_v,r_w\rangle\\
\langle r_v,r_w\rangle&\|r_w\|^2\end{pmatrix}.
\]

Both sources are reconstructed directly. v=p-y uses the frozen NF26 high
correction; w uses the exact published NF27 response coefficients. The
native two-direction energy Q2 is independently inherited from the
original signed native matrix and paid NF26 low-source coordinates.

With the unchanged original high floor C>=kappa I, kappa=207/1000,

\[
S_{x,w}=Q_2-R^*C^{-1}R\ \ge\ U_2=Q_2-\Gamma/\kappa,
\qquad R=(r_v,r_w).
\]

The producer encloses all four entries of Q2, Gamma and U2, and both
finite determinants. Native Q2 has strictly positive diagonal and
determinant. U2 has a positive v diagonal, a strictly negative w diagonal,
and a strictly negative determinant. Both sufficient matrix tests fail
rigorously after physical error payment.

The raw signed L2 covariance is not the signed inverse-weighted covariance
<r_v,C^-1 r_w>. Knowing its sign does not determine that of the weighted
quantity. NF28 does not replace the missing inverse metric by an equality.

## 2. Why completing the same unlifted background Gram cannot fix this test

w is an explicit vector in the full 55-dimensional retained complement W.
If all those retained columns remain unlifted, the full coarse collective
matrix has on w the same value

\[
Q(w,w)-\|P_F Lw\|^2/\kappa<0.
\]

It therefore cannot be positive definite, regardless of the other
uncomputed Gram entries. Changing the basis of the same fixed trial
space only applies congruence and cannot repair this negative sufficient
value. The positive native 112-dimensional restriction of NF27 and the
positive seed Schur restriction of NF26 both remain valid.

This is an original arithmetic witness against the current **coarse
assembly route with unlifted retained background**. It does not prove
that W plus F is negative, or that all possible high lifts or sharper
original response estimates fail. Obtaining the rest of that unchanged
Gram at greater precision is not enough to close this particular test.

## 3. Exact endpoint/cell moments and physical payments

The source construction retains NF22's exact endpoint logarithm,
removable-singularity polynomial, and regular-kernel N=320 construction.
It uses NF26's outward rational grid 10^-500 and constant enclosures.
The degree-40 pole exponentials and Rodrigues first moments retain paid
entire tails. All six prime powers 2,3,4,5,7,8 and both orientations are
integrated on the original thirteen cells.

Each projected source has a global polynomial, a polynomial times
log(a²-x²), and cellwise prime polynomials. Exact polynomial, global log,
global log-square and cell endpoint-log moments integrate every source
cross. Continuous endpoint limits are imposed algebraically. Prime
translated polynomials are cached once per orientation before cell
selection. No numerical quadrature or sampled endpoint error is used.

Let eta_unit=2a epsilon+8R40 with the unchanged NF26 rational bounds.
For v the full source replacement costs at most (1001/1000)eta_unit.
Its retained projection uses native P_E Lp minus approximate P_E Ly;
pay the tiny Ly error ||y||_upper eta_unit and all midpoint coordinate
radii. For w the full replacement costs ||w||_upper eta_unit, and its
retained coordinates are independently enclosed by the original native
matrix. The producer records physical errors eta_v,eta_w.

For each mixed Gram entry, the original-source enlargement is

\[
E_{ij}=\eta_i\|\widehat r_j\|_{upper}
 +\eta_j\|\widehat r_i\|_{upper}+\eta_i\eta_j.
\]

The approximant diagonal norms are bounded by exact rational square-root
arithmetic. These payments are applied before dividing by kappa or
computing any determinant. In Q(v,w), only the tiny Ly projection error
is new; its paid bound is ||y||_upper eta_unit ||w||_upper. Q(w,w) comes
directly from the authenticated native matrix.

## 4. Independent validation

The v source-square enclosures overlap NF26's paid original intervals.
Both joint high-source Grams have rigorously positive determinants,
consistent with physical covariance. The native two-direction forms are
positive definite. Exact rational comparisons verify Gamma_ww>kappa
Q_ww, U_ww<0 and det(U2)<0 for each parity, and every displayed strict
outward bracket.

A separate unsquared checker reconstructs the original source of w and
pairs it against e118 even/e117 odd. After paid source error both pairings
overlap the unchanged NF24 N720/K620 original signed projection archive.
This is an independently produced native oracle, not an identity derived
from the squared Gram. The source of w, its original high projection and
the mixed Gram all preserve the same signed arch/prime/pole conventions.

Input target, fixed high trial, NF26 certificate, NF27 response certificate
and decompressed E112 native archive hashes are authenticated. The
independent checker also authenticates the decompressed NF24 projection
archive. Published scripts, data and custody hashes retain the full
rational intervals, not the shortened displays.

## 5. Artifacts and reproducibility

- [Complete mixed high-source producer](../scripts/certify_native_mixed_high_sources_nf28_106.py).
- [Independent unsquared native projection checker](../scripts/check_native_mixed_projection_nf28_106.py).
- [Original complete mixed Gram and sufficient matrix certificate](data/RPB108_NF28_MIXED_HIGH_SOURCE_CERTIFICATE_20261009.json).
- [Native checks, strict brackets and custody](data/RPB108_NF28_MIXED_HIGH_SOURCE_VALIDATION_20261009.json).

```bash
python scripts/certify_native_mixed_high_sources_nf28_106.py \
  notes/data/RPB108_NF24_COMPENSATED_SOURCE_TARGETS_20261009.json \
  notes/data/RPB108_NF26_FIXED_HIGH_CORRECTIONS_20261009.json \
  notes/data/RPB108_NF26_HIGH_CORRECTION_CERTIFICATE_20261009.json \
  notes/data/RPB108_NF27_RETAINED_COUPLING_CERTIFICATE_20261009.json \
  INPUT_DIR/native112_N720_K620.json.gz --output certificate.json
python scripts/check_native_mixed_projection_nf28_106.py \
  notes/data/RPB108_NF24_COMPENSATED_SOURCE_TARGETS_20261009.json \
  notes/data/RPB108_NF27_RETAINED_COUPLING_CERTIFICATE_20261009.json \
  notes/data/RPB108_NF24_NATIVE_RESIDUAL_PROJECTIONS_117_118_20261009.json.gz.b64 \
  --output native_checks.json
```

## 6. NF29 frontier

The retained background needs its own high-response treatment. NF29
should test additional original high lifts on the retained response,
then pursue a collective lift on the remaining background, or establish
a sharper justified response bound for that background and its signed
mixed coupling. A successful lifted response probe would still leave
the full 55-direction background assembly to certify.

NF28 does not close the complete retained Schur matrix. Whole-domain
original positivity at 1.06 remains open; the highest certified
whole-domain aperture remains 1.05. RH, F4, cap-uniform leakage, actual
collective null exclusion and Lean closure are not claimed. Coupled CC69
remains read-only and its signed mixed-assembly question remains intact.
Paused branches and historical wording are unchanged.
