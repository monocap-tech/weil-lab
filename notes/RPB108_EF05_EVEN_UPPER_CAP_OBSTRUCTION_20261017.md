# RPB108 EF05 — the EF04 full signed upper cap fails on one original supported even vector

**Obligation:** W-EVEN-FORM, explicitly scoped local work; canonical W-ODD-NEG remains active and unaffected.
**Parent:** EF04 merged PR #143, research integration HEAD 9cc3c190161c8cc9bcf4fda14d5717c7de6ba555.
**Standing:** exact-rational original-supported-even method-class obstruction PASSED, focused EF05 Actions run 39015954905 at research-PR source head 8429f85210417bea51fd661057036a0465679182. Final-head post-note/governance replay and independent peer review remain separate. This is a negative result for an *upper-envelope sufficient method*, NEVER a negative original Weil-form witness.

## 1. The method to test, and what would refute it

For \(B=11/10\), \(H_e=L^2([-B,B])_{\mathrm{even}}\), \(Z\) physical zero extension, and original seven-prime-plus-archimedean Fourier symbol \(m\),
\[
a=\max(m,\kappa),\quad r=(\kappa-m)_+,\quad\kappa=10^{-3},\quad
A_e=Z^*\mathcal F^{-1}a\mathcal FZ\big|_{H_e}+2|c\rangle\langle c|,
\quad c(x)=\cosh(x/2).
\]
The **true** even Weil form is \(Q_e=A_e-K_{\rm true,e}\), where \(K_{\rm true,e}\) is the physical compression of \(r\).

EF04's explicit 890-source route instead introduced an **upper cap**
\[
0\preceq K_{\rm true,e}\preceq K_{\rm cap,e}
\preceq (1+\tau)UCU^*+\eta I,\qquad
\tau=2^{-16},\ \eta<1.93\cdot10^{-8},
\]
where \(K_{\rm cap,e}=2\int_0^\infty w(\xi)|\cos(2\pi\xi x)\rangle\langle\cos(2\pi\xi x)|d\xi\), and \(w_I=\kappa+h_I\) is SI10's **conservative full original signed frequency upper envelope** on all the protected-complement unresolved rational leaves.

For the EF04 sufficient Schur gate to hold, it is necessary that \(A_e\succeq K_{\rm cap,e}\), since \(K_{\rm cap,e}\preceq(1+\tau)UCU^*+\eta I\). It therefore suffices to exhibit a *genuine physical even* \(f\) for which
\[
\boxed{\langle f,K_{\rm cap,e}f\rangle>\langle f,A_ef\rangle.}
\]
This would disprove the EF04 *method* — not the original inequality \(A_e\succeq K_{\rm true,e}\) — because the upper cap may be much larger than the true signed-negative multiplier.

## 2. One supported cosine, exact global bounds

Select the explicit form-domain vector
\[
f(x)=\cos(2\pi z x)\quad(x\in[-B,B]),\qquad z=\frac{19}{25}.
\]
It is even, physically supported, and belongs to the positive operator's form domain: its zero extension has \(|\widehat{Zf}(\xi)|=O(|\xi|^{-1})\), while the original positive symbol has only logarithmic growth.

Its Fourier transform is the real, even, explicit entire function
\[
F_z(\xi)=\frac12\left(
\frac{\sin(2\pi B(\xi-z))}{\pi(\xi-z)}
+\frac{\sin(2\pi B(\xi+z))}{\pi(\xi+z)}\right),
\]
with removable singularities interpreted by continuity.
Its entire nonnegative frequency derivatives satisfy
\[
|F'_z(\xi)|\le2\pi B^2
\]
by differentiating the physical Fourier integral and using \(|f|\le1\). No arbitrary Fourier truncation or sampled substitute for the true physical vector is used.

### Lower bound for the actual EF04 cap

Reconstruct SM10's complete exact SI10 all-real signed cover — 973 unresolved positive-frequency dyadic leaves in 107 clusters, with rational heights \(h_I\) and all original seven signed prime terms retained. To lower-bound \(K_{\rm cap,e}\), *drop safely* all positive-frequency leaves outside \([0,1]\) and retain the reflected companions via the factor 2:
\[
\langle f,K_{\rm cap,e}f\rangle
\ge2\sum_{I=[l,r]\subset[0,1]}(h_I+\kappa)|I|
\left[\max\{0,\operatorname{abslo}(F_z((l+r)/2))-\pi_{\rm hi}B^2|I|\}\right]^2.
\]
The exact Fourier center values are enclosed by SI14's rational sine and Machin \(\pi\) intervals, with full derivative-width errors. All cap weights are exact original rational SI10 caps, not midpoint guesses. The focused validator requires the exact rational result to exceed **4**.

### Upper bound for the true original supported positive operator

On \(0\le\xi\le4\), split into 256 rational intervals of width \(1/64\). On each \(I=[l,r]\), with midpoint \(q\), use the genuine full original signed interval **upper**
\[
m(\xi)\le
\operatorname{arch}_{\rm upper}(\lceil r\rceil)+p_{\rm upper}(q)
+\tfrac{69}{2}(r-l),
\]
where SI14's \(\operatorname{arch}_{\rm upper}\) is the rigorous full digamma Euler-series tail and SI06's \(p_{\rm upper}\) contains the actual seven signed prime powers. The archimedean part is monotone on nonnegative frequencies. Then
\[
a(\xi)\le\max\{\kappa,m_{\rm upper}(I)\},\qquad
|F_z(\xi)|\le\operatorname{absup}(F_z(q))+\pi_{\rm hi}B^2|I|,
\]
and the exact rational sum over all 256 intervals, counting negative frequencies by reflection, upper-bounds the whole low-frequency positive contribution.

For \(|\xi|\ge4\), inherit SI15's original symbol bound
\(a(\xi)<12+\log(1+14|\xi|)\le15+\log|\xi|\).
Since \(z=19/25\), \(|\xi|\ge4\) and \(\pi>3\),
\[
|F_z(\xi)|\le\frac{|\xi|}{\pi(\xi^2-z^2)},
\quad
\frac{1}{(1-z^2/16)^2}<\frac98,
\quad |F_z(\xi)|^2<\frac{1}{8\xi^2}.
\]
Using \(\log4<3/2\) yields the **entire two-sided infinite tail**
\[
2\int_4^\infty a(\xi)|F_z(\xi)|^2d\xi
<\frac14\frac{16+\log4}{4}<\boxed{\frac{35}{32}}.
\]
No high frequency or uncharged logarithmic tail is omitted.

Finally include the **genuine original positive even pole** with an exact supported hyperbolic/trigonometric overlap:
\[
\langle f,c\rangle=
\frac{2[(1/2)\sinh(B/2)\cos(2\pi zB)+(2\pi z)\cosh(B/2)\sin(2\pi zB)]}
{1/4+(2\pi z)^2}.
\]
SI12's rational hyperbolic Taylor bounds and SI14's rational trigonometric phase enclosures give an outward interval and the conservative pole-energy bound \(2|\langle f,c\rangle|^2<0.34\).

## 3. Acceptance and mathematical significance

The exact-rational validator enforces
\[
\langle f,K_{\rm cap,e}f\rangle>4,\qquad
\langle f,A_ef\rangle<\frac72,
\]
so that
\[
\boxed{\langle f,(K_{\rm cap,e}-A_e)f\rangle>\frac12.}
\]
The inequalities are required to pass on the *actual current signed source* before claiming this theorem. They prove **the EF04 sufficient condition is impossible**:
\[
A_e\not\succeq K_{\rm cap,e},\qquad
A_e-\big[(1+\tau)UCU^*+\eta I\big]\not\succeq0,
\]
and, since \(B_e=A_e-\eta I\succ0\) and \(D=(1+\tau)C\succ0\),
\[
\boxed{D^{-1}-U^*B_e^{-1}U\not\succeq0.}
\]
Thus it is not productive to spend more computational time seeking positivity of EF04's unchanged 890-source upper-cap Schur. No numerical ill-conditioning or failure of a chosen basis causes this obstruction; it follows directly from an original physically supported even witness.

**Critical boundary:** There is NO assertion that
\(\langle f,(A_e-K_{\rm true,e})f\rangle<0\).
Indeed \(0\le r\le w\) generally strictly, and EF04's cap is deliberately overconservative. This is *not* a counterexample to the original full even Weil form or RH.

**Next EF06 action:** replace the overconservative SI10 cellwise cap with a **tighter upper** of the true negative multiplier, especially at low frequencies, while still preserving rigorous global signed tails. Before building another expensive full-source inverse, test the same physical witness for the new cap. Alternatively use an explicitly proved native RC even-source transport; do not reattempt the disproved EF04 inequality.

Replay: python3 scripts/validate_rpb108_ef05_even_cap_obstruction.py. Final-head Actions checks arithmetic and inherited analytic Fourier/upper-symbol facts; not independent peer review or Lean original-zeta formalization.

## 4. Focused exact-rational certificate values

GitHub Actions [EF05 focused run 39015954905](https://github.com/monocap-tech/weil-lab/actions/runs/39015954905) completed **SUCCESS** on the source head before this evidence annotation. With outward lower rounding for cap amplitudes, upper rounding for all signed-original positive cells, and four monotone archimedean integer endpoint enclosures:

- The complete original supported positive energy satisfies `⟨f,A_e f⟩ < 2.639461066813` (displayed outward rounded upward).
- The complete original cap already satisfies `⟨f,K_cap,e f⟩ > 4.415423238009` using only 64 rational SI10 low-frequency leaves plus reflections.
- The strict method-obstruction margin is `⟨f,(K_cap,e−A_e)f⟩ > 1.775962171196` (displayed weaker downward rounding).
- The original even positive pole is **included**, with certified contribution `<0.315952`.
- The entire high-frequency positive Fourier tail is charged by `<35/32=1.09375`; every signed-original low-frequency cell uses a whole-continuum upper bound.

These stronger actual certified margins replace the weaker rational acceptance `cap>4`, `A<7/2`, `gap>1/2`. The previous EF04 cap-positive sufficient method is therefore **mathematically obstructed conditional on the inherited original explicit-formula/operator identity**, while the actual even Weil form and RH remain OPEN.
