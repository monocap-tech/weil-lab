# RPB108 SI22 — certified pole obstruction to the SI21 four-window reference-only Birman–Schwinger gate

**Parent:** SI21 merged \`d8c17dc3c7752dcfeaa5daccfcca112ec64d4cf7\` (PR #116).  
**Track:** original signed physically supported SI, independent of native RC high-Schur.  
**Status:** the accompanying exact-rational validator must pass before this becomes a certified numerical claim. This is a **negative result about the Jensen reference**, not a negative direction of the original Weil form.

## 1. The question SI21 left open

SI21 proved the physically supported odd positive-operator lower bound
\[
A_o\succeq C_4:=\kappa I+\sum_{j=1}^{4}\gamma_j|g_j\rangle\langle g_j|,
\qquad
\kappa=\tfrac{1}{1000},\quad
\gamma_j=4r\delta_j,\quad r=\tfrac1{50},
\]
with certified whole-frequency windows centered at \((0.30,0.76,1.20,1.65)\) and original signed multiplier margins \((2.7,1.25,0.85,0.70)\). It also derived a **matrix-valued inverse upper bound** using \(C_4^{-1}\).

Can this same reference suffice for a *complete* odd Birman–Schwinger comparison, without replacing it by stronger positive information?

**SI22 proves no.** It fails on one concrete original physically supported input \(f=s\), even when all negative-frequency Fourier couplings are discarded.

## 2. Exact witness and scalar inequality

On \(H_o\subset L^2([-B,B])\), \(B=11/10\), take the original negative odd-pole vector \(s(x)=\sinh(x/2)\) and set
\[
S=\lVert s\rVert_2^2=\sinh B-B,\qquad q_j=\langle s,g_j\rangle.
\]
The original SI21 **true frequency-averaged physical** vectors \(g_j\) remain in \(C_4\), and thus
\[
\langle s,C_4s\rangle
=\kappa S+\sum_{j=1}^4\gamma_j|q_j|^2.
\]
The negative pole alone is \(K_{\mathrm{pole}}=2|s\rangle\langle s|\), and
\[
\langle s,K_{\mathrm{pole}}s\rangle=2S^2.
\]

SI22 encloses \(S\) with SI12's rigorous rational \(\sinh(B)\) Taylor bounds, encloses all four \(q_j\) with SI21's signed physically supported sine-overlap intervals and fourth-derivative Simpson error, revalidates all four whole signed frequency windows, and uses **upper** intervals for each \(q_j^2\), including the entire fourth positive contribution. Its exact mandatory gates are
\[
\boxed{\ 2S^2-\langle s,C_4s\rangle>\frac{44}{1000}=0.044\ }
\]
and, by the **correct** variational Rayleigh quotient with \(f=s\),
\[
\boxed{
2\langle s,C_4^{-1}s\rangle
=\bigl\|C_4^{-1/2}K_{\rm pole}C_4^{-1/2}\bigr\|
\ge\frac{2S^2}{\langle s,C_4s\rangle}
>\frac{33}{20}=1.65.
}
\]
The first strict numerical inequality is an original physical source-vector test against the *reference*, not a numerical experiment on an unrestricted Fourier function. The lower bound \(1.65\) is conservative; SI21's independent, correct-sign inverse *upper* remains \(<3.181750\). These are consistent two-sided inequalities for the **reference inverse** only in the SI22 lower calculation and the **original inverse** in SI21's upper comparison; do not conflate the operators.

## 3. Consequence for the complete signed coupling

The SI11 negative operator (restricted to the odd physical sector) obeys
\[
K_o=Z^*\mathcal F^{-1}(\kappa-m)_+\mathcal FZ\big|_{H_o}
+2|s\rangle\langle s|\succeq K_{\mathrm{pole}}\succeq0.
\]
Therefore
\[
\boxed{\ 
\|C_4^{-1/2}K_oC_4^{-1/2}\|
\ge\|C_4^{-1/2}K_{\mathrm{pole}}C_4^{-1/2}\|
>1.65>1.\
}
\]

**Consequently, even a perfect implementation of SI21's four-direction *reference-only* matrix upper comparison cannot certify the desired full signed Birman–Schwinger norm \(\le1\).** Adding the negative-frequency block makes this reference criterion at least as difficult, not easier.

This is **not** a proof that the original \(A_o-K_o\) is negative: \(A_o\succeq C_4\), and the actual original positive operator may contain much more strength than this sparse Jensen reference. In particular the numerical bound is **not** a lower bound for \(2\langle s,A_o^{-1}s\rangle\). It is also not RH evidence in either direction.

## 4. Quantitative design criterion for SI23

For any stronger positive reference \(C_{\rm new}=C_4+\Delta\), \(\Delta\succeq0\), to avoid the **same \(s\)-witness failure**, it is *necessary* that
\[
\boxed{\,\langle s,\Delta s\rangle >
0.044\ \text{(or at least } \ge 2S^2-\langle s,C_4s\rangle\text{ exactly)}.\,}
\]
The exact necessary condition is \(\langle s,\Delta s\rangle\ge 2S^2-\langle s,C_4s\rangle\); the rational \(>0.044\) gate is a **lower bound on the required budget**, not a universally sufficient target. For any added Jensen windows, the additional source budget is precisely \(\sum_{\rm new}\gamma_j|\langle s,g_j\rangle|^2\) (assuming independent disjoint certified windows). Added directions with total budget \(\le0.044\) are therefore provably insufficient for this specific scalar necessary condition, regardless of favorable off-diagonal inverse signs.

**SI23 choice:** prioritize a larger *continuous-frequency positive* minorant or a native physical residual-supported inverse, explicitly reporting its added positive source budget. Only after beating this pole obstruction is it efficient to expand the entire SI11 signed BS matrix. Continue the independent, smaller RC high-Schur route; do not substitute a much larger SI matrix merely because the finite-rank reference can be inverted.

## Scope, provenance, replay

No certified original nonpositivity, no full \(\|A_o^{-1/2}K_oA_o^{-1/2}\|\), no Stage I, F4, Lean or RH closure. This is a **rigorous failure certificate for this specific rank-four sufficient-reference strategy**.

Run \`python scripts/validate_rpb108_si22_reference_pole_obstruction.py\`; the structural GitHub Actions workflow reruns all SI validators. Every acceptance comparison is exact \`Fraction\` arithmetic, with genuine analytic inequalities supplied by the cited earlier SI11/SI12/SI21 notes.
