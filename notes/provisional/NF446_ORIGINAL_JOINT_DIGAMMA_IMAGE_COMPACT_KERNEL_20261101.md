# Weil-Lab NF446 — Original joint digamma/image cancellation to true compact source

**2026-11-01 PT; original Weil odd response.** Mathematical standing: **ACCEPTED EXACT SOURCE-LINEAR REPRESENTATION** of the full central digamma plus both endpoint image families, with a **certified finite original J7/J8 uniform response bound**. This is not an accepted numerical enclosure of either signed \(D_7\) or \(D_8\); W-ODD-NEG, the whole NF410/NF404 criterion and RH remain OPEN.

Research [draft PR #467](https://github.com/monocap-tech/weil-lab/pull/467), stacked on [NF445 PR #466](https://github.com/monocap-tech/weil-lab/pull/466), no main merge.

## Previous cursor → current circle → next bold

**Previous NF445:** The authentic original source-correlated \(R_m\) was recovered from 273 grouped generators with 4096-bit source intervals, and the residual image sum expressed using a single exact Laplace kernel \(K_1\). But its integrand contained \(U_{\mathrm{ent}}(B+t/2)\), the *entire generator continuation beyond physical compact support*. The original \(T_1\) image alone was about \(-3.2\times10^{139}\), so an independent image integral—even a source-correlated one—was numerically inappropriate. The authentic original central digamma response was still a different term. Six signed cells certified, J7/J8 open.

**NF446 current:** Pair **the original digamma and BOTH images before bounding**. Their exterior-analytic-source Laplace tails cancel algebraically, producing an exact integral over the source's **true compact support** \(u_4|_{[-B,B]}\). The actual compact \(u_4''\) L2 and source-native \(u_4(B),u_4'(B)\) can now be charged. Consequently \(|z(x)|<25000\) uniformly on original J7/J8, replacing the useless independent-source image \(M/N\sim10^{140}\) as a bound for the *complete response*. It is still many orders of magnitude above decision quality for signed cells of scale \(10^{-23}\).

## Original-source normalization, no altered support

Let \(B=11/10\). \(U(y)=u_4(y)\) denotes the complete odd compact source on \([-B,B]\), using all original NF407 242 selected+4 critical dyadic coefficients, 32 critical sine frequencies and the sinh pole, 273 consolidated frequency/order groups. The original NF404 center remains exact rational \(6677356497477490213/4611686018427387904\). Outside \([-B,B]\), the NF445 analytic continuation \(U_{\mathrm{ent}}\) is only a transfer identity, **not the physical source**.

The original native source SHA is \`0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce\`; original NF406 irrational support SHA \`c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675\`. Verified against the original NF443 central digamma function \`polygamma_D\`, the m≥0 images with \(a_m=m+1/4\), both exponentials and the original special \(m=0\) sinh-pole combination.

For \(0\le x\le B\), define
\[
a=2(B-x),\quad b=2(B+x),\quad
K(t)=\frac{e^{-t/4}}{1-e^{-t}},\quad
c_0=\psi(1/4)-\log\pi,\quad v=U(B).
\]

The central native digamma symbol, acting on an exponential-frequency source, satisfies
\[
D(\lambda)=\frac{\psi(1/4-\lambda/2)+\psi(1/4+\lambda/2)}2-\log\pi
=c_0+\int_0^\infty K(t)\left(1-\cosh(\lambda t/2)\right)dt.
\]

For source polynomial-frequency generators \(x^k e^{\lambda x}\), differentiation in \(\lambda\) gives the identical \(U(x\pm t/2)\) expressions with all original polynomial orders and frequencies—not a new kernel assumption.

Using NF445's exact image Laplace identity, the original left-end image family supplies
\[
+\tfrac12\int_a^\infty K(t)\,U(x+t/2)\,dt
\]
and, because the original complete \(U\) is odd, the right-end image family supplies
\[
+\tfrac12\int_b^\infty K(t)\,U(x-t/2)\,dt.
\]
Each cancels precisely the corresponding original digamma tail. The remaining three regions, with basis \((U(x),U(x+t/2),U(x-t/2))\), have exact rational coefficient vectors:

| Source-variable range | Combined coefficient vector |
|---|---|
| \(0<t<a\) | \((1,-1/2,-1/2)\) |
| \(a<t<b\) | \((1,0,-1/2)\) |
| \(b<t<\infty\) | \((1,0,0)\) |

No exterior \(U_{\mathrm{ent}}(B+t/2)\) remains. On the first interval, both \(x\pm t/2\) lie in \([-B,B]\); on the second, \(x-t/2\) lies in \([-B,B]\). This is the **original physical support**, not an invented continuation.

## Exact singularity removal, including the original principal logarithm

The original native response explicitly subtracts \(v\log(B/(B-x))/2\). Subtract \(v/2\) *inside the middle integral* and add it back analytically. Since
\[
\log(b/a)-\log(B/(B-x))=\log((B+x)/B),
\]
and \(K(t)-1/t\) is bounded through \(t=0\), the complete original central archimedean response plus both images **after its explicit principal log subtraction** equals

\[
\boxed{\begin{aligned}
\mathcal J_U(x)={}&c_0U(x)\\
&+\int_0^a K(t)\left[U(x)-\frac{U(x+t/2)+U(x-t/2)}2\right]dt\\
&+\int_a^b K(t)\left[U(x)-\frac{U(x-t/2)}2-\frac v2\right]dt\\
&+\frac v2\left[\log\frac{B+x}{B}+\int_a^b(K(t)-1/t)\,dt\right]\\
&+U(x)\int_b^\infty K(t)\,dt.
\end{aligned}}
\]

Every term is finite also at \(x=B\), by the continuous one-sided limit. The first integral shrinks to an empty interval as \(a\to0\). In the middle integral at \(x=B\), its bracket is \(O(t)\) because \(U(B)=v\), canceling \(K(t)\sim1/t\). The scalar remainder \(K(t)-1/t\) has a finite \(t=0\) limit, and \(b\ge2B>0\).

**Original removable \(m=0\) sinh-pole:** The source carrier \(c_{\mathrm{pole}}\sinh(\lambda x)\) with \(\lambda\to1/2\) gives opposite \(1/(2\varepsilon)\) Laurent residues in the digamma and native first image \(m=0\) (\(\varepsilon=1/4-\lambda/2\)). They cancel exactly; the finite result is the original native
\[
c_{\rm pole}\Bigl\{\left[\frac{\psi(1)+\psi(1/2)}2-\log\pi-B\right]\sinh(x/2)
+x\cosh(x/2)-e^{-B}\sinh(x/2)\Bigr\}.
\]
This is precisely the original NF443 \(K_{\mathrm{pole}}\) and special first-image finite remainder; do not evaluate a divergent digamma term separately. For \(m\ge1\), the original sinh image is already covered by the NF445 finite Laplace formula. Thus the joint compact identity includes the same pole as the original native transfer.

## The original full physical J7/J8 response

Inside the genuine fixed-support physical cells, the unchanged original NF405 regular source shifts are
\[
\begin{array}{c|c|c}
\text{Cell}&\text{minus regular translates}&\text{plus regular translates}\\
J_7&2,3,4,5,7,8&\varnothing\\
J_8&2,3,4,5,7,8,9&\varnothing
\end{array}
\]
and the independent NF407 principal \(r\)-jumps have the matching *active prime sets* on these particular cells. Those two roles are **not** thereby identified generally, as J1 and J2 show. The genuine physical \(z\) on either J7 or J8 is obtained from \(\mathcal J_U\) by subtracting the corresponding original weighted regular \(U(x-\log n)+v\) terms and the original exact dyadic NF404 sinh centering. No manufactured support jump at the rational integration boundary is allowed. NF444 already proved exact n9 seam cancellation and continuity.

## Rigorous original source-bound transfer: 10^140 → 25000 as a full-response envelope

The retained independent NF413 certificate established
\[
\|U''\|_{L^2(-B,B)}<256
\]
with original source radii paid. The independent NF445 4096-bit native certificate, pinned byte-exact, gives
\[
-1<v=U(B)<0,\qquad |U'(B)|<1.
\]

Since \(\sqrt{2B}=\sqrt{11/5}<3/2\), the fundamental theorem and Cauchy–Schwarz yield
\[
\sup_{[-B,B]}|U'|<1+256(3/2)=385<400,
\]
\[
\sup_{[-B,B]}|U|<1+400(2B)=881<900.
\]
These are bounds on the **original compact source**, not on the enormous exterior analytic continuation.

For \(t>0\),
\[
0<K(t)<\frac1t+1,\qquad \left|K(t)-\frac1t\right|\le1.
\]
For \(b\ge2B\), \(\int_b^\infty K(t)\,dt<4\). Also \(|c_0|<10\) (independently checked by Arb). The five pieces in \(\mathcal J_U\) admit the following conservative exact rational bounds:

| Joint source component | Strict bound |
|---|---:|
| Small-t symmetric difference \(\int_0^a\) | \(<1000\) |
| Middle source-subtracted \(\int_a^b\) | \(<2500\) |
| Finite scalar logarithmic remainder | \(<3\) |
| True source tail \(U(x)\int_b^\infty K\) | \(<3600\) |
| Constant \(c_0U(x)\) | \(<9000\) |

Therefore **\(|\mathcal J_U(x)|<17000\)** uniformly for the full positive side \(0\le x\le B\).

On J7/J8, there are at most seven genuine regular prime-power shifts. Each weight \(\Lambda(n)/\sqrt n<1\) and each source-plus-endpoint term has magnitude \(<901\), while the exact NF404 centering contributes \(<2\). Hence the **complete original physical response** satisfies

\[
\boxed{|z(x)|<25000 \quad\text{for every }x\in J_7\cup J_8.}
\]

This is a true original-source all-\(x\) bound, not a 14-index image interpolation and not an unverified Gauss quadrature. It supersedes the NF444 ~\(10^{140}\) *intermediate image* estimate for purposes of whole-response boundedness, but the two estimates are for different mathematical quantities.

The original J8 principal \(p(x)\) remains unbounded as \(x\to B\), though
\[
\int_{J_7\cup J_8}|p(x)|\,dx<9.
\]
The resulting individually rigorous, very conservative envelopes include \(\int|pz|<225000\), \(\int z^2<7\times10^8\), and \(|D_7|,|D_8|<2\times10^9\). None approaches signed decision quality at the \(10^{-23}\) scale.

## Verification and custody

[Focused original NF446 source/native custody CI #41388810482 SUCCESS](https://github.com/monocap-tech/weil-lab/actions/runs/41388810482). This verifies the original NF407 246-source SHA, NF406 seams, original NF443 digamma/image/m0 source code conventions, NF413 full true \(U''\) L2 certificate, unchanged NF445 actual 4096-bit \(U(B)\) and \(U'(B)\) interval source SHA, exact rational three-interval coefficient cancellation, original pole residue cancellation, actual J7/J8 support and rational source bounds.

Final NF446 source/custody JSON SHA256 \`3cfd2a71adf0c7fa0d9e314a8a0c7bf9cde732d60fad4c7a2346a286f0fb150a\`; artifact ID #13116791232, ZIP SHA256 \`f93aa16c6df71a0fb9f89fbb85087b4e91771e6e8ef28f9478e8bcfa20ac263f\`. Permanent compact [custody index](../data/provisional/NF446_original_joint_compact_kernel_J7_J8_custody_index.json), original raw numerical JSON retained in GitHub Actions through January 31, 2027, permanent raw repo archival still due.

## Status and next NF447

**Accepted:** Exact full original joint source-linear digamma/two-image/explicit-principal-log integration representation on *compact physical source only*, original sinh pole retained and canceled, genuine continuous \(x=B\) endpoint integrands, and true uniform \(|z|<25000\) for J7/J8. The original source absolute-largeness from exterior Laplace continuation is no longer an independent numerical obstruction to boundedness.

**Still OPEN:** A **decision-quality** fully source-correlated Arb enclosure of the compact-kernel integrals, their actual true \(pz,z^2\) continuous cell integrals and their signed \(D_7,D_8\); original principal \(E_p\), complete NF410/NF404 scalar, exterior fourth J242 upper, W-ODD-NEG, even/whole Weil, infinite domain, RH. The existing six original physical cells remain signed J1/J2/J3 positive, J4/J5/J6 negative.

**Next bold NF447:** Derive a numerically practical **endpoint-regularized kernel implementation** that preserves the original 246-source correlation and does not separately evaluate large U or central/image terms. Use validated Arb/Acb integration with exact midpoint/radius charges on a finite true-support variable \(y\in[-B,B]\), treating the removable \(t=0\) second difference and \(K-1/t\) separately. First certify representative actual near-B values and error bounds, then assemble sourcewise moment integrals for J7/J8. Do not promote a mere finite enclosure to a signed cell certificate. No main merge.
