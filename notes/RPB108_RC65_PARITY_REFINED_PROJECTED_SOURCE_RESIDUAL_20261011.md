# RPB108 RC65 — parity-refined actual projected source residual

RC65 refines the upper bound for the actual canonical rank-22 projected original source residual to

\[
\boxed{\Gamma_{22}\preceq\frac{4669}{256}M_{22}}
\qquad (4669/256=18.23828125).
\]

This reduces RC64's uniform upper bound 230/3 by exactly 1951/2560, or 76.2109375%. It uses the same actual source columns and the same actual rank-22 orthogonal projection. The new result improves a uniform bound; it does not assert that the new matrix bound is Loewner smaller than RC64's matrix in every direction.

## Refined error splitting

RC64 already certifies the nominal variational residual Y and the canonical representative error coefficient Gram EL. RC65 retains those matrices and refines the subsequent error allowances. Let Ep be RC60's full correlated physical Riesz error Gram, T the trial physical Gram, delta the RC62 actual source approximation operator error, and k_p the complete physical operator norm upper bound in parity p.

For each parity, the source transfer physical Gram is bounded by

\[
B_p=(1+v)k_p^2 E_{p,\mathrm{phys}}+(1+1/v)\delta^2 T_p,
\qquad v=1/65536.
\]

Its canonical transport and the representative-coefficient error satisfy

\[
E_p\preceq \rho(1+u)B_p+(1+1/u)EL_p,
\qquad \rho=252/257,\quad u=1/16.
\]

The final actual residual bound is

\[
A_p=(1+t_p)Y_p+(1+1/t_p)E_p,
\qquad t_{\mathrm{even}}=2,\quad t_{\mathrm{odd}}=3/2.
\]

All source, representative, and residual errors remain paid. Every matrix rounding carries an exact diagonal row-sum Loewner allowance. The matrices have exact zero mixed-parity blocks, so different parity parameters define a valid direct-sum bound.

The final comparison uses RC59's certified actual canonical Gram lower matrix M_lower directly. Exact rational PSD checks establish A_p <= lambda_p M_lower,p, and M_lower <= M_actual gives the desired canonical comparison. This avoids replacing the full lower matrix with the coarser scalar bound (3/10) P.

| Parity | Certified canonical residual upper factor | Physical Gram upper factor |
|---|---:|---:|
| Even | 4669/256 = 18.23828125 | 5855/1024 |
| Odd | 7187/512 = 14.037109375 | 137/32 |

The maximum parity factor supplies the whole-head bound. Fixed rational parameters were selected with diagnostic numerical guidance. Only the exact interval transport and rational PSD comparisons are accepted as proof evidence.

## Allowance diagnosis

The certificate separately encloses each term relative to the certified canonical Gram lower matrix. These are upper bounds on the allowances, not lower bounds on the actual source residual.

| Component | Even upper factor | Odd upper factor |
|---|---:|---:|
| Nominal variational residual Y | 4923/2048 | 5649/2048 |
| Source transfer physical B | 7047/1024 | 3995/1024 |
| Canonical representative coefficient error EL | 81/4096 | 89/4096 |
| Combined canonical variational error E | 3837/512 | 4535/1024 |

The largest remaining error allowance arises from transporting the Riesz approximation error through the complete physical operator norm bounds. Tightening that transport and the nominal projected covariance is the relevant next target. Parameter refinement alone has not reached the required scale.

## Independent replay

Generation assembles parity entry formulas. Replay independently reconstructs the source transfer by a diagonal operator congruence and verifies every final and component comparison after the exact inverse Chebyshev-to-Legendre coordinate congruence. The proof checks both native-coordinate and Legendre-coordinate PSD inequalities, exact parity zeros, certificate provenance, all paid rounding transports, and the final full 22-feature comparison.

## Evidence boundary

RC63's scalar Schur budget ceiling, using the inherited 1250-complement floor, is approximately 1.7084534755e-11. The refined upper bound is approximately 1.0675316309e12 times this ceiling. It does not certify the budget. A large upper bound does not prove that the actual residual fails the budget.

No rank-22 complement floor, positive uniform 22-feature Weil floor, negative Weil direction, full 1250 projection, aperture extension, RH, or F4 conclusion is established. The actual low-eight positive floor remains valid; the RC63 obstruction to extending its old floor remains valid.

## Added artifacts

- `scripts/validate_rpb108_rc65_parity_projected_residual_refinement.py`
- `certificates/rpb108_rc65_parity_projected_residual_refinement.json`
- This report.

Historical milestone artifacts remain unchanged.
