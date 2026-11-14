# NF514 — Authentic J242 selected-subspace leverage lower bound: NF513 cheap NO-GO gates fail

**2026-11-14 PT. SOURCE-ORIGINAL EXACT-INTEGER LOCAL PASS, with INDEPENDENT second exact-integer replay PASS. GitHub dedicated CI not accepted.** Stacked on NF513 draft PR #542; no merge into main, no full operator or RH claim.

## The actual decision

NF513 gave strict *conditional* one/two-cell original NF404 physical support NO-GO criteria if the full original selected-space leverage could be bounded above by:

| Original physical support addition | NF513 conditional original J242 leverage ceiling |
| --- | ---: |
| \(H_{4095}\) | \(\tau_{4095}\le3/25=0.12\) |
| \(H_{4094}\) | \(\tau_{4094}\le13/100=0.13\) |
| \(H_{4094}\cup H_{4095}\) | \(\tau_{\mathrm{union}}\le1/10=0.10\) |

The intended NF514 task was to measure the *complete original J242* leverages. Rather than blindly run the expensive historic 242D physical Gram/inverse, we can **disprove applicability of all three conditional sufficient tests with a fixed explicit original selected-subspace witness**.

### New certified original-source leverage LOWER bounds

Let \(O=[-549/500,549/500]\), \(B_o=549/500\), \(h=B_o/4096\), and let the true original NF505 selected space be \(J_{242}\). It contains the first **23 exact original selected generators**, with genuine original NF401/NF505 archived order

\[
j_{f,k}(x)=
\begin{cases}
x^k\sin(2\pi f x),&k\text{ even},\\
x^k\cos(2\pi f x),&k\text{ odd},
\end{cases}
\]
\(f=37/64\), \(k=0,\dots,13\) (14 generators), and \(f=211/128\), \(k=0,\dots,8\) (9 generators). The true original selected sinh pole and other 219 selected generators remain present in the total space; we are simply using a **23D subspace** to obtain an incontrovertible lower bound.

An explicit, immutable 23-vector of integer rational coefficients (denominator \(10^{105}\)) defines a genuine nonzero \(v\in J_{242}\), \(v(x)=\sum_{i=0}^{22}c_i j_i(x)\). The coefficient vector was *found numerically*, but after freezing those rational numbers **no eigenproblem, floating-point approximation, or candidate acceptance threshold remains anywhere in the proof**.

For any measurable \(D\subset O\), since the positive selected Gram \(G_O\) is from the authentic original selected space,

\[
\boxed{\tau_D=
\mathrm{tr}(G_O^{-1}C_D)
\ge
\frac{\int_D v(x)^2\,dx}{\int_O v(x)^2\,dx}.}
\]

This is a basic Rayleigh/trace inequality on the complete original physical \(J_{242}\), **not an estimate of a surrogate 23D full trace**. Adding the omitted selected generators cannot decrease the complete projection leverage. The original NF505 selected-basis node order and SHA-pinned genuine source are explicitly verified before any inequality is accepted.

Using two *independent exact integer* integrations of this SAME fixed original selected witness:

\[
\boxed{\tau_{4095}>\frac15=0.20},\qquad
\boxed{\tau_{4094}>\frac16\approx0.1666667},\qquad
\boxed{\tau_{4094\cup4095}>\frac25=0.40}.
\]

The actual rational witness Rayleigh quotients have source-authenticated outward displays

| Genuine source-original cell | Exact witness Rayleigh ratio, rounded | Rigorous simple lower |
| --- | ---: | ---: |
| \(H_{4095}\) | 0.2262513280276922865 | **> 0.20** |
| \(H_{4094}\) | 0.1741486503248350890 | **> 1/6** |
| \(H_{4094}\cup H_{4095}\) | 0.4003999783525273755 | **> 0.40** |

For the real original complete \(J_{242}\), each of the three actual \(\tau\) is **strictly GREATER** than the corresponding previously sufficient NF513 NO-GO upper ceiling \(0.12,0.13,0.10\). Hence the three proposed simple leverage-only conditional source gates are **rigorously UNREACHABLE for these actual physical cells**.

This is a **method obstruction to NF513's cheap exclusion route, not a support feasibility theorem**: it neither shows the physical cells can repair the selected NF404 gate nor rules out a more precise negative certificate involving the complete original *local fitted residual* \(e_D\).

## Exact-integer certificate, independent replay, source authenticity

The first verifier is \(\texttt{scripts/local_replay/verify_nf514_original_23D_edge_leverage_exact.py}\) with the immutable rational witness coefficients in \(\texttt{notes/data/provisional/NF514_original_J242_first23_exact_integer_selected_witness.json}\). It SHA-pins the genuine original NF505 original 242D physical source artifact raw SHA256 \(\texttt{ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec}\), verifies original NF407/NF406 source identity, exact original 23 generator nodes and original physical B/h geometry.

It reconstructs \(\pi\) using exact rational 140-term Machin \(16\arctan(1/5)-4\arctan(1/239)\), using the alternating remainder, and rigorously bounds the complete original \(\sin/\cos\) functions by exact fixed-point Taylor polynomials through degree 160. The coefficient and spatial scales are \(10^{160}\) and \(10^{250}\). The resulting *entire odd source-selected witness* \(v\) differs from its fixed-point polynomial \(q\) by strictly less than \(10^{-100}\) **uniformly on the entire actual O**. It computes \(q^2\) with integer polynomial convolution and integrates on all three true reflected physical supports using **exact rational monomial moments**, with absolute fee for integer factor quantization and the original true-function-vs-polynomial error.

Actual verified norm of the very small cancellation-preserving witness:

\[
\|v\|_{L^2(O)}^2\approx1.2466667124817237421600164628\times10^{-67},
\]

with an explicitly certified squared-integral absolute error \(<7.62\times10^{-117}\). The tiny absolute norm is **not** a problem: the fixed exact selected coefficients and high-precision rational error payments make the above Rayleigh comparisons rigorous rather than a near-singular floating-point LU assertion.

The **second independent all-integer verifier** uses 145-term Machin pi, 180 Taylor orders, polynomial scale \(10^{170}\), monomial factor scale \(10^{270}\), and a separate **direct double sum over polynomial monomial pairs** (not the first verifier's convolution). It independently checks all three strict simple rational lower bounds, source SHA/selected node identity, and overlap with the first arithmetic receipt. All passed locally. An additional 130-decimal mpmath quadrature was used for *non-certificate* cross-check only; it agrees with the exact results.

Local receipt SHA256:
- Primary original-source exact certificate: \(\texttt{b45b834bfebfdf7b8e3475e668e526d561c8cddb05a19bcfc4e98f9b945b4194}\).
- Independent re-evaluation: \(\texttt{e0a57060cee775a007ee02d74f71bc0832d3abc73be80e7a8eeb6ae4b5e966cb}\).
- Immutable original source-selected rational witness seed: \(\texttt{39a8679197447975f54629a04c9608659e47aadf61dffb6e5dea11d0df2dc6b0}\).

The source artifact itself is retained in prior original NF505 GitHub Actions run #43352403600, original native artifact #14004781980; its RC04 long-term backup remains OPEN. Original source-independent reintegration of the entire 242D Gram is **not performed** in NF514 because no such matrix inversion is mathematically necessary for this positive Rayleigh lower certificate.

## Standing

| Obligation | Standing |
| --- | --- |
| NF513 original H4094/H4095 complete W² | Source-exact LOCAL PASS |
| NF514 first 23 **original true selected** witness | Source-node SHA authenticated, exact integer coefficient witness |
| NF514 actual H4095 selected leverage lower \(>1/5\) | **SOURCE-EXACT LOCAL PASS** |
| NF514 actual H4094 selected leverage lower \(>1/6\) | **SOURCE-EXACT LOCAL PASS** |
| NF514 union selected leverage lower \(>2/5\) | **SOURCE-EXACT LOCAL PASS** |
| NF514 independent separate high-precision all-integer replay | **LOCAL PASS** |
| NF513 three leverage-only conditional physical NO-GO criteria | **RULED OUT as usable sufficient tests on these actual cells** |
| Full original 242D trace leverage numerical values | OPEN (and no longer necessary to reject the three cheap thresholds) |
| Original selected globally fitted local residual \(e_H\) | OPEN; NF512 native implementation staged, no accepted run |
| Original unconditional named-cell NF404 physical result | OPEN |
| Original admissible Weil multiplier/source image and graph domain | OPEN |
| W-ODD-NEG, full original even/odd Weil positivity, RH | OPEN |
| Focused GitHub CI | OPEN due repository repeated zero-job workflow failures; no main merge |

**Next NF515:** The local-energy-only-plus-*small*-leverage negative support route is now a rigorous **METHOD STOP for these specific cells**. Do NOT keep trying to prove \(\tau\le0.12\) or \(0.13\): the authentic original selected space contradicts those requirements. Recover and execute the full original **correlation-preserving locally fitted \(e_D\)** (NF512 architecture), or construct a sharper source-local projection-power upper certificate that remains valid at \(\tau\gtrsim0.17\) to \(0.40\). Compare source-specific observed raw local W² and the genuinely global selected fit; avoid treating pole-only local fits as globally correct. CI/source artifact custody RC02/RC04 remain separate. No RH promotion.
