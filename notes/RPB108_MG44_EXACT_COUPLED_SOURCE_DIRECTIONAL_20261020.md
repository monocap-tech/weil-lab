# MG44 — Exact original-source directional coupled residual bounds

October 20, 2026. Stacked on MG43 PR #292, whose original full-source calculation and independent all-540-matrix check passed Actions #39522608989, and final-head verification #39523329157.

## Mathematical target

The actual original 24-dimensional source basis is SI10's physical 25-generator family, transformed into MG11's 23 dual-boundary adapted sources plus its genuine sinh pole. Original signed seven-prime/digamma multiplier, complete real frequency, and SM41 tails are retained via independently accepted source-moment artifacts.

For a fixed original nonscalar source response B and exact rational v, put w=Bv. The true residual R(B)=F-A*FB satisfies the original moment identity:

\[
v^\mathsf{T}R(B)^\mathsf{T}R(B)v
=v^\mathsf{T}Hv-2v^\mathsf{T}Gw+w^\mathsf{T}Sw.
\]

The two original, separately certified Loewner moment enclosures MG24 and MG29 are both valid on the SAME source and same true G,S:

\[
L_i\preceq G\preceq U_i,\quad S\preceq S_i,\quad
H_{\rm lo}\preceq H\preceq H_{\rm up},\quad i\in\{24,29\}.
\]

Set C_i=(L_i+U_i)/2, E_i=(U_i-L_i)/2 PSD. The full PSD block matrix with diagonal E_i and off-diagonal (G-C_i) is congruent to diag(E_i+(G-C_i),E_i-(G-C_i)). Hence block Cauchy–Schwarz proves for EVERY fixed rational v,w:

\[
v^\mathsf{T}Gw \geq
 v^\mathsf{T}C_iw-
 \sqrt{(v^\mathsf{T}E_iv)(w^\mathsf{T}E_iw)}.
\]

Rounding each positive square root UP to a rational 10^-12 grid via integer isqrt gives a fully rigorous numerical lower. The first-moment lower is the scalar MAX of the MG24 and MG29 two individual valid lower values; the second-moment upper is the scalar MIN of their two individual valid upper values. Thus the original exact scalar residual upper for this v is

\[
U_{\rm ray}(v)=v^\mathsf{T}H_{\rm up}v-
2\max_i\left(v^\mathsf{T}C_iw-\operatorname{ceil}_{10^{-12}}
 \sqrt{(v^\mathsf{T}E_iv)(w^\mathsf{T}E_iw)}\right)
+\min_i w^\mathsf{T}S_iw.
\]

The archived original MG43 full matrix residual upper independently implies the scalar upper v^T U_MG43 v. Taking the MIN of the two separately valid SCALAR uppers for the SAME fixed source ray is rigorous. It is NOT a Loewner matrix minimum, and it does NOT prove an inequality for unspecified source rays.

## Convex-parameter analytical reduction

For fixed rational v and w, under a convex mixing parameter alpha between MG24 and MG29 source first-moment Loewner enclosures, c(alpha) is affine, while the square-root geometric mean sqrt(a(alpha)b(alpha)) is concave for nonnegative affine a,b. Consequently c(alpha)-sqrt(a(alpha)b(alpha)) is convex and its maximum occurs at alpha=0 or 1. Independently mixing the two S uppers is affine in beta and its minimum likewise occurs at an endpoint.

Therefore, within THIS simple per-ray Cauchy-support construction, two parental endpoints already cover the entire continuous first/second moment convex mixing family. This is not a no-go for genuinely correlated new moment information, alternative source response, or a full-source matrix SDP.

## Pinned actual-source witness set and acceptance

MG44 evaluates three independently accepted original rational rays at each of four original mesh/cutoff configurations (16/32 cells × cutoff k12/k16):

1. Exact negative source ray of the selected MG43 conservative lower certificate for the fixed B.
2. Exact negative source ray of the prior MG41 full fee-bearing conservative lower certificate for the SAME B.
3. Exact negative upper fee-scale threshold source ray from MG42 for that SAME B.

For each of 12 rays, export genuine original v, Bv, complete-source MG24 and MG29 exact first-moment center, error energies and outward square roots, second-moment bounds, original Hlo/Hup scalars, the independently valid directional residual upper, inherited MG43 scalar upper, their safe scalar intersection, and the exact new lower certificate margin.

An independently run Actions audit REBUILDS all 12 directional original source values and all root inequalities from pinned accepted MG24 #39378465438, MG29 #39440914565, MG40 #39513403010, MG41 #39519080670, MG42 #39520549337 and MG43 #39522608989. The original-source result and all numerical claims require this audit to PASS.

Important: A nonnegative lower bound on any of these 12 rays is a directional result only, never full 24D strict matrix positivity. A negative source LOWER-certificate scalar is not a negative eigenmode of the actual original Weil operator. No new full original 470D inverse, signed odd 51/56 negative cap, complete even/Weil/CC27/RH, or independent original Fourier/form/domain closure is proved. Canonical W-ODD-NEG remains OPEN.

CI pending.
