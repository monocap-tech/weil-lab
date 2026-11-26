# IV123 — Integrated original arithmetic receiver

Status: integrated IV105–109 and IV123 native Lean PASS at commit `08a5bfe4cbacec7674e52fd057804476f208186e`. This certifies the 28 named declarations selected by the integrated workflow, with only standard Lean axioms. IV110–122 remain mathematical specifications without executable Lean modules; no global positivity or RH result follows.

## Custody
- IV105–108 base: c9c1706677bb1f73ff6dbaa90dfed4e58346f821.
- IV104 exact repaired source: d228695bb70881d0cb2a9c38bd69373adc0d8200 (runs 45732560134 and 45732564118).
- IV103/109 source: c36b0d529618fb678070afad70be9db915059efd (IV109 runs 45739478439 and 45739485463).
- Exact source blobs copied, no modification to accepted theorem statements.
- IV110 specification preserved from 60b5565929b815ee046d6374586ea95b7e93ad03.

## Mathematical gates IV111–119 (not kernel-certified)
For fixed window and packed complement X, impose N physical cell means L. The combined packed smooth rows and piecewise constant cell indicators are independent by continuity at cell boundaries and vanishing at outer endpoints; smooth compactly supported tests are dense in physical L2, hence L|X is onto. Choose smooth h_i in X with L_j(h_i)=delta_ij; X=H+Z, Z=ker L.

For v in Z its primitive vanishes at cell boundaries. Dirichlet Poincare and Plancherel give low-band mass <=4 delta^2 T^2 ||v||² =16 a² T²/N² ||v||². Combined with IV110 Gårding and response payment, choose finite N,T for S_k(z)>=eta ||z||². If M>=0 bounds the error, convex combination with S_k>=||Jz||_log²-M||z||² yields W(xi)=eta/2+theta log(e+|xi|), theta=eta/[2(eta+M)], as a lower Fourier weight.

By exact packed response R, B_k(u,v)=B_a(u-Ru,v). IV109 bounds each smooth corrected row in physical L2. In the S_k-energy completion of Z, Riesz responses t_i satisfy B_k(h_i,z)=B_k(t_i,z). Set G_H=(B_k(h_i,h_j)), K=(B_k(t_i,t_j)). Exact square completion and density imply S_k>=0 on X iff G_H-K>=0. With trial y_i in Z set A_ij=B_k(h_i,y_j)+B_k(y_i,h_j)-B_k(y_i,y_j). Then K-A is the energy Gram of t_i-y_i. Residual physical rows r_i represent B_k(h_i-y_i,z); K<=A+E where E is their inverse-W Gram. For constraint representers F, replace residual synthesis R0 by R0-FD for any finite D. The inverse-metric minimizing D is (F*W^-1 F)^-1 F*W^-1 R0 if invertible. This is an upper payment, not a sign certificate. G_H-A-E>=0 is sufficient.

## Radius-2 attachment IV120–122
IV103 is quantified over arbitrary a>=0. At a=2, log n<=4 selects the 24 prime powers 2,3,4,5,7,8,9,11,13,16,17,19,23,25,27,29,31,32,37,41,43,47,49,53. Native angular coordinate is r=2 pi xi. Gamma symbol is Re psi(1/4+ir/2)-log pi, prime symbol 2 sum Lambda(n)/sqrt(n) cos(r log n). These agree at formula level with Canonical Return AP. Exact enumeration and the AP parity-circle comparison are not formalized here.

The native pole term is conj(l_-) l_+ + conj(l_+) l_-. Define c=(l_++l_-)/2 and s=(l_+-l_-)/2. Mixed pole is 2 conj(c_u)c_v-2 conj(s_u)s_v, and diagonal is 2|c|²-2|s|². It vanishes against either pole-null second argument. The new Lean module proves these identities directly from the native pole operator, subject to compilation.

Canonical Return BK (research/cr-int-t1d-co-odd-expansion, research/CR-INT-T1D-BK.md) uses radius 2, double pole-null carrier, 121 even /119 odd exceptional coordinates and relative coercivity 17/10000 and 53/10000, conditional on its inherited comparisons. Restore one moment coordinate per parity, giving candidate 122/120 finite receivers. For normalized moment coordinate, add +2 or -2 to the last diagonal entry of the Gamma-minus-prime Schur matrix. Tail unchanged since pole moments vanish there. Actual parity identity, smooth-core attachment, certified comparison operators, complete matrix signs and unrestricted support remain open. Do not substitute T1D matrices into radius 1.1 or treat a finite index bound as positivity.

No claim of Phase IV adoption, global positivity, or RH.

## Integrated native receipt and compiled-byte custody (2026-11-25 Pacific)

- Workflow run: https://github.com/monocap-tech/weil-lab/actions/runs/45748575818 at source commit `08a5bfe4cbacec7674e52fd057804476f208186e`.
- Fresh native target `ActualZetaIV123OriginalPoleReceiver` built successfully; the workflow archived five compiled `.olean` files for IV105, IV106, IV107, IV108 and IV123.
- Exactly 28 named source/axiom receipts passed. Their union of axioms is `{propext, Classical.choice, Quot.sound}`; no `sorryAx` occurs in these receipts.
- Artifact `15085227312`, SHA-256 `4d3b9a7deb4190626c28bb534cedd6a00f7b9036ba621629e79ac4b6f421583e`, 430971 bytes. Independent download verified the complete ZIP SHA-256, ZIP CRC, each of the five archived `.olean` SHA-256 entries, the 28 receipt records and the recorded commit. The exact archive is also retained as `iv123-integrated-compiled-custody.zip` in the project's file collection.
- Earlier native failure at IV105's `add_le_add_right` orientation was repaired by `add_le_add_left`; IV123's nonexistent complex numeral simplifiers were replaced by `norm_num <;> ring`. The successful run includes both repairs.

This receipt certifies the integrated named declarations and artifact bytes only. IV110–119 finite-codimension and response/Schur gates and IV120–122 radius-2 source/matrix attachment are still pending Lean implementations and original-form sign certification. The numerical Canonical Return certificates are not thereby literal Lean objects.
