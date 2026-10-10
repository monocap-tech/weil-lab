# RPB108 RC38 — thirty-two-mode certified Riesz trials

2026-10-10. Branch `research/rpb108-route-consolidation`.
Recovered parent: `261e907ff6b8aed70a1319a86717286406ef7c4f` (RC37).

## Result

At B=11/10, enlarge the trial space from modes 0–15 to Legendre modes
0–31. Retain exactly the same eight physical moment targets p_0,…,p_7.
The whole mixed residual Gram method of RC36 certifies the new rational
trials, including both endpoint logarithms.

Let r_j be the actual canonical Riesz vector of p_j, let v_j be the
new emitted rational trial, and let M=diag(2B/(2j+1)) for 0<=j<8.
For every coefficient vector a,

    ||sum a_j(p_j-L_B v_j)||_2^2
      <= (1448839429/1000000000000) a* M a,

    ||sum a_j(r_j-v_j)||_canonical^2
      <= (91276884027/64250000000000) a* M a.

| Collective squared-error upper | RC36: sixteen modes | RC38: thirty-two modes |
|---|---:|---:|
| Physical | 0.007710784010 | 0.001448839429 |
| Canonical | 0.00756076875689 | 0.00142065189148 |

The table rounds decimal upper displays upward; the rational fractions
are the proof data. The canonical squared-error bound improves by
about 81.2%. The corresponding canonical norm upper is below 0.037692.
This is an all-coefficient bound for the same eight physical targets.

RC37 excluded hard endpoint-zero conditions in the sixteen-mode space.
This pass adds approximation directions; no endpoint-zero constraint
is imposed. The targets remain eight physical moments and have not
been identified with the 8600-feature native head.

## Enlarged physical metric

Let M_32=diag(2B/(2i+1)) for 0<=i<32, and M=M_32[0:8,0:8].
Use RC35's exact rational physical overlap polynomials, exact endpoint
potential matrix, and the normalized degree-192 entire kernel series.
The scalar is evaluated at the exact RC26 midpoint, with its half-width
d_c=488163/(2*10^9) carried outside coefficient cancellation.

For the overlap polynomial O_ij(r)=sum o_m r^m and the normalized
kernel coefficients q_p,l_p, the truncated kernel entry is

    sum_p q_p sum_m o_m R^m/(p+m+1)
    -sum_p l_p sum_m o_m R^m/(p+m+1)^2,
    R=2B.

The overlap includes both spatial triangles. Add the exact endpoint
potential entry and the diagonal (H_i+c_mid)M_32,ii. Opposite-parity
entries vanish exactly. There are 272 independent same-parity
upper-triangle entries in the thirty-two-dimensional metric.

Each nominal entry is enclosed with RC30's 220-digit directed Decimal
interval arithmetic and bounded Machin pi. Its interval width is
below 1e-30; rational grid rounding is outward at denominator 10^20.
The rational midpoint matrix is G_hat. If h is the maximum rounded
half-width, then the mass-normalized actual metric error is bounded by

    E=2d_c+(4/3)*200*42^193/193! +32h/min_i M_32,ii <1/1000.

Exact rational LDL verifies G_hat-(1-E)M_32 >=0. Thus the enlarged
nominal metric is positive definite and its trial solve is well posed.
The executed E is approximately 0.00048816300000000456. The old
sixteen-by-sixteen principal block matches RC35's committed rational
metric center exactly.

## Exact solve, then explicit rational coefficient rounding

An exact rational solve first produces V_exact satisfying

    G_hat V_exact=[M;0].

Round each coefficient to the nearest multiple of 10^-30, retaining
exact zero entries in the opposite parity positions. The emitted trial
coefficient matrix V has dimension 32-by-8 and satisfies

    |V_ij-V_exact,ij| <=1/(2*10^30),
    max_ij |(G_hat V-[M;0])_ij| <10^-27.

Both claims are checked by exact rational arithmetic. The emitted
coefficients are explicitly marked as rounded, rather than as an exact
nominal solution. This keeps the committed coefficient representation
compact while preserving a deterministic construction. The executed
maximum nominal solve-entry error is approximately 1.041e-30, well
inside the asserted 1e-27 tolerance.

Most importantly, the following whole source calculation is performed
on V itself. Its rounding error is therefore included in the actual
trial residuals; no source error from coefficient rounding is omitted
or treated as though the unbounded source were uniformly bounded.

## Whole mixed residual and uncertainty transport

Apply the beta-integral convolution and six exact polynomial-log
moments of RC34–RC36 to each emitted degree-31 trial. Its midpoint,
truncated-kernel residual has the exact form

    A_j(y)+B_j(y)log y+C_j(y)log(1-y),
    y=(x+B)/R.

The eight target residuals still split into two four-dimensional parity
blocks. Enclose all twenty independent same-parity Gram entries over
the whole interval. Every interval width is below 1e-20 and is rounded
outward on the 10^-20 grid. There is no endpoint cutoff.

Let Q_hat be the rational midpoint Gram matrix and eta=8h_Q/min_j M_jj
its normalized entry-rounding budget. Exact rational LDL and bisection
certify t_Q M-Q_hat >=0, so the nominal residual-map squared norm is
at most beta_0=t_Q+eta. Independently, compute T=V^*M_32 V exactly and
certify t_V M-T >=0.

The larger valid residual-kernel tail bound is

    eps=(4/3)*224*42^193/193! <1e-40.

As in RC34, scalar uncertainty changes the source through I plus the
compressed sine-kernel band projection. Hence the source discrepancy
has physical operator norm <=delta=2d_c+eps. The actual residual map F
therefore satisfies

    ||F M^(-1/2)|| <=sqrt(beta_0)+delta sqrt(t_V).

Square outward and round upward to denominator 10^12 for beta_phys.
RC32's supported inclusion norm squared rho<=252/257, with RC24's
weak-source attachment, gives the actual canonical Riesz approximation
squared norm bound beta_canonical=(252/257)beta_phys.

## Reproduction and scope

Run from the repository root:

    python scripts/validate_rpb108_rc38_thirty_two_metric.py > /tmp/rc38_metric.json
    python scripts/validate_rpb108_rc38_thirty_two_residuals.py /tmp/rc38_metric.json > /tmp/rc38_residual.json

The residual validator's second argument defaults to the committed
RC36 mixed residual certificate, used for the strict improvement check.
Committed proof data:

- `certificates/rpb108_rc38_thirty_two_metric.json`
- `certificates/rpb108_rc38_thirty_two_residuals.json`

Execution: PASS. All 272 enlarged metric entry enclosures, nominal
metric positivity, exact solve before rounding, coefficient rounding
and emitted solve tolerance passed. All twenty whole residual Gram
entries, exact parity, interval widths, both rational Loewner bounds,
source uncertainty transport and strict improvement over RC36 passed.
A separate saved-certificate replay checked the input digest, unchanged
RC35 principal metric block, rational matrix budgets, rounded solve,
trial Gram, both PSD inequalities and outward final aggregate.

The nominal residual-map squared bound is approximately
0.001413922572, and the physical trial-map squared bound is approximately
0.893596531594. The normalized Gram rounding error is approximately
2.73e-19. Whole-source scalar and tail uncertainty raise the nominal
physical squared bound to 0.001448839429. Trial approximation remains
the dominant contribution.

Next obligation: use this enlarged certified metric to attach further
source functions, or enrich along the remaining residual directions.
The gain for these eight moments alone does not certify the native
positivity gate.

The computational assumption remains RC30's documented correctly
rounded Decimal behavior. This is analytic plus interval certification,
not a Lean theorem. Native feature attachment, native positivity,
aperture extension, RH/F4 and exact infinite Riesz inversion remain
unclaimed. Only this research branch receives new files; earlier
reports and certificates are preserved.
