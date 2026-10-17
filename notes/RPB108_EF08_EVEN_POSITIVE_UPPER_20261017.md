# RPB108 EF08 — original supported even positive-energy upper, with all frequencies paid

**Obligation:** W-EVEN-FORM (scoped), canonical W-ODD-NEG unchanged.
**Parent:** EF07 PR #152 merged at research HEAD 94527c66c0e05afe545a1b6fbe9d5188309a547a.
**Standing:** exact-rational original signed upper-energy *method discriminator* awaiting final-head CI. Not a completed even-form positivity proof, original full Weil criterion, global bridge or RH proof.

## What EF07 left open

For the actual physical even cosine \(f(x)=\cos(2\pi(19/25)x)\) on \([-B,B]\), \(B=11/10\), the full original seven-prime EF06 **negative upper cap** was rigorously bounded as
\[
0.8023309563<\langle f,K_{\rm cap,new,e}f\rangle<1.0198894827.
\]
The actual original positive form
\(A_e=Z^*\mathcal F^{-1}\max(m,\kappa)\mathcal FZ+2|\cosh(x/2)\rangle\langle\cosh(x/2)|\), \(\kappa=10^{-3}\), was only known within
\((0.4629763897,\ 2.6394610669)\). The broad upper arose from EF05's \(|\xi|\ge4\) analytic estimate \(35/32=1.09375\) and very coarse integer archimedean uppers on \([0,4]\). No strict comparison followed.

**EF08 changes the POSITIVE estimate, not the negative cap, and neither assumes nor redefines the signed original operator.** All frequency intervals and the favorable even pole remain charged.

## First complete signed region [0,4]

Partition [0,4] into exactly 4096 cells of width 1/1024. Use the rigorously monotone original archimedean upper \(\mathrm{arch}_{\rm up}(j/64)\) at the right endpoint of each containing 1/64 macrocell, derived from SI14's exact digamma Euler series and rigorous integral remainder, not floating-point sampling. For each 1/1024 midpoint \(q\), use the **original complete seven-prime signed cosine sum** interval upper \(p_{\rm up}(q)\), and the original \(|p'|<69\) derivative allowance:
\[
m(\xi)\le\mathrm{arch}_{\rm up}(\lceil64\xi\rceil/64)
+p_{\rm up}(q)+69/(2\cdot1024)
\quad\text{for every }\xi\text{ in the subcell}.
\]
Clip against \(\kappa\), round upward to exact \(10^{-6}\) rational units, and multiply by an exact outward upper of the **true zero-extended Fourier transform** \(F_z\) at \(q\), plus the physical Lipschitz remainder \(2\pi_{\rm up}B^2/(2\cdot1024)\). Charge both reflected signs. The entire [0,4] positive quadratic is covered, including portions with \(m<\kappa\).

## Second finite signed region [4,128]

Divide [4,128] into exactly 3968 rational subcells of width 1/32. Each original archimedean value is bounded by SI14's monotone original arch upper at the enclosing integer right endpoint; each prime contribution uses the true signed seven-prime cosine enclosure at its midpoint and a full \(69/(2\cdot32)\) phase/derivative allowance.

For this high region, the crude global Fourier derivative bound \(2\pi B^2\) is wasteful. Differentiate the exact physical transform
\[
F_z(\xi)=\frac12\left[\frac{\sin(2\pi B(\xi-z))}{\pi(\xi-z)}
+\frac{\sin(2\pi B(\xi+z))}{\pi(\xi+z)}\right],\quad z=19/25.
\]
At any \(\xi\ge l\ge4\), the correct derivative bound (including **both** shifted terms) is
\[
\boxed{|F_z'(\xi)|\le\frac{2B}{l-z}
+\frac{1}{\pi_{\rm lo}(l-z)^2}.}
\]
This pays the entire interval Fourier amplitude with the correct factor of two, and every local signed multiplier and amplitude is separately outward rounded in rational arithmetic. No compact-support boundary jump is discarded.

## True infinite positive tail [128,∞), both reflected signs

The inherited SI15 original growth estimate, valid for every \(\xi\ge4\), and EF05's physical Fourier decay give
\[
a(\xi)<12+\log(1+14\xi)<15+\log \xi,\qquad
|F_z(\xi)|^2<\frac1{8\xi^2}.
\]
Thus
\[
\boxed{
2\int_{128}^\infty a(\xi)|F_z(\xi)|^2\,d\xi
<\frac{16+\log128}{4\cdot128}
\le\frac{16+7\log_{\rm hi}2}{512}<\frac1{20}.
}
\]
The last rational logarithm upper is inherited from SI06. This shrinks the *high analytic tail alone* from 1.09375 to <0.05, but requires paying the substantial signed finite region [4,128] separately.

## Pole, test and disposition

Add the original exact-rational positive even pole **upper** from EF05:
\(2|\langle f,\cosh(x/2)\rangle|^2<0.315952\).
The result is a **whole** original supported quadratic upper
\[
\langle f,A_e f\rangle\le U_{[0,4]}+U_{[4,128]}+U_{\ge128}+U_{\rm pole}.
\]
The focused validator requires a strict improvement over EF07's 2.6394611 upper, with a conservative acceptance target \(<1.1\). It independently recomputes EF07's complete signed refined cap **lower** on the same physical vector and reports the certified difference
\[
\langle f,K_{\rm cap,new,e}f\rangle_{\rm lo}
-\langle f,A_e f\rangle_{\rm hi}.
\]
If positive, this certifies a method-class **no-go** for EF06's still-conservative cap. If not positive, the present comparison remains **INCONCLUSIVE**; the program must not promote a negative original even Weil direction or claim cap feasibility. Even if the method-class no-go is established, the true \(K_{\rm true,e}\le K_{\rm cap,new,e}\) may be far smaller.

**Next EF09:** sharpen only the remaining bounds necessary for a strict same-vector separation (for example the physical cap lower via better local Fourier enclosures, or positive [0,4] macrocell resolution), or switch to a direct original signed two-vector test if the full cap is no longer appropriate. Do not launch an enormous inverse based only on a one-vector pass.

**Replay:** python3 scripts/validate_rpb108_ef08_even_positive_upper.py.

**Standing:** W-EVEN-FORM OPEN. Complete original signed even-sector, full Weil, global bridge, Lean proof and RH all remain unproved; successful Actions is not independent mathematical peer review.
