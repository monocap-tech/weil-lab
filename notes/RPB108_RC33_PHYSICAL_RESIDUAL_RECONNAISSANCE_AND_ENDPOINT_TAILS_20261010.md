# RPB108 RC33 — actual physical residual reconnaissance and certified endpoint tails

2026-10-10. Independent research/rpb108-route-consolidation.
Parent recovered: 8b1ff9466a92acb62b72c647f2c09421de8f8ff3 (RC32).

## Evidence-separated result

All eight RC31 trial physical residuals f_j=p_j-L_B v_j have now
been evaluated by NONCERTIFIED floating quadrature. Their physical norms
are estimated between 0.053 and 0.090. The collective squared physical
residual estimate in the input mass metric is about 0.07613741.

Separately, exact rational arithmetic certifies each endpoint logarithm
coefficient and proves that both endpoint strips together contribute
less than 1e-12 to each column's squared physical residual.
The interior integral is NOT certified. Numerical estimates must not
be supplied to RC23 as rigorous Riesz error budgets.

## Exact attached residual and endpoint decomposition

Retain RC25's exact source identity
L_B v=T_0 v+W_B v+c_R v+K_B v. For v_j with solved coefficients a_i,
T_0 v_j=sum H_i a_i P_i(x/B).

Put R=2B, d=B-x near the right endpoint, b=v_j(B). Then

    f_j(B-d)=-(b/2)log(R/d)+g_j(d), 0<d<=R/2.

Indeed W_B(B-d)=(1/2)log(R/d)-(1/2)log(1-d/R).
The polynomial endpoint difference obeys |v(B-d)-b|<=K d.
Its product with W_B is bounded by KR/2: use
d log(R/d)<=R/e, e>2, and -log(1-d/R)<=log2<1.
The remaining b endpoint correction is bounded by |b|/2.

Define rational amplitude and derivative allowances
V=sum |a_i| and K=sum [i(i+1)/(2B)]|a_i|.
The Legendre derivative inequality follows, for example, from its
derivative expansion into lower Legendre modes and |P_n|<=1.
It bounds the physical derivative throughout the interval.

K_B has an L-infinity row bound
M=1+1/(2R)-c_lower, since
2 integral_0^R k=1+2F_R-c_R and F_R<=1/(4R).
Thus ||K_B v||_infinity<=M V.
RC26's c_lower bounds |c_R| here. Together with |p_j|<=1,
the remainder is bounded by the explicit rational number

    G_j=1+sum H_i|a_i|+(-c_lower+M)V+KR/2+|b|/2.

This is a bound on g_j, not a claimed small pointwise residual.
The left endpoint has b_left=v_j(-B)=(-1)^j b; the same allowance applies.
Exact solves verify b!=0 for every column. Thus all these residuals
really have logarithmic endpoint singularities, despite being L2.

For delta=R/2^60, put A=log(R/delta)=60log2<60.
Integrating the squared endpoint envelope exactly gives the bound

    integral_both_strips |f_j|^2
      <=2 delta [(b^2/4)(60^2+2*60+2)+|b|G_j*61+G_j^2]
      <1/10^12.

The integrals used are
integral_0^delta log(R/d) dd=delta(A+1) and
integral_0^delta log(R/d)^2 dd=delta(A^2+2A+2).
The script evaluates all constants from the actual exact RC31 coefficients.
This endpoint certificate does not discard either endpoint trace.

## Noncertified interior/source evaluation

The diagnostic uses c_R=-gamma-log(2pi R) and the full source split.
For r>0, a=2pi r, z=e a, the exact scalar Cauchy integral yields

    k(r)=2/a [pi sin(z/2)^2-sin(z)Ci(z)+cos(z)Si(z)].

The identity follows by the Laplace integral for the Cauchy density;
equivalently differentiate the sine/cosine integral expression in its
Laplace parameter and match its value at zero. The rewritten form
avoids subtracting two large 1/(2r) terms near zero. These special
functions are used only for the diagnostic, not the endpoint proof.

K_B v(x) is evaluated with both distance integrals,
integral_0^(x+B) k(r)v(x-r)dr and
integral_0^(B-x) k(r)v(x+r)dr.
Within each integral substitute r=length*y^2. In the outer half-interval
integral substitute x=B(1-y^2). These changes soften the logarithms
without dropping their contributions. Parity supplies the second half.

Fixed Gauss-Legendre quadrature orders give:
- order 128: collective squared physical estimate 0.07613764538;
- order 256: 0.07613742311;
- order 512: 0.07613740655.

The per-column norm estimates at order 512 are

    0.06682059, 0.05574355, 0.06270092, 0.05320315,
    0.06588928, 0.05810082, 0.08986325, 0.08303697.

Maximum change in these norms between orders 256 and 512 is about 1.23e-8.
These changes are convergence diagnostics, NOT error bounds.
The estimates include the entire interval; the exact endpoint-strip
certificate is independent of these sampled calculations.

## Executed artifacts and next obligation

scripts/validate_rpb108_rc33_endpoint_residuals.py: executed PASS;
exact coefficients, parity and all eight endpoint tail budgets verified.
certificates/rpb108_rc33_endpoint_residuals.json stores those proof data.

scripts/diagnose_rpb108_rc33_physical_residual.py: executed at orders
128, 256 and 512. The stored diagnostic certificate carries explicit
NONCERTIFIED flags. It requires NumPy and SciPy and takes the RC31
certificate path and optional quadrature order as arguments.

The former adaptive nested quadrature was stopped because of its cost;
the fixed transformed calculations above completed. No adaptive
error indicator is used as certification.

Next: rigorously enclose the interior residual Gram integral with
validated kernel/source evaluation and integration errors, then combine
it with the certified endpoint tails and transport through RC24.
That would give actual small whole canonical error upper bounds.
The present numerical values do not discharge that obligation.

No native head/source positivity, original aperture extension, RH/F4,
or Lean closure is claimed. Other branches are unchanged.
