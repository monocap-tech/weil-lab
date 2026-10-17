# RPB108 EF07 — full original signed even cap feasibility screen

**Obligation:** W-EVEN-FORM, explicitly scoped; canonical W-ODD-NEG remains active.
**Parent:** EF06 merged [PR #149](https://github.com/monocap-tech/weil-lab/pull/149) at e5e61ffadf43992fbbde5520e09871d64308bdc2.
**Standing:** full-global original supported Rayleigh interval pilot. The sign of the separation is to be determined by **final-head exact-rational verification**, not assumed. There is no entire even-form, full Weil, global-bridge or RH proof.

## What EF06 did and did not establish

EF05 excluded the unchanged original SI10 upper-cap method by a certified even cosine witness. EF06 reduced the certified entire cap mass from 37.62605884375 to 29.60374846875 by splitting 64 unresolved signed leaves on [0,1] into 256 original signed microcells, with exact physical whole-cell error and moment positivity. The EF05 witness's [0,1] contribution fell from an OLD rigorous lower >4.4154 to a NEW rigorous upper <0.8251.

These are different operators, and that local comparison alone does **not** establish a whole-frequency inequality of either sign.

## Entire original signed refined cap on the identical physical witness

Fix \(B=11/10\), \(\kappa=1/1000\), \(z=19/25\), and the physically supported even \(f(x)=\cos(2\pi zx)\) on \([-B,B]\). EF05 already established the exact physical zero-extension Fourier expression
\[
F_z(\xi)=\frac12\left[\frac{\sin(2\pi B(\xi-z))}{\pi(\xi-z)}
+\frac{\sin(2\pi B(\xi+z))}{\pi(\xi+z)}\right].
\]
The original odd/even parity-appropriate cap operator is
\[
K_{\rm cap,e}=2\int_0^\infty w(\xi)\,|\cos(2\pi\xi x)\rangle
\langle\cos(2\pi\xi x)|\,d\xi.
\]
Replay all **973 SI10 unresolved original signed positive-frequency dyadic leaves** and replace the 64 leaves in [0,1] by exactly 256 EF06 refined subcells. For every cap cell below 4, use full exact outward rational Fourier midpoint sine/π intervals and the signed physical derivative bound \(|F_z'|\le2\pi_{\rm hi}B^2\). Round the lower amplitude DOWN and the upper UP in 10^-6 rational units before squaring. Thus the exact full continuum on [0,4] is bounded from both sides, *not* approximated by sampled values.

For every original cap leaf \([l,r]\) above 4, use the inherited EF05 analytic bound
\[
|F_z(\xi)|^2<\frac{1}{8\xi^2}\le\frac{1}{8l^2},
\qquad \xi\in[l,r],\quad l\ge4.
\]
The entire reflected high-frequency cap is bounded above by the exact rational sum \(\sum_{l\ge4}w_I(r-l)/(4l^2)\), with rigorous lower 0. All high original signed unresolved bands up to 896 are paid; the signed protected exterior has true negative multiplier and both caps zero. No frequencies are silently omitted.

This constructs exact rational bounds
\[
K_{\rm new}^{\rm lo}(f)\le\langle f,K_{\rm cap,new,e}f\rangle
\le K_{\rm new}^{\rm hi}(f).
\]

## Independently bounded ORIGINAL positive form

Let the actual supported positive even operator be
\[
A_e=Z^*\mathcal F^{-1}a\mathcal FZ\big|_{H_e}
+2|c\rangle\langle c|,\quad a(\xi)=\max(m(\xi),\kappa),
\quad c(x)=\cosh(x/2).
\]
For a genuinely independent lower, begin with \(\kappa\|f\|^2\) (exact interval for the physical cosine norm), then add every certified signed-positive surplus from [0,4]:
\[
2\sum_{I\subset[0,4]} |I|\,
[(m_{\mathrm{lo},I}-\kappa)_+]_{\rm down}
(|F_z|_{\mathrm{lo},I})^2.
\]
Each \(m_{\mathrm{lo},I}\) uses SI07's exact monotone 64-term rational archimedean lower at the left endpoint of its **1/8** containing cell, the true seven signed-prime lower enclosure at each of 256 midpoints, and the original global 69 derivative bound across its whole width. This is conservative but rigorously positive whenever certified. Add the **lower** exact positive even pole \(2|\langle f,c\rangle|^2\) using SI12 hyperbolic and SI14 trig intervals. The upper uses EF05's already validated entire original signed 256-cell positive upper [0,4], complete analytic \(|\xi|\ge4\) logarithmic tail, and positive even pole upper.

Thus a second interval
\[
A_e^{\rm lo}(f)\le\langle f,A_e f\rangle\le A_e^{\rm hi}(f)
\]
is rigorously independent of the negative-cap envelope.

## Decision tree, *not* a preselected outcome

Define
\[
\Delta_{\rm lo}=K_{\rm new}^{\rm lo}-A_e^{\rm hi},
\qquad
\Delta_{\rm hi}=K_{\rm new}^{\rm hi}-A_e^{\rm lo}.
\]
- If \(\Delta_{\rm lo}>0\), the **new entire EF06 cap is still too conservative**, yielding a genuine one-vector obstruction to EF06's sufficient cap, not to the original signed Weil form.
- If \(\Delta_{\rm hi}<0\), the **single test function** now passes the cap comparison, but this is not a full operator proof and does not certify the 890-source Schur.
- Otherwise, the certified intervals overlap, and the same-vector full-global feasibility question is **INCONCLUSIVE**; sharpen only the needed cells or change the pilot.

The validator prints the explicit result and enforces all input coverage, correct inequality orientations, exact tail accounting and arithmetic. It never asserts the unknown sign in advance.

**Next EF08:** act on the actual EF07 classification: tighten the offending signed band(s) if no-go, sharpen the separation estimates if inconclusive, or construct a small genuine supported two-or-more-vector coupled feasibility test if the single-vector check passes. In every case W-EVEN-FORM, original full Weil form, the global bridge, Lean attachment and RH remain OPEN.

**Replay:** python3 scripts/validate_rpb108_ef07_global_even_witness.py. The exact rational arithmetic does not replace independent mathematical review of the inherited explicit formula/operator model.
