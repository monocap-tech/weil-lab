# PS25 — FINITE-SCALE, nonshrinking second-generation seam absorption by a source-true signed 12-channel majorant

**October 17, 2026 · W-PHYSICAL-SHIFT · stacked on PS24.** The unchanged original physical SI10/CC27 seven-prime signed form, including the full nonlocal digamma kernel, genuine original prime powers, positive even pole, negative odd pole and 13-source energy-dual response, is used throughout. **W-ODD-NEG, W-EVEN-FORM, full original Weil positivity, native CC27 D-Riesz norm/domain transfer and RH remain OPEN.**

## 1. Why PS24's microscopic collar iteration was insufficient

PS23 certified the original signed source-adjusted Schur on 10 windows, with two true adjacent noncompact Carleman interfaces. PS24 demonstrated a second generation at width \(2^{-192}\), retaining a strict combined \(1/8\) gap. The tiny physical increment left the meaningful complement unresolved. The proof strategy used a conservative **single scalar gap** for the entire 10-window old block; its near-critical \(\alpha=9/50\) required an unnecessarily huge new local diagonal \(\beta\) to overcome a uniform \(\gamma\sim\pi/2\).

PS25 changes the proof architecture: **keep all 12 physical component energies and their individual cross-interactions together**, instead of eliminating the entire 10-window carrier through one nearly exhausted scalar pivot. This preserves the strong positive local energy at the actual interfaces and prevents positive spare capacity elsewhere from being lost to a global minimum eigenvalue bound.

## 2. Actual original physical windows; fixed, NONSHRINKING second generation

Let \(B=11/10\), \(L=1/128\), \(E=1/2048\), \(J=[1/32,5/128]\), \(V=[1/6,1/6+L]\), \(\ell_2=\log2\). The first eight physical windows \(U\) are
\[
-J-\ell_2,\quad -[\ell_2/2-L/2,\ell_2/2+L/2],\quad -V,\quad -J,\quad J,\quad V,\quad [\ell_2/2-L/2,\ell_2/2+L/2],\quad J+\ell_2.
\]
PS23's first-generation reflected collars are
\[
X_-=[-5/128-E,-5/128],\qquad
X_+=[5/128,5/128+E].
\]
**PS25's second-generation collars are NOT microscopic:**
\[
\boxed{
Y_-=[-5/128-2E,-5/128-E],\quad
Y_+=[5/128+E,5/128+2E].
}
\]
Their width is exactly **\(E=1/2048\), the SAME as the first-generation collars**. The twelve intervals are strictly nonoverlapping in interior and reflection-symmetric. There are **four genuine touching archimedean physical Carleman seams**: \(Y_-/X_-\), \(X_-/-J\), \(J/X_+\), \(X_+/Y_+\).

The total newly positive physical width, excluding the original source, is
\[
\boxed{8L+4E=\frac{33}{512}\approx0.06445.}
\]
Thus this **finite-scale structural result does not cover the full original physical interval** of length \(11/5=2.2\); even after adding the thirteen-source physical intervals, less than 5% of the original interval length has been included.

## 3. True original prime graph: all 7 powers, 2184 source cases, 3 positive-measure links

The exact thirteen-source physical intervals remain \(I_r=[-B+\log r,-B+\log r+\delta]\), \(\delta=2B-\log9\), for PS15's thirteen labels \(r\). The validator checks **all \(12\cdot13\cdot7\cdot2=2184\)** signed prime shifts between each source interval and each twelve-window interval. Every one has strictly positive outward-rational physical separation. Therefore the true *source-to-twelve-window original prime operator* vanishes by actual geometry, **not by neglecting the prime form**.

All \( {12\choose2}\cdot7\) original internal positive-prime shift configurations are also checked, with exact symbolic treatment of boundary contacts. The only **positive-measure** original prime connections between these twelve physical windows are the three true \(\log2\) links:
\[
(0,5,2),\quad(1,10,2),\quad(6,11,2)
\]
in left-to-right interval ordering. The two n=2 endpoint contacts \((0,4,2)\) and \((7,11,2)\) are genuine measure-zero contacts and have no mixed prime correlation; they are explicitly checked instead of being counted as nonzero links or ignored.

Each true internal prime edge contributes a worst-case signed operator cross norm
\[
w_2=\frac{\log2}{\sqrt2}<\frac12,
\]
and all other original internal prime powers \(3,4,5,7,8,9\) are absent by verified physical translation support. This statement is **restricted to the twelve-window carrier**; the seven-prime operator on the uncovered original complement is unchanged.

## 4. A certified finite-size SCALAR norm majorant of an infinite-dimensional original signed form

For **every** original-form-admissible function \(h\) supported in the twelve-window union, write its twelve separately form-admissible disjoint components \(h_i\) and set \(t_i=\|h_i\|_{2}\). The PS15 sharp-characteristic domain stability follows for all twelve intervals from the truncated original digamma kernel and Carleman operator bound; this is not a piecewise constant or finite-element assumption. The scalar vector \(t\in\mathbb R_{\ge0}^{12}\) records only the masses, **not a 12-dimensional approximation to \(h\)**.

Define a 12-by-12 symmetric rational **Z-matrix** \(M\), with nonpositive offdiagonals, such that
\[
\boxed{\mathfrak S_C[h]\ge t^\top M t.}
\]
This is a rigorous uniform operator block lower bound, preserving the **entire infinite-dimensional function space inside each window**:

* Original local arch/scalar diagonal:
  \(\ d_i=11/5\) on each original width-\(L\) window, using the original 64-term positive digamma bound; \(d_i=4\) on each of the four width-\(E\) collars, using PS23's verified 256-term original digamma bound.
* For **each of four genuinely adjacent** pairs, the original noncompact \(k(s+t)\) Carleman+regular cross operator norm is bounded by \(\pi/2+\sqrt{A_iA_j}\). An outward-rational \(\pi/2<11/7\) is used; no false compactness of these seams is assumed.
* For each other strictly separated pair of intervals of widths \(A_i,A_j\), at actual minimum separation \(d_{ij}>0\), the original kernel satisfies \(k(u)\le1+1/(2u)\) and Minkowski's Hilbert–Schmidt bound yields
  \[
  \boxed{\|B_{{\rm arch},ij}\|
  \le\sqrt{A_iA_j}
  +\frac12\sqrt{\frac{A_iA_j}{d_{ij}(d_{ij}+A_i+A_j)}}.}
  \]
  The proof integrates \((d+s+t)^{-2}\) **exactly** and uses
  \[
  \iint\frac{ds\,dt}{(d+s+t)^2}
  =\log\left(1+\frac{A_iA_j}{d(d+A_i+A_j)}\right)
  \le \frac{A_iA_j}{d(d+A_i+A_j)}.
  \]
  This improved original physical cross bound is essential for **nearby but not touching** U/Y pairs. The naive distance-minimum kernel bound loses more than the available positive margin.
* Every one of the three original nonzero n=2 prime edges contributes \(-w_2t_it_j\) as the worst-case real signed cross, with the correct quadratic factor \(2\) upon summation. All seven original prime powers are accounted for.
* The original positive even pole is dropped **only as a safe lower bound**. The full negative odd pole is bounded as a rank-one negative scalar form \(-2(\sum_i s_i t_i)^2\), where \(s_i=\sqrt{A_i}\sup_{W_i}|\sinh(x/2)|\), with source-rational bounds on the supremum.
* For the **complete true thirteen-source energy inverse**, define \(b_i\) as an exact outward-rational upper bound on \(\|B_{P,W_i}\|\), including every actual arch source rectangle and the TWO original signed pole source cross operators. No source-prime terms remain, by the 2184 verified shift checks. PS16's actual original source positivity \(A_P>323/1000\) implies the **complete source subtraction**
  \[
  \boxed{
  0\le\langle h,T_Ch\rangle
  \le\frac{(\sum_i b_i t_i)^2}{323/1000}.
  }
  \]
  This *rank-one scalar* subtraction retains source energy coupling between **all distinct windows**. It is not an artificial finite-matrix source inverse or a claim that the true source operator preserves physical channels.

Each rational scalar arch, prime, odd pole and source bound is rounded **OUTWARD**. In particular,
\[
M_{ii}
=d_i-2s_i^2-\frac{b_i^2}{323/1000},\qquad
M_{ij}
=-a_{ij}-w_{ij}-2s_is_j-\frac{b_ib_j}{323/1000}
\quad (i\ne j),
\]
where \(a_{ij}\) is the original arch cross upper bound and \(w_{ij}\in\{0,w_2\}\) is verified by physical source geometry.

## 5. A short exact-rational positive certificate: weighted diagonal dominance

Instead of trusting floating-point eigenvalues of \(M\), PS25 verifies a **single strictly positive INTEGER vector**
\[
\boxed{
v=(301,197,140,327,472,703,703,472,327,140,197,301).
}
\]
With rational target \(\mu=1/4\), the validator establishes for **EVERY \(i\)**:
\[
\boxed{
\sum_{j=1}^{12}M_{ij}v_j-\frac14v_i>0.
}
\]
Since offdiagonal entries of \(M\) are all nonpositive, congruence by the positive diagonal matrix \({\rm diag}(v)\) makes \(M-\frac14I\) a real symmetric matrix with strictly positive diagonal and strictly positive row-diagonal-dominance margins. Such a matrix is positive definite. Therefore this compact check **rigorously proves**:
\[
\boxed{M>\frac14 I.}
\]
Combining with the original infinite-dimensional source-aware form majorant yields the main *unshifted actual signed result*
\[
\boxed{
\mathfrak S_C[h]>\frac14\|h\|_2^2
\qquad
(0\ne h,\quad\operatorname{supp}h\subset\text{all twelve windows}).
}
\]
All four genuine noncompact arch interfaces, three genuine signed \(\log2\) original prime links, full arch cross between every separated window, the negative odd pole, positive even pole in the correct safe direction, and true original source inverse are accounted for. Since the carrier is reflection invariant, this applies **in BOTH even and odd parity sectors**.

**This is an actual finite-scale, nonshrinking second-generation result**. It is **not** the RH theorem, not original whole physical positivity, and not PSD of the as-yet-uncovered residual.

## 6. What PS25 changes, and remaining acceptance target

Earlier PS24 demonstrated a theoretical ability to add arbitrarily tiny positive collars but did not resolve whether the sequence could advance at useful physical widths. PS25 proves that the *seemingly necessary tiny scale was a by-product of compressing a heterogeneous, spatially localized system into one global \(9/50\) pivot*. Keeping the **strong individual block diagonal energies** and using a source-aware exact signed twelve-component **scalar majorant** allows adding the second generation at the **same scale as the first**, with a **larger certified \(1/4\) combined positive margin**.

But the new source+positive twelve-window carrier still covers **less than five percent** of the original physical interval by length. To establish **whole original physical signed Weil positivity**, all still-uncovered original complementary functions and every nonlocal arch/prime/pole/source interaction with them must be included. The PS25 finite-size scalar majorant is NOT a finite-rank approximation to the whole operator; it certifies positivity only for functions physically supported on the twelve-window union.

**PS26 next:** test a practical, geometry-adaptive partition of the **complete physical complement** into enough cells (including genuine source-prime and intercell prime links) and seek a **global** source-aware signed Z-matrix/weighted-positive-vector certificate with a strictly positive gap, or produce a genuine negative witness. The RC315 necessary global even-sector positive gap ceiling (<0.043 after PS22 two-step elimination) prohibits using the local \(1/4\) margin as a proposed global bound. The exact native CC27 D-Riesz bridge and independent functional-analytic audit remain mandatory for W-ODD-NEG/W-EVEN-FORM/RH promotion.

Replay \`python3 scripts/validate_rpb108_ps25_finite_scale_majorant.py\` runs PS24→PS23→...→RC315, checks 2184 source-prime and 462 internal prime configurations, all 66 original arch physical pairs, all source/P kernel rectangles, correct signed poles and source energy inverse majorant, and the **twelve strict rational weighted-diagonal-dominance inequalities**. The 12-by-12 matrix is a **scalar bound**, not an evaluation of the true infinite-dimensional inverse Gram. A successful scoped GitHub Actions replay does not substitute for independent review of the functional-analysis derivation.
