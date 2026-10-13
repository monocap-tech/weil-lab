# RPB108 — RC169: native and canonical response transport audit

Aperture 11/10. Parent RC168: `8a282ee271cd1f1724ef11be33c3bccd3e5019ab`.
Only `research/rpb108-route-consolidation` is written. Historical checkpoints remain immutable.

RC169 pays the exact return from the conditioned source frame to all seven native carrier coordinates. It also obtains a canonical dual-response enclosure from the actual full-domain metric theorem. The audit finds a concrete distinction: the half-Gram reference gate is paid, whereas the available canonical transport enclosure is broad and the original augmented response is unevaluated.

| Quantity | Certified width relative to source D-energy |
|---|---:|
| Native reference inverse enclosure | 0.450692 |
| Native reference midpoint error upper | 0.225346 |
| Canonical dual-response enclosure from inverse monotonicity | 7.515976 |

These are sufficient enclosure bounds, not lower bounds on actual response error. The reference enclosure fails the tested width contracts at 10^-6, 10^-12 and 10^-24; it passes 1/2. The canonical enclosure fails the half-Gram width contract. No actual inverse-error obstruction is inferred from either failure.

## Exact native return

Write N for the native vector map in the order P0, psi0, f0, w14, v10, z_b6, t10. The conditioned map is S=N T with T=WX, using RC155's source frame and RC158's conditioning. Both are square invertible rational matrices. RC169 constructs T^-1 with the paid native row permutation and verifies both inverse products exactly.

For each conditioned Gram or response enclosure A, the native enclosure is T^-T A T^-1. The validator verifies the return congruence T^T A_native T=A, positivity, and the native half-Gram gate. Thus source conditioning causes no loss in the bound: U_native-L_native <= 0.450692 G_native,lower. The midpoint enclosure error is bounded in both Loewner directions by half this width. This is a quadratic response bound, not a norm error for an inverse vector.

## Actual canonical transport

RC119 proves aP <= L <= P; RC121 proves the common full supported form domain and D <= P <= 2D. Here P=D+h and L=P+R-rI, with r=789/125 and R the bounded nonnegative regular metric multiplier. Neither is the original Weil operator.

On the common form dual, inverse monotonicity gives

\[
P^{-1}\preceq L^{-1}\preceq a^{-1}P^{-1},\qquad a^{-1}=230953/32125.
\]

For the dual inputs D S, RC168's lower L_P and upper U_P therefore give L_P <= Sigma_L <= a^-1 U_P. Exact congruence supplies the corresponding native matrices. RC169 certifies the smallest 10^-6-grid upper on this enclosure width against RC168's source Gram lower: 7.515976. Acceptance checks exact rational PSD at that grid point and rejection at the preceding point. NumPy supplies only a search hint. This minimal grid statement concerns the specified enclosure, not an optimum over all valid canonical estimates.

No physical L2 source membership is required to interpret these form-dual inputs. The result does not identify them with RC115's original Fourier-source adjoints. It does not realize canonical Riesz vectors, evaluate R, or compute an original Weil or augmented action.

## Required tolerance and next obligation

The audit uses immutable RC119, RC121, RC123 and RC150 notes as hashed inputs. RC119's posterior canonical error Gram satisfies G_P <= G_c <= a^-1 G_P. RC121 supplies conditional direct canonical Chebyshev action budgets. RC123's moment enclosure rule requires a requested width eta, with moment tolerance eta/3 and a corresponding degree. Its 10^-6, 10^-12 and 10^-24 examples are targets, not a selected numerical Stage I requirement. RC150 explicitly records that the RC notes do not specify such a requirement. RC169 therefore does not invent one or relabel 1/2 as a Stage I completion criterion.

The next mathematical obligation is the bounded regular action D^-1(R-rI), on the required physical source family with its actual map errors. Attach a requested canonical tolerance to the RC119/RC121 solver contracts and certify its full correlated residual Gram. Additional accuracy on this reference seven-vector family alone does not identify or solve the whole original augmentation source family.

Original positivity still requires Hhat=A_Q+T_Weil^*T_Weil >= eta I and the signed auxiliary response T_Weil Hhat^-1 T_Weil^* <= theta I for theta<1, with the actual auxiliary metric and paid original action/residual errors. The reference and canonical metric inverse responses cannot replace that augmented inverse. Stage I, original positivity, whole-aperture extension, Global/F4, RH and Lean closure remain unclaimed.

## Reproduction

Run `scripts/validate_rpb108_rc169_native_canonical_transport.py --output certificates/rpb108_rc169_native_canonical_transport.json` with these eight inputs in order:

1. certificates/rpb108_rc168_eta_tail_moment_enclosure.json
2. certificates/rpb108_rc158_seven_inverse_assembly.json
3. certificates/rpb108_rc155_seven_source_action_interface.json
4. certificates/rpb108_rc121_diagonal_metric_equivalence.json
5. notes/RPB108_RC119_UNIFORM_REFERENCE_SOURCE_SOLVER_20261012.md
6. notes/RPB108_RC121_GLOBAL_DIAGONAL_METRIC_EQUIVALENCE_20261012.md
7. notes/RPB108_RC123_ENDPOINT_NONCLOSURE_AND_MOMENT_STOPPING_20261012.md
8. notes/RPB108_RC150_SOURCE_COVERAGE_20261012.md

Repeat with `--replay`. Replay independently reverses the scalar double sums in all four native congruences, reverses target traversal and compares the complete rational certificate. Dependency hashes, two-sided inverse identities, return congruences, source/response PSD and the accepted width matrices are checked exactly. The analytic inverse-monotonicity proof is supplied above; numerical controls do not replace it.
