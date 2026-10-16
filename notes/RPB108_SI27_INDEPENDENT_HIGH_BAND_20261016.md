# RPB108 SI27 — independent original signed high-frequency positivity joins the supported inverse

**Parent:** SI26 merged at \`7587601c0fd1d511b9c0453831ee4ef20b168547\` (PR #121).  
**Track:** structural SI, physically supported original signed archimedean and seven-prime Fourier form; native RC high-Schur remains independent.  
**Status:** strict numerical comparisons are conditioned on the accompanying exact-rational validator and final-head GitHub Actions. No full Birman–Schwinger certificate, original Weil positivity, Stage I, F4, Lean, or RH.

## 1. Change families after SI26's exact stopping certificate

SI26 established that the *entire* higher-Legendre-moment remainder of the two SI23 outer frequency bands carries operator norm less than \(1.3653\times10^{-5}\), and the resulting continuous-band **reference-only** inverse pole response remains \(>2.04549\). This does **not** constrain the stronger original \(A_o\), but it proves that refining those two bands alone cannot close the one-pole threshold \(1\).

Rather than continue their moment chain, SI27 brings in **an independent signed-original positive-frequency interval whose whole-frequency positivity was already certified in SI14**:
\[
J_7=[219/100,223/100]=[2.19,2.23],\quad
c_7=221/100=2.21,\quad r_7=1/50,\quad\delta_7=1.
\]
The SI14 128-cell rigorous signed prime/digamma lower bound and global derivative enclosure establish
\[
m(\xi)>\kappa+\delta_7=1.001\quad\text{for every }\xi\in J_7
\]
and likewise on its reflected negative interval. This is not an inferred extension of another window or a numerical sample. It is disjoint from the six existing positive windows
\[
[.22,.28], [.28,.32], [.32,.38], [.74,.78],
[1.18,1.22], [1.63,1.67].
\]

## 2. True supported physical rank-nine reference

SI25's eight vectors are the six exact Jensen frequency means plus first orthogonal Legendre moments on the two SI23 outer bands. Retain all eight. Add the **true** Jensen mean
\[
g_7(x)=\frac{1}{2r_7}\int_{c_7-r_7}^{c_7+r_7}
\sin(2\pi\xi x)d\xi
=\sin(2\pi c_7 x)\operatorname{sinc}(2\pi r_7 x),
\quad x\in[-11/10,11/10].
\]
The original signed Hilbert-space Fourier quadratic and Jensen positivity give, on the **actual physically supported odd** carrier \(H_o\),
\[
A_o\succeq C_9
=C_8+4r_7\delta_7 |g_7\rangle\langle g_7|
=C_8+\tfrac{2}{25}|g_7\rangle\langle g_7|.
\]
All nine positive-feature coefficients retain their exact original frequency weights, the positive floor \(\kappa=1/1000\) is unchanged, and the actual operator inversion remains **after physical compression**. No whole-line reciprocal is used.

## 3. Full nine-feature signed Gram with exact-rational acceptance

Let \(G:\mathbb C^9\to H_o\) synthesize the *true* nine features, \(H=G^*G\) their **full signed physical \(9\times9\) Gram**, \(q=G^*s\) the true original source overlaps for \(s(x)=\sinh(x/2)\), and \(\Gamma=\operatorname{diag}(\gamma_1,\ldots,\gamma_9)\).

Using the exact supported Woodbury identity for the **reference** \(C_9\), and order reversal \(A_o^{-1}\preceq C_9^{-1}\), obtain
\[
\boxed{
2\langle s,A_o^{-1}s\rangle
\le 2\langle s,C_9^{-1}s\rangle
=2\left[\frac{\|s\|_2^2}{\kappa}
-\frac{q^*M^{-1}q}{\kappa^2}\right],
\quad M=\Gamma^{-1}+\kappa^{-1}H\succ0.
}
\]
No signed off-diagonal Gram coupling is dropped.

All **81** entries and all nine signed source overlaps use exact-rational analytic supported sine-overlap intervals and outward rounding. The genuine averaged features remain in the formula: Simpson quadrature is only an enclosure device. The rigorous uniform fourth-derivative remainder for each degree-zero averaged feature is
\[
\tau_j=\frac{(2\pi_{\rm hi}r_jB)^4}{180},\quad B=11/10,
\]
and the original first-moment features keep SI25's rigorously paid composite Simpson fourth-derivative bounds. The errors \(3\tau_j/4\) and \(4B(\tau_i+\tau_j)\) are charged to every source and Gram entry, respectively.

A rational midpoint solution chooses a *candidate* variational witness \(z\), while the certified inequalities evaluate its **true signed outer intervals**:
\[
q^*M^{-1}q\ge 2z^\top q-z^\top M z.
\]
A pass will establish the strict original-supported pole inverse upper bound
\[
\boxed{2\langle s,A_o^{-1}s\rangle<2.}
\]
The same validator separately records the reference \(C_9-2|s\rangle\langle s|\) quadratic **only on the fixed source \(s\)**, but this is not a Birman–Schwinger operator-norm certificate.

A preliminary numerical physical Gram evaluation, used only to choose the candidate band, estimated reference inverse values around \(2.1184\) (SI25 eight features) versus \(1.9452\) (adding SI14's \(2.21\) feature). These are **not certified claims** and omit outward interval costs. The accepted SI27 bound is whatever the rational CI certifies.

## 4. Interpretation / next frontier

The new window is genuinely independent of the previously exhausted two outer bands. Its contribution may materially improve the inverse response even if its source *diagonal* quadratic \(\gamma_7|\langle s,g_7\rangle|^2\) is small, because the inverse depends on the **entire signed physical Gram and its off-diagonal couplings**.

Even a strict inverse upper \(<2\) is still above the rank-one pole BS target \(1\). There is no evidence from this certificate alone that the original inverse response equals its reference bound, and the full negative-frequency original operator \(K_o\) remains untreated.

**SI28:** search for additional *disjoint originally signed positive* bands chosen by actual **incremental supported inverse leverage** (not only \(|\widehat{s}|\) or multiplier positivity), or transfer to a native original \(A_o\)-residual inverse certificate and the full SI11 Birman–Schwinger matrix. Compare the computational costs against RC, rather than automatically increasing Gram rank.

**Replay:** \`python scripts/validate_rpb108_si27_independent_high_band.py\`. Original all-frequency signed margin subproofs and exact-rational positive inverse dual acceptances must pass GitHub Actions. No standalone Lean formalization or independent peer-review is asserted.
