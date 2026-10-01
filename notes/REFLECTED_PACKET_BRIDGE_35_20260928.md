# RPB-35 — Screw-potential collar rigidity of `ker G_{c_*}`

**Date:** 2026-09-28  
**Branch:** `research/reflected-packet-bridge`  
**Status:** **PASS AS EXACT REDUCTION / SCREW COLLAR RIGIDITY = CORE-REGULAR WEIL NULL-EXTENSION / PIECEWISE-ANALYTIC BYPASS FAILS**  
**Dependencies:** RPB-32 through RPB-34; Suzuki screw identity (-g''=W); compact-window explicit formula.  
**Promotion status:** none.

## 0. Objective

RPB-34 reduced the alignment problem to the following question.

Let

```math
0\ne u\in\ker G_c,
```

and define the whole-line screw potential

```math
F_u(x)
=
\int_{-c}^{c}
g(x-y)u(y)\,dy.
```

Then (F_u) is constant on ((-c,c)).

Can the same (F_u) remain constant on any strict enlargement

```math
(-a,a),
\qquad
a>c?
```

RPB-35 establishes that this is **exactly** the old compact-window Weil
null-extension problem for the corresponding screw-core neutral mode.

The screw representation does not supply an independent analyticity bypass.

---

## 1. Pass from the screw source to the core neutral mode

By RPB-32/33, every screw-visible neutral direction has the form

```math
u
=
Dh
=
i h',
```

with

```math
h\in H_0^1(-c,c),
\qquad
A_ch=0.
```

Extend (h) by zero outside ((-c,c)).

Because (h) has zero boundary trace at (pm c), ordinary integration by
parts is legitimate against the continuous screw kernel in the distributional
sense.

---

## 2. Exact integration-by-parts identity

Start from

```math
F_u(x)
=
\int
g(x-y),i h'(y)\,dy.
```

The boundary term vanishes, so

```math
\begin{aligned}
F_u(x)
&=
i
\int
g'(x-y)h(y)\,dy
\\
&=
i,(g'*h)(x).
\end{aligned}
```

Hence

```math
\boxed{
F_u
=
i,g'*h.
}
```

Suzuki's screw/Weil relation is

```math
\boxed{
-g''=W
}
```

as distributions.

Differentiating the previous identity gives

```math
\boxed{
F_u'
=
-i,W*h.
}
```

This identity is global and distributional.

### Source

Masatoshi Suzuki, *Aspects of the screw function corresponding to the Riemann
zeta-function*, J. London Math. Soc. 108 (2023), especially formula (1.1),
definition (g=-Psi), and §3.5 where (-g''=W) is obtained.

---

## 3. Screw--Weil collar equivalence

Let (Isubsetmathbb R) be any nonempty open interval.

Since (F_u) is continuous,

```math
F_u
\text{ is constant on }I
```

if and only if

```math
F_u'=0
```

on (I) distributionally.

Using Section 2,

```math
\boxed{
F_u
\text{ constant on }I
\iff
W*h=0
\text{ on }I.
}
```

Thus the proposed screw-potential collar rigidity question is exactly a
Weil-operator exterior null question.

---

## 4. Exact equivalence under support enlargement

Let (a>c), and let

```math
J_{c,a}u
```

denote zero extension of (u) to (L_0^2(-a,a)).

Likewise let (widetilde h) be the zero extension of (h) to
((-a,a)). Since (hin H_0^1(-c,c)),

```math
\widetilde h
\in
H_0^1(-a,a).
```

The following statements are equivalent:

```math
\boxed{
\begin{aligned}
&J_{c,a}u\in\ker G_a
\\
\Longleftrightarrow;&
F_u
\text{ is constant on }(-a,a)
\\
\Longleftrightarrow;&
W*\widetilde h=0
\text{ on }(-a,a)
\\
\Longleftrightarrow;&
B_a\widetilde h=0.
\end{aligned}
}
```

Because (A_a) extends the screw-core operator (B_a),

```math
B_a\widetilde h=0
\Longrightarrow
A_a\widetilde h=0.
```

Conversely, for this fixed zero extension already lying in (H_0^1(-a,a)),

```math
A_a\widetilde h=0
\Longrightarrow
B_a\widetilde h=0.
```

Hence on screw-visible core modes,

```math
\boxed{
J_{c,a}u\in\ker G_a
\iff
\widetilde h\in\ker A_a.
}
```

This is the core-regular null-extension problem.

---

## 5. Relation to `AZ-FIN-WEIL-NULL-EXTENSION`

The canonical Horizon-1 interface asks whether the zero extension of a
nonzero endpoint neutral mode satisfies the correct compact-window equation on
a strict enlargement.

RPB-35 shows that, for the nonzero screw-visible core neutral directions
supplied by RPB-33,

```math
\boxed{
\text{screw-potential collar persistence}
\iff
\text{Weil null-extension persistence}.
}
```

Therefore the screw collar problem is not a new independent exit around

```text
AZ-FIN-WEIL-NULL-EXTENSION
```

but a more concrete realization of that same interface on the core-regular
neutral subspace.

The interface is nonvacuous because RPB-33 proved

```math
\ker G_{c_*}\ne\{0\}.
```

---

## 6. Explicit arithmetic structure of the screw kernel

For (t>0), Suzuki's explicit zeta screw function may be separated as

```math
\boxed{
g(t)
=
g_{\rm sm}(t)
+
\sum_{\log n\le t}
\frac{\Lambda(n)}{\sqrt n}
(t-\log n),
}
```

where (g_{\rm sm}) is the non-prime archimedean/pole part and is real
analytic for (t>0).

Equivalently,

```math
g_{\rm pr}(t)
=
\sum_n
\frac{\Lambda(n)}{\sqrt n}
(t-\log n)_+.
```

Thus (g) is continuous but its first derivative changes at the arithmetic
knots

```math
t=\log n.
```

Distributionally on (t>0),

```math
\boxed{
g_{\rm pr}''(t)
=
\sum_n
\frac{\Lambda(n)}{\sqrt n}
\delta(t-\log n).
}
```

This is exactly the prime-delay content recovered after differentiating the
screw potential.

---

## 7. Moving-kink formula on a right collar

Fix (x>c). Then (x-y>0) for almost every
(y\in[-c,c]), so the positive-(t) formula applies.

For one prime delay

```math
\ell_n=\log n,
```

the contribution to (F_u) is

```math
P_n(x)
=
\frac{\Lambda(n)}{\sqrt n}
\int_{-c}^{c}
(x-y-\ell_n)_+
u(y)\,dy.
```

On a subinterval where

```math
x-\ell_n\in(-c,c),
```

one may write

```math
P_n(x)
=
\frac{\Lambda(n)}{\sqrt n}
\int_{-c}^{x-\ell_n}
(x-y-\ell_n)u(y)\,dy.
```

Hence, for almost every such (x),

```math
\boxed{
P_n''(x)
=
\frac{\Lambda(n)}{\sqrt n}
u(x-\ell_n).
}
```

Summing over the finitely many delays meeting the compact support gives

```math
\boxed{
F_{u,\rm pr}''(x)
=
\sum_{n:\,x-\log n\in(-c,c)}
\frac{\Lambda(n)}{\sqrt n}
u(x-\log n).
}
```

This is the exact arithmetic-kink regularity transfer.

---

## 8. Piecewise analyticity of (g) does not make (F_u) analytic

The proposed collar-rigidity shortcut was:

```math
g
\text{ piecewise analytic}
\quad\Longrightarrow?\quad
F_u=g*u
\text{ analytic on the collar}.
```

Section 7 rules this out for the actual source regularity.

The source satisfies only

```math
u\in L^2(-c,c)
```

at the screw level.

The moving arithmetic kink transfers this (L^2) source directly into the
second derivative of the convolved prime term:

```math
P_n''(x)
=
a_nu(x-\ell_n).
```

Thus (P_n) is locally of Sobolev species (H^2) on such a region, but it is
not generically analytic.

Consequently:

```math
\boxed{
\text{piecewise analyticity of }g
\not\Rightarrow
\text{analyticity of }F_u.
}
```

The ordinary identity theorem cannot be used to propagate collar constancy.

---

## 9. The differentiated collar equation is the existing finite-delay Weil equation

If (F_u) is constant on a right collar, then Section 3 gives

```math
W*h=0
```

there.

Using the compact-window explicit formula, this is precisely the equation
species

```math
\boxed{
\mathcal A_\infty h
-
\sum_{\log n<2a}
\frac{\Lambda(n)}{\sqrt n}
(
\tau_{\log n}
+
\tau_{-\log n}
)h
+
\mathcal R_{\rm pole}h
=
0
}
```

with the appropriate strict-right threshold convention.

On the right exterior collar, (h(x)=0), but the inward shifts

```math
h(x-\log n)
```

can lie inside the old support.

Therefore the equation does not reduce to the archimedean term alone.

The screw formulation has reconstructed the same finite-delay exterior
equation already isolated by Horizon 1.

---

## 10. Existing logarithmic-Laplacian unique continuation does not close this equation

There is a known weak unique-continuation theorem for the whole-space
logarithmic Laplacian:

if a function (f) and (L_\Delta f) both vanish on a nonempty open set,
then (f\equiv0) under the theorem's stated integrability hypotheses.

This is established in the logarithmic-Laplacian extension/UCP literature
(Chen--Hauer--Weth, *An extension problem for the logarithmic Laplacian*,
Theorem 5.1 in the cited formulation).

That theorem does not directly apply here.

On the exterior collar,

```math
h=0,
```

but the actual Weil equation gives schematically

```math
L_\Delta h
=
-
\left[
\text{bounded archimedean remainder}
+
\text{finite prime translations}
+
\text{finite-rank pole term}
\right]h.
```

The right-hand side need not vanish on the collar:

- (h(x-\log n)) may lie in the interior support;
- the finite-rank pole term is global;
- a bounded nonlocal archimedean remainder need not vanish merely because
  (h) vanishes locally.

Therefore the hypothesis

```math
L_\Delta h=0
\text{ on the same collar}
```

is not available.

So existing logarithmic UCP does not discharge the actual Weil collar problem.

---

## 11. Thresholds are automatically carried by the global screw identity

One advantage of the screw formulation is bookkeeping.

The whole-line identity

```math
-g''=W
```

contains all prime-power atoms globally.

When the support is enlarged from (c) to (a), the condition

```math
F_u'=-iW*h=0
\quad\text{on }(-a,a)
```

automatically includes any new prime delay whose atom becomes visible across
the strict-right threshold.

Thus the screw collar equation reproduces the same distinction already encoded
in the canonical interface:

- away from a prime threshold, the active finite delay set is locally stable;
- at a threshold, the equality-threshold term enters on every strict right
  enlargement.

No separate ad hoc correction is needed in the global screw distribution.

---

## 12. No triangular delay elimination follows from the outer collar

The right-collar equation contains only finitely many active shifts, but it is
not triangular in the selected source.

For (x\in(c,c+\varepsilon)),

```math
x-\log n
```

samples several different interior subintervals whenever several prime powers
satisfy

```math
\log n<2c+\varepsilon.
```

At the same time the archimedean convolution remains global over the whole
source support.

Thus the largest or smallest prime delay cannot be isolated by support order
alone.

No induction from the exterior boundary toward the interior is obtained from
the retained equation.

This is another form of the same nonlocal obstruction recorded in
`AZ-FIN-WEIL-NULL-EXTENSION`.

---

## 13. Exact RPB-35 stop line

RPB-35 therefore establishes an exact identification, not a closure theorem:

```math
\boxed{
\begin{aligned}
&u\in\ker G_c,
\quad
u=Dh,
\quad
h\in H_0^1(-c,c)
\\[1mm]
&\mathcal L_{c,a}u=0
\\
&\iff
F_u
\text{ constant on }(-a,a)
\\
&\iff
W*h=0
\text{ on }(-a,a)
\\
&\iff
\widetilde h
\text{ is a core-domain null extension to }a.
\end{aligned}
}
```

The piecewise-analytic structure of (g) does not currently turn this
equivalence into rigidity because the arithmetic kinks transfer the unknown
source into moving delay terms.

---

## 14. RPB-35 determination

```math
\boxed{
\textbf{RPB-35 — SCREW-POTENTIAL COLLAR RIGIDITY IS EXACTLY THE CORE-REGULAR WEIL NULL-EXTENSION INTERFACE.}
}
```

Positive result:

```math
\boxed{
F_u'=-iW*h
}
```

for (u=Dh), which gives an exact equivalence between screw collar persistence
and the physical exterior null equation.

Negative result:

```math
\boxed{
\text{piecewise analytic }g
\not\Rightarrow
\text{an analytic screw potential for }u\in L^2.
}
```

The prime kinks reproduce the finite arithmetic-delay equation rather than
removing it.

Existing logarithmic-Laplacian UCP also does not apply directly because the
finite translations and global lower-order terms need not vanish on the collar.

Therefore the RPB neutral line has now **refolded into**
`AZ-FIN-WEIL-NULL-EXTENSION` on a nonzero core-visible neutral subspace.

Next cursor:

```text
RPB-36 / FINITE-DELAY UNIQUE CONTINUATION FOR CORE-NEUTRAL WEIL MODE
```

The next pass should test whether the known unique-continuation mechanism for
the logarithmic Laplacian can be extended to the actual finite-delay Weil
operator under the special hypotheses available here:

1. compact support of (h);
2. (H_0^1) core regularity;
3. simultaneous left and right exterior collar equations;
4. finitely many arithmetic delays;
5. finite-rank pole contribution;
6. endpoint neutral/screw-kernel origin.

The target is a genuine theorem of the form

```math
h=0
\text{ and }
\mathcal W^{\rm ext}h=0
\text{ on an exterior collar}
\Longrightarrow
h\equiv0,
```

or a precise no-go showing why the finite delays defeat the logarithmic UCP
mechanism even with the RPB-33 core regularity.
