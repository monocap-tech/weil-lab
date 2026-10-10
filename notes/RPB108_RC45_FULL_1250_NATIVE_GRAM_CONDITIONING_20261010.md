# RPB108 RC45 — conditioning of the entire 1250-feature native Gram

2026-10-10. Parent RC44: `d5c78000555439983889176e766915becf1bab99`.
Only `research/rpb108-route-consolidation` is written.

## Result

For the entire RC44 native head, let M be the actual canonical Riesz Gram
and P_phys the exact physical Chebyshev polynomial Gram. A whole-space
analytic argument with exact rational budgets proves

    (1/30)P_phys <=M <=(252/257)P_phys.

Thus the exact physical Gram preconditioner gives

    condition(P_phys^(-1/2) M P_phys^(-1/2))
       <=7560/257 <29.417.

This covers all **1250** native features, not only the previously certified
eight-feature block. In raw Chebyshev coefficients it additionally proves

    (11/750000)I <=M <=(4356/1285)I,
    condition(M)<=59400000/257 <231129.

The actual full Gram entries and projection are not evaluated. This
resolves an explicit full-head conditioning obligation and supplies a
coarse inverse envelope, without certifying the original Weil head floor
or combined source residual. No new aperture positivity is claimed.

## Definitions and exact physical Gram

The carrier, B=11/10, Fourier convention exp(-2pi i xi x), and logarithmic
weight w(xi)=log(e+|xi|) are unchanged. RC44's feature count is n=1250.
Let q_j(x)=T_j(x/B), and let r_j be the canonical Riesz representative of
ell_j(h)=integral q_j(x)i h(x)dx. Define

    R a=sum_(j=0)^(n-1) a_j r_j,
    M=R^*R,
    (P_phys)_ij=integral_(-B)^B q_i(x)q_j(x)dx.

These two Grams are distinct. The physical Gram has exact rational entries

    (P_phys)_ij=0                         if i-j is odd,
    (P_phys)_ij=B[1/(1-(i+j)^2)+1/(1-(i-j)^2)] otherwise.

This follows from T_i T_j=(T_(i+j)+T_|i-j|)/2 and
integral_(-1)^1 T_k(t)dt=2/(1-k^2) for even k, zero for odd k. No zero
denominator occurs in the same-parity formula. The validator exposes this
entry generator for the entire matrix; no dense file is required.

The physical formula agrees exactly with RC39's full eight-feature
physical block. Replay independently checks 136 entries through degree
15 by Chebyshev recurrence in the power basis and direct integration.

## Upper canonical energy for every physical polynomial

Let p be any complex polynomial of degree below n on (-B,B), with zero
extension outside. Use the normalized Legendre basis in physical L2.
The endpoint Christoffel bound and |P_j(t)|<=1 give

    |p(B)|, |p(-B)| <= n/sqrt(2B) ||p||_2.

The exact derivative identity

    P_j'(t)=sum_(k<j, j-k odd) (2k+1)P_k(t)

implies integral_(-1)^1 |P_j'|^2=j(j+1). The squared norms of the physical
derivatives of all normalized basis vectors therefore sum to

    sum_(j=0)^(n-1) j(j+1)(2j+1)/(2B^2)
       =n^2(n^2-1)/(4B^2).

Cauchy-Schwarz on the coefficient expansion gives

    ||p'||_2 <=n sqrt(n^2-1)/(2B) ||p||_2,
    ||p'||_1 <=n^2/sqrt(2B) ||p||_2.

Integration by parts includes both endpoint jumps of the zero extension:

    |Fourier(p)(xi)|
      <=[|p(B)|+|p(-B)|+||p'||_1]/(2pi|xi|)
      <=(n^2+2n)/(sqrt(2B)2pi|xi|) ||p||_2.

No endpoint-zero constraint is imposed. This tail estimate also pays the
finite logarithmic Fourier energy of the supported polynomials, whose
membership in the canonical carrier is inherited from the trial framework.

Set T=n^4 and A2=(n^2+2n)^2/(2B). Below T, Plancherel gives an energy
bound log(e+T)||p||_2^2. Above T, log(e+x)<=log x+3/x yields

    tail_energy/||p||_2^2
      <=A2/(2pi^2)[(log T+1)/T+3/(2T^2)].

A fresh positive exponential partial sum proves log1250<36/5, so
log T<144/5. Using pi>3 and e<3, the entirely rational total budget is

    C_budget=144/5+3/T
       +A2/18[(144/5+1)/T+3/(2T^2)]
       =29.554935259799223... <30.

Hence every polynomial p of degree below 1250 satisfies

    ||p||_D^2 <=30 ||p||_2^2.

This is an all-coefficient bound, including complex coefficients. Finite
degree samples are not its proof: the Legendre identities and closed
trace formula establish the uniform estimate.

## Transfer to the actual canonical Riesz Gram

For q=sum a_j q_j, the corresponding combined moment functional has
canonical Riesz representative R a. Testing that functional on the same
physical polynomial q gives, by Riesz duality,

    ||R a||_D^2
      >=||q||_2^4/||q||_D^2
      >=(1/30)||q||_2^2.

Thus M>=(1/30)P_phys. Conversely RC32's inclusion norm
||i||^2<=rho=252/257 gives ||i^*q||_D^2<=rho||q||_2^2, hence
M<=rho P_phys. These bounds attach to the actual Riesz representatives,
not a polynomial trial Gram substituted for M.

Congruence by P_phys^(-1/2) immediately gives the claimed preconditioned
condition bound 30rho. This certifies conditioning in a specified exact
metric; it does not evaluate the canonical matrix or propose its entries.

## Explicit raw-coordinate bounds

For p(t)=sum a_j T_j(t), Chebyshev orthogonality gives

    integral_(-1)^1 |p(t)|^2/sqrt(1-t^2)dt
      =pi |a_0|^2+(pi/2)sum_(j>=1)|a_j|^2.

The weight is at least one, so P_phys<=pi B I<(22/7)B I. For a lower
bound, choose delta=1/(2n^2). On the interior the weighted integral is
at most delta^(-1/2) times the unweighted integral. On the two endpoint
intervals its weight integral is at most 4sqrt(delta). The Christoffel
supremum bound |p|^2<=n^2/2 times its unweighted squared norm therefore
gives

    weighted_norm_squared <=2sqrt(2)n unweighted_norm_squared.

Combining this with the coefficient formula, and pi>3>2sqrt2, proves

    P_phys >=B/(2n) I.

Applying the canonical bounds gives the stated Euclidean eigenvalue and
condition estimates. They remain conservative; no actual eigenvalue
distribution or optimal condition number is computed.

## Coarse full-head inverse and safe source interface

Order reversal under inversion supplies the whole actual inverse envelope

    (257/252)P_phys^(-1) <=M^(-1)<=30 P_phys^(-1).

P_phys is specified by the exact entry formula and is positive definite.
Its full inverse is not computed here. The envelope is much coarser than
RC40's low-eight inverse enclosure; that tighter principal-block result
remains valid on its stated scope.

For later actual source matrices V_src=R^*sigma and U=sigma^*sigma, the
full-head residual Gram Gamma=U-V_src^*M^(-1)V_src consequently obeys

    U-30 V_src^*P_phys^(-1)V_src
       <=Gamma
       <=U-(257/252)V_src^*P_phys^(-1)V_src.

No actual full-head U or V_src is supplied. This is a lawful inverse-error
transport interface, not a certification of Gamma<=M/90000. The complete
archimedean/prime/pole correlations and original actual head inequality
A>=M/4000 still require certification.

## Validation and remaining work

Generation passes 74 exact rational checks: low-block custody, derivative
identities and norms, the full degree-1250 trace and endpoint sums,
logarithmic/frequency budgets, metric constants, and condition/inverse
ratios. Independent replay verifies physical Gram entries by direct power
integration and rechecks the whole budgets and input hashes.

Run:

    python scripts/validate_rpb108_rc45_full_head_conditioning.py
    python scripts/validate_rpb108_rc45_full_head_conditioning.py --replay certificates/rpb108_rc45_full_head_conditioning.json

Generation and replay pass. The infinite Fourier integrals, Riesz duality,
and all-degree polynomial bounds are analytic proofs above, not Lean
formalization. The elementary pi bounds and Plancherel convention are
inherited. This pass uses no numerical special-function evaluation.

The full native Gram is now quantitatively conditioned, but its entries,
validated high-precision inverse/solves, full canonical projector, original
Weil head floor, and complete mixed source residual remain unevaluated.
RC44's whole-complement floor is unchanged. Historical files and other
branches are preserved; no positivity at 1.10, RH/F4, or Lean closure is
claimed.
