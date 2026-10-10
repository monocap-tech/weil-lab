# RPB108 RC35 — sixteen-mode certified Riesz trials for eight physical moments

2026-10-10. Branch `research/rpb108-route-consolidation`.
Recovered parent: `0e82dfb5a7357a7935a4e7a3cb8c7331fa582a2d` (RC34).

## Result

At the same cap B=11/10, enlarge the trial space from Legendre modes
0–7 to modes 0–15, while retaining exactly the same eight physical
moment targets p_0,…,p_7. The newly solved trials have certified whole
physical source residuals, including both endpoint logarithms.

| Target j | RC34 physical norm upper, rounded up | RC35 physical norm upper, rounded up |
|---|---:|---:|
| 0 | 0.067494 | 0.029521 |
| 1 | 0.056097 | 0.025783 |
| 2 | 0.062957 | 0.026061 |
| 3 | 0.053409 | 0.022878 |
| 4 | 0.066062 | 0.023672 |
| 5 | 0.058252 | 0.021186 |
| 6 | 0.089994 | 0.022757 |
| 7 | 0.083155 | 0.020770 |

The proof data are the rational squared upper bounds in the residual
certificate; the table is rounded upward for display.
Let M_8=diag(2B/(2j+1)) for 0<=j<8, and let r_j be the canonical
Riesz vector of the physical moment p_j. For arbitrary coefficients a,

    ||sum a_j(p_j-L_B v_j)||_2^2
      <= (33108051013/2200000000000) a* M_8 a,

    ||sum a_j(r_j-v_j)||_canonical^2
      <= (2085807213819/141350000000000) a* M_8 a.

The bounds are approximately 0.0150491141 and 0.0147563298.
The validator proves the simpler strict bounds 0.0151 and 0.015.
The canonical squared-error bound improves RC34's 0.15126546598 by
about 90.2%; its norm bound is about 0.1215. This is still above the
separate 0.0025 native target, and these eight physical moments have
not been identified with the 8600-feature native head.

## Certified enriched metric and exact trial solve

The source decomposition and Fourier convention remain those of
RC24–RC34. Write p_i(x)=P_i(x/B), R=2B, and M_16=diag(2B/(2i+1)).
The sixteen-dimensional metric is evaluated using RC34's entire
kernel expansion, truncated at n<=192 at the exact rational scalar
midpoint c_mid. The scalar half-width is d_c=488163/(2*10^9).
The normalized kernel coefficients q_p and l_p represent

    R k(Rs) = sum q_p s^p + sum l_p s^p log s + remainder.

For the exact rational overlap polynomial

    O_ij(r)=integral_-B^(B-r)
      [p_i(x)p_j(x+r)+p_j(x)p_i(x+r)] dx,

write O_ij(Rs)=sum o_m R^m s^m. Then the truncated kernel matrix entry is

    sum_p q_p sum_m o_m R^m/(p+m+1)
    - sum_p l_p sum_m o_m R^m/(p+m+1)^2.

The overlap already includes both spatial triangles. Add the exact
endpoint potential matrix from RC30 and the diagonal
(H_i+c_mid) M_16,ii. Odd-parity entries vanish exactly.
The interval evaluator uses RC30's 220-digit directed Decimal class
and its bounded Machin enclosure of pi. Each computed nominal entry
interval has width below 1e-30, then is rounded outward on the 1e-20
grid; its rational midpoint defines G_hat.

The uniform kernel tail is bounded by

    eps_metric=(4/3)*200*42^193/193!.

Scalar uncertainty acts through I plus the compressed sine-kernel
band projection, so it contributes at most 2d_c in physical operator
norm. If h is the maximum rounded entry half-width, the full
mass-normalized metric error satisfies

    E = 2d_c + eps_metric + 16 h/min_i M_16,ii < 1/1000.

The executed E is approximately 0.00048816300000000115. Exact rational
LDL checks establish G_hat-(1-E)M_16 >=0. The coefficients V, a
16-by-8 rational matrix, solve

    G_hat V = [M_8; 0]

exactly. Thus the first eight physical moments are attached to their
new trials; the extra eight modes enrich the approximation. The
whole residual calculation below certifies the resulting trials
against the actual source, independently of treating G_hat as exact.

## Whole residual enclosure and collective transport

Apply RC34's beta-integral convolution formulas to the degree-15
trials. The residual at the scalar midpoint and truncated kernel is
exactly A_j(y)+B_j(y)log y+C_j(y)log(1-y), with y=(x+B)/R.
Parity V_ij=0 for i-j odd is checked exactly before using reflection.
The same six exact polynomial-log moments from RC34 evaluate its
whole physical squared norm. There is no endpoint cutoff.

The residual validator uses the slightly larger valid tail majorant

    eps_residual=(4/3)*208*42^193/193! <1e-40

(approximately 7.84e-44). Each nominal squared-norm interval has width
below 1e-20. Its upper square root is increased by

    (2d_c+eps_residual) ||v_j||_2,

where ||v_j||_2^2=sum_(i=0)^15 M_16,ii V_ij^2 is exact rational.
Squaring outward and rounding upward to denominator 10^12 gives the
per-column physical squared upper bounds.

The collective estimate uses the residual-map trace bound
sum_j epsilon_j^2/M_8,jj. It bounds every coefficient combination;
it is not a computed maximum eigenvalue of a residual Gram matrix.
RC32's supported inclusion norm squared <=252/257, together with
RC24's weak-source attachment, transports that trace bound to the
canonical Riesz approximation error quoted above.

## Reproduction and scope

Run from the repository root:

    python scripts/validate_rpb108_rc35_enriched_metric.py > /tmp/rc35_metric.json
    python scripts/validate_rpb108_rc35_enriched_residuals.py /tmp/rc35_metric.json > /tmp/rc35_residual.json

Committed proof data:

- `certificates/rpb108_rc35_enriched_metric.json`
- `certificates/rpb108_rc35_enriched_residual.json`

Both validators executed successfully. The residual validator was
rerun with the sharper aggregate assertions. Exact dimension, parity,
solve and positivity checks, interval widths, source-error budgets and
aggregate rational inequalities passed. The computational assumption
remains RC30's documented correctly rounded Decimal behavior; this
is analytic plus interval certification, not a Lean theorem.

Further enrichment or a residual Gram calculation can reduce the
remaining approximation bound. Native source attachment and the
native positivity gate remain separate obligations. No exact infinite
Riesz inverse, native head positivity, aperture extension, RH/F4
result or Lean closure is claimed. Only this research branch receives
these new files; earlier milestone artifacts are preserved.
