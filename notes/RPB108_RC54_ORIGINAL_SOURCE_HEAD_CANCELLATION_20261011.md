# RPB108 RC54 — original-source cancellation in actual head transport

2026-10-11 UTC. Parent RC53:
`4a2601c205dfab4f1a28ff972dba30ee34fd6d20`.
Only `research/rpb108-route-consolidation` is written.

## Result and scope

All eight individual actual native directions now have strictly
positive original-Weil diagonal enclosures. Exact interval PSD checks
also certify a four-dimensional subspace floor:

    Q(h)>=(1/200)||h||_D^2
    for h in span{actual native representatives r_0,r_1,r_6,r_7}.

On the previously certified two-dimensional span, the stronger result is

    Q(h)>=(1/17)||h||_D^2
    for h in span{r_6,r_7},

improving RC52–RC53's 1/21 floor. These statements use actual head and
canonical metric enclosures, including all couplings inside the named
subspaces. They are not inferred from diagonal positivity alone.

The full eight-feature head floor remains open. RC53's orthogonal
residual allowance below 3.238 M_8 is retained. A tested original-source
global lift gives a weaker allowance, so it does not replace RC53.
The full 1250-feature system and whole-aperture positivity remain open.
Independent reflected/affine/exponential replay passes. No RH/F4 or
Lean closure is claimed.

## Original physical source and exact Riesz identity

Let q_j be the original physical native Chebyshev feature polynomial,
R the actual canonical Riesz map, V the rounded 32-mode trial map,
and i the canonical-to-physical inclusion. The native Riesz identity is

    R=i^*q,
    <R_j,h>_D=<q_j,ih>_physical.

In particular, q and V are different physical polynomials. The
combined bounded physical remainder K is RC52's signed sum of the
archimedean, prime and pole actions. The original canonical source is

    R+sigma_total=i^*(q+K iR),
    sigma_total=i^*K iR.

Let Pi_8 be the canonical orthogonal projector onto ran(R). Since
Pi_8 R=R, the projected original and remainder sources are exactly equal:

    (I-Pi_8)(R+sigma_total)=(I-Pi_8)sigma_total.

This motivates adding q before the physical-to-canonical lift, while
leaving K acting on V in the nominal source calculation. No actual
Riesz representative is replaced by q or V.

## New feature-to-source covariance

RC52 supplies the complete nominal trial remainder source F_nom and
its self-Gram. Form the nominal original physical source

    F_original,nom=q+F_nom.

Compute all 32 ordered same-parity feature-to-remainder pairings
J_source,ij=<q_i,F_nom,j>_physical. Their symmetric contribution gives

    U_original,nom=P+U_remainder,nom+J_source+J_source^*,

where P is the exact physical native feature Gram. All opposite-parity
pairings vanish exactly. Each of the eight q_j is generated from the
native Chebyshev-to-Legendre conversion; replay checks it against the
direct Chebyshev recurrence.

Archimedean pairings integrate the polynomial and both logarithmic
parts of RC50's bounded nominal source. Replay uses parity reflection
to replace the log(1-y) contribution by a second log y contribution.
Prime pairings integrate the summed active translated source on every
one of RC48's fifteen support segments. Replay independently maps each
segment to [0,1] and uses affine polynomial moments.

The signed pole pairing is 2(-1)^i m_q,i m_V,j on matching parity,
where m_q,i=<q_i,exp(x/2)> and RC49 supplies m_V,j. Generation uses a
degree-100 exponential Taylor integral and pays its uniform tail by
the feature coefficient L1 bound. Replay instead uses the exact
polynomial exponential primitive Q'+(B/2)Q=p in t=x/B coordinates.
Both pole signs are retained.

Directed 220-digit intervals enclose the new pairings. Saved rational
endpoints have denominator 10^25. The original source Gram is rounded
to a Loewner envelope using the checked P>=I/8 and the 64h P allowance,
where h is its maximum entry halfwidth. RC52's nominal source error
delta<49/200000 remains paid.

## The global lift test and retained residual bound

Using RC53's actual physical source transfer envelope D_source gives

    (R+sigma_total)^*(R+sigma_total)
       <=rho[(1+t)U_original,nom,up+(1+1/t)D_source],
    rho=252/257.

Exact rational PSD bisection tests eight rational t values. The selected
value is 1/2; the resulting low-eight canonical allowance is
4.222652367196195... M_8, below 4.223 M_8. It also bounds the projected
residual, but is worse than RC53's 3.2375584720655657... M_8 envelope.
The latter is copied unchanged as the retained residual certificate.

Thus adding the identity source does not by itself improve the residual
allowance under the current global lift estimate. This is a limitation
of this tested bound, not a lower bound on the actual residual and not
an impossibility theorem for sharper source lifting.

## Exact cancellation in the original head transfer

The same original source gives a sharper actual head identity. Set
E=R-V, G_trial=V^*V in the canonical norm, and F_trial=q+K iV.
Writing the original head as Q_8=M_8+(iR)^*K iR, expand and use
R=i^*q to obtain the exact matrix identity

    Q_8=G_trial+(iV)^*K iV
          +(iE)^*F_trial+F_trial^*(iE)
          -E^*E+(iE)^*K iE.

Indeed, expanding M_8 and subtracting the two cross terms involving
q leaves G_trial-E^*E. This removes the larger K iV action from the
linear error terms and replaces it by the original source F_trial.
The negative canonical error Gram is retained with its correct sign.

Let n_j be an upward square root of U_original,nom,jj_upper, v_j an
upward square root of the physical trial Gram T_jj, and s_j=n_j+delta v_j.
RC47 supplies the physical Riesz error allowances e_j and canonical
ones c_j. RC52 supplies the physical parity norm bounds k_even,k_odd.
RC38 gives the canonical trial metric enclosure

    |G_trial-G_trial,nom|_ij<=E_metric sqrt(T_ii T_jj).

Using RC52's nominal trial remainder head H_nom, the transfer radius
apart from -E^*E is

    (E_metric+delta)sqrt(T_ii T_jj)
       +e_i s_j+e_j s_i+k_(i mod 2)e_i e_j.

For a diagonal, -E^*E lies in [-c_i^2,0]. For an off-diagonal it lies
in [-c_i c_j,c_i c_j]. Add these allowances to G_trial,nom+H_nom,
then intersect with RC52's original actual head enclosures. This pays
the metric, source approximation, physical transfer and canonical
quadratic error without double-counting an identity term.

## Actual diagonal enclosures

Display endpoints are rounded further outward from the saved rationals.

| Native feature | Actual original Weil diagonal |
|---:|---:|
| 0 | [0.026518, 0.048871] |
| 1 | [0.030096, 0.048221] |
| 2 | [0.017697, 0.033036] |
| 3 | [0.020801, 0.033938] |
| 4 | [0.020381, 0.034092] |
| 5 | [0.011884, 0.021509] |
| 6 | [0.049930, 0.065153] |
| 7 | [0.050614, 0.064432] |

All eight exact lower endpoints are positive. This certifies eight
individual directions, not positivity on their combined span.

## Four-dimensional and stronger two-dimensional floors

For S={0,1,6,7} and theta=1/200, enclose each entry of
Q_S-theta M_S using the actual head and RC47 metric intervals. Let C_S
be its interval center and R_S its halfwidth matrix. Define

    B_S=C_S-diag(row_sums(R_S)).

For arbitrary complex coefficients, the entry error is bounded by the
diagonal row-sum allowance. Thus Q_S-theta M_S>=B_S. The validator
checks B_S is PSD by exact rational elimination, proving the named
four-dimensional floor. RC39's positive canonical Gram bound ensures
the four representatives are independent. No numerical eigensolver
is used in this certificate.

For features 6 and 7, exact opposite-parity decoupling gives
Q_67=M_67=0. The validator checks Q_ii_lower>M_ii_upper/17 for both
diagonals, proving the stronger 1/17 floor on their two-feature span.

Other same-parity couplings remain unresolved. The named subspace
certificates do not imply the full eight-feature floor or the much
larger 1250-feature floor. The final projected-source gate is also
unmet; its tighter low-eight allowance remains RC53's.

## Reproduction and next obligations

Inputs, in order: RC39 native, RC43 prime, RC46 archimedean, RC47
transport, RC49 pole moments, RC52 complete source, RC53 projected
source, and RC38 metric. Hashes and shared dependencies are checked.

    python scripts/validate_rpb108_rc54_original_source_cancellation.py
    python scripts/validate_rpb108_rc54_original_source_cancellation.py --replay certificates/rpb108_rc54_original_source_cancellation.json

Replay verifies all new feature pairings, the original-source Gram,
the retained residual bound, the signed head cancellation, historical
intersections and both exact subspace floors. Next obligations include
finer actual Riesz-map control, weak coupled head directions, sharper
canonical source lifting and projection beyond eight features. RC44's
complement floor and RC45's full-head conditioning certificate are
preserved. This numerical work is separate from Lean formalization.
