# RPB108: certified finite coercivity with the first actual prime

## Terminology and theorem

**Physical coercivity on E** means Q(f) >= tau ||f||_(L2)^2 for every f in the specified trial span E, with tau>0. **Shifted pivot certificate** means positive interval Schur pivots for the matrix Q_E-tau G_E, where G_E is the physical L2 Gram matrix. Neither term asserts a bound on the entire logarithmic carrier.

At a=1/2 let E be the complex span of P_n(x/a) times the indicator of [-a,a], n=0,...,7. The actual native Weil form satisfies

Q(f) > (1/200000) ||f||_(L2)^2 for every nonzero f in E.

This is an analytic finite theorem backed by exact rational interval execution. It includes the actual prime-2 contribution and the actual same-vector pole moments. It uses the physical matrix identity from `REFLECTED_PACKET_BRIDGE_108_EXACT_PHYSICAL_MATRIX_FORMULA_20261005.md`, with the rational enclosure method from `REFLECTED_PACKET_BRIDGE_108_RATIONAL_FINITE_CERTIFICATE_20261005.md`.

## Scaled archimedean enclosure

Set L=4a=2 and y=t/L, so 0<=y<=1. Write C_ij(Ly/2)=sum c_k y^k, with c_0=delta_ij=2a/(2i+1) for i=j and zero otherwise. The integral in the physical formula becomes integral A(y)B(Ly) dy, where

A(y)=[exp(-Ly)delta_ij-exp(-Ly/4)C_ij(Ly/2)]/y,
B(z)=z/(1-exp(-z)).

Use N=60 for the exponentials and K=40 Bernoulli pairs. Retain the full product with the exact correlation polynomial before dividing by y. Its constant vanishes exactly. Put Csum=sum |c_k|. The uniform error bounds are

|B(Ly)-B_K(Ly)| <= 4*(L/6)^(2K+2)/(1-(L/6)^2),
|B_K(Ly)| < 3,
|A-A_N| <= 9*L^(N+1)/(N+1)! * [delta_ij+Csum/4^(N+1)],
|A| <= (3L/4)delta_ij + sum_(k>=1)|c_k|.

The first two follow from the Bernoulli coefficient bound proved in the prior certificate. The exponential estimate uses exp(2)<9. The product error is bounded by 3 times the A remainder plus the displayed A bound times the B remainder. Polynomial integration is exact rational arithmetic. Pole moment Taylor errors use exp(a/2)<2, giving radius 4a*sum |coefficients(P_i)|*(a/2)^(N+1)/(N+1)!.

The constant is -gamma-log pi-log(1-exp(-L)). The previous rational Machin, logarithm, and gamma enclosures apply. Every interval operation rounds outward to the rational grid with spacing 10^(-50).

## Exact first-prime custody

Rational logarithm bounds establish log 2 < 1 < log 3. Thus 2 is the only integer prime power with log n <= 2a=1. Its native entry is

-[2 log 2/sqrt(2)] C_ij(log 2).

The log enclosure is inserted into the same correlation polynomial at y=log 2/(2a). Horner interval evaluation encloses its value. Sqrt(2) is enclosed by integer square-root arithmetic at the rational grid scale; interval division encloses the coefficient. No floating prime coefficient is used. Opposite-parity correlation and pole entries vanish exactly.

## Shifted matrix proof and validation

In this unnormalized basis G_E is diagonal with entries 2a/(2i+1). Subtract tau G_E with tau=1/200000 from the entry enclosures. Exact interval Schur elimination returns eight positive rational pivot lower endpoints, recorded in `notes/data/RPB108_RATIONAL_PRIME_CERTIFICATE_20261005.json`. Their decimal displays are approximately

0.08800961, 0.09076131, 0.003631918, 0.01924299,
0.004797053, 0.001533913, 0.000001178281, 0.03955597.

Positive Schur pivots prove Q_E-tau G_E positive definite over the real and complex scalars, establishing the theorem. These pivots are not eigenvalue bounds. The rationally checked maximum entry width is below 2*10^(-29).

Run `python scripts/certify_native_legendre_small_window.py --half`. The default a=1/4 run reproduces the previously recorded JSON exactly. A deliberately negative diagonal is rejected, and unaudited apertures are rejected. Normalized entry midpoints agree with the physical floating pilot to within 4*10^(-14); this comparison is diagnostic only. Lean source and its certified checkpoint are unchanged.

## What this buys for the positive carrier

Apply the established same-vector identity Q(f)=||S_+f||^2-||S_Bf||^2 on E. The theorem gives ker(S_+|E)={0} and ||S_Bf||<||S_+f|| for nonzero f in E. Therefore

T_E(S_+f)=S_Bf

is well-defined on S_+(E), and is a strict contraction there. Its definition retains the same f throughout. If M_E=||S_+|E|| with the physical L2 norm on E, then

||T_E||^2 <= 1-tau/M_E^2 < 1.

This is a finite-range factorization; no numerical value of M_E is claimed. It cannot extend to the full positive completion without a compatible uniform estimate on a dense exhaustion or another independent global argument. Nor does finite trial-space positivity bound the uncontrolled complement. Thus this theorem supplies concrete actual finite input but does not prove ker S_+ subset ker S_B or S_B* S_B <= S_+* S_+ on all D. The independent endpoint-null Gaussian upper estimate/endpoint exclusion remains absent. F4 entry and FULL TRANSPORT CLOSED remain open; there is no actual negative witness or exact endpoint null claimed here.
