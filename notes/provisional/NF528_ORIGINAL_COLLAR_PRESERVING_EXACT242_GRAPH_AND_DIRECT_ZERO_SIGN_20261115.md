# NF528 — The ORIGINAL 242-moment smooth approximation can stay INSIDE the original collars

**2026-11-15 PT: NEW ANALYTIC PROOF, not newly Lean-compiled.** Original NF494 U400 SHA \`39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181\` unchanged. Retains NF523 source bounds and rank, NF524 actual all-multiplicity two-source sampling/graph facts and unconditional divisor dyadic count, and NF527 two-collar positivity. No Green-span density, no assumed RH, no generic physical native Fourier-multiplier bridge required for this carrier-specific zero-side sign.

## Critical strengthened construction

Let \(B=11/10,\ \delta=1/500,\ a=B-\delta,\ c=B-\delta/2,\ E=(-B,-a)\cup(a,B)\). Let \(\ell_U\) be the original source-built real odd NF498/NF523 endpoint logarithmic vector, and \(h=\mathbf1_{(a,B)}\ell_U\) its original positive-collar half, with \(\ell_U(x)=h(x)-h(-x)\).

For \(1/2\le s<1\), define \(h_s(x)=h(c+(x-c)/s)\). Its support lies in \((c-s\delta/2,c+s\delta/2)\Subset(a,B)\). Choose even unit-mass \(\eta_{\epsilon_s}\in C_c^\infty\) supported in \((-\epsilon_s,\epsilon_s)\), with \(\epsilon_s=(1-s)\delta/4\), and set \(g_s=(h_s-h_s\circ(-\mathrm{id}))*\eta_{\epsilon_s}\). Then **\(g_s\in C_c^\infty(E)\), is odd and real, and \(g_s\to\ell_U\) in \(H^{1/4}\)**: the fixed separation of collars permits positive/negative H^{1/4} cutoff, affine compression is strongly continuous, and the mollifier radius tends to zero. This is more precise than the global dilation in NF524: *nothing leaves E*.

For ALL complex \(z\) in the actual zero strip \(|\Im z|\le1/2\), the ONE-COLLAR endpoint-log estimate inherited from the original NF523/NF524 U400 and derivative-tail source is
\[
 |F_h(z)|\le C(1+\log(2+t))/(1+t),\quad t=|\Re z|,\quad C=10^{-4}.
\]
Its proof is the same original M0/M1 small/large-height split and integration by parts performed separately on the positive collar, not a synthetic source. Crucial affine Fourier identity:
\[
F_{h_s}(z)=s\,e^{iz(1-s)c}\,F_h(sz).
\]
Since \(s(1+t)/(1+st)\le1\), \(\log(2+st)\le\log(2+t)\), and the phase/mollifier moduli are uniformly bounded on the strip, \(F_{g_s}\) obeys a uniform constant \(8C\), hence \(F_{g_s-\ell_U}\) a constant \(9C\), times the SAME logarithmic-over-linear envelope.

For each actual divisor dyadic band \(D_n\), the preexisting proved bound \(#D_n\le A(n+2)2^n\) WITH all multiplicities and the true two-source samples \(p_\pm(f;q)=[F_f(\bar z_q)\pm F_f(z_q)]/\sqrt2\) give a uniform squared tail
\[
\sum_{n\ge N}\sum_{q\in D_n}(|p_+(g_s-\ell_U;q)|^2+|p_-(g_s-\ell_U;q)|^2)
\le16A(9C)^2\,\frac{2(N+2)^3+6(N+2)^2+18(N+2)+26}{2^N}.
\]
Finite-band convergence follows from L² and bounded window evaluation. Consequently **\(g_s\to\ell_U\) in the COMPLETE actual two-source graph norm**, not just physical H^{1/4}.

## Preserve EXACTLY all 242 original moments without ever leaving E

Select an even nonnegative \(\chi\in C_c^\infty(E)\) positive on a nonempty open subinterval of the positive collar and its reflection. Use the unchanged genuine 242 odd analytic \(j_i\) from NF522/NF523, including the sinh-pole mode. The true \(242\times242\) weighted Gram \(M_{ij}=\int\chi(x)j_i(x)j_j(x)\,dx\) is positive definite by inherited original analytic independence + identity theorem on ANY nonempty collar subinterval. This is existence, not a computed 242×242 inverse.

Put \(b_j=\chi j_j\in C_c^\infty(E)\), \(d_i(s)=\langle j_i,\ell_U-g_s\rangle\), \(c_s=M^{-1}d(s)\), \(\phi_s=g_s+\sum_{j<242}(c_s)_jb_j\). Each \(\phi_s\) is odd real **strictly collar-supported smooth**, preserves ALL 242 selected original moments **exactly**, and converges to \(\ell_U\) in the complete actual source graph: \(d(s)\to0\) by L², \(c_s\to0\), and each fixed smooth \(b_j\) has \(\ell^2\) source samples by complex-strip \(O(t^{-2})\) Fourier decay and the existing actual multiplicity dyadic count.

Thus the simultaneous triple gate is met at the analytic level:
\[
\phi_s\in C_c^\infty(E),\quad\forall i<242:\langle j_i,\phi_s\rangle=\langle j_i,\ell_U\rangle,\quad
\|\phi_s-\ell_U\|_{\rm full\ two-source\ graph}\to0.
\]

## Direct genuine ZERO-side sign, no generic native multiplier identity required

For EVERY \(\phi_s\), its true smooth compact autocorrelation \(C_s(t)=\int\phi_s(u)\overline{\phi_s(u-t)}du\) has entire transform \(F_{C_s}(z)=\overline{F_{\phi_s}(\bar z)}F_{\phi_s}(z)\) (the repository's existing generic \`neutralWindowCorrelation_rawTransform\` identity). The ACTUAL imported \`Zeta23.WeilEF.EF_lit_zeta\` directly yields the genuine multiplicity-preserving zero-side sum
\[
Z(\phi_s)=\sum_q\overline{F_{\phi_s}(\bar z_q)}F_{\phi_s}(z_q)
=\mathrm{ARCH}(\phi_s)-\mathrm{PRIME}(\phi_s)+\mathrm{POLE}(\phi_s).
\]
All \(\phi_s\) lie inside E, so the **NF527 full support-only coercivity** now holds on EVERY approximant, and **only n=9** appears in the prime term on every approximant:
\[
Z(\phi_s)>\tfrac1{10}\|\phi_s\|_2^2.
\]
The full-two-source graph norm converges, hence both raw sample families converge in \(\ell^2\), and \(Z(\phi_s)\to Z(\ell_U)\) by Cauchy–Schwarz. Taking the limit gives \(Z(\ell_U)\ge\tfrac1{10}\|\ell_U\|_2^2\). The inherited original NF523 nonzero \(U(B)<-10^{-11}\) and derivative bound imply \(\|\ell_U\|_2^2>3.2\cdot10^{-32}\), hence **analytically \(Z(\ell_U)>3.2\cdot10^{-33}>0\)**.

**This route does NOT require NF526's separate uncompiled generic native Fourier-multiplier identity!** The signed source covariance is the same full zero-side sum by elementary source P/N algebra and the ACTUAL conjugate-ordinate divisor involution, including all multiplicity copies. In the Hilbert graph convention the two \(\sqrt2\) normalizations give samples \((A\pm B)/2\), hence \(\sum_q(\overline{P_f}P_g-\overline{N_f}N_g)=\sum_q\overline{A_f}B_g\). The existing repository's \`neutralLogPairSource_mixed_difference\` establishes the pointwise arithmetic on its constructed Green images; its generalization to full source graph has not been Lean compiled.

## Verification and strict scope

Local script \`scripts/local_replay/verify_nf528_collar_preserving_geometry_and_normalization_exact.py\` checks strict E support under rational affine contractions and mollifier margins, fixed interior Gram correction support, the 1/10 NF527 rational margin, exact P/N Hilbert/zero-side mixed normalization on a ten-row paired divisor pattern retaining multiple copies, and the dyadic tail recurrence. All rational checks PASSED locally. These checks are NOT the infinite-dimensional analytic proof, DO NOT replay original U400, DO NOT compute original 242×242 Gram inverse, and are NOT a Lean build.

- New original E-preserving exact-242-moment **graph convergence**: ANALYTIC, formal Lean OPEN.
- Direct genuine smooth correlation imported explicit formula: mathematical premise already in repo; generic specialization Lean OPEN.
- Same-original-vector positive **zero-side/source quadratic**: ANALYTIC conditional on these graph premises; Lean OPEN.
- General native Fourier multiplier identity on arbitrary source: separate OPEN, no longer prerequisite here.
- Original Green packet closed-span membership, global W_ODD_NEG and RH: OPEN.
- New CI, main merge: NOT DONE.

**NF529:** Formally compile the minimal direct smooth E-correlation EF, graph P/N normalization and collar-preserving exact-moment source-graph limit; then promote this original-source *positive* certificate. Do not substitute unrelated Green density or global RH claims.