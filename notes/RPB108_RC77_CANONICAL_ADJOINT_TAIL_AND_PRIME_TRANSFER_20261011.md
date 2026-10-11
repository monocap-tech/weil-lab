# RC77: canonical adjoint tail and projected prime transfer

Date: 2026-10-11. RPB108 route consolidation. Status: PASS.

RC77 certifies a projection-sensitive prime transfer bound by controlling the physical embedding on the actual canonical head complement. It also supplies an analytic proof that the canonical embedding and its adjoint are compact on a fixed finite aperture. RC75's physical noncompactness result therefore does not prevent canonical projected prime tails from decaying.

| Quantity | Certified result |
| --- | --- |
| Actual head rank; existing source input count | 38; 22 |
| Selected frequency cutoff L | 11/5 |
| Complement embedding norm upper tau | less than 0.793924075499 |
| Projected prime norm upper divided by sqrt(rho) | less than 2.284120202957 |
| Unchanged full physical prime norm upper | 11669/4096 = 2.848876953125 |
| Actual rank-38 residual upper relative to actual original 22-input canonical Gram | 377/256 = 1.47265625 |
| Even factor; Young parameter | 377/256; 5/8 |
| Odd factor; Young parameter | 177/128; 5/8 |
| RC76 residual factor | 853/512 = 1.666015625 |
| Fractional decrease of residual upper bound | 99/853, approximately 11.60610% |

All decimal statements round upward. The JSON contains exact rational constants. The required scalar source budget remains uncertified.

## Definitions and exact interface

Let B=11/10. The canonical Hilbert carrier consists of physical vectors supported in [-B,B], with norm squared

||z||_can^2 = integral_R log(e+|xi|) |Fourier(i z)(xi)|^2 dxi,

using Fourier convention exp(-2*pi*i*xi*x). Here i is the physical embedding, with inherited ||i||^2<=rho=252/257. Its adjoint i* maps physical L2 vectors to the canonical carrier.

The actual canonical projection Pi_m projects onto the Riesz images i*p of all physical polynomials of degree less than m. RC70 certifies the actual rank-38 head; no nominal finite trial inverse is substituted for it. For z in the canonical orthogonal complement of this head,

<i z,p>_phys = <z,i*p>_can = 0

for every such polynomial. Thus the physical vector f=i z has exactly vanishing moments through degree m-1. This is the interface used below.

## Moment annihilation controls the embedding tail

For |xi|<=L, subtract the degree-(m-1) Taylor polynomial of exp(-2*pi*i*xi*x) in the integral defining Fourier(f)(xi). All polynomial terms vanish by the moment identities. The real-axis integral Taylor remainder is bounded by |2*pi*xi*x|^m/m!, without an exponential factor. Cauchy-Schwarz in x, followed by integration in xi, gives

integral_{|xi|<=L} |Fourier(f)(xi)|^2 dxi <= theta_m(L) ||f||_phys^2,

where

theta_m(L) = 4 B L (2*pi*B*L)^(2m) / [(m!)^2 (2m+1)^2].

On the complementary band, the canonical weight is at least log(e+L), hence

integral_{|xi|>L} |Fourier(f)(xi)|^2 dxi <= ||z||_can^2 / log(e+L).

Plancherel and theta_m(L)<1 imply

||i z||_phys^2 <= ||z||_can^2 / [(1-theta_m(L)) log(e+L)].

Consequently ||i(I-Pi_m)||<=tau_m(L), where tau_m(L)^2 is the right-hand coefficient. By adjoint duality,

||(I-Pi_m)i*|| = ||i(I-Pi_m)|| <= tau_m(L).

This estimate applies to every physical input of the adjoint, without requiring any frequency assumption on that input or on a translated output. In particular, it remains valid despite aperture restriction and the prime operator's support cutoffs.

## Rank-38 executable certificate

The validator tests seven exact cutoffs: 2, 21/10, 11/5, 9/4, 23/10, 111/50, 56/25. It encloses e and pi by directed intervals, uses pi's upper endpoint in theta, and uses a lower enclosure of log(e_lower+L). The reciprocal coefficient is then an upper bound for the true embedding tail squared. Each tested theta is strictly between zero and one. An exact integer root ceiling yields tau, and the selected bound has tau^2<rho.

Independent replay verifies the e enclosure with a rational Taylor series and geometric tail, pi with Machin arctangent series, and every logarithm with the positive rational atanh series from RC66. It reconstructs theta separately from the exact moments

integral_{-B}^B x^76 dx = 2 B^77/77,

integral_{-L}^L xi^76 dxi = 2 L^77/77.

Root ceilings and every transfer comparison are exact rational checks. Analytic inequalities are supplied in this report, rather than represented as Lean proofs.

## Projected prime transfer and actual source covariance

Keep RC76's complete physical paired-prime bound kappa=11669/4096. The adjoint-tail bound gives

||(I-Pi_38)i* K_pr|| <= tau kappa.

The certificate stores an upward root ceiling beta_pr for tau*kappa/sqrt(rho), approximately 2.2841202029561. This replaces kappa in the previous transfer sum expressed in units of sqrt(rho). RC74's projected arch bound and RC73's parity pole bounds remain available and unchanged. For parity p set

k_p = beta_arch + beta_pr + beta_pole,p.

With RC67's physical Riesz-error Gram E_phys, RC68's source approximation error delta, nominal trial physical Gram T, and nu=1/65536, the projected transfer enclosure divided by rho is

E = (1+nu) D_k E_phys D_k + (1+1/nu) delta^2 T.

The approximation-error term conservatively retains the earlier global embedding bound. Exact outward rounding and rational PSD tests certify E_RC76-E>=0. Retaining RC76's residual Young parameters also proves improvement of the entire residual enclosure in Loewner order.

Using RC71's degree-less-than-38 nominal subtraction residual Gram W, a finite parity Young search selects t_even=t_odd=5/8. Exact PSD comparisons against RC67's actual canonical input Gram lower certify

Gamma_38 <= (377/256) M_22.

Replay independently contracts the nominal trial physical Gram and checks the final relative comparisons after exact physical-coordinate congruence. This scalar improvement is an improvement of the certified upper bound, not a measured change in the actual residual.

## Compactness and the physical noncompactness distinction

For each fixed L, theta_m(L) tends to zero as m tends to infinity. Therefore

limsup_m ||i(I-Pi_m)||^2 <= 1/log(e+L).

Letting L tend to infinity gives ||i(I-Pi_m)|| -> 0. Since i Pi_m is finite rank, i is compact; so is its adjoint i*. This argument concerns the exact polynomial Riesz heads at arbitrary finite m and does not require numerical evaluation of their matrices. Their linear independence follows from injectivity of the polynomial functionals: a supported smooth physical test can detect any nonzero polynomial. The rank-38 numerical estimate uses RC70's certified head.

For every bounded physical operator K, the same reasoning gives ||(I-Pi_m)i*K|| -> 0. In particular, the canonical projected prime operator tails decay even though RC75 proves that the full physical prime operator K_pr is noncompact and its physical polynomial projection tails do not decay uniformly.

These claims concern different maps: K_pr on physical L2, and i*K_pr into the logarithmic canonical carrier. There is no contradiction. Compactness establishes eventual qualitative decay on this fixed aperture; it supplies neither a practical rank sufficient for the source budget nor positivity of an enlarged Weil head.

## Provenance and remaining obligations

Input order: RC76, RC75, RC74, RC73, RC71, RC68, RC67, RC70, RC59, RC43. The certificate records all ten SHA-256 hashes and checks RC76's nine-input provenance against the remaining nine inputs.

- scripts/validate_rpb108_rc77_canonical_adjoint_tail.py
- certificates/rpb108_rc77_canonical_adjoint_tail.json
- notes/RPB108_RC77_CANONICAL_ADJOINT_TAIL_AND_PRIME_TRANSFER_20261011.md

Generation and independent replay passed. Replay command using the default repository paths:

`python scripts/validate_rpb108_rc77_canonical_adjoint_tail.py --replay certificates/rpb108_rc77_canonical_adjoint_tail.json`

The required scalar source budget and any actual rank-38 budget failure remain unproved. The source input scope remains 22, a 38-input covariance remains unevaluated, and no larger Weil head floor is certified. There is no whole-aperture positivity extension, RH, F4, or Lean formalization claim. The next quantitative frontier is to exploit the canonical tail estimate on the specific source errors or to improve the Riesz approximation itself.
