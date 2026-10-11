# RPB108 RC55 — weak head Schur blocks and correlated directional errors

2026-10-11 UTC. Parent RC54:
`c56af8d12b3b708e4c57685f66c077f978c4c3c9`.
Only `research/rpb108-route-consolidation` is written.

## Result and evidence boundary

RC54's actual four-feature floor reduces the remaining low-eight
target inequality Q_8>=M_8/4000 to two actual 2-by-2 Schur-complement
positivity obligations, one even and one odd. Their interval inverse
and Schur-entry enclosures are now certified.

Two concrete weak directions are attached to the original source
identity. Correlated actual-map transport narrows their quadratic
enclosures by factors 12.107577899... and 21.017437793..., compared
with summing the existing entry intervals. Both improved intervals
still contain zero. This pass does not prove either actual negativity
or the full head floor.

Exact rational controls show that the existing head entry intervals,
parity, strong-subspace floor and global native metric bounds admit
both an indefinite head and a head meeting the 1/4000 target. Thus
those enclosure facts alone cannot decide the full low-eight target.
The controls are not realizations of the original Weil operator or
of all its source correlations.

The actual four-feature 1/200 floor, stronger two-feature 1/17 floor,
all eight positive individual directions and RC53's residual allowance
below 3.238 M_8 are preserved. The full 1250-feature head, projected
source gate and whole-aperture positivity remain open. Generation and
independent inverse/witness/directional replay pass. No RH/F4 or Lean
closure follows.

## Exact Schur reduction

Define J=Q_8-theta M_8 with theta=1/4000. Use the strong native features
S={0,1,6,7}, already certified by RC54 to satisfy

    Q_S>=(1/200)M_S.

Then J_SS>=(1/200-1/4000)M_S>0. The exact original head target is
therefore equivalent to positivity of its weak Schur complement.
Parity splits this into two smaller obligations:

| Parity | Strong features | Weak features |
|---|---|---|
| Even | 0, 6 | 2, 4 |
| Odd | 1, 7 | 3, 5 |

For each block, write

    J_parity=[[A,B],[B^*,D]],
    Delta=D-B^*A^(-1)B.

The required low-eight target holds if and only if both actual Delta
blocks are PSD. This reduction uses the actual canonical metric and
original head. It does not replace them by nominal trial matrices.
It also does not discharge the separate full 1250-feature target.

## Interval inverse and Schur enclosures

Subtract theta times the actual metric entry enclosures from RC54's
actual head entry enclosures, with outward rational endpoints. For
each strong 2-by-2 interval block [[a,b],[b,d]], enclose

    determinant=ad-b^2,
    A^(-1)=(1/determinant)[[d,-b],[-b,a]].

The determinant lower endpoints are strictly positive. Interval
products and positive-denominator division enclose all inverse and
weak Schur entries. They retain every B^*A^(-1)B term and all signed
off-diagonal couplings. Opposite-parity entries are exactly zero.

Replay verifies exact inverses at every endpoint corner. Independently,
an LDL factorization of the rational control strong block uses pivot
d-b^2/a and reproduces its inverse. All PSD and inverse statements use exact
rational arithmetic, with no numerical eigensolver in the certificate.

## Positive and negative controls inside the entry enclosures

Let Q_c and M_c be the centers of the actual head and metric entry
intervals. M_c lies in its enclosure and satisfies the inherited global
native metric inequalities alpha P<=M_c<=rho P, where P is the exact
physical native feature Gram, alpha=8947777583/17179869184 and
rho=252/257.

The negative control is Q_minus=Q_c. Its diagonals are all positive,
and it satisfies the strong four-feature floor. Nevertheless, exact
rational vectors in both parity sectors have negative quadratics.
Those vectors are constructed from the center Schur blocks, rather
than inferred from floating eigenvalues.

For a center block Q_c=[[A_c,B_c],[B_c^*,D_c]], form
Delta_c=D_c-B_c^*A_c^(-1)B_c. Choose a rational weak vector w with
w^*Delta_c w<0 and set v_strong=-A_c^(-1)B_c w. Then

    v^*Q_c v=w^*Delta_c w<0 exactly.

The even center Schur block has a negative first diagonal, so w=(1,0)
suffices. The odd center Schur block has positive diagonals but negative
determinant; $w=(-\Delta_{c,12}/\Delta_{c,11},1)$ gives the negative quadratic.
The certificate emits both full eight-component rational witnesses.

The positive control is Q_plus=Q_c+P/500. Every entry still lies inside
RC54's enclosure, and an exact PSD check verifies

    Q_plus>=M_c/4000.

It also satisfies the strong four-feature floor. Thus the entry boxes
contain controls on both sides of the target, even after those existing
metric and strong-block constraints are imposed. This establishes
insufficiency of that enclosure information alone. It does not say
the actual head equals either control, and it does not show that the
controls satisfy the full correlated source-construction data.

## Correlated actual transport along the weak witnesses

The same rational vectors are probes of the actual original head.
Keep E=R-V, with R the actual canonical native Riesz map and V the
rounded 32-mode trial map. RC54's exact original-source identity gives

    Q_8=G_trial+H_trial
          +(iE)^*F_original,trial+F_original,trial^*(iE)
          -E^*E+(iE)^*K iE.

For each probe v, use the whole correlated Gram envelopes, not a sum
of column allowances:

    e=v^*B_phys v,
    c=v^*B_can v,
    u=v^*U_original,nom,up v,
    t_v=v^*T v.

RC47 supplies B_phys and B_can; RC54 supplies U_original,nom,up;
T is the physical trial Gram. If delta is RC52's source approximation
allowance, the linear error is bounded by

    L_v=2 sqrt(e)[sqrt(u)+delta sqrt(t_v)].

The metric and trial source errors are E_metric t_v and delta t_v.
The physical quadratic error is bounded by k_parity e, and the negative
canonical Gram contribution lies in [-c,0]. Nominal head entry rounding
is paid by the exact coefficient-weighted halfwidth sum. These produce
the saved actual quadratic intervals.

Replay checks the linear allowance using squared rational inequalities
and verifies the independent square-completion witness identity. The
vectors are unnormalized rational combinations; the display below
divides each quadratic by v^*P v, the physical native feature norm.
These are not canonical-metric Rayleigh quotients.

| Probe | Actual Q(v)/(v*P v), rounded outward | Width improvement |
|---|---:|---:|
| Even weak direction | [-0.000783514, 0.000798778] | >12.10x |
| Odd weak direction | [-0.000622371, 0.000621781] | >21.01x |

Both signs remain unresolved. A negative quadratic for Q_c is a
control-matrix witness, not a negative quadratic for the actual Q_8.

## What the measured error budget requires next

The following approximate quantities are normalized by each probe's
v^*P v. They describe allowances, not actual error magnitudes.

| Quantity | Even probe | Odd probe |
|---|---:|---:|
| Nominal trial quadratic | 0.0000110653 | 0.0000025464 |
| Canonical metric allowance | 0.0004301357 | 0.0003595295 |
| Archimedean approximation allowance | 0.0002150678 | 0.0001797648 |
| Physical Riesz/source linear allowance | 0.0000282098 | 0.0000098732 |
| Physical Riesz quadratic allowance | 0.0001142985 | 0.0000700668 |
| Negative canonical Riesz Gram allowance | 0.0000068672 | 0.0000056827 |

The metric and archimedean approximation terms dominate these nearly
null directions. Finer Riesz control alone would leave those larger
allowances in place. Conversely, removing those two terms alone would
still leave unresolved physical Riesz terms larger than the nominal
quadratics. A successful refinement needs both better metric/source
precision and sharper actual-map error, while retaining correlations
in the weak directions. The nominal centers must also be updated when
their defining approximations change.

The Schur blocks identify where those improvements enter the full-head
gate. The two probes diagnose concrete uncertainties; resolving their
signs alone would not establish PSD of both complete Schur blocks.
This pass does not enlarge the source map or projection beyond eight
features. RC44's complement floor and RC45's conditioning certificate
remain available unchanged.

## Reproduction

Inputs, in order: RC39 native, RC47 transport, RC43 prime, RC38 metric,
RC52 complete source, and RC54 original-source/head cancellation.
Hashes and shared dependencies are checked.

    python scripts/validate_rpb108_rc55_weak_head_schur.py
    python scripts/validate_rpb108_rc55_weak_head_schur.py --replay certificates/rpb108_rc55_weak_head_schur.json
