# NJDG-6 — mode-weighted critical-curvature transfer and finite-row nonspan

**Date:** 2026-09-30  
**Repository:** monocap-tech/weil-lab  
**Branch:** \`research/nextjet-derivative-geometry\`  
**Status:** **COMPLETE EXACT NO-BYPASS / THE FROZEN TWO-MODE RENJET NEAR KERNEL IS ENTIRE AND NONCONSTANT / ANY FINITE COLLECTION OF CRITICAL-VALUE AND CRITICAL-CURVATURE ROWS PRODUCES ONLY FINITE RATIONAL RESOLVENT KERNELS / NO EXACT LINEAR TRANSFER FROM FINITE DERIVATIVE-CRITICAL DATA TO THE MODE-WEIGHTED RENJET EXISTS / THE TWO-MODE FIRST-JET OBJECT IS EXACTLY THE LEADING COEFFICIENT OF THE EXISTING Q-LOC COMPLEMENT WEDGE / DERIVATIVE-GEOMETRY REENTRY NOW REQUIRES A GENUINELY NEW WEIGHTED OR INFINITE-FAMILY THEOREM / NEXTJET NOT PROVED**  
**Parent:** NJDG-5  
**Canonical Key-C status:** unchanged

## 0. Objective

NJDG-5 showed that a simple derivative critical point enriched by
\[
\frac{\zeta''(\tau)}{\zeta(\tau)}
\]
or
\[
\frac{\Xi''(\tau)}{\Xi(\tau)}
\]
supplies the first pole-removed logarithmic-derivative jet at \(\tau\).

NJDG-6 asks whether the already frozen SOURCE-II two-mode structure converts that unweighted critical curvature into the **mode-weighted** first RENJET without any complement-adaptive choice.

The answer is **no by exact kernel type**.

## 1. First RENJET for one exponential mode

For
\[
\psi_t(s)=e^{t(s-c)},
\]
write
\[
w_\mu=\mu-c
\]
and
\[
A=A_{F,\Omega}.
\]

SOURCE-II-3 gives the normalized first joint RENJET
\[
\mathfrak J(t)
=
\frac n2\psi_t''(c)
+
(\psi_tA)'(c)
+
\sum_{\mu\in\Omega}
m_\mu K_t(w_\mu),
\]
where
\[
K_t(w)
=
\frac{e^{tw}-1-tw}{w^2}.
\]

Since
\[
\psi_t(c)=1,\qquad
\psi_t'(c)=t,\qquad
\psi_t''(c)=t^2,
\]
we have
\[
\boxed{
\mathfrak J(t)
=
\frac n2t^2
+
tA(c)
+
A'(c)
+
\sum_{\mu\in\Omega}
m_\mu K_t(w_\mu).
}
\tag{1}
\]

Thus the mode-weighted near population is exactly
\[
\boxed{
Q_t(\Omega)
=
\sum_{\mu\in\Omega}
m_\mu K_t(w_\mu).
}
\tag{2}
\]

## 2. Mode-depth structure

The kernel has the entire expansion
\[
\boxed{
K_t(w)
=
\sum_{q=0}^{\infty}
\frac{t^{q+2}}{(q+2)!}w^q.
}
\tag{3}
\]

Equivalently,
\[
K_t(w)
=
\int_0^t
(t-r)e^{rw}\,dr.
\tag{4}
\]

Hence
\[
\frac{\partial^2}{\partial t^2}K_t(w)=e^{tw}.
\tag{5}
\]

The RENJET near term is therefore a finite Volterra transform of the local exponential population
\[
E_\Omega(r)
=
\sum_{\mu\in\Omega}
m_\mu e^{r(\mu-c)}.
\]

This is already the source-family geometry used by SOURCE-II. It is not an unweighted resolvent statistic.

## 3. Frozen two-mode wedge

SOURCE-II-7 fixes, from selected data only, a pair of positive mode depths
\[
t,u
\]
with a nonzero selected source wedge.

Let
\[
C(t),C(u)
\]
be the selected scalar-preservation mode row and
\[
N_C
=
\sqrt{|C(t)|^2+|C(u)|^2}.
\]

The selected-only construction guarantees
\[
N_C>0.
\]

The nonzero source wedge also forces
\[
t\ne u,
\]
because every antisymmetric wedge vanishes on the diagonal \(t=u\).

Define the first-RENJET wedge
\[
\boxed{
W_{\rm REN1}(t,u)
=
C(u)\mathfrak J(t)-C(t)\mathfrak J(u).
}
\tag{6}
\]

Its near-population kernel is
\[
\boxed{
W_{t,u}(w)
=
C(u)K_t(w)-C(t)K_u(w).
}
\tag{7}
\]

## 4. The frozen wedge kernel is nonconstant

Using (3),
\[
W_{t,u}(w)
=
\sum_{q=0}^{\infty}
\frac{
C(u)t^{q+2}
-
C(t)u^{q+2}
}{(q+2)!}
w^q.
\tag{8}
\]

Suppose \(W_{t,u}\) were constant.

Then its \(w^1\) and \(w^2\) coefficients would vanish:
\[
C(u)t^3=C(t)u^3,
\tag{9}
\]
\[
C(u)t^4=C(t)u^4.
\tag{10}
\]

Because \(t,u>0\), if either \(C(t)\) or \(C(u)\) vanished, (9) would force both to vanish, contradicting \(N_C>0\).

Thus both are nonzero. Dividing (10) by (9) gives
\[
t=u,
\]
contradicting the nonzero frozen wedge.

Therefore
\[
\boxed{
W_{t,u}(w)
\text{ is entire and nonconstant.}
}
\tag{11}
\]

## 5. What one enriched critical point can see

Let
\[
\tau=c+\delta
\]
be a simple derivative critical point.

The critical-value equation sees the near divisor through kernels of the form
\[
\frac1{\delta-w}.
\]

The critical-curvature equation sees
\[
\frac1{(\delta-w)^2}.
\]

After selected/completion terms are separated, any linear scalar extracted from the value and curvature rows has \(w\)-dependence in
\[
\boxed{
\mathcal R_\delta
=
\operatorname{span}
\left\{
1,\,
\frac1{\delta-w},\,
\frac1{(\delta-w)^2}
\right\}.
}
\tag{12}
\]

This is the critical-row span.

## 6. Exact one-point nonspan

Assume an exact linear transfer existed:
\[
W_{t,u}(w)
=
a
+
\frac b{\delta-w}
+
\frac d{(\delta-w)^2}.
\tag{13}
\]

The left side is entire.

Therefore the principal part of the right side at \(w=\delta\) must vanish:
\[
b=d=0.
\]

Equation (13) would then make \(W_{t,u}\) constant, contradicting (11).

Hence
\[
\boxed{
W_{t,u}
\notin
\mathcal R_\delta.
}
\tag{14}
\]

So one enriched critical point cannot exactly reconstruct the frozen mode-weighted near kernel by any linear combination of its critical-value and critical-curvature rows.

This is an algebraic no-bypass, independent of estimates.

## 7. Finite critical frames do not change the kernel type

Take finitely many derivative critical points
\[
\tau_j=c+\delta_j
\]
and, at each point, finitely many enriched logarithmic-derivative jets.

Their zero-divisor kernels lie in a finite span of
\[
\frac1{(\delta_j-w)^k},
\qquad
1\le k\le r_j.
\]

Any such finite linear combination is rational/meromorphic in \(w\), with poles only at the finitely many \(\delta_j\).

If it equals the entire function \(W_{t,u}(w)\) identically, every principal part at every \(\delta_j\) must vanish.

The zero-divisor contribution then collapses to an entire rational function, hence a polynomial; in the present finite-resolvent span it is in fact constant after the \(w\)-independent selected/completion rows are separated.

But \(W_{t,u}\) is nonconstant and contains an infinite Taylor tail.

Therefore
\[
\boxed{
\text{no finite collection of critical-value/curvature/higher-resolvent rows}
}
\]
\[
\boxed{
\text{can exactly synthesize the frozen mode-weighted kernel by a universal linear identity.}
}
\tag{15}
\]

This does not rule out a new nonlinear actual-zeta theorem, an approximation theorem on the actual finite zero set, or a continuum of critical data.

It closes the finite-row exact linear transfer.

## 8. The critical-point condition does not repair the nonspan

At a zeta-prime critical point,
\[
\frac{\zeta'}{\zeta}(\tau)=0.
\]

This supplies one additional first-resolvent relation among the actual zeros.

Modulo that relation, the available zero-divisor kernels remain in the same finite rational span.

The mode-weighted kernel remains entire and nonconstant.

Thus imposing the critical equation does not convert (14) into an identity.

## 9. Relation to the Q-loc complement wedge

SOURCE-II-4 writes the full tower mode value as
\[
T(t)
=
\sum_{r=1}^{K}
L^{-r}\mathfrak J_r(t).
\]

LOTUS-SHADOW-7 defines
\[
\boxed{
W_{\rm cmp}^{(K)}(t,u)
=
C(u)T(t)-C(t)T(u).
}
\tag{16}
\]

Expanding,
\[
W_{\rm cmp}^{(K)}(t,u)
=
\sum_{r=1}^{K}
L^{-r}
\left[
C(u)\mathfrak J_r(t)
-
C(t)\mathfrak J_r(u)
\right].
\tag{17}
\]

Therefore
\[
\boxed{
W_{\rm REN1}(t,u)
=
C(u)\mathfrak J_1(t)-C(t)\mathfrak J_1(u)
}
\tag{18}
\]
is exactly the first-jet coefficient of the already canonical multiplier-free complement wedge.

So even a theorem controlling the complete two-mode first RENJET is not a new independent geometry.

It is a leading-order theorem on the existing Q-loc complement-response shadow.

## 10. Why first-order control still would not close the tower

SOURCE-II-4 does not prove that
\[
\mathfrak J_1
\]
dominates the higher jets.

LOTUS-SHADOW-7 explicitly permits an internal-jet-cancellation branch in the normalized finite jet profile.

Hence a derivative-curvature theorem that controls only
\[
W_{\rm REN1}
\]
could leave
\[
r\ge2
\]
tower contributions projectively large.

Therefore the full derivative route would still require either:

1. a hierarchy theorem reducing the tower to the first jet; or
2. corresponding weighted control at every required finite jet order; or
3. a direct theorem on the full complement wedge.

The third is exactly RH-T0117 / the existing complement-wedge gate.

## 11. Exact outcome of the mode-weighted curvature attempt

NJDG-5 supplied:
\[
\text{critical point + curvature}
\Longrightarrow
\text{unweighted first field jet}.
\]

NJDG-6 shows:
\[
\boxed{
\text{finite enriched critical rows}
\not\Longrightarrow
\text{exact frozen mode-weighted RENJET kernel}
}
\tag{19}
\]
by universal linear algebra.

And after the fixed two-mode elimination,
\[
\boxed{
\text{mode-weighted first RENJET}
=
\text{first coefficient of the existing complement wedge}.
}
\tag{20}
\]

Thus the attempted derivative-to-mode weighting does not create a weaker independent theorem interface.

## 12. What remains logically possible

The exact nonspan leaves three genuinely new possibilities.

### MW-A — continuum critical transform

Control a sufficiently rich family of critical-curvature data so that an integral transform reconstructs the exponential/Volterra kernel.

This would require an actual-zeta theorem on a continuum or growing family of derivative-critical data, not finitely many critical points.

### MW-B — actual-zero finite-set interpolation

Exploit special relations of the **actual** finite near zero set to match \(W_{t,u}(w_\mu)\) using finitely many critical rows with projective conditioning.

This would be a new actual-zeta interpolation theorem and must preserve the every-packet quantifier.

### MW-C — direct weighted critical identity

Find an arithmetic/explicit-formula identity at derivative critical points whose zero-side kernel is already
\[
W_{t,u}(w)
\]
or the full higher-jet complement wedge.

This would bypass the rational critical-row span rather than synthesize the exponential kernel from it.

No such theorem is currently in custody.

## 13. NJDG-6 determination

- Frozen two-mode near kernel is entire: **YES**.
- It is nonconstant on the nonzero SOURCE-II wedge: **YES**.
- One critical value + curvature row exactly spans that kernel: **NO**.
- Any finite collection of finite-order critical rows exactly spans it by a universal linear identity: **NO**.
- The critical-point equation changes that kernel-type obstruction: **NO**.
- Critical curvature may still help through a new nonlinear actual-zeta theorem: **YES / OPEN**.
- First-RENJET two-mode wedge is new relative to LOTUS-SHADOW-7: **NO**.
- It is the leading coefficient of the existing complement wedge: **YES**.
- First-jet control automatically controls the full finite tower: **NO**.
- Direct derivative-to-full-wedge theorem proved: **NO**.
- NEXTJET proved: **NO**.
- KPH floor proved: **NO**.
- RH proved: **NO**.

## 14. Route consequence

The finite critical-point / finite curvature enrichment line is exhausted as an **exact linear transfer mechanism**.

Do not open another pass that merely adds a finite number of derivative critical points or finite derivative orders and attempts to interpolate the exponential RENJET kernel.

Re-entry requires genuinely new weighted information: a continuum/growing critical transform, actual-zero interpolation with controlled conditioning, or a direct weighted identity.

## 15. Next cursor

\[
\boxed{
\text{NJDG-7 / DIRECT WEIGHTED CRITICAL IDENTITY SCREEN}
}
\]

Priority order:

1. search for identities obtained by inserting exponential or compact-band weights into logarithmic-derivative equations at derivative critical points;
2. require the zero-side kernel to match the frozen SOURCE-II mode family before any complement data are read;
3. compare every candidate immediately with RH-T0117 to determine whether it is merely the complement wedge in disguise;
4. reject finite rational-resolvent interpolation by NJDG-6;
5. if no genuinely weighted critical identity exists, freeze the derivative-geometry branch at TSTOP rather than opening another coordinate rewrite.
