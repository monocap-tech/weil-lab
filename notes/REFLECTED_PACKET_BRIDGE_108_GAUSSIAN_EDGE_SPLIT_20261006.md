# RPB108: endpoint test truncation leaves a genuine edge pairing

Date: 2026-10-06 (America/Los_Angeles). Source `fb0cfa4f087debb34b9b35029051748861d70a29`.
Definitions: [Gaussian edge split](../docs/TERMINOLOGY_RPB108_GAUSSIAN_EDGE_SPLIT.md).
Global/F4 lane; no aperture computation.

## Actual hard split closes its domain gate

Let h be an actual full-native null vector at a, and put g_R=K_R*h with the unchanged project Gaussian. The supported-L2 promotion theorem gives a global L2 representative for m_a(D)h. Hence the full residual q_h=m_a(D)h+p_h is locally L2, zero almost everywhere on (-a,a), and Gaussian-admissible on the whole line. The core pairs with g_R by L2 Cauchy-Schwarz; the exponentially growing pole pairs absolutely by the already proved Gaussian bound.

The interior truncation
\[
g_R^{\rm in}=1_{[-a,a]}g_R
\]
belongs to D_a. For a fixed R, g_R and its first derivative are bounded on that finite interval. Integration by parts, keeping the two endpoint values, bounds its Fourier transform by C_R/(1+|xi|). This gives finite logarithmic energy. No zero endpoint trace or H1 membership is asserted. Thus Q_a(g_R^in,h)=0 is a lawful endpoint-domain null equation.

The physical residual representation, with its already removed endpoint distributions, yields exactly
\[
\boxed{\mathcal A_a(h;\overline{g_R})
=\int_{|x|>a}q_h(x)\overline{g_R(x)}\,dx.}
\tag{1}
\]
This strengthens the test-domain bookkeeping from smooth interior cutoffs to the full hard truncation. The existing smooth collar/far-field localization remains valid and is not reopened.

Equation (1) removes the entire endpoint-interior test contribution. It supplies no smallness of the exterior pairing. The supports can touch at the endpoint, so the fixed-separation exponential Gaussian estimate cannot be used there. The bound C_R for the truncated test is not uniform as R grows, and membership of that test does not put the whole-line g_R in D_a.

## Fixed step control rejects regularity-only summability

Take a>=1/2 and define
\[
h=1_{[a-1,a]},\qquad q=-1_{[a,a+1]},\qquad
B_R=\int q(x)\overline{K_R*h(x)}\,dx.
\]
Both functions have physical L2 norm one. Their Fourier transforms decay as O(1/|xi|), so each belongs to every finite logarithmic space and to H^alpha for every alpha<1/2. They have disjoint interiors, q vanishes on (-a,a), and for 0<s<=1 their squared edge-collar masses are exactly s. In particular they satisfy every fixed subcritical collar estimate s<=s^(2alpha), 0<alpha<1/2.

These are fixed vectors, not R-dependent concentration vectors. The same h is used in every B_R. Their regularity norms are finite constants independent of R.

However,
\[
\boxed{\Re B_R=
\frac{1}{2\sqrt\pi}R^{-3/2}
+O(R^{-5/2})+O(R^{-1/2}e^{-R/4}).}
\tag{2}
\]
Consequently the positive real part is eventually bounded below by a positive constant times R^(-3/2). At integer R=n,
\[
\sum_{n\ge2}\frac{n^{3/2}}{\log(e+n)}
(\Re B_n)_+=\infty.
\tag{3}
\]
This rejects the functional implication from the stated regularity, collar powers, interior residual vanishing and touching-support geometry to the new weighted action moment.

Here q is an independently assigned residual. It is **not** claimed to equal m_a(D)h+p_h. The actual h is a lawful logarithmic carrier vector, but no native nullity, contact, actual source matrix or arithmetic realization is asserted for this pair. The control does not disprove an estimate using the full prescribed Euler/prime/pole equation.

## Exact overlap calculation and asymptotic sign

Set u=x-a, v=a-y. For 0<u,v<1, x-y=u+v. The overlap length at t=u+v is
\[
\ell(t)=
\begin{cases}t,&0<t<1,\\2-t,&1<t<2,\\0,&\text{otherwise}.\end{cases}
\]
Therefore
\[
\Re B_R=-\frac{\sqrt R}{2\sqrt\pi}
\int_0^2\ell(t)e^{-Rt^2/4}\cos(Rt)\,dt.
\tag{4}
\]
The minus sign comes from q=-1, not from a changed pole convention.

Replacing ell(t) by t on [0,infinity) introduces absolute error at most
\[
\frac{\sqrt R}{2\sqrt\pi}
\int_1^\infty 2t e^{-Rt^2/4}dt
=\frac{2}{\sqrt{\pi R}}e^{-R/4}.
\tag{5}
\]
Indeed ell=t below one and |ell-t|<=2t above one.

With z=sqrt(R)t and lambda=sqrt(R), the replacement in (4) is
\[
-\frac{1}{2\sqrt{\pi R}}I(\lambda),
\qquad
I(\lambda)=\int_0^\infty F(z)\cos(\lambda z)dz,
\quad F(z)=z e^{-z^2/4}.
\]
All derivatives of F are integrable and vanish at infinity. Four integrations by parts give
\[
I(\lambda)=-\frac{F'(0)}{\lambda^2}
+\frac{F'''(0)}{\lambda^4}
+\frac1{\lambda^4}\int_0^\infty F''''(z)\cos(\lambda z)dz.
\tag{6}
\]
Since F'(0)=1 and F'''(0)=-3/2,
\[
I(\lambda)=-\lambda^{-2}+O(\lambda^{-4}).
\]
Equations (5)-(6) prove (2), including its positive leading sign. The remainder constant is finite, for example using |F'''(0)|+||F''''||_1. No oscillatory numerical quadrature is needed.

The polynomial derivative is
\[
F''''(z)=\left(\frac{15}4z-\frac54z^3+\frac1{16}z^5\right)e^{-z^2/4}.
\]
The three absolute Gaussian monomial integrals are 2, 8 and 64, so ||F''''||_1<=43/2. Combining this with |F'''(0)|=3/2 gives the explicit relative bound
\[
|2\sqrt\pi R^{3/2}\Re B_R-1|
\le23/R+4R e^{-R/4}.
\]
Since e^(R/4)>=(R/4)^4/24, the right side is at most 23/R+24576/R^3, at most 29/64 for R>=64. Thus
\[
\Re B_R\ge\frac1{4\sqrt\pi}R^{-3/2}\qquad(R\ge64).
\tag{6a}
\]
This provides a rigorous eventual sign and lower constant without relying only on asymptotic notation.

For (3), the summands are eventually at least C/log(e+n). This positive series diverges: log(e+n)<=C' n for all n>=2, so it dominates a positive multiple of the harmonic series. The failure is stronger than the borderline 1/(n log n) rate in the preceding action-moment note.

## Why endpoint truncation does not restore a support gap

The control's q is zero throughout the interior and its supports overlap h only on a measure-zero endpoint. Nevertheless Gaussian convolution transports mass across that endpoint on the R^(-1/2) physical scale. Oscillation gives the polynomial signal (2), rather than an exponential suppression. Measure-zero support intersection is not positive support separation.

A general operator estimate also shows why an R-dependent cutoff cannot create a gap for free. For profiles supported on opposite sides of zero, define
\[
h_R(y)=R^{1/4}e^{iRy}f(\sqrt R\,y),\qquad
q_R(x)=R^{1/4}e^{iRx}g(\sqrt R\,x),
\]
with f supported in (-1,0), g in (0,1), both real nonnegative and L2-normalized. Their masses are one. Substitution gives
\[
\int q_R(x)\overline{K_R*h_R(x)}dx
=\frac1{2\sqrt\pi}\int_0^1\int_{-1}^0
g(s)f(t)e^{-(s-t)^2/4}dt\,ds>0,
\tag{7}
\]
independent of R. The phases cancel exactly. Thus the cross-endpoint Gaussian operator has no decaying L2-to-L2 norm. These varying vectors need not obey uniform fractional null-space estimates and are not a counterexample in the fixed finite actual kernel; the fixed control (2) is the one matching all stated qualitative subcritical regularity.

There is no assertion that (7) is the actual residual map. The actual boundary-scaling theorem already identifies the half-Carleman singularity in that residual; it also explicitly scopes its norm-only obstruction to general carrier vectors. Neither control supplies an arithmetic endpoint exclusion.

## Smallest actual theorem left by this attack

The hoped-for implication was:

    actual endpoint nullity kills the hard interior Gaussian test
    + local L2 residual and every fixed subcritical regularity/collar bound
    -> finite weighted signed Gaussian action moment.

The first step is now proved by (1). The second does not follow from those functional properties: (2)-(3) reject the regularity-only inference. The missing information must use the exact dependence q_h=m_a(D)h+p_h, including the prescribed prime shifts and signed pole, or another independent consequence of the full null equation.

A smallest sufficient target is finite liminf of
\[
\sum_{n=2}^N\frac{n^{3/2}}{\log(e+n)}
\Re\int_{|x|>a}q_h(x)\overline{K_n*h(x)}dx
\tag{8}
\]
for every vector of a real basis of the hypothetical full kernel. By (1), this is exactly the prior genuine-action target. Its negative part has the already proved finite budget; bounded partial sums along a sequence would suffice. The basis quantifier cannot be replaced by one retained vector without the applicable nullity/parity condition. No bound on (8) is obtained here.

This obstruction belongs to endpoint exclusion. It attaches no prescribed historical packet. Physical h, cutoff a, selected coordinates and actual pole are unchanged in (1) and (8). Changing or truncating the test vector is not changing h, and supplies no enlarged mixed-null equation. Dilation and the scalar inverse-boundary moment are unused.

## Custody and standing

Pinned sources and repeated exact overlap, derivative-polynomial and rate controls are in notes/data/RPB108_GAUSSIAN_EDGE_SPLIT_20261006.json. Those controls verify the algebra in (4)-(6), not the actual arithmetic target (8). The domain, integration-by-parts and asymptotic arguments are analytic, not Lean certified. Historical notes, Lean/compiler/workflows and prior certificates remain unchanged. Aperture custody is preserved; F4 and FULL TRANSPORT CLOSED remain open.
