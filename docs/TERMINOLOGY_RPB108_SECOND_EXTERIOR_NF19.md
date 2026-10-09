# RPB108 terminology — second native exterior response and residual (NF19)

Date: 2026-10-09 UTC. Additive definitions for independent Phase Geometry.
Do not alter or relabel historical CC53 first-mode collective response.

**Original native physical split.** Fix aperture a=53/50. The complete
unshifted signed Weil form Q has physically orthonormal Legendre low
space E112 and positive original physical orthogonal high space F112.
Let E_e and E_o be the 56-dimensional parity components of E112.

**Two-mode exterior trial space H2,p.** For even parity p=e set
H2,e=span{e112,e114}; for odd parity p=o set
H2,o=span{e113,e115}. Both are within F112 in the original logarithmic
supported form domain. Their complete original Q Gram is C2,p>0.
The mixed original native Gram from E_p to H2,p is B2,p.

**Collective two-mode normalized reaction.**
\[
R_{2,p}:=\sup_{x\in E_p\setminus\{0\}}
\frac{\langle B_{2,p}^*x,C_{2,p}^{-1}B_{2,p}^*x\rangle}
     {Q(x,x)}.
\]
This is a finite two-dimensional high-trial inverse computation,
not the full inverse on F112. The strict certificate R2,p<r
is equivalent to the finite positive block
\[
\begin{pmatrix}rA_p&B_{2,p}\\B_{2,p}^*&C_{2,p}\end{pmatrix}>0
\]
when A_p>0,C2,p>0. The ratio R2,p is defined with the original complete
Q including the signed poles; it is not the pole-free constrained CC52 gate.

**First-to-second residual trial response.** Let G1,p be the first-mode
C-high elimination already defined by CC53, and G2,p the full two-mode
C-high elimination. Then the form T2,p=G2,p-G1,p is nonnegative and rank
at most one, due to eliminating an additional C-orthogonalized high
direction. The separate quantity
\(\sup_{x\ne0}T2,p(x,x)/A_p(x,x)\)
is NOT generally equal to R2,p-R1,p. Nevertheless its value is at least
R2,p-R1,p, because \(G1,p\le R1,p A_p\) and a maximizing direction
for G2,p exists. The remainder after two trial modes remains open.

**Residual infinite response.** For the complete high C-form Riesz
source lift W on F112, define G_full,p=C(W.,W.). Its still-unmeasured
nonnegative remainder G_full,p-G2,p is NOT controlled by the finite
two-mode result. Full original whole-domain positivity requires
\(A_p-G_{\mathrm{full},p}>0\), rather than only A_p-G2,p>0.

All inequalities are scoped to the original source and the fixed target
cap; no old-gap-independent arithmetic frame bound is presumed.

**Rational low-energy three-space and twice-invisible existence.**
Let V3,p be the span of three explicitly specified rational E112 parity
vectors. A strict certificate \(\varepsilon_p M(V3,p)-Q(V3,p)>0\)
proves both their linear independence and that EVERY nonzero vector in
V3,p has positive original native physical Rayleigh below epsilon_p,
using the established original E112 positivity. The two measured native
pairings \(Q(x,e_{112+p})\) and \(Q(x,e_{114+p})\) define a linear
map V3,p -> C^2 of rank at most two. Its kernel therefore contains a
nonzero vector with BOTH measured pairings EXACTLY zero. This is an
existence theorem for an original positive low-energy retained vector,
NOT an explicit coefficient calculation for that corrected kernel
vector, not an original Q-null and not invisibility to all F112 sources.
