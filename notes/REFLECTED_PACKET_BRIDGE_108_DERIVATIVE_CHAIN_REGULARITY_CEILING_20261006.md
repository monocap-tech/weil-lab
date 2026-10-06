# RPB108: derivative chains constrain actual null regularity

Base: research 08f7e03046454ff95344a4713b524e8f29f5a0c8.

## Result

Fix an actual window a>0, let D_a be the canonical supported logarithmic form domain, and let K_a be the kernel of the full actual native mixed form. Write r=dim K_a, finite by the already proved identity-plus-compact theorem.

If r>0, then
\[
K_a\cap\{h:\partial^j h\in D_a,\ 0\le j\le r\}=\{0\}.
\tag{1}
\]
All derivatives here are derivatives of the global zero extension, not merely interior derivatives. Consequently, for every epsilon>0,
\[
K_a\cap H^{r+\epsilon}(\mathbb R)=\{0\}.
\tag{2}
\]
In particular no nonzero actual null vector can have a smooth compactly supported zero extension. The theorem does not supply the missing derivatives of an actual null vector, exclude K_a, or establish RH.

This uses the full interior mixed equation. It is independent of the rank-one inverse-moment average audited in the preceding pass.

## Derivative domain before use

Use Fourier convention exp(-2 pi i x xi) and w(xi)=log(e+|xi|). The domain in (1) can equivalently be specified by
\[
\int_{\mathbb R}(1+|\xi|^{2r})w(\xi)
 |\widehat h(\xi)|^2\,d\xi<\infty,\qquad
\operatorname{ess\,supp}h\subset[-a,a].
\tag{3}
\]
Distributional differentiation preserves support. Condition (3) makes every derivative through order r a genuine supported logarithmic vector. It rules out boundary delta distributions through those orders.

For epsilon>0, the inequality w(xi)<=C_epsilon(1+|xi|^2)^epsilon shows H^{r+epsilon} is contained in (3). Ordinary H^r alone is not identified with (3); the logarithmic weight on the top derivative still matters.

## Exact commutation, including the pole

Freeze the actual finite prime multiplier at the same window a, including equality at log n=2a. The known full residual of a supported vector is the distribution
\[
\mathcal R_a h=m_a(D)h+p_h,\qquad
p_h(x)=M_-(h)e^{x/2}+M_+(h)e^{-x/2},
\quad M_\pm(h)=\int e^{\pm y/2}h(y)\,dy.
\tag{4}
\]
Full mixed nullity is precisely the vanishing of (4) on (-a,a), first against compact smooth tests and then on D_a by form continuity and density. No exterior vanishing is asserted.

Suppose h and its global derivative h' belong to D_a. Then h is globally H^1, is compactly supported, and its absolutely continuous representative has zero values at both support endpoints. Integration by parts therefore gives
\[
M_-(h')=\tfrac12 M_-(h),\qquad
M_+(h')=-\tfrac12 M_+(h).
\tag{5}
\]
There is no endpoint contribution. Thus p_{h'}=p_h'. The multiplier in (4) commutes with distributional differentiation; in particular every fixed prime translation does so. Hence
\[
\mathcal R_a(h')=\partial_x(\mathcal R_a h).
\tag{6}
\]
If h is weak-null and h' is a legitimate D_a vector, (6) vanishes on the interior. Density and continuity of the full native form imply h' is also weak-null.

The premise h' in D_a is essential. An interior derivative accompanied by nonzero boundary traces cannot be substituted into (5)-(6) as a supported L2 vector. Nor does this argument translate h to a larger window.

## The derivative chain cannot fit in the finite kernel

Under (3), repeated application of (6) puts
\[
h,h',\ldots,h^{(r)}
\]
in K_a. Every nonzero globally compactly supported h has these r+1 derivatives linearly independent whenever they exist as L2 vectors.

Indeed, a relation sum_{j=0}^r c_j h^{(j)}=0 transforms into
\[
\left[\sum_{j=0}^r c_j(2\pi i\xi)^j\right]\widehat h(\xi)=0
\quad\hbox{a.e.}
\tag{7}
\]
A nonzero polynomial has only finitely many real roots. Equation (7) would force the L2 Fourier transform to vanish almost everywhere, unless the polynomial is identically zero. For nonzero h, every c_j must therefore vanish. This argument needs neither a presumed endpoint trace nor pointwise analyticity of the Fourier transform.

The r+1 independent vectors contradict dim K_a=r. This proves (1), and the weight comparison proves (2). For r=0 the kernel is already zero and the statement is vacuous.

A second useful formulation is: if every vector of K_a has its global derivative in D_a, then differentiation maps the finite-dimensional K_a to itself; the same polynomial argument implies K_a=0. It is enough to prove K_a is contained in H^{1+epsilon} for one epsilon>0. Such regularity has not been established.

## Recovered source regularity does not yet trigger the theorem

The native weak-derivative note of 2026-10-03 supplies a global L2 weak derivative for constructed Green syntheses. Its own scope does not attach the retained WD-T38 vector or its full weak-null equation.

The H1 Green membership note of 2026-10-04 proves that H1_0 physical vectors have lawful logarithmic and full-source coordinates and lie in the Green graph closure. It does not prove a logarithmic derivative, derivatives through the kernel dimension, or derivative invariance of K_a. Coordinate membership is not the full mixed-null identity.

The currently derived regularity of actual null vectors, H^s for every s<1/2 and every finite logarithmic weight, falls short of even the first global derivative needed here. Those facts are consistent with (1)-(2). Ordinary H1 membership of a constructed Green vector cannot silently be upgraded to condition (3) with r=1.

Thus this pass gives a regularity ceiling and an exact sufficient exclusion criterion, not an additional regularity bootstrap. If future actual-null regularity crosses that criterion, finite nullity immediately closes the contradiction without requiring an exterior-tail annihilation estimate. At present the missing actual regularity or independent arithmetic exclusion remains open.

## Sources and validation

Repository sources, read at the base commit:

- REFLECTED_PACKET_BRIDGE_108_TRANSLATION_NULL_EXTENSION_OBSTRUCTION_20261004.md: actual translation covariance, canonical finite nullity, and the full native/source domain.
- REFLECTED_PACKET_BRIDGE_108_ACTUAL_EXTERIOR_MOMENT_RIGIDITY_20261005.md: full residual formula; exterior detection does not imply its annihilation by interior nullity.
- REFLECTED_PACKET_BRIDGE_108_NATIVE_WEAK_DERIVATIVE_20261003.md and REFLECTED_PACKET_BRIDGE_108_H1_GREEN_MEMBERSHIP_20261004.md: the precise recovered Green regularity scope.
- REFLECTED_PACKET_BRIDGE_108_FRACTIONAL_NULL_REGULARITY_20261005.md: the established subcritical actual-null regularity.

Validation is an analytic proof: global integration by parts with both pole signs explicit, distributional commutation, full-domain density, and Fourier-polynomial independence. No numerical controls are presented as proof of a universal theorem. No Lean source or workflow changes, new CI run, retained-witness attachment, numerical aperture advance, or RH conclusion. The numerical positivity frontier remains 81/100. F4 and FULL TRANSPORT CLOSED remain open.
