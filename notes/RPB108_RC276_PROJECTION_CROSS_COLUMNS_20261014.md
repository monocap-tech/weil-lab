# RPB108 — RC276: full cross-column centers and covariance bounds

Parent RC275: `dc1c08ac86a1429d475e44921e34efd447cd9dfc`.
Branch: `research/rpb108-route-consolidation`. Aperture B=11/10.

RC276 materializes the two cross-column centers for the remaining rank-608
projection auxiliary gate: 235 even coordinates and 371 odd coordinates, with
the opposite-parity entries exactly zero. It also certifies a joint dual-mass
error budget for each complete column and a Loewner upper bound for their Schur
payment. No new Weil action, reference operator or response trial is introduced.

The positive auxiliary pair from RC275 is preserved. The remaining principal
response block is not evaluated here. The paid cross bounds are too broad for
the available coarse principal-block bound to close positivity; they do not
prove a negative direction. The full 606-dimensional Schur problem, Stage I,
RH, F4 and Lean remain open.

| Cross-column certificate, approximately | Even | Odd |
|---|---:|---:|
| Remaining same-parity coordinates | 235 | 371 |
| Nonzero center coordinates | 32 | 31 |
| Center dual-mass norm squared | 0.000306496055274 | 0.000336220688529 |
| Complete error dual-mass norm squared upper | 0.00422984441740 | 0.00223450356475 |
| Error covariance / pivot lower, in native mass | 2.16081564914 | 0.740939024551 |
| Full cross-payment native-mass operator norm upper | 3.48070582520 | 1.42724946549 |

These are upper enclosure costs, not measured negative eigenvalues or a fraction
of completion. The JSON contains exact fractions and the complete native ordering.

## Obtain the cross centers from the existing trials

For a parity source u_b=P_b, b=0 or 1, use the same exact trial Z_b as RC272–275.
Let N_P be the unchanged D-Riesz reference, and define

\[
 w_b=N_P^{-1}D^{-1}u_b,\qquad
 e_b=D^{-1}u_b-N_PZ_b,\qquad
 x_b=w_b-Z_b=N_P^{-1}e_b.
\]

For a remaining auxiliary test vector v of the same parity, its physical pairing
with u_b is zero. Thus the corresponding row of the native gate is

\[
 C_b(v)=-\lambda_b\langle w_b,v\rangle_2
        =\widehat C_b(v)+E_b(v),
\]

\[
 \widehat C_b(v)=-\lambda_b\langle Z_b,v\rangle_2,
 \qquad E_b(v)=-\lambda_b\langle x_b,v\rangle_2.
\]

The original operators and sources are real; these formulas extend to arbitrary
complex auxiliary combinations with the consistent conjugate-linear first
inner-product convention. Opposite-parity rows vanish by actual reflection
symmetry, including their errors.

In the physical native Legendre basis,

\[
 \boxed{\widehat C_{b,j}=-\lambda_b\,m_j\,Z_{b,j},
 \qquad m_j=\frac{2B}{2j+1}.}
\]

Every coordinate is therefore exact rational arithmetic. The 32 even and 31 odd
nonzero centers lie within degree 64. Centers above the trial degree are zero;
the actual cross entries there are still covered by the error budget, not
asserted zero. The certificate gives global remaining indices, native degrees,
masses, centers and diagnostic scalar error radii for all 606 coordinates.

## A physical projection coercivity bound

The cross-error bound uses the complete inverse residual correction already paid
at RC275. To convert it to the physical auxiliary metric, first derive a lower
form on the retained physical projection P.

For the inherited concentration budget write

\[
 G_P(h,h)\ge\gamma\|h\|_c^2-p\|J_Uih\|_2^2
                     +\lambda\|Pih\|_2^2.
\]

Canonical-to-physical inclusion has norm at most one. On physical vectors,
Plancherel gives ||J_U P||<=1, and the exact comparison kernel gives
||J_U(I-P)||<=delta, with delta^2 the inherited physical Hilbert--Schmidt bound.
Put a=||Pih||_2 and b=||(I-P)ih||_2. The full original form then satisfies

\[
 G_P(h,h)\ge(\gamma+\lambda-p)a^2
       +(\gamma-p\delta^2)b^2-2p\delta ab.
\]

With beta=gamma-p*delta^2>0, completing this scalar quadratic gives

\[
 \boxed{G_P\succeq\kappa P,\qquad
 \kappa=\gamma+\lambda-p-
             \frac{p^2\delta^2}{\gamma-p\delta^2}>0.}
\]

The exact accepted lower values are approximately 9.63386352749 even and
10.30666239135 odd. These are coercivity coefficients for the retained physical
projection component, not full canonical reference floors. The complement still
uses its separately certified positive reference bounds.

For x_b=N_P^-1 e_b, the complete residual identity gives

\[
 G_P(x_b,x_b)=\langle e_b,N_P^{-1}e_b\rangle_D\le R_b,
\]

where R_b is RC275's full correction upper, including resolved output, the
infinite model tail, source uncertainty and every remaining global fault. Hence
||P x_b||_2^2<=R_b/kappa. No individual original-action error or retained-only
residual is substituted for this complete quantity.

## Joint error covariance in the exact native metric

Let M_b be the exact diagonal mass matrix on the remaining same-parity degrees.
Orthogonality of the native physical basis gives the complete row inequality

\[
 \boxed{E_bM_b^{-1}E_b^*\le\varepsilon_b^2,
 \qquad\varepsilon_b^2=\lambda_b^2R_b/\kappa_b.}
\]

Equivalently, |E_b v|^2<=epsilon_b^2 v*M_b v for every complex coefficient vector
v simultaneously. It implies a scalar entry radius epsilon_b*sqrt(m_j), but
those radii are not treated as independent coordinate errors.

The true same-parity error row can correlate across every degree. Its realized
outer product has rank at most one; the conservative mass-matrix envelope need
not have rank one. Across both parities, the actual cross matrix and its error
each have rank at most two. No claim is made that their unknown directions lie
in a known two-dimensional uncertainty subspace.

An exact finite control checks that entrywise squared error bounds miss the
off-diagonal covariance: a row (1,1) has outer product with all entries one,
which is not bounded by the identity matrix. The correct dual-norm budget gives
the valid envelope 2I instead.

## Pay the actual Schur coupling

Let Gamma be the actual positive auxiliary pivot block and let Gamma_lo be its
diagonal matrix of RC275 lower bounds. Then Gamma^-1<=Gamma_lo^-1. For any theta>0,
weighted Young's inequality gives

\[
 C^*\Gamma^{-1}C\preceq
 (1+\theta)\widehat C^*\Gamma_{lo}^{-1}\widehat C
 +(1+\theta^{-1})E^*\Gamma_{lo}^{-1}E.
\]

The joint error contract bounds the last covariance by the parity direct sum

\[
 E^*\Gamma_{lo}^{-1}E\preceq
 \bigoplus_b\frac{\varepsilon_b^2}{g_b}M_b,
\]

where g_b is the corresponding native pivot lower bound. The certificate records
the exact center rows and 1/g_b, so the center payment is specified by two rank-one
factors without storing a dense 606-square matrix. It also records the theta=1
structured bound with center factor two and error coefficients 2*epsilon_b^2/g_b.

For a simpler complete row norm bound, the dual-mass triangle gives

\[
 C_b^*\Gamma_b^{-1}C_b\preceq q_bM_b,\qquad
 q_b=\frac{(\|\widehat C_b\|_{M_b^{-1}}+\varepsilon_b)^2}{g_b}.
\]

The table reports these q_b. All pivot and residual inequalities concern the same
actual reference and exact trials; no statistical independence is assumed between
their certificates. This is an upper payment for the true coupling, not an
entrywise estimate substituted into a Loewner inequality.

## What remains unproved

The exact remaining form is R=F-C*Gamma^-1 C. Given a certified F_lo<=F, a
sufficient lower bound is F_lo minus either paid cross envelope above. The
remaining principal block F is still not evaluated.

The projection coercivity theorem alone gives a safe full auxiliary response norm
upper lambda/kappa, approximately 2.1510 even and 2.1029 odd. Neither is below one.
Combining its coarse principal lower bound (1-lambda/kappa)M_b with the full cross
payment gives negative lower coefficients, approximately -4.6317 and -2.5302.
These only show that this coarse sufficient certificate does not pass; they do
not prove R negative or produce an original negative direction.

Both source pivots remain positive. The new result is the complete cross-center
and covariance interface needed by their Schur elimination. To finish the full
gate, one must obtain a sharper remaining-principal response bound or improve the
inverse-response trials enough to reduce the required cross payments, while
retaining all errors.

## Reproduction and preservation

```bash
python scripts/validate_rpb108_rc276_projection_cross_columns.py \
  --output certificates/rpb108_rc276_projection_cross_columns.json
python scripts/validate_rpb108_rc276_projection_cross_columns.py \
  --output certificates/rpb108_rc276_projection_cross_columns.json --replay
```

All 263 inherited blob pins are verified, including equality of the trial
coefficients used by the residual and cross-center certificates. Replay reverses
dependency and exact dual-norm accumulation order and compares the full
certificate. Exact controls check the completed projection quadratic, correlated
dual-mass errors and weighted Schur payments for several positive Young parameters.
The analytic proof is not Lean formalization.

The original below-0.01 ceiling 608, nonpositive ceiling 582, legacy signed pivots,
new positive auxiliary pair and separate eight-source canonical inverse width
485647/1000000 are unchanged. The full Schur gate and Stage I remain open.
