# RC107 — original compression spectral census and coupled actions

Date: 2026-10-11. Aperture a=11/10. Branch: `research/rpb108-route-consolidation`.

## Result and completion boundary

The actual original Weil operator, compressed to the existing 22-dimensional canonical Riesz span, has exactly five eigenvalues per parity strictly below 1/100. Its remaining twelve compression spectral directions have a positive canonical floor of 1/100. These are exact rational enclosure results, not rounded eigenvalue acceptance. Moreover, the entire original 22-feature compression is positive: even floor 1e-18, odd floor 1e-16. Its five-candidate blocks remain positive after their six native strong directions and all internal couplings are eliminated.

The full original operator has at least ten eigenvalues below 1/100, and at most 1,250. The latter upper bound comes from the inherited complete-head complement floor, not from the 22-feature compression. No full-operator upper count of ten is proved. The positive compression floor is not a positive floor on the full orthogonal complement of those ten directions.

RC107 also certifies original-operator action residuals and coupled-response norm uppers for fixed rational candidates. These retain the original source and metric errors. The resulting individual norm allowances cannot close the direct ten-candidate Schur test. This is a failure of those enclosures, not a proof of large actual coupling or a negative Weil direction.

Thus the requested full spectral certificate is not complete. Spectral coverage of the omitted head, a positive floor on the resulting actual strong space, and positivity/correlation certification of the exceptional block after the omitted original space is eliminated remain open. The previously certified six-direction corrected positive span is retained.

## Operator and coordinates

Let A_Q=I+i*Ki be the bounded selfadjoint original canonical Weil operator. The canonical embedding is compact at this fixed aperture by RC77, so A_Q-I is compact and the essential spectrum is {1}. A spectral subspace below a fixed threshold less than 1 is finite-dimensional.

Let q_j be the existing 22 physical native targets and u_j=i*q_j their actual canonical Riesz vectors. The 64-degree physical trial vectors v_j approximate i u_j. In canonical notation write e_j=u_j-v_j. All trial pairings below use the actual canonical metric where required; G_0 denotes its certified nominal 64-by-64 center, with physical mass perturbation upper delta_G. No physical polynomial span is substituted for a canonical Riesz span.

A floating generalized eigensolve selected rational coordinate vectors for each parity. Each vector was scaled to maximum coefficient one and rounded to the fixed rational grid 1e-15. The selected coordinates are embedded in the validator. Floating eigenvalues are not inputs to acceptance. Positive actual metric lower bounds prove that each eleven-vector parity family spans its full native Riesz space.

## A sharper original head enclosure

The main improvement is to retain source-response alignment in the Riesz transport, rather than pay the product of a Riesz error and the norm of an entire physical source.

For a target coordinate combination, define the actual trial source

\[
f_j=q_j+K i v_j,\qquad s_j=i^*f_j.
\]

RC83 supplies a fixed 64-dimensional canonical response trial z_j; RC84 supplies signed physical residual covariance for the corresponding nominal source minus L_nom z_j. The actual operator corrections are then attached. In particular, the canonical response error obeys a certified diagonal bound

\[
\|s_j-z_j\|_c^2\le E_j^{\rm response}.
\]

In the validator this bound is formed from the contracted raw RC84 residual interval, the actual canonical operator correction applied to z_j, the actual source correction applied to v_j, and the embedding factor rho=252/257. The three physical residual contributions are summed before squaring; their independence is not assumed.

The original form satisfies

\[
\langle u_i,A_Qu_j\rangle_c
=\langle v_i,A_Qv_j\rangle_c
+\langle e_i,s_j\rangle_c+\langle s_i,e_j\rangle_c
-\langle e_i,e_j\rangle_c
+\langle i e_i,K i e_j\rangle_2.
\]

This identity follows by expanding u=v+e and using i*q_j=u_j. In particular, the canonical error Gram has a minus sign after the full source is used in the linear terms.

For the linear source pairing, use

\[
\langle e_i,s_j\rangle_c
=\langle e_i,z_j\rangle_c
+\langle e_i,s_j-z_j\rangle_c.
\]

Its first term has an exactly computable nominal center

\[
\langle q_i,i z_j\rangle_2-\langle v_i,z_j\rangle_{G_0},
\]

with actual metric allowance delta_G times the physical norms of v_i and z_j. Its remaining term is bounded by the product of the canonical Riesz error norm and the canonical source-response residual norm. This uses the actual correlated response z_j instead of the norm of s_j.

The remaining original trial-form error, signed canonical error term, and bounded physical K quadratic term are paid separately. Diagonal Riesz error bounds contract the raw RC81 signed intervals directly; a broad eleven-vector Loewner upper is not substituted for those diagonal contractions. All 66 signed same-parity head entries are enclosed for each parity. Symmetric row-sum interval allowances yield Q_lo <= Q_actual <= Q_hi.

This response alignment is what made the exact five-per-parity census pass. The earlier generic linear source norm allowance did not certify that count.

## Actual canonical metric enclosures

Let J contain the exact target/trial pairings, G_T the nominal trial canonical Gram, and T the physical trial Gram. Expansion of the canonical Riesz error gives

\[
M_{\rm actual}=J+J^*-G_{T,\rm actual}+\mathrm{Gram}_c(e).
\]

The actual error Gram is positive and has a certified upper E_c. Thus

\[
M_{\rm lo}=J+J^*-G_T-\delta_GT,
\qquad
M_{\rm hi}=M_{\rm lo}+2\delta_GT+E_c.
\]

Both metric endpoints are in the same fixed candidate coordinates as the head endpoints. Exact strict positivity of M_lo proves independence. For every positive threshold t,

\[
Q_{\rm lo}-tM_{\rm hi}
\preceq Q_{\rm actual}-tM_{\rm actual}
\preceq Q_{\rm hi}-tM_{\rm lo}.
\]

Negative inertia of the left endpoint is an upper count of compression eigenvalues below t; negative inertia of the right endpoint is a lower count. Matching counts give an exact compression count. No squaring or inversion of an unproved actual metric is used.

## Certified compression census

Each parity compression has dimension eleven. Intervals below are certified counts of eigenvalues strictly below the threshold; a single number means the count is exact.

| Canonical threshold | Even compression count | Odd compression count |
|---|---:|---:|
| 1/1000 | 4–5 | 4–5 |
| 1/100 | 5 | 5 |
| 1/10 | 6 | 5 |
| 1/2 | 6–7 | 6 |
| 1 | 7–9 | 8–9 |
| 3/2 | 10 | 10 |
| 2 | 11 | 11 |

At 1/100 both enclosure pencils are nonsingular with matching inertia. There is no compression eigenvalue at that threshold; the upper twelve compression spectral modes therefore have a strictly positive floor of at least 1/100. The exact low spectral subspace of this compression exists and has dimension ten, but its eigenvectors have not been equated with the ten fixed rational candidates.

Minmax transfers the lower counts to the full operator. It does not transfer the compression upper counts. Consequently there are at least ten full-operator eigenvalues below 1/100. On the other hand, the complete 1,250-feature complement has original floor alpha=247/2500>1/100. If a full low spectral space had dimension greater than 1,250, it would intersect that complement nontrivially, contradicting its Rayleigh lower. This proves the full low count upper 1,250.

The twelve strong compression spectral vectors need not be invariant under A_Q. Their couplings to omitted directions prevent using their compression floor as a full-space floor.

## Positivity of the complete native compression and its exceptional block

The unweighted interval lower is suitable for the broad census but discards weak/strong scale information near zero. A second rigorous interval lower retains it. Choose positive rational scales

\[
d_i=1/\sqrt{|Q_{{\rm center},ii}|},
\]

using a rational upper square root at grid 1e-40. Put

\[
r_i=\sum_j\mathrm{radius}_{ij}d_j/d_i,
\qquad L=Q_{\rm center}-\mathrm{diag}(r_i).
\]

For any symmetric entry error E inside the certified radii, congruence by diag(d_i) proves diag(r_i)+E is positive semidefinite: its diagonal dominates the absolute off-diagonal row sum after congruence. Hence L is an actual original-head Loewner lower. An additional outward lower rounding at grid 1e-60 keeps the stored matrix compact.

Exact positivity and actual metric upper comparisons prove

| Original native parity compression | Canonical positive floor |
|---|---:|
| Even eleven-space | 1e-18 |
| Odd eleven-space | 1e-16 |

This is a new full 22-direction original compression positivity certificate. It does not eliminate the remaining original operator. The globally corrected six-direction certificate is a different, previously proved result.

Partition each stored L into the first five fixed candidates W and the last six fixed candidates T. Its exact Schur lower is

\[
L_{WW}-L_{WT}L_{TT}^{-1}L_{TW}.
\]

The inverse is checked by exact multiplication. The Schur matrix is strictly positive, with canonical weak-coordinate margin at least 1e-18 even and 1e-16 odd. Loewner monotonicity of Schur complements follows by minimizing the quadratic form over the T coordinates, so it transfers this lower to the actual original native compression. This certifies the exceptional candidate block with all its native coupled entries, without reducing the couplings to individual norm uppers. It is not the Schur complement over the infinite remainder or the full 1,250-feature head.

## Explicit canonical floor inside the native space

There is also a floor on an explicitly specified orthogonal complement, without replacing its unknown actual projection by a numerical projection. In each parity let W be the span of the first five fixed rational candidates, and let T be the span of the last six. The full native space is their direct sum. Exact metric lower checks give M_W >= I and M_T >= (1/5)I in these candidate coordinates.

For the actual mixed metric entries, the identity above gives

\[
|M_{ij}|\le |(J+J^*-G_T)_{ij}|
+\delta_G\sqrt{T_{ii}T_{jj}}+\sqrt{E_{c,i}E_{c,j}},
\]

where the E_c,i are the separately contracted canonical error diagonal uppers. Squaring and summing over the five-by-six mixed block gives a Frobenius upper u. Consequently the actual canonical projection P_W obeys

\[
\|P_Ww\|_c\le\delta\|w\|_c,\qquad
\delta=\sqrt{5u},\quad w\in T.
\]

This follows from the exact projection Gram M_TW M_W^(-1) M_WT, inverse order M_W^(-1)<=I, the Frobenius norm bound, and the metric lower on T. The certified delta uppers are approximately 0.000198785 even and 0.000150324 odd.

Direct exact head/metric checks give original floors 3/200 on the fixed even high span T and 1/10 on the odd high span. With kappa the inherited physical K norm, the full canonical operator norm is at most N_A=1+rho kappa. For z=w-P_Ww,

\[
Q(z)\ge[\beta_T-N_A(2\delta+\delta^2)]\|w\|_c^2.
\]

The bracket is positive and ||z||<=||w||. The projection map from T onto the actual native space intersected with W perpendicular is onto. Outward rounding therefore certifies the floors

| Actual canonical subspace | Original floor |
|---|---:|
| Even native eleven-space intersected with five-candidate span perpendicular | 0.008596 |
| Odd native eleven-space intersected with five-candidate span perpendicular | 0.096454 |

These are original-form lower bounds on six explicit remaining native directions per parity. They control canonical orthogonality rigorously. They still do not control directions outside the native 22-space.

## Original coupled-action enclosures

For each fixed rational candidate u_j choose a rational Ritz center theta_j by rounding the ratio of its head and metric centers upward on the grid 1e-25. Then

\[
(A_Q-\theta_j)u_j
=(z_j-\theta_j v_j)+(s_j-z_j)
+i^*K i e_j-\theta_j e_j.
\]

The first term is evaluated through G_0 plus its actual mass allowance. The other three terms use the certified response error, physical Riesz error and K norm, and canonical Riesz error. Triangle bounds give a rational upper d_j for the actual canonical norm of this residual.

Using the actual metric diagonal lower gives

\[
\mathrm{dist}(\theta_j,\sigma(A_Q))
\le d_j/\sqrt{M_{{\rm lo},jj}}.
\]

This is a full-operator spectral inclusion, not a compression eigenvalue claim. It follows from the spectral theorem: if all spectral values were farther away, the norm of (A_Q-theta_j)u_j would exceed that distance times the norm of u_j. Whenever the enclosing interval is below 1, the included spectral point is a discrete eigenvalue. Overlapping inclusion intervals do not certify distinct eigenvalues; the independent minmax census provides the ten-mode lower count.

Rounded spectral-distance uppers for the first five candidate columns are:

| Candidate index | Even | Odd |
|---|---:|---:|
| 0 | 1.070e-8 | 4.849e-8 |
| 1 | 1.006e-6 | 4.723e-6 |
| 2 | 5.398e-5 | 6.812e-4 |
| 3 | 7.206e-3 | 2.190e-2 |
| 4 | 8.417e-2 | 5.209e-2 |

The candidate vectors belong to the native Riesz span N. Thus P_(N perpendicular) A_Q u_j=P_(N perpendicular)(A_Q-theta_j)u_j has norm at most d_j. The same inequality applies to projection onto the canonical orthogonal complement of the five-candidate span in that parity. For five columns, Cauchy–Schwarz gives the common response Gram upper 5 diag(d_j^2), recorded in the certificate. This is a valid original coupled-response enclosure, not an evaluation of its exact Gram. It is not the complement-eliminated F response from RC103.

## Precise failure of the present norm-budget closure

The census proves at least six full even eigenvalues below 1/10, and at least six full odd eigenvalues below 1/2. By dimension intersection, the original strong floor outside *any* five-dimensional parity exception can be at most 1/10 even, 1/2 odd. This restriction does not require numerically projecting the exception.

For the ten fixed candidates, let Q_jj^up be the separately certified actual head diagonal upper. Even the individual allowance d_j^2 exceeds beta_max Q_jj^up for every first-five column. The ratios at these maximum permitted floors are approximately:

| Candidate index | Even ratio, beta_max=1/10 | Odd ratio, beta_max=1/2 |
|---|---:|---:|
| 0 | 52.37 | 4.81 |
| 1 | 38.57 | 5.83 |
| 2 | 20.02 | 3.84 |
| 3 | 20.73 | 5.27 |
| 4 | 41.10 | 4.03 |

A direct Schur certificate using these individual norm allowances (or the larger common diagonal Gram upper) cannot pass, even with the optimistic actual-head upper in place of a positive lower. Actual coupling could be much smaller. Signed projection capture, fused effective responses, an enriched exceptional span, or a new structural estimate may change the outcome. This rejection does not certify that the candidates or original operator are nonpositive.

## Replay, publication, and remaining obligations

The validator checks eleven input hashes, exact original metric and source attachments, rational coordinate independence, signed head intervals, and seven inertia thresholds per parity. Independent replay reverses the signed contractions and replaces LDL pivot signs by ratios of leading principal determinants computed with fraction-free Bareiss elimination. Both runs agree exactly; replay reports PASS.

Repository reproduction:

```sh
python scripts/validate_rpb108_rc107_original_compression_spectral_census.py > /tmp/rc107.json
python scripts/validate_rpb108_rc107_original_compression_spectral_census.py --replay /tmp/rc107.json
```

Published artifacts are the validator, `certificates/rpb108_rc107_original_compression_spectral_census.json`, and this note. No new source integrals are evaluated; existing rigorous arithmetic intervals are newly contracted and combined.

What remains is to prove spectral coverage beyond the observed compression, establish a floor on the actual resulting strong space, and certify positivity of all remaining exceptional directions with their correlations. Six corrected directions are positive; the original nonpositive spectral dimension upper remains 1,244. Ten low modes are not ten nonpositive modes. The native candidate block and its native Schur complement are positive. The exceptional block corrected for the omitted original space is not proved positive, and neither whole-aperture positivity at 1.10, RH nor Global/F4 is closed.
