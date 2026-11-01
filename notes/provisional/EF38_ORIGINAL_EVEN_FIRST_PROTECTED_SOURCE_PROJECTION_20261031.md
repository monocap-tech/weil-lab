# EF38 — Genuine original first SI10 source-row projection of the signed prime–pole response

**Date:** 2026-10-31 America/Los_Angeles. **Canonical theorem obligation:** W-EVEN-FORM OPEN. Parent EF37 [PR #441](https://github.com/monocap-tech/weil-lab/pull/441), final-head source [Actions #41251871731](https://github.com/monocap-tech/weil-lab/actions/runs/41251871731) SUCCESS. EF33 original genuine 471-bell signed coercivity and restricted first-source/kernel Schur S2>1/500, EF34 conditional unseen cofinite residual eta>0, EF37 original signed seven-prime/pole combined norm squared <7/10 and entire arch cutoff norm <3/5 retained with independent analytic-domain review.

## 1. The EXACT one-source projection (not the full 469-source projection)

Original SI10 first even protected source

[
e(x)=\mathbf{1}_{[-B,B]}(x)\cos(\omega x),\quad
B=11/10,\quad \omega=2\pi(37/64).
]

Let u=<cosh(x/2),e> be the *original* genuine even-pole first-source overlap, with EF32 outward interval u<0. Write the actual physical original **seven-prime-plus-pole** source response on the original I as

[
z(x)=-\sum_{n=2,3,4,5,7,8,9}w_n
 \bigl[e(x+\log n)+e(x-\log n)\bigr]
 +2u\cosh(x/2),\quad
 w_n=\frac{\log p}{\sqrt n},\ n=p^k.
]

No original n4/n8/n9 term is discarded. On each of the eight positive-half original source cutoff cells from EF37, the original seven signed prime translations take the exact form
z(x)=P_j cos(omega x)+Q_j sin(omega x)+2u cosh(x/2), with all interval coefficients retained at 340-digit outward fixed-point precision. Exact original physical primitive formulae give

[
\|e\|_{L^2(I)}^2
=B+\frac{\sin(2\omega B)}{2\omega},
]

and the signed source pairing

[
\langle z,e\rangle
=2\sum_{j=1}^{8}\left[
P_j\int_{a_j}^{b_j}\cos^2(\omega x)dx
+Q_j\int_{a_j}^{b_j}\sin(\omega x)\cos(\omega x)dx
+2u\int_{a_j}^{b_j}\cosh(x/2)\cos(\omega x)dx
\right].
]

The original strict 340-digit directed native source checks yield:

- true source physical squared norm \(\|e\|^2\) centered near **1.2363494115**;
- genuine correlated seven-prime/pole squared norm \(\|z\|^2\) centered near **0.66725385396**;
- actual signed pairing \(\langle z,e\rangle\) near **+0.79811961755**;
- original optimal single protected-row coefficient \(\alpha=\langle z,e\rangle/\|e\|^2\) near **+0.64554535324**;
- **true source-row projected physical squared residual**
  [
  \boxed{
  \|z-\alpha e\|_{L^2(I)}^2
  =\|z\|^2-\frac{\langle z,e\rangle^2}{\|e\|^2}
  \approx0.15203144352 <\frac4{25}=0.16.
  }
  ]

The rigorous result is the strict exact-rational outward inequality, not reliance on rounded floats. The reduction of the original prime–pole squared energy relative to \(\|z\|^2\) is approximately 77.2%. This is a **real original source projection**, not an abstract rational toy or unprojected triangle envelope.

## 2. Complete original signed response and first-source cofinite upper

The original full signed even first-source gradient is

[
g_e=a_{\rm arch}(37/64)e+z+h_{\rm arch,cut},
]

where the first arch multiplier row lies EXACTLY in genuine original SI10 V469, and the complete arch cutoff \(h_{\rm arch,cut}\) is EF26/EF29's original physical half-integer Laplace response. EF37 independently certified its full norm \(\|h_{\rm arch,cut}\|<3/5\), with the first 100 native source components and the entire infinite tail enclosed, not discarded.

Because the **actual original** first source e belongs to V469, the true physical orthogonal cofinite F=V469^perp satisfies P_F e=0. Consequently

[
\|P_Fg_e\|
=\|P_F((z-\alpha e)+h_{\rm arch,cut})\|
\le \|z-\alpha e\|+\|h_{\rm arch,cut}\|
<\frac25+\frac35=1.
]

With the original positive signed even SI10 complete cofinite lower bound
q_even(f,f)>mu||f||², mu=17/25000, the actual first-source full cofinite energy-dual and EF34 residual satisfy

[
\boxed{
0<\eta\le\|P_Fg_e\|^2/\mu
<\frac{25000}{17}\approx1470.5882353.
}
]

The lower eta>0 still relies on EF34's original noncanceling jump and independently stated pseudolocality/domain premises. The upper uses the original EF26/EF29 arch physical identity, EF32 genuine pole, SI06 all-seven prime translations, the SI10 cofinite floor and the exact real L2 source projection, with independent analytic form-domain review open.

This is approximately a **2.102-fold tighter upper than EF37** eta<105125/34. It does NOT establish eta<S2: the bound is still vastly above EF33 S2>1/500.

## 3. What was NOT computed and why EF39 is necessary

- The actual 469x469 protected-source Gram and all 468 other projected coefficients are **not** computed or inverted.
- The entire remaining arch cutoff response and its cross-correlation with the genuine prime–pole source z remain bounded by \(\|h_{\rm arch,cut}\|<3/5\), not integrated jointly; projecting it on the first e could improve the bound further.
- The genuine original cofinite Riesz inverse response and exact eta remain unmeasured.
- No original full-cofinite first-source Schur sign or 469D complete even Schur / W-EVEN-FORM PSD is certified.
- The earlier EF35 sufficient gate \(\|g_e-v\|^2<17/12500000\) for some original V469 combination remains UNMET.
- The odd branch remains paused OPEN, whole Weil and RH OPEN.

**EF39 entry:** compute a single correlation-preserving original physical source-gradient square including the complete quarter-digamma cutoff cross with all seven arithmetic shifts and true even pole, and its exact projection onto first protected row. Then, if quantitative condition warrants, add further explicitly verified original SI10 source modes one by one using stable positive-definite Gram/Schur certificates and finite-dimensional independent error bounds. Distinguish a verified partial source projection from the true entire 469-source projection; the full inverse-energy correction remains a separate gate.

## 4. Custody and verification separation

Validator: `scripts/validate_rpb108_ef38_original_even_first_protected_row_projection.py`.
Dedicated original 340-digit source workflow: `.github/workflows/ef38-original-even-first-protected-row-projection.yml`.
First native source Actions [#41258140982](https://github.com/monocap-tech/weil-lab/actions/runs/41258140982) **SUCCESS** with the original eight-cell signed projection, genuine EF32 positive pole, full EF37 arch tail, and governance PASS. Independent review of the original physical Fourier/quarter-digamma cutoff identity, strong source domain and cofinite form/core remains OPEN. No main merge. No RH closure.
