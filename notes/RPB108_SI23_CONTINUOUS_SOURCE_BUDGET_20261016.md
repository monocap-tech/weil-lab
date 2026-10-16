# RPB108 SI23 — continuous-frequency source recovery clears the SI22 rank-four witness

**Parent:** SI22 merged at \`45815f452cafe5bc79da910d9f1a6342ad1fdbc8\`, PR #117.  
**Track:** original signed physically supported Structural Investigation. Independent of the native RC high-Schur front.  
**Scope:** rigorous **positive source-quadratic** recovery for one original supported odd input \(s\). The augmented operator's full Birman–Schwinger norm remains unknown; this is not Stage I, global Weil positivity, Lean, F4, or RH.

## 1. SI22 obstruction and an unused continuous positive band

SI22 found that the SI21 rank-four Jensen reference \(C_4\) fails the original odd-pole necessary test on the actual physical function \(s(x)=\sinh(x/2)\):
\[
2\|s\|_2^4-\langle s,C_4s\rangle>0.04415827.
\]
Here \(C_4=\kappa I+\sum_{j=1}^4\gamma_j|g_j\rangle\langle g_j|\) on the **original supported odd Hilbert space** \(H_o\subset L^2([-11/10,11/10])\), with \(\kappa=1/1000\).

Crucially, SI13 had *already* certified the actual original signed archimedean/seven-prime multiplier \(m(\xi)>7/5\) throughout the *entire reflected* interval \(\pm[0.22,0.38]\). SI21 used just \([0.28,0.32]\) in that range. We can therefore add **without overlap or double counting** the original continuous positive-frequency contributions from
\[
E=[0.22,0.28]\cup[0.32,0.38],\qquad -E.
\]
Take \(\delta=1399/1000\), so \(m(\xi)>\kappa+\delta=1.4\) for every \(\xi\in\pm E\).

## 2. Genuinely continuous positive operator, not another Jensen rank-one

Define \(h_\xi(x)=\sin(2\pi\xi x)\) and
\[
T_{E,o}:=2\int_E |h_\xi\rangle\langle h_\xi|\,d\xi\succeq0,
\qquad
\boxed{C_{23}=C_4+\delta T_{E,o}\preceq A_o.}
\]
The integral \(T_{E,o}\) is **retained as a continuous-frequency operator**. It has not been replaced by a two-column (or other finite-rank) point-sampling approximation. The two SI23 midpoint evaluations are only tools for enclosing the integral of its true physical source energy.

This Loewner inequality uses *both* sets of independently certified frequency margins with disjoint supports: the four SI21 central Jensen windows and the two SI13 outer portions. Positive operator terms are additively dominated by the original supported \(A_o\), while the positive floor \(\kappa I\) is never eroded. Parity gives the reflected negative frequency halves exactly; the odd projection carries the factor 2.

## 3. Exact-rational lower bound on the continuous source energy

For the original physical odd source,
\[
q(\xi)=\langle s,h_\xi\rangle
=\int_{-B}^B\sinh(x/2)\sin(2\pi\xi x)\,dx,\quad B=11/10,
\]
so
\[
\langle s,\delta T_{E,o}s\rangle
=2\delta\int_E |q(\xi)|^2\,d\xi.
\]
Use SI18's *exact original physically supported analytic* rational interval enclosure for \(q\) at \(c_1=1/4\) and \(c_2=7/20\) and SI13's global rigorous derivative bound
\[
|q'(\xi)|\le
2\pi\left(4B\cosh(B/2)-8\sinh(B/2)\right)<3.
\]
Every \(\xi\) in each respective outer interval \([c_j-0.03,c_j+0.03]\) consequently satisfies
\[
q(\xi)\ge q_{\mathrm{lo}}(c_j)-0.03\,D=:a_j>0.43,
\]
where \(D\) is the explicit exact-rational upper enclosure on the derivative. The lower bound is valid at **every real frequency**, not just the midpoint.

The SI23 validator checks in exact \(\mathrm{Fraction}\) arithmetic:
\[
\boxed{2\delta\int_E |q(\xi)|^2\,d\xi
\ge 2\delta\sum_{j=1}^2 0.06\,a_j^2>0.063.}
\]
It independently recomputes SI21's four true frequency-averaged Jensen source overlaps with the Simpson fourth-derivative enclosure, both lower and upper source quadratics \(\langle s,C_4s\rangle\), the complete original negative pole \(2\|s\|^4\), the strict SI22 deficit, all four original signed central-window margins, and SI13's full continuous signed outer-window positivity.

The resulting mandatory gates are:
\[
\boxed{\langle s,C_{23}s\rangle-2\|s\|^4>0.018,}
\]
and, **only for the fixed test vector \(s\)**,
\[
\boxed{
\frac{2\|s\|^4}{\langle s,C_{23}s\rangle}<0.9.
}
\]
The latter is a single *Rayleigh quotient*, **not** an upper bound on the operator Birman–Schwinger norm or on \(2\langle s,C_{23}^{-1}s\rangle\).

## 4. Meaning and the next obligation

SI22's rigorous **reference-level necessary obstruction** for the original pole input \(s\) is now removed using original signed positive frequency information that was already available, but previously omitted by the sparse four-window Jensen reference.

This does **not** prove \(C_{23}\succeq 2|s\rangle\langle s|\). Even when the quotient at \(s\) is below 1, some other supported test vector may have a larger quotient; in fact the rank-one pole's exact Birman–Schwinger norm is \(2\langle s,C_{23}^{-1}s\rangle\), still unknown. Nor does it dominate SI11's **full** physically supported negative-frequency continuum \(K_o\). Passing the source-vector necessary test alone cannot imply Stage I positivity or RH.

**SI24:** build a finite positive *moment* minorant (e.g. orthogonal Legendre modes in each continuous frequency interval) or an actual physical residual-controlled inverse response for \(C_{23}^{-1}s\), retaining rigorous positive Bessel/Jensen variance. Measure the rank and residual costs against RC's independently certified native high-Schur route. Do not interpret this one-input recovery as a full operator spectral result.

**Replay:** \`python scripts/validate_rpb108_si23_continuous_source_budget.py\` with all prior SI regressions in GitHub Actions. No Lean or independent peer-review claim.
