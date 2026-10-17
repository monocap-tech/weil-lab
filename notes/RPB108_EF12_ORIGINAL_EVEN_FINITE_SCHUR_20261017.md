# RPB108 EF12 — original even form: cofinite-to-finite residual Schur reduction

**Priority-2 obligation:** W-EVEN-FORM. Canonical W-ODD-NEG remains the priority-1 obligation and is untouched.
**Parent:** EF11's direct original signed physical one-vector diagnostic, pending final-head exact rational CI.
**Standing:** structural conditional reduction and exact rational sign regression. Not an actual finite original Weil PSD certificate.

## Why the pivot is obligatory

EF10 demonstrated that the original EF06/EF07 *conservative*
negative-frequency cap does **not** satisfy the proposed domination
against the genuine positive even operator on a physical cosine.
No amount of inverting the same sufficient cap matrix can establish
that false domination.

EF11 instead evaluates the actual physical signed quadratic
\(q_e(f,f)=2\int_0^\infty m(\xi)|\widehat f(\xi)|^2d\xi
+2|\langle f,\cosh(x/2)\rangle|^2\)
on one even vector. That is a useful direct diagnostic but is not
all-vector positivity.

## Exact finite exceptional-space obligation

Assume the required original even Weil form \(q_e\) is densely
defined, closed, and lower semibounded on its actual physical
Hilbert-space form domain \(\mathcal D\). This form-domain property
must be checked in any instance; it is **not** established by this
abstract note.

Let \(V\subset\mathcal D\) be an explicit finite-dimensional
**even-parity invariant** exceptional space, and let
\(W=V^\perp\cap\mathcal D\). Assume an independently proved
original **signed** cofinite bound

\[
q_e(w,w)\ge\gamma\|w\|_2^2\quad(w\in W),\qquad \gamma>0.
\]

SI10 supplies a cofinite positivity mechanism, but the specific
even-sector exceptional basis, actual domain identification,
required \(\gamma\), and cross blocks must be carried explicitly.
Nothing here silently upgrades a surrogate cap to the original form.

Fix a real basis \(v_1,\ldots,v_d\) for \(V\). For each \(i\),
the original mixed functional \(w\mapsto q_e(v_i,w)\) must be
continuous on the Hilbert space \((W,q_e|_W)\). Given the stated
closed, lower-semi-bounded assumptions and a finite-dimensional
\(V\subset\mathcal D\), this follows from the usual shifted-form
Cauchy-Schwarz estimate and \(q_e|_W\ge\gamma\|\cdot\|^2\).
By Riesz representation, there is a unique \(h_i\in W\) with

\[
q_e(h_i,w)=q_e(v_i,w)\qquad\forall w\in W.
\]

Let \(A_{ij}=q_e(v_i,v_j)\) and define the **true original signed
Schur complement**

\[
\boxed{S_{ij}=A_{ij}-q_e(h_i,h_j).}
\]

Completing the form-square exactly proves

\[
\boxed{q_e\ge0\text{ on }\mathcal D\quad\Longleftrightarrow
\quad S\succeq0.}
\]

This is the exact whole even-sector acceptance test, subject to
the explicit form-domain and cofinite hypotheses. A positive
one-vector result, a positive finite Ritz restriction, or an
unverified numerical inverse does not imply it.

## Certified forward residual version — no hidden inverse

Choose finite computed approximations \(\widetilde h_i\in W\)
and original-form residual functionals

\[
r_i(w)=q_e(v_i,w)-q_e(\widetilde h_i,w).
\]

For the exact Riesz errors \(\delta_i=h_i-\widetilde h_i\),
\(r_i(w)=q_e(\delta_i,w)\). Suppose independently certified
**uniform dual energy** estimates give

\[
\|r_i\|_{W,q_e^*}^2\le\rho_i^2.
\]

The computable symmetric Ritz-Schur matrix is

\[
\begin{split}
M_{ij}
&=q_e(v_i,v_j)-q_e(v_i,\widetilde h_j)
-q_e(\widetilde h_i,v_j)
+q_e(\widetilde h_i,\widetilde h_j).
\end{split}
\]

Let \(E_{ij}=q_e(\delta_i,\delta_j)\). Exact completion gives

\[
\boxed{S=M-E,\qquad
0\preceq E\preceq
\left(\sum_{i=1}^{d}\rho_i^2\right)I_d.}
\]

Therefore an actually checkable **sufficient** criterion is

\[
\boxed{
M-\left(\sum_i\rho_i^2\right)I_d\succeq0
\quad\Longrightarrow\quad
q_e\succeq0\text{ on its full even form domain}.}
\]

It is safe but may be overly conservative; the exact Schur criterion
is necessary and sufficient, while the scalar residual test is only
sufficient. If the matrix test fails, it does NOT show the original
even form fails.

## Required non-negotiable attachments before completion

- Explicit parity-preserving physical exceptional carrier \(V\), with its original even-domain basis and actual SI10 cofinite \(\gamma\).
- Every original signed \(q_e(v_i,v_j)\) matrix coefficient, including all seven-prime frequencies, infinite tail and even pole.
- Original-form approximate Riesz lifts \(\widetilde h_i\), not a preselected false conservative cap inverse.
- Uniform full-complement dual-energy residual bounds \(\rho_i\), including the infinite complement. Finite matrix residuals alone are insufficient.
- Exact rational PSD certificate for the resulting finite Schur lower bound and an independent final-head audit.
- Downstream full Weil composition/global bridge and Lean original-zeta attachment remain separate open obligations.

The sibling odd research may share *algorithms* for residual certification,
but **no odd-sector theorem substitutes for this even obligation**.

**Executable:** `python3 scripts/validate_rpb108_ef12_even_finite_schur_algebra.py`.
The small exact-rational 2+3 dimensional block regression checks both
positive and negative toy cases and the residual sign, but does
not instantiate an actual original Weil operator.
