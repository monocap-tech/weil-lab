# RC78: Legendre Fourier transfer

Date: 2026-10-11. RPB108 route consolidation. Status: PASS.

RC78 replaces the real-axis Taylor remainder by the orthogonal Legendre remainder for Fourier plane waves. The same estimate tightens RC77's canonical adjoint tail and RC74's projected archimedean transfer. Both improvements propagate into the existing actual rank-38 residual for the existing 22 source inputs.

| Quantity | Certified result |
| --- | --- |
| Actual head rank; source input count | 38; 22 |
| Canonical complement embedding norm upper | less than 0.723521873569 |
| Selected embedding cutoff L | 41/10 |
| Projected prime norm upper divided by sqrt(rho) | less than 2.081573011452 |
| Projected arch norm upper divided by sqrt(rho) | less than 0.658841303879 |
| Selected arch cutoff L | 79/20 |
| Actual residual relative to actual original canonical input Gram | 5241/4096 = 1.279541015625 |
| Even factor; Young parameter | 5241/4096; 1/2 |
| Odd factor; Young parameter | 611/512; 1/2 |
| RC77 residual factor | 377/256 = 1.47265625 |
| Fractional decrease of certified scalar upper bound | 791/6032, approximately 13.11340% |

Exact rationals are stored in the JSON. The source budget remains uncertified; this decrease is a comparison of upper bounds, not a measurement of actual leakage.

## Legendre remainder bound

Use B=11/10, Fourier convention exp(-2*pi*i*xi*x), canonical weight w(xi)=log(e+|xi|), and rho=252/257. Let P_n denote the ordinary Legendre polynomial on [-1,1], with squared norm 2/(2n+1). Let D_n=(2n+1)!! and z=2*pi*B*xi.

Rodrigues' formula and n integrations by parts give

integral_{-1}^1 P_n(t) exp(i*z*t) dt

= (i*z)^n/(2^n*n!) integral_{-1}^1 (1-t^2)^n exp(i*z*t) dt.

All boundary terms vanish. Since z is real and

integral_{-1}^1 (1-t^2)^n dt = 2^(n+1)*n!/D_n,

the coefficient integral has modulus at most 2*|z|^n/D_n. Orthogonal Legendre expansion and Parseval therefore bound the physical squared norm of the degree-less-than-m plane-wave remainder by

2*B sum_{n>=m} (2n+1) |2*pi*B*xi|^(2n)/D_n^2.

Integrating over |xi|<=L cancels the factor 2n+1. With Z=2*pi*B*L,

integral_{-L}^L ||plane-wave remainder||_phys^2 dxi

<= 4*B*L sum_{n>=m} Z^(2n)/D_n^2.

The ratio of successive integrated terms is Z^2/(2n+3)^2. If r=Z^2/(2m+3)^2<1, the sum is at most

theta_leg(m,L) = 4*B*L*Z^(2m) / [D_m^2*(1-r)].

The completeness and norm identities for Legendre polynomials justify the orthogonal expansion in physical L2. All sum-integral interchanges above have nonnegative terms. This derivation bounds the entire infinite tail and does not truncate it numerically.

## Canonical adjoint tail

RC77 established that z in the actual canonical head complement satisfies <i z,p>_phys=0 for every physical polynomial p of degree less than m. Substitute the Legendre projection of each Fourier plane wave in this pairing. Its polynomial part vanishes, and Cauchy-Schwarz gives

integral_{|xi|<=L} |Fourier(i z)(xi)|^2 dxi <= theta_leg(m,L) ||i z||_phys^2.

The high-frequency canonical weight gives

||i z||_phys^2 <= ||z||_can^2 / [(1-theta_leg(m,L))*log(e+L)]

whenever theta_leg<1. Thus the same coefficient bounds ||i(I-Pi_m)||^2 and ||(I-Pi_m)i*||^2. This is a property of the actual canonical projection, rather than the nominal trial inverse.

For m=38, the exact cutoff search selects L=41/10, with an upward root ceiling tau less than 0.723521873569. RC76's full physical prime norm remains kappa=11669/4096. Consequently

||(I-Pi_38)i*K_pr|| <= tau*kappa.

An upward root ceiling beta_pr for tau*kappa/sqrt(rho) is stored in the certificate. The physical prime operator itself remains noncompact; this bound concerns the composition into the canonical carrier.

## Projected archimedean transfer

The established full physical arch remainder multiplier bound is K=643/100. RC66's high-frequency bound is

|m_arch(xi)| <= log(1+e/|xi|)+1/(2*|xi|).

For |xi|<=L, subtract the Legendre polynomial projection of the output plane wave in the inverse Fourier integral. Each resulting physical polynomial has degree less than 38, so its Riesz image belongs exactly to the actual head and is annihilated by I-Pi_38. The low-frequency remainder operator has Hilbert-Schmidt norm at most K*sqrt(theta_leg(38,L)).

For the high-frequency input, the physical multiplier norm is at most h_L=log(1+e/L)+1/(2L). The low and high frequency input pieces are orthogonal. The triangle inequality followed by scalar Cauchy-Schwarz therefore gives

||(I-Pi_38)i*K_arch|| <= sqrt(rho)*sqrt(K^2*theta_leg(38,L)+h_L^2).

No orthogonality of the outputs is assumed. The selected cutoff L=79/20 yields beta_arch less than 0.658841303879 in units of sqrt(rho), improving RC74's 1.063327072317 bound. RC77 had retained that RC74 arch bound unchanged.

## Exact validation and source propagation

Nine rational cutoffs are tested: 7/2, 15/4, 19/5, 77/20, 39/10, 79/20, 4, 81/20, 41/10. Generation uses a product for D_38, directed interval enclosures for e, pi and logarithms, and exact rational tail sums and root ceilings.

Independent replay verifies e by a rational Taylor series with geometric tail, pi by Machin arctangent bounds, and logarithms by the positive atanh series. It checks the separate factorial identity D_m=(2m+1)!/(2^m*m!), computes the Rodrigues moment as the exact finite sum

sum_{j=0}^m 2*(-1)^j*binom(m,j)/(2j+1),

and reconstructs the integrated first Legendre term from the physical coefficient normalization and exact frequency moment. It verifies the geometric closure identity and the embedding and arch root conditions.

Keep RC73's projected parity pole bounds, RC67's sharp physical Riesz-error Gram E_phys and actual canonical input Gram lower, RC68's operator approximation error delta, nominal trial physical Gram T, and RC71's degree-less-than-38 nominal subtraction residual Gram W. Let k_p=beta_arch+beta_pr+beta_pole,p and nu=1/65536. The projected transfer enclosure divided by rho is the outward-rounded matrix

E=(1+nu) D_k E_phys D_k+(1+1/nu)*delta^2*T.

Exact PSD tests prove E_RC77-E>=0. At RC77's unchanged residual Young parameters, the entire residual enclosure improves in Loewner order. A finite exact parity search selects t_even=t_odd=1/2 and certifies

Gamma_38 <= (5241/4096) M_22.

Replay also reconstructs T by direct mass contraction and verifies the final comparisons after exact physical-coordinate congruence. Generation and independent replay passed. These are executable rational certificates accompanied by the analytic proof above, not Lean formalizations.

## Provenance and remaining frontier

Inputs in order: RC77, RC76, RC75, RC74, RC73, RC71, RC68, RC67, RC70, RC59, RC43. SHA-256 hashes bind all eleven inputs. RC77's ten-input provenance is checked against the remaining ten inputs.

- scripts/validate_rpb108_rc78_legendre_fourier_transfer.py
- certificates/rpb108_rc78_legendre_fourier_transfer.json
- notes/RPB108_RC78_LEGENDRE_FOURIER_TRANSFER_20261011.md

Independent replay with the default repository input paths:

`python scripts/validate_rpb108_rc78_legendre_fourier_transfer.py --replay certificates/rpb108_rc78_legendre_fourier_transfer.json`

The actual canonical target head has rank 38 and the input covariance still has 22 source features. The required scalar source budget, any actual rank-38 budget failure, a 38-input source covariance, and a larger Weil floor remain unresolved. No whole-aperture positivity extension, RH, F4, or Lean formalization is claimed. Further quantitative work must control the particular source residuals or improve the Riesz approximation; qualitative canonical compactness alone does not supply a sufficient practical rank.
