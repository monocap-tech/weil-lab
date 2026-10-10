# RPB108 RC37 — endpoint-zero trials excluded in the fixed sixteen-mode space

2026-10-10. Branch `research/rpb108-route-consolidation`.
Recovered parent: `d834a02d5ac0d35dce21dad5d901184cfe3aa456` (RC36).

## Result

A hard zero condition at both endpoints removes the leading endpoint
logarithms from polynomial sources, but it cannot improve the present
sixteen-mode Riesz approximation. This is now a certified fixed-space
exclusion, rather than a numerical observation about one construction.

For each physical target p_j, 0<=j<8, let v_j be the RC35 trial and
r_j its actual canonical Riesz vector. Every polynomial trial u of
degree <=15 with u(-B)=u(B)=0 satisfies

    ||r_j-u||_canonical^2 - ||r_j-v_j||_canonical^2 >1/200.

The sharper per-target increase lower bounds are:

| Target j | Every endpoint-zero trial: canonical squared-error increase lower, rounded down |
|---|---:|
| 0 | 0.010545 |
| 1 | 0.009763 |
| 2 | 0.009994 |
| 3 | 0.007789 |
| 4 | 0.007892 |
| 5 | 0.006271 |
| 6 | 0.006565 |
| 7 | 0.005362 |

With physical input mass M=diag(2B/(2j+1)), ANY eight-target trial map
whose columns are endpoint-zero polynomials of degree <=15 has
collective canonical squared-error norm at least

    38796938739/1000000000000 =0.038796938739.

This exceeds RC36's upper bound 0.00756076875688716 for the existing
trials. Consequently this constraint cannot beat the current certified
collective approximation within the fixed sixteen-dimensional space.
RC36 remains the best certified construction in this comparison.

## Endpoint constraint and its exact nominal minimizer

Keep B=11/10 and the RC35 rational metric center G_hat, physical mass
M_16 and coefficients V. Its certified form error is

    |z*(G_actual-G_hat)z| <= E z*M_16 z,
    E<1/1000,   G_hat >=(1-E)M_16.

The source Riesz identity is ell_j(u)=<p_j,u>_physical. RC35's exact
solve G_hat V=[M;0] therefore gives nominal Galerkin stationarity.
For any coefficient vector u, writing z=u-v_j, the difference between
nominal squared Riesz errors is z*G_hat z. The unknown squared norm
of r_j cancels in comparisons.

Define b_even and b_odd to have entries 1 in the corresponding parity
positions and 0 elsewhere. The two endpoint-zero conditions are
exactly b_even*u=b_odd*u=0, since P_i(1)=1 and P_i(-1)=(-1)^i.
The metric is parity block diagonal and v_j has parity j.
For q equal to the parity of j, put

    h_q=G_hat^(-1)b_q,
    d_q=b_q*h_q >0,
    w_q=h_q/d_q,
    t_j=b_q*v_j=v_j(B),
    u_j^0=v_j-t_j w_q.

All quantities are exact rational. The validator checks both endpoint
zeros, parity and the constrained stationarity equation

    G_hat u_j^0 = [M;0]_j - (t_j/d_q)b_q.

Thus u_j^0 uniquely minimizes nominal squared Riesz error subject to
both endpoint zeros. The minimum nominal error increase is

    c_j=t_j^2/d_q >0.

In particular, for EVERY endpoint-zero u in this space,

    (u-v_j)*G_hat(u-v_j) >=c_j.

No parity restriction on the competing u is needed: an opposite-parity
component adds a nonnegative term and does not lower this constrained
minimum.

## Uniform transport to the actual canonical metric

The exact actual-error difference is the nominal difference plus

    u*(G_actual-G_hat)u - v_j*(G_actual-G_hat)v_j.

Put z=u-v_j. The elementary inequality
||u||_physical^2 <=2||z||_physical^2+2||v_j||_physical^2,
together with G_hat >=(1-E)M_16, gives

    actual squared-error difference
      >= [(1-3E)/(1-E)] z*G_hat z -3E||v_j||_physical^2
      >= [(1-3E)/(1-E)] c_j -3E||v_j||_physical^2.

The positive factor is valid because E<1/1000. Every final lower bound
is proved >1/200 by exact rational arithmetic and rounded downward
for the certificate. This uniform estimate applies to all endpoint-zero
competitors, not just the nominal minimizer.

For any eight-column endpoint-zero approximation, select a coefficient
vector supported on one target. The old squared Riesz error is
nonnegative, so the normalized new error is at least the corresponding
increase divided by M_jj. The maximum of these eight lower bounds,
rounded downward, gives 0.038796938739 (the strongest target is j=6).
It is strictly above the committed RC36 canonical upper bound.

The separate comparison of u_j^0 itself uses the sharper uncertainty
budget E(||u_j^0||_physical^2+||v_j||_physical^2); it is also certified
for all eight columns.

## Whole-source countercontrol

For the constructed endpoint-zero u_j^0, the source residual loses its
leading log y and log(1-y) endpoint coefficients. Indeed those are
u_j^0(-B)/2 and u_j^0(B)/2. This regularity improvement does not pay for
the nominal approximation cost above.

RC36's whole polynomial-log calculation independently encloses the
physical source residual of column 0. Use the same source-operator
uncertainty delta=2d_c+(4/3)*208*42^193/193!, and reverse the norm
triangle inequality:

    ||p_0-L_B u_0^0||_2
      >= ||p_0-L_0 u_0^0||_2-delta||u_0^0||_2.

The certified physical squared residual lower is
9352027083/250000000000 =0.037408108332. Its normalized collective
physical squared lower is
9352027083/550000000000 >0.017003685605,
which already exceeds RC36's physical upper 0.00771078401.
Both endpoint logarithms are integrated over the whole interval;
no cutoff or sampling estimate is used in this proof.

## Reproduction, next obligation and scope

Run from the repository root:

    python scripts/validate_rpb108_rc37_endpoint_zero_control.py > /tmp/rc37.json

Default inputs are the committed RC35 enriched metric and RC36 mixed
residual certificates. Explicit input paths are also accepted.
`certificates/rpb108_rc37_endpoint_zero_control.json` records the metric
input digest, exact constrained coefficients, rounded-down error
increase bounds and the whole-source control.

Execution: PASS. Exact metric positivity, trial attachment, both
endpoint zeros, constrained stationarity, all eight uniform actual
error increases, the collective exclusion and the whole physical
residual lower passed. A separate fast certificate replay also checked
the stored coefficients and exact rational budgets. Computational
assumptions remain RC30's correctly rounded Decimal behavior for the
whole residual enclosure; the fixed-space canonical exclusion uses
exact rational algebra and RC35's certified metric-error bound.

Next: retain the existing trials while enriching their approximation
space or using a supported residual-minimization construction. The
exclusion is specific to degree <=15 and hard zero endpoint values.
It does not exclude larger spaces, softer endpoint adjustments,
nonpolynomial trials or convergence to the true Riesz vectors.

These remain eight physical Legendre targets. No native 8600-feature
attachment, native positivity, new aperture positivity, RH/F4 theorem
or Lean closure is claimed. Only this research branch receives new
files; earlier artifacts are preserved.
