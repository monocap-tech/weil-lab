# RPB108 SI29 — original physically supported odd-pole threshold test

**Parent:** SI28 merged at \`4799a0033a7b3ff1efd5998b85c5005a73ccbc9f\` (PR #123). **Track:** Structural SI; independent native RC high-Schur front. **Status:** the strict pole-only result is contingent on a passing exact-rational validator and final-head Actions.

## Why SI29 changes the significance of the bound

SI28 rigorously established the original odd inverse scalar
\[
2\langle s,A_o^{-1}s\rangle<1.159387
\]
on the *original physical carrier* \(H_o=L^2([-11/10,11/10])_{\rm odd}\), using eleven original signed positive-window Jensen/Bessel features. However, the **pole-only** Birman–Schwinger gate requires the **upper bound** to be less than \(1\).

A numerical **screen only** of additional disjoint positive bands suggested the three:
\[
\begin{array}{c|c|c|c}
c &J=[c-r,c+r],\;r=0.02&\delta&4r\delta\\\hline
0.72 &[0.70,0.74]&0.75&0.06\\
2.80 &[2.78,2.82]&0.40&0.032\\
3.40 &[3.38,3.42]&4.00&0.32
\end{array}
\]
The original eleven-window reference has nine different physical frequency bands, and these three are disjoint from every old band (the first touches SI21's \([0.74,0.78]\) only at an endpoint). They are also mutually disjoint. Reflections to negative frequencies are included by evenness of the original signed multiplier.

## Actual signed whole-frequency certificates

Each proposed margin must pass SI28's **exact-rational whole-frequency** test:
\[
\operatorname{arch}_{\rm lo}(a)
+\operatorname{prime}_{\rm lo}((a+b)/2)
-\frac{69}{2}(b-a)>\kappa+\delta,\qquad
\kappa=1/1000,
\]
for every one of the 128 rational subcells \([a,b]\) in each new band. The archimedean monotonicity, original seven-prime signed cosine intervals, and derivative magnitude less than 69 are re-used from SI06, SI13, SI28. Consequently, *if the validator passes*, \(m(\xi)>\kappa+\delta\) for **every real \(\xi\)** in each reflected band. A pointwise numerical scan is not a certification.

## Fourteen-feature true physical positive reference

For \(h_\xi(x)=\sin(2\pi\xi x)\) and \(J=[c-r,c+r]\), the **true supported** mean
\[
g_{c,r}(x)=(2r)^{-1}\int_Jh_\xi(x)d\xi
=\sin(2\pi cx)\operatorname{sinc}(2\pi rx)
\]
satisfies the exact positive Jensen variance inequality
\[
2\int_J |h_\xi\rangle\langle h_\xi|\,d\xi
\succeq4r|g_{c,r}\rangle\langle g_{c,r}|.
\]
SI29 retains all eleven true SI28 positive Jensen/Bessel features, including its two degree-one orthogonal moments, and adds the three **independently supported** mean features. Thus for \(\Gamma=\operatorname{diag}(\gamma_j)>0\) and true synthesis \(G:\mathbb C^{14}\to H_o\):
\[
A_o\succeq C_{14}=\kappa I_o+G\Gamma G^*
\succeq C_{11}\succeq\kappa I_o.
\]
This is the **original signed physical operator**, not a whole-line reciprocal or an unconstrained Fourier projection.

Set \(H=G^*G\), \(q=G^*s\), \(s(x)=\sinh(x/2)\), \(M=\Gamma^{-1}+H/\kappa\succ0\). The correct-sign Woodbury bound holds:
\[
2\langle s,A_o^{-1}s\rangle
\le 2\langle s,C_{14}^{-1}s\rangle
=2\left[\frac{\|s\|^2}{\kappa}-\frac{q^*M^{-1}q}{\kappa^2}\right].
\]
For any exact rational dual witness \(z\),
\[
q^*M^{-1}q\ge 2z^*q-z^*Mz.
\]
The validator pays **all 196** entries of the *true* full signed physical Gram with their correct signs. SI18's original supported analytic sine-overlap bounds supply its center-node enclosures; normalized Simpson is *only* an enclosure of the **true** averaged and degree-one moment functions, with the **uniform fourth-derivative error** included. All fourteen source overlaps, the physical support and the original scalar floor are retained. The mathematical gate, to be accepted **only on passing CI**, is
\[
\boxed{2\langle s,A_o^{-1}s\rangle<1.}
\]

This yields a **strict pole-only original odd-sector Birman–Schwinger theorem**:
\[
\left\|A_o^{-1/2}(2|s\rangle\langle s|)A_o^{-1/2}\right\|
=2\langle s,A_o^{-1}s\rangle<1,
\qquad
A_o-2|s\rangle\langle s|\succ0.
\]
The exact gate is about the **actual original supported \(A_o\)** through a rigorously subordinate positive reference, not a claim that the actual inverse equals the reference inverse.

## Vital limitation: original negative-frequency coupling remains

The full odd negative operator from SI11 is
\[
K_o=K_{{\rm negfreq},o}+2|s\rangle\langle s|,
\qquad K_{{\rm negfreq},o}\succeq0.
\]
SI29 **does not** bound \(A_o^{-1/2}K_{{\rm negfreq},o}A_o^{-1/2}\) or any cross-effect in the full Birman–Schwinger norm. Strict pole-only positivity can be destroyed by an additional negative continuum. Nor does SI29 address the original even sector, all apertures, Stage I, F4, Lean formalization or RH.

**Next SI30:** retain the original pole margin and bring in at least one **genuine signed negative-frequency** supported mode, with a certified *matrix-valued* inverse comparison and complete operator-norm remainder. SI11's finite negative-frequency compression error and the independent native RC high-Schur machinery are the relevant comparators. Do not call SI29 an RH proof or a full signed BS certificate.

Replay \`python scripts/validate_rpb108_si29_pole_threshold_three_bands.py\`. The integration workflow reruns every older SI validator. All numerical acceptances are in Python \`fractions.Fraction\`; the Loewner identities are analytic, not Lean formalization.
