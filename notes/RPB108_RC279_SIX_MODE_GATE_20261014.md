# RPB108 — RC279: six-mode response enclosures and an enlarged positive block

Parent RC278: `0c17460bcf360d02c9007d6b387733c30676adbe`.
Branch: `research/rpb108-route-consolidation`. Aperture B=11/10.

RC279 resolves the original polynomial output profiles P0 through P5 through
degree 2048, pays every higher output degree, and certifies coupled inverse
response enclosures for the three lowest auxiliary modes of each parity.
The actual even gate restricted to **P0,P4** is jointly positive. Together with
the certified odd **P1** direction this enlarges the positive auxiliary block
from dimension 2 to **3**, leaving a **368-dimensional** exact Schur problem
in the unchanged rank-371 reference.

The full six-mode block is **not certified positive**. Its upper enclosures
have positive inertia, while the available lower enclosures are indefinite;
this does not prove an actual negative direction. The new block-to-remaining
cross columns still need payment. Stage I, RH, F4 and Lean remain open.

| Selected actual auxiliary block | Even | Odd |
|---|---:|---:|
| Tested degrees | 0,2,4 | 1,3,5 |
| Jointly certified positive degrees | 0,4 | 1 |
| Native coefficient Euclidean floor lower, approximately | 0.0000309852892727 | 0.00586765699482 |
| Selected covariance Young parameter | 21/25 | 32/25 |
| Remaining same-parity coordinates | 140 | 228 |

These floors refer to the listed native coordinate blocks. They are not global
canonical floors or normalized eigenvalues of the original Weil operator.
The original nonpositive index upper bound 301, the upper bound 371 at 0.01,
and the inherited lower bound 10 below 0.01 are preserved. The three positive
auxiliary directions are not subtracted from those independent index bounds.

## Resolve six complete polynomial actions

The reference is RC278's G=G0+C_b P_b. Its full diagonal lower form is

\[
 G\succeq W:=D_{P_b}+(D-C_b)_{Q_b}\succeq\mu_b D>0.
\]

The projector ranks are 142 even and 229 odd, with first omitted degrees
284 and 459. Let N=D^-1 G, the D-energy Riesz reference.

For each input P_d, d=0,...,5, retain the pinned original finite action center
in full: length 129 for P0 and P1, length 65 for the other four profiles.
Recompute the complete seven-prime model using the pinned RC273 boundary-jump
projection method. The actual prime shifts and coefficients are enclosed using
RC43; their complete model faults remain paid. Generate every matching-parity
prime output coefficient through degree 2048 by the exact boundary identity
and interval Legendre recurrences. The helper also checks two high coefficients
against direct rational integration of the piecewise polynomial model.

Above the retained original center, combine these prime coefficients with the
exact endpoint contribution. The old regular omitted-output norm is paid as a
global fault rather than silently discarded. Pole Taylor faults, regular
kernel faults, old retained-center rounding, old prime arithmetic faults, the
new prime model fault and new coefficient rounding are all retained.

For every degree above 2048, combine the signed endpoint tail from RC252 and
the remaining prime physical tail converted to D energy. Orthogonal capture
is subtracted only from the same prime model's full output energy. The JSON
contains all finite centers, complete global fault norms and tail certificates.
Opposite-parity coefficients are exactly zero by reflection.

The standalone model tail bounds are approximately 4.4915e-5 in even parity
and 4.9070e-5 in odd parity, in D energy. Global fault norms are at most about
6.263e-8. These are action-model costs, not inverse responses or original
negative eigenvalues. In particular, the tail after 2048 is not asserted zero.

## Four trial directions for three simultaneous sources

For each parity let Z0 denote the exact rescaled source trial from RC278, with
e0=D^-1 P_base-N Z0. Use the trial basis

\[
 [Z_0,P_{base},P_{base+2},P_{base+4}].
\]

This spans the same four-dimensional trial space as RC272, since Z0 has a
nonzero coefficient of the fourth residual polynomial. Reconstruct its actual
form Gram intervals by an exact basis change from the pinned original
four-trial intervals and the new exact diagonal augmentation.

For the three physical sources u_j=P_(base+2j), choose a rational trial column
by solving the midpoint trial system and rounding its coefficients downward.
This proposal does not itself certify an inverse. For trial coefficients
(a_j,b_0j,b_1j,b_2j), the actual residual is exactly

\[
 e_j=a_je_0+D^{-1}(u_j-a_jP_{base})
       -\sum_{k=0}^2 b_{kj}N P_{base+2k}.
\]

Reconstruct the finite model of e0 through 2048 from RC278's low residual
centers and the rescaled RC274 high physical numerator intervals. Its source
rounding, high interval radii, global action fault and infinite tail all remain
paid. The six newly resolved polynomial profiles supply the other action
terms. The low D-inverse source uncertainty is separately enclosed for each
new source combination.

## Full matrix residual covariance

The exact response identity for simultaneous trials Z is

\[
 T=U^*Z+Z^*U-Z^*GZ+E^*D N^{-1}E.
\]

The correction is added and is positive semidefinite. The middle terms give
an interval enclosure for the complete 3-by-3 variational center, including
off-diagonal response entries. A symmetric row-radius enclosure converts
entry intervals to a Loewner interval.

Inverse order G>=W bounds the full residual Gram by the W-inverse Gram. On
degree n the finite model uses weight

\[
 \frac{mass_n(H_n+s_{upper})}{w_n},\qquad
 w_n=1\ (n\text{ retained}),\quad
 w_n=1-\frac{C_b}{H_n+s_{lower}}\ (n\text{ omitted}).
\]

All finite residual columns remain combined in this weighted Gram. Every
signed cross product is enclosed outward before summation. Its interval
row radius yields the stored matrix S, a Loewner upper bound for the full
finite-model covariance. No entrywise squaring assumption is made.

Let eps_k bound the W-inverse norm of each of the four reused action error
vectors: e0's error and the three polynomial action errors. These bounds
include all omitted outputs and all global faults. Let r_j be the weighted
source-rounding energy for source column j, and Y the 4-by-3 trial coefficient
matrix. Cauchy-Schwarz for five contributions gives the joint noise envelope

\[
 V=5\sum_{k=0}^3\varepsilon_k^2Y_k^*Y_k
               +15\operatorname{diag}(r_j).
\]

The factors allow every correlation within an action error vector and every
correlation between source-rounding columns. For each tested theta>0,

\[
 \boxed{E^*D N^{-1}E\preceq(1+\theta)S+(1+1/\theta)V.}
\]

Subtracting this full matrix from Mass-C_b times the variational center gives
a lower bound for the actual native gate. The upper gate follows by dropping
the added positive residual correction. Every tested theta is rational;
theta runs from 1/100 through 2. The certificate selects a positive joint
subblock containing the old base source, maximizing dimension among the
tested subsets and then its certified native floor. There is no claim of an
optimal subset or parameter for the actual operator.

## What passed and what remains undecided

The two-dimensional even restriction on P0,P4 has an exact positive definite
lower matrix. Its floor is certified by reciprocal inverse trace, followed by
an exact positive-semidefinite check after subtracting the floor times the
identity. The odd P1 restriction is positive by the same test. Opposite parity
couplings vanish, so these combine into one three-dimensional positive block.

The tested full three-mode gates do not pass this covariance enclosure. Both
stored upper enclosures have inertia (3 positive, 0 negative, 0 zero), while
the stored lower enclosures are indefinite. Thus the enclosure leaves the
full six-mode question open and proves no actual negative direction. Separate
positive diagonal bounds are not counted as a positive coupled block.

The remaining 368-coordinate Schur form is defined using the actual inverse
of the certified positive block. RC278's two-column cross bound cannot be
transferred to this enlarged block; new block-to-remaining couplings must be
paid before claiming a lower bound for the new Schur form.

The finite residual matrices and remaining tails also identify a concrete
refinement: the noise covariance still treats omitted outputs of several
nearly cancelling trial directions separately. Combining their prime boundary
jump profiles before taking the tail norm could preserve those cancellations.
Higher cutoffs or better inverse actions are alternatives. None is asserted
completed here.

## Validation

The validator checks 272 inherited Git blob pins. Normal generation and reverse
replay recompute all six high-output profiles and compare the complete rational
certificate. The reverse replay uses the inherited higher interval precision,
reversed finite sums and independent output checks. Exact controls verify
correlated covariance payment, rejection of an unsupported diagonal-only
covariance bound, and the full matrix Young inequality at three parameters.

```bash
python scripts/validate_rpb108_rc279_six_mode_gate.py --output certificates/rpb108_rc279_six_mode_gate.json
python scripts/validate_rpb108_rc279_six_mode_gate.py --output certificates/rpb108_rc279_six_mode_gate.json --replay
```

The rank-371, rank-608 and rank-639 reference certificates and the eight-source
canonical inverse width 485647/1000000 remain preserved. RC280 should pay the
enlarged-block cross columns or sharpen the unresolved coupled response bounds,
especially the omitted-output covariance. Full original positivity remains
the acceptance gate.
