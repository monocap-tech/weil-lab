# RPB108 — RC271: exact diagonal projection reference operators

Parent RC270: `3fc9cd092f9f49e18cc0fe28c68257e8991df8c6`.
Branch: `research/rpb108-route-consolidation`. Aperture B=11/10.

RC271 constructs two new positive reference operators for the unchanged original
Weil form. Their augmentations are exact physical Legendre projections, of ranks
608 and 582. The entire native auxiliary metric is diagonal and exact, and the
added D-energy action is diagonal. No frequency Gram, rational Fourier kernel,
Taylor truncation, or Fourier-augmentation product error is needed for these new
augmentations. Actual original Weil actions and full inverse-response covariance
remain necessary. No full response gate or Stage I closure is claimed.

The legacy rank-639 rational Fourier augmentation and its two certified positive
signed pivots remain intact. The new operators are alternatives with different
inverse responses; the old pivots and inverse action budgets do not transfer.

## From canonical coverage to a physical projection factor

Use a parity row from RC270, with its exact concentration budget

\[
 \langle h,A_Qh\rangle_c\ge\gamma\|h\|_c^2-p\|J_Uih\|_2^2.
\]

Here i is canonical-to-physical inclusion and J_U denotes physical Fourier
restriction. Let E_m be the physical Legendre polynomial span of the retained
matching degrees j<m, and let P be the physical L2-orthogonal projection onto E_m.
The span agrees exactly with the retained Chebyshev polynomial span. The exact
comparison kernel X_m therefore annihilates (I-P) on the parity carrier:

\[
 X_m(I-P)=0,\qquad
 \|J_U(I-P)\|_2\le\delta,
 \quad \delta^2\text{ is RC270's physical Hilbert--Schmidt upper bound}.
\]

This uses the physical kernel bound before canonical restriction, not merely a
canonical operator estimate applied to an arbitrary physical vector. Plancherel
also gives ||J_U P||<=1. For theta>0, complex Hilbert-space Young's inequality gives

\[
 \|J_U f\|_2^2\le(1+\theta)\|Pf\|_2^2
       +(1+\theta^{-1})\delta^2\|(I-P)f\|_2^2.
\]

Define the new exact reference operator

\[
 H_P=A_Q+\lambda i^*Pi,\qquad
 \lambda=p(1+\theta).
\]

Since ||i||<=1, the projection term cancels the first allowance and yields

\[
 H_P\succeq\eta I_c,\qquad
 \eta=\gamma-p(1+\theta^{-1})\delta^2>0.
\]

All original arithmetic allowances are those of RC270. This is a new exact
finite-rank correction, rather than an assertion that the Fourier augmentation
equals a projection. No new special-function or prime-operator estimate enters.

For the rank-608 model choose theta=1. For the rank-582 model put
beta=gamma-p*delta^2>0 and theta=2p*delta^2/beta, giving eta=beta/2 before downward
rounding. The certificate materializes all four rational coefficients and floors.

| Model | Parity rank | lambda, approximately | Canonical reference floor, approximately |
|---|---:|---:|---:|
| 608 even | 236 | 20.72240014 | 0.00974182697639 |
| 608 odd | 372 | 21.67419381 | 0.0100585200578 |
| 582 even | 227 | 32.11802285 | 0.000390308278326 |
| 582 odd | 355 | 68.63702827 | 0.0000994317529079 |

These are positive augmented reference floors, not lower bounds for A_Q itself.
Although rank 582 is smaller, its weak reference floor makes the safe inverse
conditioning bounds much worse. The rank-608 reference is the next response
target because it retains a floor comparable to the legacy reference while
removing its nontrivial frequency metric and Fourier augmentation action.
No claim of measured runtime improvement or global optimality is made.

## Every source and every added action is explicit

In the native physical basis P_j(x/B), the mass is

\[
 m_j=\frac{2B}{2j+1},\qquad
 Pf=\sum_{j\in I}\frac{P_j\langle P_j,f\rangle_2}{m_j}.
\]

The complete auxiliary Gram is Mass=diag(m_j). The 608-model indices are even
0,2,...,470 and odd 1,3,...,743. The 582-model indices are even 0,2,...,452 and odd
1,3,...,709. All indices and masses are materialized in the JSON. Their functionals
are independent, so i*E_m has exactly the stated rank. Diagonal mass normalization
is an exact isometry; no dense auxiliary Gram factorization is needed.

On the common canonical/D-energy form domain, write D P_j=(H_j+s)P_j, with H_j the
harmonic number, and let N0 represent the original form. The new D-Riesz operator is

\[
 N_P=N_0+\lambda D^{-1}P.
\]

For each retained j the added action multiplies its coefficient by
lambda/(H_j+s); it is zero on all other Legendre degrees. The D-energy source for
physical auxiliary polynomial P_j is D^-1 P_j=P_j/(H_j+s). Every source coefficient
and augmentation multiplier is enclosed using the inherited common interval for
s. These interval bounds share one actual s; independence of their uncertainties
is not assumed. The physical augmentation form lambda*Mass is exactly rational.

This removes the Fourier kernel from the added action only. N0 still contains the
complete original archimedean, pole and prime terms, with their existing action
and error obligations. RC271 performs no new original Weil actions or inverse
responses.

## Exact response criterion in the diagonal native metric

Let C=P i map the canonical carrier to E_m with its physical inner product. Then
H_P=A_Q+lambda C*C and

\[
 B_P=\lambda C H_P^{-1}C^*\succeq0.
\]

The standard block Schur congruence, with H_P uniformly positive, gives

\[
 A_Q\succ0\quad\Longleftrightarrow\quad I_{E_m}-B_P\succ0.
\]

Negative index and nullity also agree between the original form and this finite
auxiliary gate. In native coefficients it is the generalized matrix inequality

\[
 \boxed{\mathrm{Mass}-\lambda T\succ0,\qquad
 T_{jk}=\langle P_j,N_P^{-1}D^{-1}P_k\rangle_2.}
\]

The cancellation identity H_P^-1 i*=N_P^-1 D^-1 is the same common-form argument as
RC230: N_P=M H_P, with M=D^-1 L. It requires no commutation of M and N_P, and no
separately approximated canonical Riesz images. It uses the new N_P, not the old
rational Fourier reference operator.

Let U synthesize native physical auxiliary polynomials, and let Y be any trial
source-response map. With e=D^-1 U-N_P Y, the exact native response satisfies

\[
 T=U^*Y+Y^*U-Y^*DN_PY+e^*DN_P^{-1}e.
\]

The final term is added and is a covariance matrix. If mu I_D<=N_P<=nu I_D, its
bounds are nu^-1 e*De <= e*D N_P^-1 e <= mu^-1 e*De. Thus an upper residual Gram
provides an upper response correction to be subtracted from the native gate.
Entrywise residual errors or positive individual source tests alone do not close
the full matrix inequality. All trial, original-action, truncation and propagated
rounding errors must be paid in the actual residual.

## Fresh bounds and conditional inverse budgets

Use the legacy RC114 positive reference upper b_old only to infer A_Q<=b_old I.
Then H_P<=(b_old+lambda)I because ||P i||<=1. The common-form comparison
(32125/230953)D<=L<=2D gives fresh bounds

\[
 \mu=(32125/230953)\eta,\qquad
 \nu=2(b_{old}+\lambda),\qquad
 \|D^{-1}U\|_{E_m\to D}^2\le1/s_{lo}.
\]

All endpoints are rounded outward. For the 608 reference, RC230's positive
Chebyshev recurrence is run afresh with these new endpoints:

| Parity | D lower mu, approximately | D upper nu, approximately | Residual degree for response correction <=1e-6 | Degree for <=1e-12 |
|---|---:|---:|---:|---:|
| Even | 0.001355064414 | 99.13831228 | 1590 | 2524 |
| Odd | 0.001399115651 | 93.70174763 | 1522 | 2416 |

These are sufficient exact-action polynomial budgets, not executed responses,
inexact-action budgets, or optimal degrees. They are slightly larger than the
legacy RC230 budgets, so rank reduction does not by itself prove fewer actions.
The rank-582 safe D condition bounds are approximately 2.25 million even and
13.57 million odd; no polynomial inverse degrees are certified for that model in
this checkpoint. Generic zero-trial response upper bounds exceed one for all four
rows, so a positive reference alone does not discharge the gate.

## Validation and next obligation

The validator checks all 248 inherited blob pins, materializes every source/mass
and diagonal multiplier, and verifies three exact finite controls with negative,
zero and positive original forms. They use a nonidentity auxiliary metric and
noncommuting canonical/D operators, check the positive reference, preserve both
negative index and nullity in the finite gate, and verify the added residual
identity and its upper bound. These controls are not actual negative Weil
directions. Direct polynomial integration checks the physical Legendre mass rule.

```bash
python scripts/validate_rpb108_rc271_diagonal_projection_reference.py \
  --output certificates/rpb108_rc271_diagonal_projection_reference.json
python scripts/validate_rpb108_rc271_diagonal_projection_reference.py \
  --output certificates/rpb108_rc271_diagonal_projection_reference.json --replay
```

Replay reverses dependency, source-diagonal and control traversal and compares
the entire certificate exactly. The inverse recurrence includes independent exact
binomial checks through degree 24. The analytic argument above is not a Lean
formalization.

The original strict-below-0.01 ceiling 608, nonpositive ceiling 582, and separate
eight-source inverse width 485647/1000000 are preserved. The legacy positive
signed pivots cannot simply be credited to the new models. Next: assemble paid
original-action residuals for the 608-source projection reference, compare its
actual response margins with the legacy route, and certify the full diagonal-metric
gate before any Stage I claim. Global/F4 and RH remain separate and open.
