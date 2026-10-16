# RPB108 SI24 — certified rank-six supported Jensen inverse comparison from SI23 continuous bands

**Parent:** SI23 merged \`3841b6af8947b3f0e9cb6acf80327eb48c6cd6af\` (PR #118).  
**Front:** independent SI original signed physically supported Fourier program; the native RC high-Schur route remains primary and independent.

## 1. From one-vector positive recovery to an inverse upper comparison

SI23 proved an actual physically supported **one-input** quadratic surplus by retaining the full continuous-frequency positive operator on the outer bands
\[
E=[0.22,0.28]\cup[0.32,0.38].
\]
That did not control the Birman–Schwinger supremum, and it did not estimate the inverse \(C_{23}^{-1}s\).

SI24 constructs a **second**, smaller positive reference \(C_6\preceq C_{23}\) that is finite-rank over the original scalar floor \(\kappa=1/1000\). This provides a tractable, certified **inverse upper bound** for the original supported odd operator \(A_o\).

Retain all four SI21 frequency-averaged features at centers \(0.30,0.76,1.20,1.65\), each with radius \(0.02\) and original signed multiplier margin \((2.7,1.25,0.85,0.7)\). Add Jensen-averaged sine features centered at \(0.25,0.35\), each with radius \(0.03\) and margin \(1.399\). The latter margins follow from SI13's **all-frequency** original signed \(m(\xi)>1.4\) throughout \(\pm[0.22,0.38]\). All six positive-frequency windows are disjoint up to endpoints, so no positive multiplier contribution is counted twice.

Let \(h_\xi(x)=\sin(2\pi\xi x)\) on the true physical interval \([-11/10,11/10]\). For each window \(J_j=[c_j-r_j,c_j+r_j]\), use its **true** average
\[
g_j(x)=\frac1{2r_j}\int_{J_j}h_\xi(x)\,d\xi
=\sin(2\pi c_jx)\,\operatorname{sinc}(2\pi r_jx).
\]
Exact Jensen/variance positivity gives
\[
T_{J_j,o}=2\int_{J_j}|h_\xi\rangle\langle h_\xi|\,d\xi
\succeq4r_j|g_j\rangle\langle g_j|.
\]
Hence on the original odd supported Hilbert carrier,
\[
\boxed{
A_o\succeq C_{23}\succeq C_6
=\kappa I_o+\sum_{j=1}^{6}\gamma_j|g_j\rangle\langle g_j|,
\quad\gamma_j=4r_j\delta_j.
}
\]
The \(\kappa\) floor is retained exactly. No whole-line reciprocal or unsupported replacement of the physical inverse occurs.

## 2. Full actual supported \(6\times6\) inverse comparison

Let \(G:\mathbb C^6\to H_o\) synthesize the true six \(g_j\), and let
\[
H_{ij}=\langle g_i,g_j\rangle_{L^2([-B,B])},
\quad q_i=\langle g_i,s\rangle,
\quad \Gamma=\operatorname{diag}(\gamma_j),
\quad M=\Gamma^{-1}+\kappa^{-1}H.
\]
Since \(H\) is the actual physical Gram, \(M\succ0\). By inverse order and the **reference-only** Woodbury identity,
\[
2\langle s,A_o^{-1}s\rangle
\le2\left(\frac{\|s\|_2^2}{\kappa}
-\frac{q^*M^{-1}q}{\kappa^2}\right).
\]
For any rational \(z\in\mathbb Q^6\), the exact variational inequality is
\[
q^*M^{-1}q\ge2z^\top q-z^\top Mz.
\]
The candidate \(z\) comes from a rational midpoint system only; its actual variational score is bounded **from below** using outward signed intervals for every \(q_i\) and \(M_{ij}\), so all 36 physical Gram entries and every cross term are paid with correct signs. The validator uses SI18's exact rational physical analytic sine-overlaps, with Simpson only to enclose the *true* frequency-averaged features.

For each individual window radius \(r_i\),
\[
\tau_i=\frac{(4\pi r_i B)^4}{2880}
\]
bounds the true average minus its normalized three-point Simpson quadrature **uniformly** over physical \(x\in[-B,B]\). For differing radii,
\[
|\langle g_i,g_j\rangle-\langle \tilde g_i,\tilde g_j\rangle|
\le 2B(\tau_i+\tau_j),\quad
|\langle s,g_i\rangle-\langle s,\tilde g_i\rangle|
<\frac34\tau_i.
\]
These bounds avoid *all* hidden truncation and physical-support errors.

**Exact gate to be certified in Actions**:
\[
\boxed{2\langle s,A_o^{-1}s\rangle<9/4=2.25,}
\]
a strict improvement from SI21's \(<4\) mandatory rational gate (SI21's tighter displayed numerical upper was 3.181749...). This is an **upper** bound; being above 1 does not imply that the actual inverse response exceeds 1.

## 3. Stronger finite reference also clears SI22's original source witness

In addition, SI24 computes a **lower bound on the rank-six reference's own** quadratic response
\[
\langle s,C_6s\rangle=\kappa\|s\|^2+\sum_{j=1}^6\gamma_j|\langle s,g_j\rangle|^2.
\]
The exact rational validator asserts
\[
\boxed{\langle s,(C_6-2|s\rangle\langle s|)s\rangle>0.046}
\]
and the single-vector Rayleigh quotient
\[
\frac{2\|s\|_2^4}{\langle s,C_6s\rangle}<0.71.
\]
The latter quotient is **not** the supremum over supported inputs, hence not the rank-one pole BS norm \(2\langle s,C_6^{-1}s\rangle\).

This distinguishes SI22's reference failure, SI23's continuous source recovery, and SI24's physically supported **inverse upper comparison**.

## 4. Remaining obstacle / SI25 gate

SI24 does **not** establish the one-pole inverse threshold \(2\langle s,A_o^{-1}s\rangle\le1\), let alone the complete SI11 negative-frequency Fourier continuum, its signed physical couplings, or positive original Weil form. A rank-six reference may still be far weaker than the complete continuous-frequency supported positive operator. It may be computationally wiser to exploit **frequency-moment rank two or higher** over each outer band, and then to construct a matrix-valued positive reference for the full signed BS block with correct residuals. Compare costs to the separate 301-direction native RC high-Schur route.

**SI25:** expand from mean-only Jensen to at least one additional *orthogonal* frequency moment per continuous band, retaining an exact positive Bessel remainder. Certify the resultant 8×8 (or larger) full physical Gram and odd-pole inverse **upper**; then evaluate whether actual supported \(K_o\) matrix computation is now competitive.

Replay: \`python scripts/validate_rpb108_si24_jensen_six_inverse.py\`. All numerical accept/reject decisions use Python \`Fraction\`; CI reruns all SI validators. No Lean formalization or independent complete RH proof is claimed.
