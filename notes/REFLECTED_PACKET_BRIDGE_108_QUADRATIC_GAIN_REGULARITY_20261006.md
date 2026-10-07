# RPB108: quadratic finite-response gain is exactly global H1 regularity

Date: 2026-10-06. Recovered live source: `f176ca18a0adc15e1bb2441e2cb17b855147d45e`.
Definitions: [registered terminology](../docs/TERMINOLOGY_RPB108_QUADRATIC_GAIN_REGULARITY.md).
Lane: global/F4. The independent whole-domain aperture frontier remains 23/25.

## Exact criterion

Fix a hypothetical actual nonnegative null window c and its finite-dimensional full native kernel K_c. Use the fresh actual finite selection separating K_c, and shrink b>c so that G_b is coercive and there are no new prime thresholds in (2c,2b]. This is possible because the prime-power thresholds are locally discrete. Retain the right cutoff, including any equality threshold at c. In the fixed logarithmic carrier use the physical support inclusions and the compensators of FRESH_FIXED_RIGHT_PACKET and COMPENSATOR_RESIDUAL.

For h in K_c, u=-R_c h, t=c+s and r_s=A_t Ih, define
\[
e_s(h)=\langle r_s,G_t^{-1}r_s\rangle
=\|(C_t-C_c)u\|^2
=\langle u,[\Lambda(t)-\Lambda(c)]u\rangle.
\tag{1}
\]
For nonzero h this is strictly positive for every sufficiently small s>0 by the established strict-margin obstruction. The vector Ih is unchanged; the compensator and the test carrier change. The following equivalence is new:
\[
\boxed{h\in H^1(\mathbb R)
\quad\Longleftrightarrow\quad e_s(h)=O(s^2)
\quad\Longleftrightarrow\quad e_s(h)=o(s^2).}
\tag{2}
\]
This is an analytic conditional theorem, not an established arithmetic bound on e_s, and not Lean certified.

## Quadratic gain implies a derivative

Put z_s=tau_s h-Ih, where tau_s h(x)=h(x-s). Both vectors lie in D_t. Actual simultaneous translation invariance and unchanged-support custody give Q_t(tau_s h)=Q_t(Ih)=0. The fixed right cutoff agrees with the native cutoff throughout this small interval. With the flux orientation of EXACT_TRANSLATION_BOUNDARY_FLUX,
\[
F_h(s)=\operatorname{Re}Q_t(z_s,Ih)
=-D_m(s)+(\cosh(s/2)-1)P_0,
\qquad Q_t(z_s)=-2F_h(s).
\tag{3}
\]
Here P_0=2 Re(conjugate(M_-(h)) M_+(h)) is the scalar Hermitian pole diagonal, distinct from the physical residual function. Equality-threshold prime translations remain in m. No enlarged mixed-null equation is used.

Every retained selected negative row is an actual exponential profile on the fixed compact support. Changing variables in its translated pairing, and using its bounded derivative on [-b,b], gives a finite constant B_R with
\[
d_s=\|R_t z_s\|^2\le B_R^2s^2\|h\|_2^2.
\tag{4}
\]
This differentiates the finite observation profiles, not h. Effective Cauchy-Schwarz, using r_s as the full mixed residual and (1) as its squared dual norm, gives
\[
|F_h(s)|^2\le e_s(h)\,g_t(z_s,z_s)
=e_s(h)(-2F_h(s)+d_s).
\tag{5}
\]
When F_h(s)<0, solving this scalar quadratic yields
\[
(-F_h(s))_+\le e_s+\sqrt{e_s^2+e_s d_s}
\le2e_s+\sqrt{e_s d_s}.
\tag{6}
\]
The same bound is trivial when F_h(s)>=0. The established actual multiplier envelope and signed flux identity give, for w(xi)=log(e+|xi|),
\[
D_w(s)=\int w(\xi)(1-\cos(2\pi\xi s))|\widehat h(\xi)|^2d\xi
\le4e_s+2\sqrt{e_s d_s}+2Z_c s^2\|h\|_2^2.
\tag{7}
\]
Thus e_s=O(s^2) implies D_w(s)=O(s^2). Fatou applied along any sequence s decreasing to zero, with
(1-cos(2 pi xi s))/s^2 tending to 2 pi^2 xi^2, proves
\[
\int \xi^2w(\xi)|\widehat h(\xi)|^2d\xi<\infty.
\tag{8}
\]
In particular h has a global L2 derivative, with the zero extension understood globally. This argument needs a lower control on the signed flux; the already available one-sided upper bound on F is insufficient. It uses no inverse-boundary-moment injectivity.

## A derivative implies strictly smaller than quadratic gain

Suppose h is globally H1. The supported-L2 promotion theorem proves g=h' belongs to K_c, including its canonical logarithmic domain, and m_c(D)g is globally L2. Define the physical full residual function
\[
q_h=m_c(D)h+M_-(h)e^{x/2}+M_+(h)e^{-x/2}.
\]
It is locally L2 and vanishes on (-c,c). Global H1 of the supported h supplies zero endpoint traces. Integration by parts gives M_-(g)=M_-(h)/2 and M_+(g)=-M_+(h)/2. Consequently q_h'=q_g in distributions on every compact interval. There is no endpoint delta: both core distributions have the global L2 representatives supplied by promotion. Hence q_h is locally H1 across both endpoints, and its continuous representative has q_h(c)=q_h(-c)=0.

For the exterior collars Omega_s=(c,c+s) union (-c-s,-c), the one-dimensional integral Cauchy-Schwarz estimate gives
\[
\|q_h\|_{L^2(\Omega_s)}^2
\le\frac{s^2}{2}\|q_g\|_{L^2(\Omega_s)}^2=o(s^2).
\tag{9}
\]
Indeed |q_h(c+x)|^2<=x integral_0^x |q_g(c+y)|^2dy, and integration bounds the inner coefficient by s^2/2; the other edge is identical. Absolute continuity of locally L2 mass supplies the little-o.

Coercivity of G_b compresses to a uniform g_t(v,v)>=beta ||v||_log^2>=beta ||v||_2^2 on this interval. No new prime activates, so the full enlarged residual against v in D_t is exactly the ordinary pairing of v with q_h on Omega_s. Its squared dual effective norm therefore satisfies
\[
e_s(h)\le\beta^{-1}\|q_h\|_{L^2(\Omega_s)}^2=o(s^2).
\tag{10}
\]
Equations (7)-(10) prove (2). Analytic constants may depend on the fixed window, selection and h; no uniform arithmetic rate has been obtained.

## Finite-response regularity flag and the remaining theorem

Let E=ker D(c) and B_c=-G_c^{-1}R_c*:E to K_c be the established isomorphism. Then
\[
E_1=\{u\in E:\langle u,[\Lambda(c+s)-\Lambda(c)]u\rangle=O(s^2)\}
=B_c^{-1}(K_c\cap H^1(\mathbb R)).
\tag{11}
\]
The prior finite-source regularity flag gives dim E_1<=max(dim E-1,0). For each u outside E_1,
\[
\limsup_{s\downarrow0}
\frac{\langle u,[\Lambda(c+s)-\Lambda(c)]u\rangle}{s^2}=\infty.
\tag{12}
\]
This is a limsup statement; it asserts neither a limit nor a positive linear lower bound. In dimension one it applies to every nonzero endpoint coefficient.

The smallest sufficient global theorem exposed by this pass is the actual arithmetic estimate, at every hypothetical nonnegative contact,
\[
\Pi_E[\Lambda(c+s)-\Lambda(c)]\Pi_E\le C s^2 I_E
\quad(0<s<s_0).
\tag{13}
\]
If (13) were proved, (2) would put all of K_c in global H1. Automatic derivative promotion would make differentiation an endomorphism of this finite-dimensional kernel, contradicted by Fourier-polynomial independence. Thus it would exclude every finite contact and complete the global endpoint leg. Equivalently, it suffices to prove a right Lipschitz estimate for (C_t-C_c) restricted to E in the fixed positive carrier.

**The estimate (13) is unproved.** Norm continuity, finite rank, coercive effective covariance, analytic observation profiles and strict Loewner monotonicity do not supply it. The moving physical support projection is the unsmoothed part of the inverse problem. Abstract rates e_s=s and e_s=s^3 are both continuous and strictly increasing, while only the latter is quadratic; these are rate controls, not actual arithmetic contacts. The earlier shifted archimedean non-H1 groundstate further prevents inferring H1 from smooth finite forcing and coercive inversion alone.

The exact failed implication is continuity/strict positive gain increment -> quadratic upper bound on the contact eigenspace. Its missing hypothesis belongs to **endpoint exclusion**, not fresh retained attachment or same-vector null transport. The fresh analytic morphology remains attached conditionally; prescribed historical packet identity remains separately unproved. The unchanged physical h remains neutral diagonally in every enlargement, with nonzero full mixed residual and gain excess (1). Dilation is not used, and none of these equations promotes it to enlarged weak-nullity.

## Custody and validation boundary

Pinned source blobs and exact repeat-control output are recorded in notes/data/RPB108_QUADRATIC_GAIN_REGULARITY_20261006.json. Controls check the signed scalar bound, collar Poincare constant and distinct rate behaviors using rational arithmetic. They do not certify the Fourier/domain proof, actual null existence or (13). Historical notes and certificates are unchanged. No Lean/compiler/workflow change or new axiom audit is asserted. F4 and FULL TRANSPORT CLOSED remain open.
