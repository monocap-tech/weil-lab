# RPB108: shrinking-collar logarithmic gain

Base: research 4ddb580133b74c966d0a39682c78a8e52c938ab4.

## Improved actual estimate

For a lawful actual endpoint weak-null vector h in D_a, let q be its constructed gapless residual and let M_R be its exact moving-Gaussian Fourier mass. There are finite constants C_a,R_a such that
\[
M_R\le
 \frac{C_a}{(\log R)^4}\|h\|_2^2
 +C_a\frac{\sqrt R}{\log R}e^{-\sqrt R/16}\|h\|_2^2,
\qquad R\ge R_a.
\tag{1}
\]

The new input proved here is quantitative smallness of the genuine residual in a shrinking exterior collar:
\[
\|q\|_{L^2(a<|x|<a+\delta)}
 \le\frac{C_a}{\log(1/\delta)}\|h\|_2
\tag{2}
\]
for sufficiently small delta>0.

This improves the previous M_R=O((log R)^(-2)) bound. It is still logarithmic, not exponential, and does not force h=0.

## Terminology before use

**Shrinking exterior collar:** B_delta={x:a<|x|<a+delta}. It is the true zero-gap residual region adjacent to the source support.

**Local concentration bound:** an L2 mass estimate for h on a short measurable set derived from its squared-logarithmic Fourier norm, not from a boundary trace.

**Shrinking-collar logarithmic gain:** the extra factor 1/log(1/delta) in the residual L2 norm, used in (2) and then in the actual Gaussian action.

No endpoint vanishing rate, H1 regularity, positive support gap or unproved iterated regularity is included in these definitions.

## The already derived endpoint regularity

The preceding actual residual theorem gives
\[
q=T_h+p_h,\qquad q=0\text{ on }(-a,a),\qquad
\|T_h\|_2\le K_a\|h\|_2,
\]
and
\[
\|w\widehat h\|_2\le H_a\|h\|_2,\qquad
w(\xi)=\log(e+|\xi|),\quad H_a=K_a+C_a.
\tag{3}
\]
Physical multiplier-domain membership in the first estimate was proved from endpoint nullity. It is not a new assumption here.

## Local concentration from Fourier truncation

Write H=||h||_2 and L=||w Fourier(h)||_2. Let E be measurable with length ell. Decompose h=h_low+h_high at Fourier radius T.

By Fourier Cauchy-Schwarz,
\[
\|h_{\rm low}\|_\infty^2\le2T H^2,
\qquad
\|h_{\rm high}\|_2^2\le\frac{L^2}{w(T)^2}.
\]
Thus
\[
\int_E|h|^2
 \le4\ell T H^2+\frac{2L^2}{w(T)^2}.
\tag{4}
\]
For ell<=C eta and T=eta^(-1/2), equation (3) implies
\[
\|1_E h\|_2
 \le C_{a,C}
 \left(\eta^{1/4}+\frac1{\log(1/\eta)}\right)H
\tag{5}
\]
for 0<eta sufficiently small. This holds at every physical location, not only at the two endpoints.

## Archimedean residual mass in the collar

The actual off-support archimedean kernel is
\[
-k(v),\qquad k(v)=\frac{e^{-|v|/2}}{1-e^{-2|v|}},
\quad k(v)\le\frac{C_k}{|v|}.
\]
At the right endpoint write x=a+d, y=a-r. For 0<d<delta, split the source integral at r=eta, with 0<eta<2a.

For 0<r<eta, the proved Carleman L2 estimate gives
\[
\|\operatorname{arch}_{\rm near}\|_{L^2(0,\delta)}
 \le\pi C_k\|1_{(a-\eta,a)}h\|_2.
\]
For eta<=r<=2a, ordinary Cauchy-Schwarz gives the pointwise bound
\[
|\operatorname{arch}_{\rm far}(a+d)|
 \le C_k H
 \left(\int_\eta^{2a}\frac{dr}{(d+r)^2}\right)^{1/2}
 \le C_k H\eta^{-1/2}.
\]
Integrating over d in (0,delta) yields
\[
\|\operatorname{arch}_{\rm far}\|_{L^2(0,\delta)}
 \le C_k H\sqrt{\delta/\eta}.
\]

Choose eta=sqrt(delta), with delta small enough that eta<2a. Equation (5) gives the combined right collar norm at most
\[
C_a H\left(\delta^{1/8}
 +\frac1{\log(1/\delta)}+\delta^{1/4}\right).
\]
The left endpoint is identical. Since each positive power of delta is bounded by a constant divided by log(1/delta) for small delta, the combined archimedean collar norm is at most C_a H/log(1/delta).

This estimates the genuine singular kernel up to the boundary, without inventing a support gap.

## Prime translations and pole

The actual native prime part has finitely many terms
\[
-\frac{\Lambda(n)}{\sqrt n}
 \bigl(h(x-\log n)+h(x+\log n)\bigr).
\]
For x in B_delta, each shifted evaluation restricts h to the translate of a set of length 2delta. Apply (5) to that set and sum the finitely many actual coefficients. Their total collar norm is at most C_a H/log(1/delta).

The exact pole satisfies |p_h(x)|<=C_a H exp(|x|/2). On B_delta with delta<=1, its L2 norm is at most C_a sqrt(delta)H, which is absorbed into the same logarithmic bound.

Adding the three actual contributions proves (2). Complex cancellation is not assumed; this is an absolute upper bound for the combined residual.

## Shrinking-collar Gaussian action

The exact residual realization and its Gaussian pole integrability give
\[
\mathcal A_a(h;\overline{g_R})
 =\int_{|x|>a}q(x)\overline{g_R(x)}\,dx,
\qquad g_R=K_R*h.
\]
For the near collar, (2) and ||g_R||_2<=sqrt(M_R) imply
\[
\left|\int_{B_\delta}q\,\overline{g_R}\right|
 \le\frac{C_a H}{\log(1/\delta)}\sqrt{M_R}.
\tag{6}
\]

For |x|>=a+delta, put t=|x|-a. The exact kernel gives the previously proved pointwise estimate
\[
|g_R(x)|\le C_a\sqrt R H e^{-Rt^2/8}.
\]
Since t>=delta,
\[
e^{-Rt^2/8}\le
 e^{-R\delta^2/16}e^{-Rt^2/16}.
\]
Consequently
\[
\|1_{\{|x|\ge a+\delta\}}g_R\|_2
 \le C_a\sqrt R e^{-R\delta^2/16}H,
\]
and
\[
\int_{|x|\ge a+\delta}|g_R(x)|e^{|x|/2}\,dx
 \le C_a\sqrt R e^{-R\delta^2/16}H.
\]
The remaining Gaussian and exponential-weighted Gaussian integrals are uniformly bounded for R>=1 and 0<delta<=1.

Use ||T_h||_2<=K_a H for the core and the exact pole growth bound separately. The far residual pairing is therefore at most
\[
C_a\sqrt R e^{-R\delta^2/16}H^2.
\tag{7}
\]
No cutoff derivative, distributional order or assumed pointwise residual regularity is needed for this split: q is already constructed locally L2 and T_h globally L2.

Equations (6)--(7) give
\[
|\mathcal A_a(h;\overline{g_R})|
 \le\frac{C_a H}{\log(1/\delta)}\sqrt{M_R}
 +C_a\sqrt R e^{-R\delta^2/16}H^2.
\tag{8}
\]

## Absorption against actual coercivity

Take delta=R^(-1/4), so log(1/delta)=(log R)/4 and R delta^2=sqrt(R). For all sufficiently large R, the collar estimates apply, and
\[
|\mathcal A_a(h;\overline{g_R})|
 \le\frac{C_a H}{\log R}\sqrt{M_R}
 +C_a\sqrt R e^{-\sqrt R/16}H^2.
\tag{9}
\]

Actual Gaussian coercivity supplies, with L_R=log R-C'_a,
\[
L_R M_R
 \le\frac{C_a H}{\log R}\sqrt{M_R}
 +C_a\sqrt R e^{-\sqrt R/16}H^2
 +D_a(1+\log R)e^{-R/4}H^2.
\]
For large R, L_R>=(log R)/2. Young's inequality bounds the first right-hand term by
\[
\frac{L_R}{2}M_R+
 \frac{C_a^2H^2}{2L_R(\log R)^2}.
\]
Absorb half the left side and divide by L_R. The first error is O(H^2/(log R)^4). The genuine separated-tail error is O(sqrt(R) exp(-sqrt(R)/16)H^2/log R). The earlier exp(-R/4) term is absorbed into that error for sufficiently large R. This proves (1).

## What has advanced

We now have a quantitative shrinking-boundary estimate derived from actual endpoint nullity and the genuine residual. Choosing a moving collar improves the Gaussian logarithmic rate by two powers.

The leading term remains logarithmic. The stretched-exponential far-field error does not make the whole bound exponential; it cannot be substituted for the leading term. Therefore the one-sided Gaussian zero theorem does not apply.

No iteration to arbitrary logarithmic powers, Sobolev regularity, holomorphic strip or RH conclusion is asserted. Obtaining such an iteration would require further regularity estimates for the residual that are not proved here.

This is a substantive boundary estimate on the correct same-vector carrier, not another representation record. Independent boundary null exclusion and FULL TRANSPORT CLOSED remain open.

## Validation and cursor

Analytic proof from direct Fourier truncation, the actual Carleman kernel and finite prime translations, derived squared-logarithmic endpoint regularity, exact residual realization and actual Gaussian coercivity. No new external input, Lean source/workflow change or CI result. Certified code remains cb92c1b4dfca298cbc79d5b7d25598ea370236bf; Actions run 37236113125/job 111535430775.

At 4ddb580, derived squared-logarithmic Fourier regularity gives a quantitative local concentration bound on h. Splitting the actual exterior digamma/Carleman kernel at source depth eta=sqrt(delta), and retaining every finite native prime translation and the pole, proves ||q||_L2(a<|x|<a+delta)<=C_a||h||_2/log(1/delta) for small delta. The exact zero-gap residual representation then bounds its near Gaussian action by C_a||h||_2 sqrt(M_R)/log(1/delta); the separated far action is <=C_a sqrt(R) exp(-R delta^2/16)||h||_2^2 using the derived global L2 core and weighted pole estimate. Choosing delta=R^(-1/4) and absorbing against actual log-R coercivity proves M_R<=C_a||h||_2^2/(log R)^4+C_a sqrt(R)/log(R) exp(-sqrt(R)/16)||h||_2^2 for sufficiently large R. This is a genuine shrinking-boundary improvement over the previous log^(-2) estimate, derived from lawful endpoint nullity with no support gap, assumed graph density or prior operator-domain membership. It remains logarithmic and does not trigger the one-sided exponential zero theorem. No unproved iteration to arbitrary log powers, actual endpoint existence, RH conclusion or new Lean/CI claim. FULL TRANSPORT CLOSED and independent boundary null exclusion remain open.
