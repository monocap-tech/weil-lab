# RPB108 RC58 — actual source leakage rules out consecutive heads through 21

RC58 proves that **every consecutive native head with 8 through 21 features fails the revised projected-source threshold** Gamma_N <= M_N/64,000,000. At least **22 consecutive native features** are necessary for that particular source threshold. This is a necessary condition, not a certificate that 22 features suffice.

The obstruction is actual source leakage, detected by exact canonical-complement tests. It is not merely an upper bound that remains too large. The low-eight Weil floor certified in RC57 remains valid. No negative Weil direction or obstruction to the full 1250-feature projection is proved.

## Objects and the lower-bound interface

Work at cap B=11/10. Let R_j be the actual canonical Riesz representative of the physical native Chebyshev feature q_j, and Pi_N the actual canonical orthogonal projection onto their span for j=0,...,N-1. The bounded complete original remainder is K; its canonical source columns are sigma_j=i* K iR_j. For a coefficient vector v supported in the first eight features, put

\[
r_N(v)=\frac{\|(I-\Pi_N)\sigma_v\|_{\rm can}^2}
{\|R_v\|_{\rm can}^2}.
\]

The original source R_v+sigma_v has the same projected residual whenever N>=8, since R_v belongs to the head.

A **complementary source detector** here means a physical polynomial z, regarded as a vector in the canonical carrier, with exact zero canonical pairing against all head representatives. The Riesz identity gives

\[
\langle z,R_j\rangle_{\rm can}=\langle iz,q_j\rangle_{\rm phys}.
\]

For z=P_n(x/B), the physical Legendre polynomial of degree n, this pairing vanishes for every physical polynomial of degree below n. Thus z is in the canonical complement of every consecutive native head with N<=n. These tests are physical Legendre vectors, not native Riesz representatives.

The same conclusion holds for a test z=sum_{n>=d} w_n P_n(x/B): it lies in every such complement with N<=d. Exact rational monomial integrations verify this moment orthogonality.

If an actual source pairing has distance a from zero, the canonical test norm has upper bound Z_up, and the actual input norm ||R_v||can^2 has upper bound M_v,up, then canonical Cauchy–Schwarz proves

\[
r_N(v)\ge\frac{a^2}{Z_{\rm up}M_{v,\rm up}},\qquad 8\le N\le d.
\]

This is a directional Rayleigh lower bound. It is not a Loewner lower bound on the entire residual Gram. One strict lower witness above the proposed upper threshold is enough to disprove that threshold.

## Actual source attachment and paid errors

Use the two exact RC56 source-input vectors, supported respectively in the even and odd low-eight features. RC58 reconstructs their old nominal complete physical trial source, including the bounded archimedean part, every active signed prime translation, and the signed pole term.

Let t=v*Tv and let e_phys be the correlated actual physical Riesz-error squared upper bound already certified for this vector in RC56. The actual physical source differs from the nominal trial source by at most

\[
\epsilon_v=k_{\rm parity}\sqrt{e_{\rm phys}}+\delta_S\sqrt t.
\]

The complete parity operator norm pays the change from the trial to the actual representative. RC56's delta_S pays the old-to-new constant-center correction and all source kernel approximation slack. Therefore a test of physical squared norm m has pairing allowance sqrt(m) epsilon_v. The actual pairing enclosure is obtained by adding this allowance to the rigorously enclosed nominal pairing.

For a Legendre combination w, the canonical test norm upper bound is

\[
Z_{\rm up}=w^*G_{32,\rm nom}w+\delta_G w^*D_{32}w,
\]

where delta_G is the RC56 corrected metric error budget and D32 is the exact diagonal physical Legendre mass matrix. All tests use degrees at most 31, within the already certified 32-mode metric.

The source-input norm upper bound is the smaller of rho v*Pv, rho=252/257, and v*Mup v from RC57. M_v,up bounds the canonical norm of R_v, **not** the norm of sigma_v. No physical norm is substituted for an actual canonical norm.

## Evaluated detectors and certified results

The validator evaluates all 24 single-degree tests from degrees 8 through 31, using the matching source parity. It then constructs 24 explicit combinations supported in the remaining degrees of each parity. Their exact coefficients are

w_n = midpoint(nominal source pairing with P_n) / physical mass(P_n).

This selects a useful test using the nominal physical mass geometry. Every resulting actual lower bound still pays the full source and metric errors. No floating eigenvector enters the certificate.

The revised source budget is exactly 1/64,000,000 = 1.5625e-8. The following displays approximate exact rational lower endpoints in the certificate.

| Test | Head counts covered | Certified directional residual ratio lower | Ratio to budget |
|---|---|---:|---:|
| Single odd degree 13 | 8–13 | 6.1393466391e-8 | 3.9292 |
| Even combination, degrees 8–30 | 8 | 1.3615625899e-7 | 8.7140 |
| Odd combination, degrees 11–31 | 8–11 | 4.2589802023e-7 | 27.2575 |
| Odd combination, degrees 13–31 | 8–13 | 4.0227780805e-7 | 25.7458 |
| Odd combination, degrees 15–31 | 8–15 | 8.5584814458e-8 | 5.4774 |
| Odd combination, degrees 17–31 | 8–17 | 4.3006869444e-8 | 2.7524 |
| Odd combination, degrees 19–31 | 8–19 | 2.2405979759e-8 | 1.4340 |
| Odd combination, degrees 21–31 | 8–21 | 1.6749744666e-8 | 1.0720 |

Only the displayed parity's degrees occur in each combination. In particular, the last row uses degrees {21,23,25,27,29,31} and remains orthogonal to all native physical features of degrees 0 through 20. Its lower endpoint strictly exceeds the budget, so the source threshold fails even after projection onto a 21-feature consecutive native head. It also fails for every nested smaller head containing the first eight features.

The combination beginning at degree 23 has an inconclusive zero lower bound after the paid errors. It does not certify zero leakage or establish that 22 features satisfy the threshold. The minimum count of 22 is specific to consecutive degree-ordered native heads and this fixed source budget; it is not a universal dimension lower bound for arbitrary selected subspaces or for positivity itself.

## Independent replay

Generation encloses the bounded archimedean pairing using both endpoint logarithms, prime pairings using polynomial primitives on the 15 active translation segments, and pole pairings using exponential Taylor integrals with a separately paid uniform tail.

Replay independently checks:

- reflected same-parity archimedean logarithmic moments;
- prime integration after affine substitution of each segment to [0,1];
- closed exponential primitives for the signed pole pairings;
- exact physical moment orthogonality, hence the canonical-complement identity;
- exact squared square-root allowances and the directional Cauchy–Schwarz lower quotients;
- all fixed single and combined detector coefficients and input certificate hashes.

The replayed nominal pairings must lie inside the stored outward rational enclosures. Both generation and replay pass. From the repository root:

```sh
python scripts/validate_rpb108_rc58_complementary_source_leakage.py > certificates/rpb108_rc58_complementary_source_leakage.json
python scripts/validate_rpb108_rc58_complementary_source_leakage.py --replay certificates/rpb108_rc58_complementary_source_leakage.json
```

## Retained results and next obligation

The actual low-eight floor Q8>=M8/2,900,000 from RC57 is retained. RC58 constructs no enlarged head floor, no exact projection matrix, and no full 1250-feature source Gram. The RC44 complement floor still belongs to the 1250-feature complement, not to the low-eight or 21-feature complements. No whole-aperture positivity, aperture extension, RH, or F4 completion is claimed.

The next frontier is an enlarged actual native projection, beginning at 22 features or beyond, together with its head-floor certificate. Increasing precision in the same low-eight projection cannot meet the revised source threshold: the strict actual lower witnesses already rule it out.
