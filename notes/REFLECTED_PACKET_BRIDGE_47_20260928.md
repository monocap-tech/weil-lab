# RPB-47 — Global threshold Mellin-amplitude matching

**Date:** 2026-09-28  
**Branch:** \`research/reflected-packet-bridge\`  
**Status:** **PASS AS RETYPING / THRESHOLD AMPLITUDES ARE LAWFUL MELLIN RESIDUES / ZERO MEAN AND UNIT GAIN DO NOT FORCE THEM TO VANISH / GLOBAL REALIZATION REDUCES TO A FINITE-DIMENSIONAL BOUNDARY-TRANSFER MATRIX**  
**Dependencies:** RPB-22, RPB-24, RPB-30, RPB-33, RPB-45, RPB-46.  
**Promotion status:** none.

## 0. Objective

RPB-46 proved that the prime-threshold endpoint equation admits genuine local
\(L^2\)-admissible conormal species.

The remaining question was global:

> does the actual finite-dimensional screw-visible neutral kernel realize a
> nonzero coefficient in one of those threshold Mellin channels, or do the
> global neutral, zero-mean, parity, and Birman--Schwinger unit-gain relations
> force every such coefficient to vanish?

RPB-47 answers the structural part.

The endpoint amplitudes can be defined lawfully as Mellin residues.

Parity reduces the left/right duplication.

The zero-mean law is a value constraint at Mellin parameter \(z=1\), whereas
the threshold amplitudes are residues at distinct nonreal Mellin points.

The Birman--Schwinger relation lives on the finite selected coefficient space
and does not contain an existing identity with the boundary Mellin residue.

Therefore no current global relation forces the threshold amplitudes to
vanish.

The remaining problem is a finite-dimensional boundary-transfer calculation
from the unit-gain eigenspace to the endpoint Mellin channels.

---

## 1. Threshold setup

Assume the only surviving support case from RPB-45:

\`\`\`math
2c=\log n_0,
\qquad
n_0=p^m.
\`\`\`

Set

\`\`\`math
a_0
=
\frac{\Lambda(n_0)}{\sqrt{n_0}}.
\`\`\`

In one screw-source parity block,

\`\`\`math
u(-x)
=
\varepsilon_u u(x),
\qquad
\varepsilon_u\in\{+1,-1\}.
\`\`\`

Near the right endpoint put

\`\`\`math
f(s)
=
u(c-s),
\qquad
0<s<\delta.
\`\`\`

Strict threshold persistence gives the local equation

\`\`\`math
\boxed{
\frac12
\int_0^{2c}
\frac{f(r)}{s+r}\,dr
+
\varepsilon_u a_0 f(s)
+
A_f(s)
=
0,
}
\`\`\`

where \(A_f\) is real analytic near \(s=0\).

---

## 2. Localize the endpoint equation

Choose cutoffs

\`\`\`math
\chi_0,\chi_1
\in
C_c^\infty([0,\delta))
\`\`\`

with

\`\`\`math
\chi_0=1
\`\`\`

near \(0\) and

\`\`\`math
\chi_1=1
\`\`\`

on the support of \(\chi_0\).

Write

\`\`\`math
f_0
=
\chi_1 f.
\`\`\`

The contribution to the Carleman integral from

\`\`\`math
(1-\chi_1)f
\`\`\`

is analytic in \(s\) near \(0\), because its integration variable stays a
positive distance from the endpoint.

Therefore the singular endpoint equation is equivalently

\`\`\`math
\boxed{
\frac12
\mathcal C f_0
+
\varepsilon_u a_0 f_0
=
B_f
}
\`\`\`

near \(0\), modulo multiplication by \(\chi_0\), where

\`\`\`math
B_f
\in
C^\omega
\`\`\`

near the endpoint.

Here

\`\`\`math
(\mathcal C f_0)(s)
=
\int_0^\infty
\frac{f_0(r)}{s+r}\,dr.
\`\`\`

---

## 3. Mellin transform of the localized Carleman equation

Define

\`\`\`math
\widehat f_M(z)
=
\int_0^\infty
f_0(s)s^{z-1}\,ds.
\`\`\`

Since \(f_0\in L^2\) with compact support,

\`\`\`math
\widehat f_M(z)
\`\`\`

is initially holomorphic for

\`\`\`math
\Re z>\frac12.
\`\`\`

For

\`\`\`math
0<\Re z<1,
\`\`\`

Fubini gives the classical Mellin identity

\`\`\`math
\begin{aligned}
\mathcal M(\mathcal C f_0)(z)
&=
\int_0^\infty
f_0(r)
\left[
\int_0^\infty
\frac{s^{z-1}}{s+r}\,ds
\right]dr
\\
&=
\frac{\pi}{\sin(\pi z)}
\widehat f_M(z).
\end{aligned}
\`\`\`

Thus the principal Mellin equation is

\`\`\`math
\boxed{
m_{\varepsilon_u}(z)
\widehat f_M(z)
=
H_f(z),
}
\`\`\`

where

\`\`\`math
\boxed{
m_{\varepsilon}(z)
=
\frac{\pi}{2\sin(\pi z)}
+
\varepsilon a_0
}
\`\`\`

and \(H_f\) consists of the Mellin transform of the analytic forcing plus
cutoff/localization terms.

The localization terms are holomorphic across the noninteger indicial points.
The analytic forcing contributes only the standard integer Mellin poles coming
from its Taylor series.

Therefore every **noninteger** pole of the continued
\(\widehat f_M\) must lie at a zero of \(m_{\varepsilon_u}\).

---

## 4. Agreement with the RPB-46 indicial family

Let

\`\`\`math
z=-\beta.
\`\`\`

Then

\`\`\`math
m_{\varepsilon}(-\beta)
=
-\frac{\pi}{2\sin(\pi\beta)}
+
\varepsilon a_0
=
\mathfrak m_\varepsilon(\beta).
\`\`\`

Thus the Mellin poles occur exactly at the RPB-46 indicial exponents.

The roots are simple because

\`\`\`math
\cos(\pi\beta)
\ne0
\`\`\`

at the log-oscillatory roots.

Therefore the endpoint coefficient in one channel is canonically a Mellin
residue.

---

## 5. Lawful threshold Mellin amplitudes

For every \(L^2\)-admissible indicial root \(\beta\), define

\`\`\`math
\boxed{
\mathfrak a_\beta(u)
=
\operatorname*{Res}_{z=-\beta}
\widehat f_M(z).
}
\`\`\`

Changing the cutoff \(f_0=\chi f\) by another cutoff equal to one near the
endpoint changes the Mellin transform only by an entire function at
\(z=-\beta\).

Hence

\`\`\`math
\boxed{
\mathfrak a_\beta
\text{ is cutoff-independent}.
}
\`\`\`

It is linear in the source.

For a real source,

\`\`\`math
\boxed{
\mathfrak a_{\bar\beta}(u)
=
\overline{
\mathfrak a_\beta(u)
}.
}
\`\`\`

This supplies the lawful threshold Mellin-amplitude map requested at the
previous cursor.

---

## 6. The full amplitude vector separates persistent nonzero germs

Let

\`\`\`math
\mathcal I_{\varepsilon_u}
\`\`\`

be the \(L^2\)-admissible indicial set and define

\`\`\`math
\boxed{
\mathfrak A_c(u)
=
\left(
\mathfrak a_\beta(u)
\right)_{\beta\in\mathcal I_{\varepsilon_u}}.
}
\`\`\`

Suppose a threshold-persistent source has

\`\`\`math
\mathfrak A_c(u)=0.
\`\`\`

Then the localized Mellin transform has no noninteger indicial poles.

The endpoint germ is therefore analytic modulo possible integer-power terms.

Now let the first nonzero Taylor coefficient be

\`\`\`math
f(s)
=
b_k s^k
+
O(s^{k+1}),
\qquad
b_k\ne0.
\`\`\`

Direct division gives

\`\`\`math
\int_0^\delta
\frac{r^k}{s+r}\,dr
=
P_k(s)
+
(-1)^{k+1}
s^k\log s
+
\text{analytic},
\`\`\`

where \(P_k\) is a polynomial.

The threshold multiplication term

\`\`\`math
\varepsilon_u a_0 f(s)
\`\`\`

and the remainder \(A_f(s)\) are analytic.

They cannot cancel the nonzero

\`\`\`math
s^k\log s
\`\`\`

term.

Contradiction.

Hence every Taylor coefficient vanishes.

Since the endpoint germ is analytic, it follows that

\`\`\`math
f=0
\`\`\`

near the endpoint.

RPB-43 interior analyticity then forces

\`\`\`math
u\equiv0.
\`\`\`

Therefore:

\`\`\`math
\boxed{
u\ne0
\text{ and threshold-persistent}
\Longrightarrow
\mathfrak A_c(u)\ne0.
}
\`\`\`

The full amplitude vector separates nonzero persistent modes.

---

## 7. Parity removes the second endpoint copy

The left endpoint germ is determined by parity:

\`\`\`math
u(-c+s)
=
\varepsilon_u u(c-s).
\`\`\`

Therefore its Mellin residues are fixed linear/reflected copies of the
right-endpoint residues.

No independent left amplitude vector is needed.

Thus the global threshold problem has one endpoint amplitude system per parity
block, not two unrelated boundary systems.

---

## 8. Zero mean is a Mellin value, not a Mellin residue

Since

\`\`\`math
f(s)
=
u(c-s),
\`\`\`

we have

\`\`\`math
\begin{aligned}
\widehat f_M(1)
&=
\int_0^{2c}
f(s)\,ds
\\
&=
\int_{-c}^{c}
u(x)\,dx.
\end{aligned}
\`\`\`

The screw source lies in the zero-mean space, so

\`\`\`math
\boxed{
\widehat f_M(1)=0.
}
\`\`\`

By contrast, the threshold amplitudes are residues at

\`\`\`math
z=-\beta.
\`\`\`

For the first admissible channels these points have real parts

\`\`\`math
-\frac12
\quad\text{or}\quad
-\frac32,
\`\`\`

and nonzero imaginary parts.

There is no identity in the current theory relating the ordinary Mellin value

\`\`\`math
\widehat f_M(1)
\`\`\`

to the residues at those points.

Hence:

\`\`\`math
\boxed{
\text{zero mean does not force threshold Mellin amplitude zero}.
}
\`\`\`

For odd screw sources, zero mean is automatic by parity.

---

## 9. Return to the finite-dimensional unit-gain eigenspace

Let

\`\`\`math
E_*
=
\ker(\mathsf K_c-I)
\`\`\`

be the endpoint Birman--Schwinger unit-gain eigenspace.

RPB-30 gives the neutral-resolvent isomorphism

\`\`\`math
\boxed{
J_*:
E_*
\longrightarrow
\ker A_c,
\qquad
J_*v
=
A_{B,c}^{-1}\Phi_c^*v.
}
\`\`\`

For a screw-visible/core neutral direction,

\`\`\`math
h
=
J_*v
\in
H_0^1(-c,c)
\`\`\`

and

\`\`\`math
u
=
Dh.
\`\`\`

Therefore, on any unit-gain direction whose endpoint germ is
threshold-compatible, define

\`\`\`math
\boxed{
\mathfrak T_{\beta,c}(v)
=
\mathfrak a_\beta
\left(
D J_*v
\right).
}
\`\`\`

This is a linear boundary-transfer row on the finite selected eigenspace.

---

## 10. Precise domain of the boundary-transfer row

The Mellin residue description belongs to the threshold-compatible subspace

\`\`\`math
\boxed{
E_*^{\rm tc}
=
\left\{
v\in E_*:
D J_*v
\text{ satisfies the threshold endpoint singular compatibility}
\right\}.
}
\`\`\`

A genuinely persistent vector lies in

\`\`\`math
E_*^{\rm pers}
\subseteq
E_*^{\rm tc}.
\`\`\`

Thus RPB-47 does **not** assign the conormal residue expansion to an arbitrary
unit-gain vector before threshold compatibility is established.

On \(E_*^{\rm tc}\), however, every amplitude row is lawful.

---

## 11. Unit gain does not annihilate the boundary-transfer row

The Birman--Schwinger condition is

\`\`\`math
\boxed{
\mathsf K_cv=v.
}
\`\`\`

Equivalently, it is the inverse-background extremal relation

\`\`\`math
\langle
A_{B,c}^{-1}\Phi_c^*v,
\Phi_c^*v
\rangle
=
\|v\|^2.
\`\`\`

This is a finite-dimensional energy identity.

The threshold Mellin amplitude is instead a boundary residue of

\`\`\`math
D A_{B,c}^{-1}\Phi_c^*v.
\`\`\`

No RPB theorem identifies the functional

\`\`\`math
v
\longmapsto
\mathfrak a_\beta
\left(
D A_{B,c}^{-1}\Phi_c^*v
\right)
\`\`\`

with a row of

\`\`\`math
\mathsf K_c-I.
\`\`\`

Therefore

\`\`\`math
\boxed{
\mathsf K_cv=v
\not\Longrightarrow
\mathfrak T_{\beta,c}(v)=0
}
\`\`\`

from the currently established identities.

Conversely, unit gain does not imply that the amplitude is nonzero.

The two data are differently typed.

---

## 12. Finite-dimensional collapse of the remaining amplitude problem

Although the formal indicial set contains infinitely many periodic copies,

\`\`\`math
\beta,
\beta+2,
\beta+4,
\dots,
\`\`\`

the domain

\`\`\`math
E_*^{\rm tc}
\`\`\`

is finite dimensional.

Therefore the family of all boundary-transfer rows

\`\`\`math
\left\{
\mathfrak T_{\beta,c}
\right\}
\subset
(E_*^{\rm tc})^*
\`\`\`

has finite-dimensional linear span.

Hence there exist finitely many admissible channels

\`\`\`math
\beta_1,\dots,\beta_M
\`\`\`

whose rows span every Mellin-amplitude functional on the threshold-compatible
unit-gain space.

This gives a finite boundary matrix

\`\`\`math
\boxed{
\mathbf T_c:
E_*^{\rm tc}
\longrightarrow
\mathbb C^M,
\qquad
v
\longmapsto
\left(
\mathfrak T_{\beta_j,c}(v)
\right)_{j=1}^{M}.
}
\`\`\`

For a nonzero persistent vector, the full amplitude-separation theorem implies
that at least one row is nonzero.

Thus the apparently infinite endpoint Mellin problem reduces to finite
linear algebra on the actual unit-gain space.

---

## 13. Why this still does not decide strict persistence

The vanishing/nonvanishing of \(\mathbf T_c\) is only the nonanalytic boundary
part of the right-limit equation.

After the admissible conormal singularities are matched, the remaining
exterior defect is analytic.

Strict persistence requires that analytic defect to vanish as an actual germ,
not merely to be analytic.

Therefore the complete right-limit boundary transfer has two layers:

1. **Mellin/conormal layer**
   \[
   \mathbf T_c;
   \]
2. **analytic remainder layer**, determined by the global interior neutral
   mode.

RPB-47 computes neither layer numerically from the selected coordinates.

It proves that both layers live on a finite-dimensional source space and that
the existing unit-gain relation does not already solve them.

---

## 14. Exact status of the global-realization question

The following statements are now established:

\`\`\`math
\boxed{
\begin{aligned}
&\text{strict persistence}
\Longrightarrow
2c=\log n_0,
\\
&\text{strict persistence}
\Longrightarrow
v\in E_*^{\rm tc},
\\
&v\ne0\text{ persistent}
\Longrightarrow
\mathfrak A_c(DJ_*v)\ne0.
\end{aligned}
}
\`\`\`

But neither

\`\`\`math
\mathbf T_c=0
\`\`\`

nor

\`\`\`math
\ker\mathbf T_c=\{0\}
\`\`\`

follows from

\`\`\`math
\mathsf K_c|_{E_*}=I.
\`\`\`

So the selected Birman--Schwinger crossing has not yet decided the threshold
boundary amplitudes.

This is now the exact global threshold Mellin-amplitude matching gap.

---

## 15. RPB-47 determination

\`\`\`math
\boxed{
\textbf{RPB-47 — THRESHOLD MELLIN AMPLITUDES ARE LAWFUL BOUNDARY RESIDUES, BUT ZERO MEAN AND UNIT GAIN DO NOT FORCE THEIR VANISHING.}
}
\`\`\`

Lawful amplitude:

\`\`\`math
\boxed{
\mathfrak a_\beta(u)
=
\operatorname*{Res}_{z=-\beta}
\int_0^\delta
u(c-s)s^{z-1}\,ds.
}
\`\`\`

Zero-mean separation:

\`\`\`math
\boxed{
\widehat f_M(1)=0
\quad\text{is independent of the residues at }z=-\beta.
}
\`\`\`

Birman--Schwinger boundary transfer:

\`\`\`math
\boxed{
\mathfrak T_{\beta,c}(v)
=
\mathfrak a_\beta
\left(
D A_{B,c}^{-1}\Phi_c^*v
\right).
}
\`\`\`

The remaining threshold realization problem is finite dimensional, but its
boundary-transfer matrix is not supplied by the current Weil/Birman--Schwinger
package.

Next cursor:

\`\`\`text
RPB-48 / THRESHOLD BIRMAN--SCHWINGER BOUNDARY-TRANSFER MATRIX
\`\`\`

The next pass should attempt to compute the boundary-transfer rows directly
from the resolvent extremizer

\`\`\`math
h_v
=
A_{B,c}^{-1}\Phi_c^*v
\`\`\`

at a threshold:

1. derive a boundary Mellin formula for the background resolvent;
2. express the first admissible amplitude row in selected-coordinate form;
3. determine whether the finite matrix has full column rank on \(E_*\);
4. if not computable from the current background operator, isolate the exact
   missing resolvent boundary symbol.
