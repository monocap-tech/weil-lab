# EF31 — Exact Chebyshev generator of original SI10 even source/pole kernel

2026-10-31. Canonical W-EVEN-FORM OPEN. Parent EF30 PR #425, head 978df86e95ba0f719ea394e6e810aa299f5c76bf. Accepted exact original rank470/nullity1: Actions #41236300352 and tightened #41236609475 SUCCESS. Odd W-ODD-NEG is paused/OPEN; whole Weil/RH OPEN.

## Exact original source/pole constraints

Keep the **unchanged original** SI10 centers c_j, source orders p_j (107 clusters; sum p_j=469), and the original 471 EF28 disjoint even bell pairs x_l=l/512, 1<=l<=471. EF30 proved the full physical 470×471 source/pole moment matrix Htilde has exactly the sampled rowspace and kernel, with no numerical approximation. EF29 preserved the true original signed 471-vector gtilde modulo an actual source row.

Define theta_j=2*pi*c_j/512, z_j=cos(theta_j), t=cosh(1/1024)>1, and T_l the first Chebyshev polynomial (T_l(cos theta)=cos(l theta)). EF30 checks that the 214 conjugate sampled phase roots are distinct and not self-conjugate, hence the 107 z_j are distinct, and sin(theta_j)!=0. The original monic algebraic polynomial

P(z) = product_j (z-z_j)^(p_j), deg P=469

encodes all **actual** sampled source jets. A coefficient vector w=(w_1,...,w_471) corresponds to R_w(z)=sum_(l=1)^471 w_l T_l(z). For original k even/odd source rows, the constraints sum_l w_l l^k cos(theta_j l)=0 or sum_l w_l l^k sin(theta_j l)=0 are, up to nonzero scalar factors, d_theta^k R_w(cos theta)|_(theta_j)=0 for 0<=k<p_j. Since sin(theta_j)!=0, these are equivalent to P|R_w. The TRUE positive even-pole row is exactly R_w(t)=sum_l w_l cosh(l/1024)=0. Absence of the bell index l=0 means the T_0 coefficient of R_w is zero.

Define L(f)=(1/pi)*integral_(0)^pi f(cos theta)dtheta. Its exact monomial moments are L(z^(2m))=binom(2m,m)/4^m, L(z^(2m+1))=0. L(f) is exactly the Chebyshev T_0 coefficient. Thus every exact original kernel vector is equivalent to

R(z)=P(z)(z-t)(a z+b), deg R<=471, L(R)=0.

## Explicit exact nonzero generator

Set U(z)=P(z)(z-t), A=L(U), B=L(zU), and R_*(z)=U(z)(B-A*z). This polynomial has degree <=471, satisfies P|R_*, R_*(t)=0, and L(R_*)=B*A-A*B=0. Write its Chebyshev expansion as R_*(z)=sum_(l=1)^471 w_{*,l}T_l(z).

The pair (A,B) cannot be (0,0): otherwise U and zU would be TWO linearly independent true source/pole-neutral polynomials of degree <=471, each with zero T_0 coefficient, contradicting EF30's **certified original rank470/nullity1**. Hence w_* != 0 and span(w_*)=ker(Htilde). This is the exact original one-dimensional kernel direction, without 470×470 Gram inversion or floating SVD. It is SYMBOLIC, not an outward-enclosed numerical orientation.

In particular, **there is no nonzero algebraic-coordinate exact pole-neutral w**: such a vector would make e^(1/1024) satisfy a nonzero Laurent polynomial with algebraic coefficients sum_l w_l(X^l+X^(-l)), contradicting Hermite–Lindemann. Rational pole-neutral vectors are necessarily approximations requiring an explicit pole-error budget.

## Signed residual acceptance interface — still OPEN

Original EF28 bell Gram is d I with d=231/8388608. The true original EF29 source mixed residual is EXACTLY

delta = abs(sum_l gtilde_l*w_{*,l}) / sqrt(sum_l w_{*,l}^2).

EF29's subtraction of a_arch(c0) times an ACTUAL source row does not affect this contraction. The sufficient negative-even witness gate remains delta^2 > 34*d*(A_source+2*u^2), where A_source=q0(e,e), u=<cosh(x/2),e>, and e is the native first SI10 even source. A_source must NOT be confused with A=L(U) above.

A future certified approximate unit kernel vhat with ||v-vhat||<=eta, ghat with ||g-ghat||<=epsilon, would yield
delta >= max(0, abs(<ghat,vhat>)-epsilon*(1+eta)-||ghat||*eta).
EF29's 100-term per-coordinate omitted arch Laplace tail <1e-19 contributes to epsilon less than sqrt(471)*1e-19 <2.2e-18 **by itself**; add outward finite source intervals and kernel errors separately. Exact symbolic existence by itself is neither a positive delta lower nor a condition-number estimate. The original A_arch diagonal is uncomputed; neither corrected full even Schur sign nor RH is classified.

**Standing:** exact polynomial kernel parameterization deduced from accepted original EF30 rank and exact original EF30 moment-row equivalence. Regression checks original source inventory and separate rational toy Chebyshev algebra only; no original numeric kernel or signed contraction is asserted. Independent analytic digamma/domain audit remains required.

**EF32 next:** compute an outward-enclosed normalized original Chebyshev kernel or a mathematically equivalent quotient, contract against ALL 471 actual EF29 signed outward intervals from artifact #13054987778, enclose A_arch separately if the residual is decisive, and compare to full true even threshold. If source conditioning/cancellation prevents this, produce quantified finite-grid METHOD STOP, not a claim about even positivity or RH. No main merge.
