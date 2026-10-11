# RC79: uniform canonical adjoint tail transport

Date: 2026-10-11. RPB108 route consolidation. Status: PASS.

RC79 propagates RC78's actual canonical adjoint tail norm through the nominal polynomial residual, archimedean remainder, signed pole approximation, and source approximation error. Those terms previously retained the global embedding norm. The prime term already used the tail bound and receives no duplicate factor.

| Quantity | Certified result |
| --- | --- |
| Actual target head rank; existing source input count | 38; 22 |
| Tail embedding norm upper tau, inherited from RC78 | less than 0.723521873569 |
| Squared tail/global embedding ratio s=tau^2/rho | approximately 0.533870486880434 |
| Projected arch bound divided by sqrt(rho) | less than 0.481391895666 |
| Projected prime bound divided by sqrt(rho), unchanged | less than 2.081573011452 |
| Actual residual relative to original actual 22-input canonical Gram | 417/512 = 0.814453125 |
| Even factor; Young parameter | 417/512; 5/8 |
| Odd factor; Young parameter | 393/512; 5/8 |
| RC78 residual factor | 5241/4096 = 1.279541015625 |
| Fractional decrease of the certified scalar upper bound | 635/1747, approximately 36.34803% |

The relative upper bound is now below one. This is not the required scalar source budget, which remains uncertified, and it does not establish Weil positivity.

## The uniform tail map

Let B_38=(I-Pi_38)i*, with i* the adjoint of the physical embedding into the logarithmic canonical Hilbert carrier. RC78 proves ||B_38||<=tau, while the inherited global bound is ||i*||<=sqrt(rho), rho=252/257.

The actual head contains i*p for every physical polynomial p of degree less than 38. Thus B_38 p=0 exactly. If F_nom is the nominal physical source and p is RC71's physical polynomial subtraction, then

B_38 F_nom = B_38(F_nom-p).

Let W be RC71's physical Gram upper for the nominal subtraction residual. Applying the uniform operator norm to every linear combination of its 22 columns proves the canonical covariance bound

Gram(B_38 F_nom) <= tau^2 W.

This improves the prior rho W bound in Loewner order. It requires no evaluation of actual projection coefficients and introduces no additional Riesz error for the polynomial subtraction.

## Archimedean and pole transfer

RC78's arch argument constructs a physical polynomial output on the low Fourier band and bounds its physical remainder; the high-band physical output is also bounded. Its total physical remainder norm upper is the stored beta_arch,old, before the final global embedding contraction. Since the polynomial is annihilated by B_38, replace sqrt(rho) by tau in that contraction.

Set s=tau^2/rho and choose an exact upward root ceiling sigma>=sqrt(s), with sigma<1. The new arch bound, expressed in units of sqrt(rho), is

beta_arch,new = sigma beta_arch,old.

RC73's signed pole argument likewise subtracts a physical cosh/sinh Taylor polynomial of degree less than 38 and bounds its physical remainder. The same substitution gives beta_pole,new,p=sigma beta_pole,old,p for both parities.

The prime bound from RC78 already equals an upward enclosure of tau*kappa/sqrt(rho). It is retained unchanged. Applying another sigma to that bound would not follow from this argument and is explicitly excluded in the certificate.

## Approximation error and correlated transfer

Keep RC67's sharp physical Riesz-error Gram E_phys, its nominal 64-dimensional trial coefficients V, physical trial Gram T, and actual canonical input Gram lower M_lo. Keep RC68's physical source approximation operator error delta. The projected approximation-error covariance is bounded by tau^2*delta^2*T, replacing rho*delta^2*T.

For parity p, let k_p=beta_arch,new+beta_prime+beta_pole,new,p and let nu=1/65536. The outward-rounded transfer matrix divided by rho is

E=(1+nu) D_k E_phys D_k+(1+1/nu)*delta^2*s*T.

The canonical transfer upper is E_can=rho E. All components are parity preserving. The error covariance proof retains the same correlated Young estimate as before, with the stronger operator constants.

Exact rational PSD tests certify E_RC78-E>=0 and rho W-tau^2 W>=0. The final residual upper is

A(t)= (1+t_p)*tau^2 W+(1+1/t_p)*rho E.

Using RC78's unchanged Young parameters first proves a whole-matrix Loewner improvement over RC78's residual enclosure. A finite exact search then selects t_even=t_odd=5/8. After outward rounding, parity PSD comparisons against M_lo establish

Gamma_38 <= (417/512) M_22.

The decrease compares certified scalar upper bounds, not the actual residual values.

## Validation and provenance

Generation assembles the trial Gram by matrix contraction and the final covariance in units of rho. Independent replay constructs T by direct physical mass sums, forms the transfer by diagonal congruence, and assembles the residual directly from tau^2 W and E_can. It independently verifies the final PSD comparisons after inverse Chebyshev-to-Legendre congruence. The sigma root ceiling, positivity, provenance, and unchanged-parameter Loewner comparisons are exact rational checks.

Input order: RC78, RC71, RC68, RC67, RC70, RC59, RC73. All seven SHA-256 hashes are recorded. RC78's relevant inherited input hashes are checked against all six remaining inputs. RC78 supplies the previously replayed analytic tail certificate; RC79 does not introduce a new Fourier estimate.

- scripts/validate_rpb108_rc79_uniform_adjoint_tail_transport.py
- certificates/rpb108_rc79_uniform_adjoint_tail_transport.json
- notes/RPB108_RC79_UNIFORM_ADJOINT_TAIL_TRANSPORT_20261011.md

Generation and independent replay passed. Replay with default repository input paths:

`python scripts/validate_rpb108_rc79_uniform_adjoint_tail_transport.py --replay certificates/rpb108_rc79_uniform_adjoint_tail_transport.json`

The source input scope remains 22 and the actual target projection rank remains 38. The required scalar source budget, any actual rank-38 budget failure, a 38-input source covariance, and a larger Weil head floor remain unresolved. No whole-aperture positivity extension, RH, F4, or Lean formalization is claimed. Further work must tighten the actual source residual or its Riesz approximation enough for the source budget; crossing the value one does not discharge that obligation.
