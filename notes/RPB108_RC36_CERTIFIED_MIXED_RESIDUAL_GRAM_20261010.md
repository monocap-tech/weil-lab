# RPB108 RC36 — certified mixed residual Gram bound

2026-10-10. Branch `research/rpb108-route-consolidation`.
Recovered parent: `577d7facab1ad8a5e662e2a38799cfa8b9d1c511` (RC35).

## Result

Keep RC35's sixteen trial modes and the same eight physical Legendre
moment targets at B=11/10. Certify their mixed whole residual pairings
and replace the trace estimate with an exact rational matrix inequality.

The executed all-coefficient bounds are

    ||sum a_j(p_j-L_B v_j)||_2^2
      <= (771078401/100000000000) a* M a,

    ||sum a_j(r_j-v_j)||_canonical^2
      <= (48577939263/6425000000000) a* M a.

| Collective squared-error upper | RC35 trace bound | RC36 mixed Gram bound |
|---|---:|---:|
| Physical | 0.01504911410 | 0.00771078401 |
| Canonical | 0.01475632978 | 0.00756076876 |

The rational fractions are the proof data; the table uses rounded-up
decimal displays. RC36 improves RC35's canonical squared-error bound
by about 48.8%. Its canonical norm upper is below 0.086953.
This remains an approximation certificate for eight physical moments.

The new estimate is for arbitrary combinations of the same eight
physical targets. It does not attach the 8600 native features or certify
native source/head positivity.

## Nominal residual Gram enclosure

Let M=diag(2B/(2j+1)) for 0<=j<8. Let V be the committed 16-by-8
rational coefficient matrix of RC35, and let T=V^*M_16 V be its exact
physical trial Gram matrix. The validator rechecks G_hat V=[M;0]
and the exact parity condition V_ij=0 when i-j is odd.

RC35 constructs each midpoint-scalar, degree-192 kernel residual as

    f_j^0(y)=A_j(y)+B_j(y)log y+C_j(y)log(1-y),
    y=(x+B)/(2B).

Use the same six exact polynomial-log moments of RC34 to integrate
f_i^0 f_j^0 over the whole interval, with physical Jacobian 2B.
All nine products of the three summands are retained in each pairing.
Opposite-parity entries vanish exactly: reflection sends f_j^0 to
(-1)^j f_j^0, and the physical measure is invariant. Consequently
there are two four-dimensional parity blocks and twenty independent
nonzero-parity upper-triangle entries, including eight diagonals.
Both endpoint logarithms are included; there is no cutoff.

Each pairing is evaluated using RC30's 220-digit directed Decimal
interval class and bounded Machin enclosure of pi. Every interval
width is below 1e-20, then it is rounded outward to a rational interval
on the 1e-20 grid. Its midpoint defines the symmetric rational matrix
Q_hat. Every diagonal enclosure overlaps the previous RC35 nominal
squared-norm enclosure, providing a consistency check.

If h is the maximum rounded half-width, then for the exact nominal
Gram Q_0,

    ||M^(-1/2)(Q_0-Q_hat)M^(-1/2)|| <= eta=8h/min_j M_jj.

This follows from the uniform entry error and the Euclidean matrix
norm bound. Exact rational LDL certification produces t_Q such that

    t_Q M-Q_hat >=0.

Therefore the nominal residual map F_0:a -> sum a_j f_j^0 satisfies

    ||F_0 M^(-1/2)||^2 <= beta_0=t_Q+eta.

A rational bisection supplies a tight accepted upper endpoint; every
accepted matrix inequality is checked by exact rational LDL. No
floating-point eigensolver enters the proof. The rounded Q_hat itself
need not be assumed positive semidefinite.

## Whole-source uncertainty as an operator bound

Certify a second exact rational inequality

    t_V M-T >=0,

so ||V M^(-1/2)||_physical^2 <=t_V. RC34–RC35 establish the whole
source-operator discrepancy between the exact source L_B and the
truncated midpoint source L_0:

    ||L_B-L_0||_(physical -> physical) <= delta,
    delta=2d_c+(4/3)*208*42^193/193!,
    d_c=488163/(2*10^9).

The scalar discrepancy is carried by I plus the compressed sine-kernel
band projection. The remaining entire-kernel tail has its uniform
row-integral bound. Thus, for F:a -> sum a_j(p_j-L_B v_j),

    ||F M^(-1/2)||
      <= sqrt(beta_0)+delta sqrt(t_V).

Square with outward interval arithmetic and round upward to denominator
10^12 to obtain beta_phys. This transports uncertainty for the entire
trial map, preserving the gain from mixed pairings rather than adding
per-column squared bounds by trace.

RC32's supported inclusion norm squared <=rho=252/257 and RC24's
weak-source attachment then give

    ||sum a_j(r_j-v_j)||_canonical^2
      <=rho beta_phys a* M a,

where r_j is the canonical Riesz vector of the physical moment p_j.
The nominal matrix enclosure and the separate source discrepancy
jointly certify the actual bound; Q_hat is not asserted to be the
actual source-residual Gram matrix.

## Reproduction and scope

Run from the repository root:

    python scripts/validate_rpb108_rc36_mixed_residual_gram.py > /tmp/rc36.json

The default inputs are the committed RC35 enriched metric and whole
residual certificates. An explicit pair of input paths is also accepted.
The metric input's SHA-256 digest is recorded in
`certificates/rpb108_rc36_mixed_residual_gram.json`.

Execution: PASS. All twenty whole mixed pairings were enclosed;
eight diagonal consistency comparisons, exact trial attachment and
parity, interval widths, both rational Loewner inequalities, source
transport and strict improvement over RC35 passed. A separate fast
replay of the saved certificate checked the input digest, rational
entry centers and rounding budget, the exact trial Gram, both PSD
inequalities, outward final norm budget and canonical aggregate.

The nominal squared map bound is approximately 0.00762995455,
the physical trial-map squared bound is approximately 0.89358608584,
and the normalized rational Gram rounding budget is approximately
2.73e-19. The source uncertainty raises the nominal squared bound to
the actual physical bound 0.00771078401. Thus the remaining bound is
primarily trial approximation error, rather than interval rounding.

Next obligation: improve the trials further while retaining the whole
residual calculation, and separately establish attachment to the
native source features. A sharper estimate for these eight moments
alone does not discharge the native positivity gate.

The computational assumption remains RC30's documented correctly
rounded Decimal behavior. This is analytic plus interval certification,
not a Lean theorem. Native source attachment, native positivity,
aperture extension, RH/F4 and exact infinite Riesz inversion remain
unclaimed. Earlier reports and certificates are preserved; only this
research branch receives new files.
