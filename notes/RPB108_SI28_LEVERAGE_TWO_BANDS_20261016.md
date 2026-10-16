# RPB108 SI28 — inverse-leverage selection of two independent positive-frequency bands

**Parent:** SI27 merged in \`a222bdfa15331478bd6a8c2d8bc13d95532062bf\`, PR #122.  
**Front:** original signed supported structural SI; native RC high-Schur remains independent.  
**Status:** numerical gates are proposed until the full exact-rational GitHub Actions replay passes. Neither original full Weil positivity nor a complete negative-frequency Birman–Schwinger bound has been established.

## 1. Why test *inverse leverage* rather than positive-frequency height?

SI26 rigorously exhausted all higher moment refinements of the two SI23 outer bands as a way to make that restricted *reference* satisfy the pole threshold. SI27's independent positive band around 2.21 instead produced the certified original supported one-pole upper
\[
2\langle s,A_o^{-1}s\rangle<1.987944.
\]
That improvement was much larger than higher outer-band moment refinement. The natural next target is the **resolvent-leverage criterion**, not merely \(m(c)\) or \(|\widehat s(c)|\).

For a physical supported reference \(C\succ0\), a true mean Jensen feature \(g\), and its strictly positive coefficient \(\gamma\), the exact rank-one Sherman–Morrison identity gives
\[
\boxed{
2\langle s,C^{-1}s\rangle
-2\langle s,(C+\gamma|g\rangle\langle g|)^{-1}s\rangle
=
\frac{2\gamma|\langle g,C^{-1}s\rangle|^2}
{1+\gamma\langle g,C^{-1}g\rangle}\ge0.
}
\]
The leverage is controlled by the **actual physical inverse direction**, including all signed Gram cross-interactions. A band with a relatively small \(s\)-overlap can have high leverage, while a band with a high multiplier can be redundant.

A *noncertifying* numerical screen of whole-frequency signed multiplier candidates and the supported nine-feature Gram selected:
\[
\begin{array}{c|c|c|c}
\text{center}&\text{window}&\text{original signed margin }\delta&\gamma=4r\delta\\
2.10 &[2.08,2.12]&1.2&0.096\\
2.32 &[2.30,2.34]&2.5&0.20
\end{array}
\]
Both have \(r=1/50\) and are disjoint from each other and SI27's existing \([2.19,2.23]\) band, as well as the six earlier windows.

The screen estimated the reference responses \(\sim1.9452\) for SI27's nine features, \(\sim1.1642\) after adding the 2.10 feature, \(\sim1.2355\) with 2.32 alone, and \(\sim1.1111\) with both. These approximate values are **not acceptance criteria or rigorous results**; rigorous outward interval costs are charged below.

## 2. Whole-frequency positivity on original signed operator

For each new \([c-r,c+r]\), the code reuses SI13's exact rational archimedean monotone lower \(\mathrm{arch}_{\rm lo}(a)\), SI06's original signed seven-prime midpoint enclosure \(p_{\rm lo}\), and SI06's certified full prime derivative bound \(69\). In each of 128 rational cells \([a,b]\), it checks
\[
\boxed{
\mathrm{arch}_{\rm lo}(a)
+p_{\rm lo}((a+b)/2)-\tfrac{69}{2}(b-a)
>\kappa+\delta,\qquad\kappa=1/1000.
}
\]
The \(\pm\) reflected bands inherit the same positive original signed multiplier \(m\). These continuum certificates replace numerical multiplier sampling for *all acceptance decisions*. Previous SI21, SI13 and SI14 signed windows are also rechecked; all nine frequency intervals (seven old, two new) have disjoint interiors.

Write \(h_\xi(x)=\sin(2\pi\xi x)\) for the actual odd physically supported interval \(I=[-11/10,11/10]\). The true Jensen mean over the new window \(J=[c-r,c+r]\) is
\[
g_{c,r}(x)=\frac1{2r}\int_{c-r}^{c+r}h_\xi(x)d\xi
=\sin(2\pi c x)\,\mathrm{sinc}(2\pi r x).
\]
The exact Bessel/Jensen inequality on the supported odd carrier gives
\[
2\int_J |h_\xi\rangle\langle h_\xi|d\xi
\succeq4r|g_{c,r}\rangle\langle g_{c,r}|.
\]
Consequently the original positive operator obeys
\[
\boxed{
A_o\succeq C_{11}
=C_9+\tfrac{12}{125}|g_{2.10,\,0.02}\rangle\langle g_{2.10,\,0.02}|
+\tfrac15|g_{2.32,\,0.02}\rangle\langle g_{2.32,\,0.02}|.
}
\]
The original \(\kappa I\) floor is unchanged, and all original SI25 mean and orthogonal first-frequency-moment features remain.

## 3. Rigorous 11×11 physical inverse response

Let \(G\colon\mathbb C^{11}\to H_o\) synthesize the eleven **true** physical features and \(q=G^*s\), \(H=G^*G\) their full 11×11 signed physical Gram. Put \(\Gamma=\mathrm{diag}(\gamma_i)\succ0\) and \(M=\Gamma^{-1}+\kappa^{-1}H\succ0\). By inverse order and **exact** physical Woodbury,
\[
2\langle s,A_o^{-1}s\rangle
\le 2\langle s,C_{11}^{-1}s\rangle
=2\left(\frac{\|s\|^2}{\kappa}
-\frac{q^*M^{-1}q}{\kappa^2}\right).
\]
All 121 physical Gram entries and all eleven source overlaps are enclosed by SI18's exact-rational analytical supported sine overlaps; each true Jensen mean is enclosed by its rigorously charged single-panel Simpson fourth derivative, and the two true SI25 first moments use the existing rigorously charged eight-panel composite Simpson bounds. In particular
\[
\tau_{\mathrm{mean},j}=\frac{(2\pi_{\rm hi}r_jB)^4}{180},\quad
\tau_{\mathrm{moment},j}=\frac{3(4\beta_j^3+\beta_j^4)}{180}(1/4)^4,
\quad\beta_j=2\pi_{\rm hi}r_j B.
\]
The source and full physical Gram outward errors are paid conservatively by \(3\tau_i/4\) and \(4B(\tau_i+\tau_j)\). All signed cross couplings remain.

A rational midpoint linear solve picks a *dual witness* \(z\), but the true correction is rigorously bounded by
\[
q^*M^{-1}q\ge 2z^*q-z^*Mz
\]
evaluated with **all outward interval endpoints**. There is no whole-line reciprocal, source-only approximation, or omission of the positive inverse residual.

The code independently reproduces the original nine-feature upper, constructs a ten-feature upper with 2.10, an alternative ten-feature upper with 2.32, and the full eleven-feature upper. The proposed exact gates, subject to full CI, are
\[
\boxed{
\begin{aligned}
2\langle s,C_{9}^{-1}s\rangle&<2,\\
2\langle s,C_{10(2.10)}^{-1}s\rangle&<4/3,\\
2\langle s,C_{10(2.32)}^{-1}s\rangle&<3/2,\\
2\langle s,C_{11}^{-1}s\rangle&<5/4=1.25.
\end{aligned}}
\]
Because \(A_o\succeq C_{11}\), the last inequality certifies the same **upper** for the original supported odd pole response, if the exact validator accepts.

The difference of *rigorous upper enclosures* is not automatically a rigorous lower bound on leverage. The exact rank-one formula above establishes nonnegative monotonicity; interval-aware lower-gain certification would additionally require the two-sided supported inverse enclosures developed in SI26.

## 4. What this means and the next obligation

This is a stronger strategic route than simply increasing outer-band Legendre rank. But **1.25 is still above the necessary pole-only Birman–Schwinger threshold of 1**, and even closing the pole-only threshold would not dispose of the full supported original negative-frequency operator \(K_o\), its cross-couplings, or the even sector.

**SI29:** either find another **disjoint** original signed positive region with measurable *resolvent* gain (rather than positive multiplier height alone), or switch to a native physically supported inverse residual that captures the full operator instead of the sparse \(C_{11}\). Explicitly compare the cost to RC's independently developing high-Schur method. Stop adding low-leverage moments or counting reference-only nonnegativity as an original theorem.

Replay: \`python scripts/validate_rpb108_si28_leverage_two_bands.py\` and the full RPB108 SI regression. The exact-rational CI and analytic operator arguments certify only what is explicitly checked, not a formal Lean proof or a solution to RH.
