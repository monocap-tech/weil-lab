# RPB108 — RC278: smaller positive reference and two paid new pivots

Parent RC277: `bf38411bc8696b55901ea6ddab301e1009760c05`.
Branch: `research/rpb108-route-consolidation`. Aperture B=11/10.

RC278 constructs a new positive reference of rank **371**, down from 608,
and certifies its full infinite-dimensional lower and upper bounds. Rescaling
the existing actual-response trial polynomials certifies two positive auxiliary
pivots for this changed reference, leaving a **369-dimensional** Schur problem.
Their cross-column covariance is paid as well. The remaining principal response
block is not evaluated; full original positivity and Stage I remain open.

| Certificate | Even | Odd |
|---|---:|---:|
| New reference rank | 142 | 229 |
| Retained Legendre degrees | 0,2,...,282 | 1,3,...,457 |
| New augmentation coefficient C, approximately | 9.82442681243419 | 10.29572175268419 |
| Global D-energy lower bound mu | 0.02045154377097 | 0.02029033365187 |
| Global D-energy upper bound nu | 5.12925023009425 | 3.97184193638926 |
| D-energy condition number upper | 250.80014925 | 195.75044967 |
| Canonical reference floor lower | 0.01022577188549 | 0.01014516682594 |
| Newly certified native auxiliary pivot lower | 0.00678531949212 | 0.00708442483227 |
| Remaining auxiliary coordinates | 141 | 228 |
| Full cross-payment mass norm upper | 0.756950490614 | 0.622132070487 |

All displayed decimals are summaries of exact outward rational certificates.
The JSON contains the authoritative values. The original index bounds remain
301 at zero and 371 at 0.01, including equality; the inherited lower bound of
10 below 0.01 remains. The positive auxiliary pair is not subtracted from
these independent index bounds. RH, F4 and Lean remain open.

## Construct and bound the reference globally

Use RC277's actual original lower form G0>=D-C_b I, separately in each parity.
Let P_b be the physical L2 orthogonal Legendre projection onto the degrees in
the table, Q_b=I-P_b, and lambda_b=C_b. Define

\[
 G_{new}=G_0+C_bP_b,\qquad
 H_{new}=A_Q+C_b i^*P_bi,\qquad
 N_{new}=N_0+C_bD^{-1}P_b.
\]

Here i is canonical-to-physical inclusion, and N_new is the D-Riesz reference.
No frequency Gram is required; the augmentation is an exact diagonal physical
Legendre multiplier. With first omitted degrees 284 even and 459 odd,

\[
 \boxed{G_{new}\succeq D_{P_b}+(D-C_b)_{Q_b}\succeq\mu_b D,}
\]

\[
 \mu_b=1-C_b/(H_{first}+s_{lower})>1/50.
\]

The diagonal inequality holds on the full form domain and all higher degrees,
because D's harmonic weights increase. It is not a finite-section claim. RC121's
global L<=2D implies H_new>=mu_b/2 in the canonical metric, strictly above 0.01.

For an upper bound use h<=D from the same metric theorem and the exact identity

\[
 G_0=D+h-(789/125)I-K_{reg}+K_{prime}+K_{pole}.
\]

The regular norm bound is RC274's 0.49942681243419..., the complete actual prime
norm bound is RC277's 3013/1000, and the positive pole allowance is
2||cosh(x/2)||_2^2 in even parity and zero in odd parity. The odd pole is negative
and can be dropped for this upper bound. Since C_b P_b<=C_b I,

\[
 G_{new}\preceq2D+
 (k_{reg}+3013/1000+k_{pole,+}+C_b-789/125)I
 \preceq\nu_bD,
\]

using I<=D/s_lower and replacing a negative parenthesized remainder by zero
if needed. Thus mu_b<=N_new<=nu_b in D energy. No commutation between the
canonical metric and the original operator is assumed.

The reference has a bounded inverse in D energy and in the canonical metric.
For the physical polynomial column operator U and native mass matrix Mass,
the full auxiliary gate is

\[
 \boxed{Mass-C_b T,\qquad
 T_{ij}=\langle P_i,N_{new}^{-1}D^{-1}P_j\rangle_2.}
\]

The finite augmentation factorization and the standard block Schur congruence
identify its nonpositive inertia with that of the original form, separately
by parity. In particular, positivity of the reference alone does not prove
positivity of this gate or of the original operator.

## Reuse actual responses with the changed residual fully paid

Let Z_old be RC272's four-trial polynomial for source u=P_b, and lambda_old
the rank-608 reference coefficient. RC274 has already certified its complete
original output through degree 2048, its infinite output tail, and the remaining
global action faults. Set Z_new=t Z_old for a positive exact rational scalar t.
The new reference has different augmentation and rank, so old pivots and old
residuals cannot simply be transferred.

Both projections contain every nonzero degree of Z_old (degree at most 64).
Writing e_old=D^-1 u-N_old Z_old therefore gives the exact identity

\[
 \boxed{e_{new}=t e_{old}+D^{-1}
 [(1-t)u+t(\lambda_{old}-C_b)Z_{old}].}
\]

The added term has degree at most 64. On those degrees the validator updates
the residual center and recomputes the actual D-inverse source uncertainty for
u-t C_b Z_old. It also pays its new center rounding. Above degree 64 every
actual original residual numerator, omitted-output tail and remaining global
fault from RC274 scales by t, with squared costs scaling by t^2.

To choose t, let a=<u,Z_old>_2 and let [q_lo,q_hi] enclose
G_new(Z_old,Z_old). This interval is obtained from RC272's actual variational
center by subtracting (lambda_old-C_b)||Z_old||_2^2. Choose t as a downward
rational rounding of a/((q_lo+q_hi)/2). The resulting scales are approximately
2.10543348631 even and 2.09336539631 odd. The new variational center has bounds

\[
 2ta-t^2q_{hi}\le c_{new}\le2ta-t^2q_{lo}.
\]

The global lower form supplies the following diagonal inverse weights:

\[
 w_j=1\quad(j\text{ retained}),\qquad
 w_j=1-C_b/(H_j+s_{lower})\quad(j\text{ omitted}).
\]

The complete residual energy is weighted by 1/w_j before paying the remaining
global faults with 1/mu_b. Source uncertainty, model energy and global faults
are combined by the norm triangle inequality. The inverse-response identity
retains the **added** correction

\[
 T_{bb}=c_{new}+\langle e_{new},N_{new}^{-1}e_{new}\rangle_D.
\]

The complete correction upper bounds are approximately 0.000115669420874 even
and 0.000105040341192 odd. Consequently both new native gate pivots
mass_b-C_b T_bb are strictly positive as shown in the table. Opposite parity
couplings vanish exactly. These are newly verified pivots for H_new, rather
than inherited signs from the rank-608 or rank-639 models.

## Pay the complete cross columns

The stronger lower form gives G_new>=d_b P_b, with
d_b=H_b+s_lower. If x=N_new^-1 e_new, its residual correction bounds G_new(x,x),
so ||P_b x||_2^2<=correction/d_b. For the remaining same-parity auxiliary row,

\[
 \widehat C_{bj}=-C_b\,mass_j\,(Z_{new})_j,\qquad
 E_b Mass_b^{-1} E_b^*\le C_b^2\,correction/d_b.
\]

The JSON specifies the trial coefficients, remaining degrees, center dual-mass
norm and joint covariance radius. This determines every center, including the
zero centers above degree 64; the actual entries there still have paid error.
Opposite-parity centers and errors vanish. Errors within a parity are allowed
to correlate fully. For every theta>0 the full Schur payment satisfies

\[
 C^*\Gamma^{-1}C\preceq
 (1+\theta)\widehat C^*\Gamma_{lo}^{-1}\widehat C
 +(1+1/\theta)\bigoplus_b
 [(radius_b^2/\Gamma_{lo,b})Mass_b].
\]

The complete mass-norm payment bounds improve from RC276's 3.48070582520 and
1.42724946549 to approximately 0.756950490614 and 0.622132070487 for this changed
reference. They are enclosure costs, not eigenvalues of the original operator.
Positivity still requires a principal-block lower bound that pays these costs.

## Conditional inverse-action cost and validation

The full-source D interval also makes a new exact polynomial-inverse route
substantially shorter. Running the pinned positive Chebyshev recurrence with
the new interval and the same generic auxiliary correction targets gives:

| Generic correction target | Old even degree | New even degree | Old odd degree | New odd degree |
|---|---:|---:|---:|---:|
| 1e-6 | 895 | 80 | 829 | 71 |
| 1e-12 | 1445 | 134 | 1340 | 119 |

These are certified residual-polynomial degrees for different references;
inverse-polynomial degrees are one smaller. They are not new executed operator
actions, measured runtime ratios, or completed inverse responses for all sources.
Every eventual operator action and its propagated error must still be paid.

The validator checks 269 inherited Git blob pins. Normal generation and reverse
replay produce identical rational JSON. Exact controls verify inverse order for
a noncommuting reference, the added residual identity for several trial scales,
and the changed-reference residual update. Existing rank-608 and rank-639
references, their certificates, and the eight-source canonical inverse width
485647/1000000 remain preserved.

```bash
python scripts/validate_rpb108_rc278_smaller_positive_reference.py --output certificates/rpb108_rc278_smaller_positive_reference.json
python scripts/validate_rpb108_rc278_smaller_positive_reference.py --output certificates/rpb108_rc278_smaller_positive_reference.json --replay
```

RC279 should bound the remaining principal response or execute the shorter
paid polynomial inverse construction. The full 369-dimensional Schur inequality,
including the joint cross covariance, remains the acceptance gate for this route.
