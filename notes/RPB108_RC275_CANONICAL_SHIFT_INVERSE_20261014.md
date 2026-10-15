# RPB108 — RC275: both projection auxiliary-source gates pass

Parent RC274: `1ea489864b2ba62f5f94c521b8f55c79128e5683`.
Branch: `research/rpb108-route-consolidation`. Aperture B=11/10.

RC275 certifies a positive two-source auxiliary gate on span{P0,P1} for RC271's
rank-608 physical projection reference. The new even native gate lower bound is
greater than 0.00195752211396, and the odd bound is greater than 0.00301577254092.
Opposite-parity pairing vanishes exactly. The complete rank-608 gate is still
unevaluated; after the two positive pivots its exact remaining Schur problem has
dimension 606, with all same-parity cross terms still required.

This is a new positive auxiliary pair, not Stage I closure or a positive spectral
floor for the original Weil operator. The legacy rank-639 reference and its own
two positive signed pivots are preserved separately. The independent original
nonpositive-dimension ceiling remains 582; the new pair is not subtracted from it.

| Actual response quantity, approximately | Even P0 | Odd P1 |
|---|---:|---:|
| Added inverse correction at RC274 | 0.000267340430606 | 0.000138910903095 |
| Added inverse correction at RC275 | 0.0000948953151583 | 0.0000490245027323 |
| Actual inverse response upper | 0.106070844280 | 0.0336952583882 |
| Native auxiliary gate lower | **0.00195752211397** | **0.00301577254093** |
| Native auxiliary gate upper, preserved | 0.00392398083404 | 0.00407833914453 |

Exact outward fractions in the certificate determine acceptance. The augmentation,
sources, four-trial coefficients, variational centers, complete original-output
model and global fault budgets are unchanged. No new original or augmented action
is executed. The improvement comes from retaining more of the exact canonical
form identity in the inverse lower bound.

## A stronger canonical lower form

On the common canonical/D-energy form domain, RC231 gives

\[
 L=D+h-rI_2+\mathcal R,\qquad r=789/125,
 \quad h(x)=-\tfrac12\log(1-(x/B)^2),
\]

where

\[
 \mathcal R=\chi\mathcal F^{-1}
       \log(1+e/|\xi|)\mathcal F\chi.
\]

The endpoint multiplication form is nonnegative by RC121. On the smooth supported
core the remainder form is the integral of the nonnegative multiplier
log(1+e/|xi|) times the squared Fourier modulus. Its bounded supported-input
extension is therefore nonnegative by continuity. This does not assert that the
singular multiplier is bounded on unrestricted ambient Fourier L2.

Consequently, as a full-domain form inequality,

\[
 \boxed{L\succeq D-rI_2.}
\]

The right side can be negative in low degrees. It is not inverted globally by
itself, nor treated as a positive canonical norm. Its use is inside a lower bound
that also retains the physical projection term.

## Keep the canonical shift in the projection reference

For the unchanged reference and any accepted Young parameter theta, RC272 gives

\[
 G_P\succeq\alpha L+\kappa P,
 \quad\alpha=\gamma-p(1+\theta^{-1})\delta^2>0,
 \quad\kappa=\lambda-p(1+\theta)>0.
\]

Instead of replacing L by the coarser global comparison aD, retain its shift:

\[
 G_P\succeq\alpha D-r\alpha I_2+\kappa P,
 \qquad
 N_P\succeq\alpha I_D-r\alpha D^{-1}+\kappa D^{-1}P.
\]

For all accepted candidates the validator checks kappa>r*alpha. On retained
degrees the safe diagonal lower endpoint is therefore
alpha+(kappa-r*alpha)/(H_n+s_hi)>0. On omitted degrees it is
alpha*(1-r/(H_n+s_lo)). The first omitted matching degrees are 472 even and 745
odd. Their D weights exceed r, so the entire omitted part is positive. The
retained projection controls the low degrees where D-rI alone was inadequate.

The original-form estimate from RC274 also remains available:

\[
 N_P\succeq I_D-C D^{-1}+\lambda D^{-1}P.
\]

For a single global convex weight t, combine these two lower forms before taking
an inverse. With positive retained coefficient, the safe endpoints are

\[
 b_n=(1-t)\alpha+t+
 \frac{(1-t)(\kappa-r\alpha)+t(\lambda-C)}{H_n+s_{hi}}
 \quad(n\text{ retained}),
\]

\[
 b_n=(1-t)\alpha+t-
 \frac{(1-t)r\alpha+tC}{H_n+s_{lo}}
 \quad(n\text{ omitted}).
\]

Let b_Y=alpha*(1-r/(H_n0+s_lo))>0 and b_O=1-C/(H_n0+s_lo)<0 at the first omitted
degree n0. The safe mixing limit is b_Y/(b_Y-b_O). Fractions j/20, j=0,...,18, of
a downward-rounded limit are checked. The resulting global lower floor is
(1-t)b_Y+t*b_O>0. Retained diagonals have a larger lower bound, and the omitted
diagonals increase with degree. The infinite residual model tail uses the lower
endpoint at its first degree after 2048.

This is a global form argument. Neither an entrywise maximum of lower forms nor
commutation with the actual inverse is assumed. Inverse operator order gives the
diagonal majorant used to pay the same complete residual as RC274.

## Exact residual payment and positive pair

The resolved model energy V, source-diagonal uncertainty R_s and remaining global
D-fault norm epsilon retain their previous meanings. The new correction is

\[
 C_{inv}=\left[\sqrt V+\sqrt{R_s}
      +\sqrt{\epsilon^2/b_{global}}\right]^2.
\]

All output through degree 2048 and the infinite model tail remain paid. The
correction is added to the inverse variational center, and the native gate is
mass(b)-lambda*T_b. The exact accepted candidates use theta=0.66 and t approximately
0.03789568244 even, and theta=0.47 and t approximately 0.03544875581 odd. They are
selected from a finite rational proposal set; no optimality claim is made.

The actual original operator, both parity projection references, their inverses
and the source maps commute with reflection. Therefore the cross pairing between
these opposite-parity auxiliary sources is exactly zero. The complete pair gate
is diagonal and positive on every complex linear combination. Its floor in the
physical auxiliary metric is at least 0.0008897827790755. This is the auxiliary
metric, not the original canonical spectral floor.

## Fresh all-source inverse bounds

The new diagonal form is also a uniform theorem on the entire parity carrier.
Using theta=99/100 without mixing gives

\[
 \mu_{new}=\alpha\left(1-\frac r{H_{n0}+s_{lo}}\right)>0.
\]

The validator checks kappa>r*alpha, so retained degrees have lower bound at least
alpha>mu_new. The original RC271 upper nu is unchanged and remains valid for this
same reference operator. The auxiliary source map still has squared D-norm bound
1/s_lo in its exact physical mass metric. RC230's positive Chebyshev recurrence
is rerun using these fresh endpoints; old inverse budgets are not transferred.

| All-source exact-action bound | Even | Odd |
|---|---:|---:|
| Previous D lower floor | 0.00135506441404 | 0.00139911565062 |
| New D lower floor | 0.00390305000493 | 0.00428073807420 |
| Unchanged D upper endpoint | 99.13831228 | 93.70174763 |
| Old residual degree for correction <=1e-6 | 1590 | 1522 |
| New residual degree for correction <=1e-6 | 895 | 829 |
| Old residual degree for correction <=1e-12 | 2524 | 2416 |
| New residual degree for correction <=1e-12 | 1445 | 1340 |

These are sufficient conditional exact-action degrees for the full auxiliary
source operator. They are not executed full-range solves, optimal degrees,
inexact-action propagation budgets or measured runtime claims.

## The exact remaining coupled obligation

Write the native auxiliary gate Mass-lambda*T in the ordered pair plus remaining
degrees as

\[
 G_{aux}=\begin{pmatrix}\Gamma&C\\C^*&F\end{pmatrix},
 \qquad \Gamma\succ0.
\]

Here Gamma is the actual diagonal pair gate, with the certified lower endpoints
above. Positivity of the full matrix is equivalent to

\[
 \boxed{F-C^*\Gamma^{-1}C\succ0.}
\]

The remaining native degrees have ranks 235 even and 371 odd, total 606. Their
indices and safe inverse pivot upper bounds are recorded in the certificate. The
same-parity cross columns C are not zero by reflection, and their Gram payment
cannot be omitted. Any approximate cross columns require paid weighted error
covariance before accepting a lower Schur bound. None of that remaining matrix
is evaluated here.

This dimension 606 belongs to the new rank-608 auxiliary reduction. It is not
obtained by subtracting two pivots from the independent canonical nonpositive
ceiling 582, which remains unchanged. An exact finite matrix control has two
positive pivots and two negative remaining Schur directions, demonstrating why
the pair alone cannot close the full gate.

## Reproduction and preserved scope

```bash
python scripts/validate_rpb108_rc275_canonical_shift_inverse.py \
  --output certificates/rpb108_rc275_canonical_shift_inverse.json
python scripts/validate_rpb108_rc275_canonical_shift_inverse.py \
  --output certificates/rpb108_rc275_canonical_shift_inverse.json --replay
```

All 260 inherited blob pins are checked. Replay reverses dependencies, proposal
traversal and exact accumulations and compares the entire certificate. New exact
controls check the positive-remainder shift identity and inverse order with
noncommuting D operators; the inverse recurrence has independent exact binomial
checks through degree 24. The supplied analytic proof is not Lean formalization.

The original below-0.01 count ceiling 608, nonpositive ceiling 582, legacy signed
pivots and separate eight-source canonical inverse width 485647/1000000 are
preserved. Next: construct the new pair's same-parity cross columns and certify
the remaining 606-dimensional coupled form. Stage I, global/F4 and RH remain open.
