# SZ-KERNEL-EDGE-GERM-12 — Linear defect floor and partial superflat transfer

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Immediate residue:** SZ-KERNEL-EDGE-GERM-11  
**Target tested:** SUPERFLAT-TO-DEFECT TRANSFER  
**Public promotion:** forbidden

## 0. Objective

GERM-11 proved that the endpoint/projection mismatch is dynamically
observable on every nonzero edge obstruction.

The remaining question was whether the original all-orders collar flatness can
force that mismatch to vanish.

This pass gives a mixed answer.

### Positive transfer

Collar superflatness does propagate from the mean-corrected observation to the
two raw exterior residuals.  Hence the shifted old-exterior term in GERM-8's
entry-zone formula is superflat.

This remains true uniformly along the compressed orbit inside the
finite-dimensional obstruction.

### Negative transfer

The finite archimedean moment defect itself has an unavoidable **linear**
lower bound in the translation width.

Thus a nonzero obstruction cannot make the whole moment mismatch superflat.

The linear mismatch must be carried by the boundary-prefix/projection channel,
not by the shifted old-exterior residual.

So the transfer problem has been narrowed to one exact interface:

\[
\boxed{
\text{superflat collar}
\quad\text{vs.}\quad
\text{finite-order boundary/projection ejection}.
}
\]

No contradiction is obtained yet because no theorem identifies those two
quantities.

---

# I. Setup

## 1. Canonical obstruction representative

Let

\[
P=P_c^+,
\qquad
F=F_\infty,
\qquad
E=F\cap P^\perp.
\]

Transport \(E\) into right-edge source coordinates

\[
E_+
=
U_+E
\subset
H:=L^2(0,L),
\qquad
L=2c.
\]

Assume

\[
d=\dim E_+>0.
\]

Let

\[
\Pi:H\to E_+
\]

be the orthogonal projection and

\[
A_\ell
=
\Pi S_\ell|_{E_+}
\]

the canonical compressed truncated shift from GERM-10.

Because both \(S_\ell\) and \(\Pi\) are contractions,

\[
\boxed{
\|A_\ell\|\le1.
}
\]

---

# II. Finite archimedean moment chart

## 2. Choose a square separating chart

The full moment family

\[
M_m(f)
=
\int_0^L
e^{-(2m+1/2)s}f(s)\,ds
\]

separates \(E_+\).

Since \(E_+\) has dimension \(d\), choose indices

\[
1\le m_1<\cdots<m_d
\]

such that the map

\[
\boxed{
B:
E_+\to\mathbb C^d,
\qquad
Bf=
\left(
M_{m_1}(f),\ldots,M_{m_d}(f)
\right)
}
\]

is an isomorphism.

Write

\[
\lambda_j
=
2m_j+\frac12
\]

and

\[
\boxed{
D_J^+(\ell)
=
\operatorname{diag}
\left(
e^{\lambda_1\ell},
\ldots,
e^{\lambda_d\ell}
\right).
}
\]

Define the finite-chart mismatch

\[
\boxed{
R_J(\ell)
=
BA_\ell
-
D_J^+(\ell)B.
}
\]

This is a finite-dimensional compression of the full GERM-10/11 moment
defect.

---

# III. A linear lower bound for the mismatch

## 3. Trace identity

Since \(B\) is invertible,

\[
R_J(\ell)B^{-1}
=
BA_\ell B^{-1}
-
D_J^+(\ell).
\]

Taking traces and using similarity invariance,

\[
\boxed{
\operatorname{tr}
\left(
R_J(\ell)B^{-1}
\right)
=
\operatorname{tr}A_\ell
-
\sum_{j=1}^d e^{\lambda_j\ell}.
}
\]

---

## 4. Contraction bound

Because

\[
\|A_\ell\|\le1,
\]

we have

\[
\Re\operatorname{tr}A_\ell
\le d.
\]

Therefore

\[
\begin{aligned}
-\Re\operatorname{tr}
\left(
R_J(\ell)B^{-1}
\right)
&\ge
\sum_{j=1}^d
\left(
e^{\lambda_j\ell}-1
\right)\\
&\ge
\ell
\sum_{j=1}^d
\lambda_j.
\end{aligned}
\]

Thus

\[
\left|
\operatorname{tr}
\left(
R_J(\ell)B^{-1}
\right)
\right|
\ge
\ell
\sum_{j=1}^d\lambda_j.
\]

Using

\[
|\operatorname{tr}X|
\le
d\|X\|,
\]

we obtain

\[
d
\|R_J(\ell)\|
\|B^{-1}\|
\ge
\ell
\sum_{j=1}^d\lambda_j.
\]

Hence

\[
\boxed{
\|R_J(\ell)\|
\ge
c_J\,\ell,
}
\]

where

\[
\boxed{
c_J
=
\frac{
\sum_{j=1}^d\lambda_j
}{
d\|B^{-1}\|
}
>0.
\]

This holds for every admissible

\[
\ell>0.
\]

---

## 5. Consequence

A nonzero edge obstruction has a fixed finite moment chart in which the
canonical translation mismatch is never flatter than first order:

\[
\boxed{
R_J(\ell)\ne o(\ell).
}
\]

In particular,

\[
\boxed{
R_J(\ell)
\text{ cannot be superflat as }\ell\downarrow0.
}
\]

This strengthens GERM-11's qualitative mismatch theorem.

No regularity of the kernel vectors is used.

The proof uses only:

- finite-dimensional moment separation;
- the contractivity of truncated translation/compression;
- and the expanding ideal multipliers
  \[
  e^{\lambda_j\ell}.
  \]

---

# IV. Independent source-side curvature floor

## 6. Autocorrelation identity

There is also a chart-free source-side finite-order obstruction.

Extend

\[
f\in H
\]

by zero to the real line.

Then

\[
\langle S_\ell f,f\rangle_H
\]

is the ordinary translation autocorrelation of the zero extension.

With any fixed unitary Fourier normalization,

\[
\boxed{
\|f\|_2^2
-
\Re\langle S_\ell f,f\rangle
=
\int_{\mathbb R}
\left(
1-\cos(\xi\ell)
\right)
|\widehat f(\xi)|^2\,d\xi
}
\]

up to the fixed Fourier normalization constant.

Because

\[
f\in E_+,
\]

\[
\langle A_\ell f,f\rangle
=
\langle S_\ell f,f\rangle.
\]

---

## 7. Uniform quadratic lower bound on \(E_+\)

Fix

\[
R>0.
\]

Define

\[
q_R(f)
=
\int_{|\xi|\le R}
\xi^2|\widehat f(\xi)|^2\,d\xi.
\]

For nonzero compactly supported \(f\),

\[
q_R(f)>0.
\]

Indeed, if \(q_R(f)=0\), then the continuous entire Fourier transform of \(f\)
vanishes on an interval and hence identically.

Since \(E_+\) is finite dimensional, the unit sphere is compact and therefore

\[
\boxed{
q_R(f)
\ge
\kappa_R\|f\|^2
}
\]

for some

\[
\kappa_R>0.
\]

For sufficiently small \(\ell\), use

\[
1-\cos t
\ge
\frac14t^2
\qquad
(|t|\le1)
\]

to get

\[
\boxed{
\|f\|^2
-
\Re\langle A_\ell f,f\rangle
\ge
c_R\ell^2\|f\|^2.
}
\]

Consequently

\[
\boxed{
\|(I-A_\ell)f\|
\ge
c_R\ell^2\|f\|.
}
\]

Thus the compressed translation cannot be infinitely tangent to the identity
on a nonzero obstruction.

The moment-chart theorem in Section III is stronger for the intertwining
defect: it gives a linear, rather than quadratic, floor.

---

# V. Mean-corrected collar flatness

## 8. Raw and mean-corrected residuals

For

\[
u\in F_\infty,
\]

write

\[
r_+(\delta)
=
F_u(c+\delta)-C_u,
\]

\[
r_-(\delta)
=
F_u(-c-\delta)-C_u,
\]

and

\[
\mu(\delta)
=
m(c+\delta)-C_u.
\]

The mean-corrected residuals are

\[
R_+(\delta)=r_+(\delta)-\mu(\delta),
\]

\[
R_-(\delta)=r_-(\delta)-\mu(\delta).
\]

The canonical collar norm is

\[
\boxed{
\Delta_{c,c+\varepsilon}(u)^2
=
\int_0^\varepsilon
\left(
|R_+(\delta)|^2
+
|R_-(\delta)|^2
\right)d\delta.
}
\]

For \(u\in F_\infty\),

\[
\Delta_{c,c+\varepsilon}(u)
=
o(\varepsilon^N)
\qquad
\forall N.
\]

---

# VI. The moving mean is superflat

## 9. Differential identity for the mean correction

The ratified mean formula gives

\[
2(c+\delta)\mu(\delta)
=
\int_0^\delta
\left(
r_+(s)+r_-(s)
\right)ds.
\]

Differentiate:

\[
2\mu
+
2(c+\delta)\mu'
=
r_++r_-.
\]

Since

\[
r_++r_-
=
R_++R_-+2\mu,
\]

we obtain

\[
\boxed{
2(c+\delta)\mu'(\delta)
=
R_+(\delta)+R_-(\delta).
}
\]

Also,

\[
\mu(0)=0.
\]

---

## 10. Estimate

For sufficiently small \(\varepsilon\),

\[
|\mu(\delta)|
\le
\frac1{2c}
\int_0^\delta
\left(
|R_+(s)|+|R_-(s)|
\right)ds.
\]

By Cauchy--Schwarz,

\[
\boxed{
\sup_{0<\delta<\varepsilon}
|\mu(\delta)|
\lesssim_c
\varepsilon^{1/2}
\Delta_{c,c+\varepsilon}(u).
}
\]

Hence for every \(N\),

\[
\boxed{
\sup_{0<\delta<\varepsilon}
|\mu(\delta)|
=
o(\varepsilon^N).
}
\]

The moving mean correction is itself superflat.

---

# VII. Raw exterior residuals are superflat in \(L^2\)

## 11. Transfer

Since

\[
r_\pm
=
R_\pm+\mu,
\]

we have

\[
\|r_\pm\|_{L^2(0,\varepsilon)}
\le
\|R_\pm\|_{L^2(0,\varepsilon)}
+
\varepsilon^{1/2}
\|\mu\|_{L^\infty(0,\varepsilon)}.
\]

Therefore

\[
\boxed{
\|r_\pm\|_{L^2(0,\varepsilon)}
=
o(\varepsilon^N)
\qquad
\forall N.
}
\]

Thus collar superflatness survives removal of the moving-mean correction.

This is a genuine superflat-transfer theorem.

---

# VIII. The GERM-8 entry residual is superflat

## 12. Shifted old exterior residual

GERM-8 showed that on the entry strip of a translated kernel vector,

\[
F_{T_{\ell,c}u}(-c+s)
=
C_u
+
r_-(\ell-s)
-
B_{\ell,+}u(-c+s),
\qquad
0<s<\ell.
\]

Take the translation width equal to the shrinking scale

\[
\ell=\varepsilon.
\]

Then

\[
\|r_-(\ell-\cdot)\|_{L^2(0,\ell)}
=
\|r_-\|_{L^2(0,\ell)}.
\]

Hence for

\[
u\in F_\infty,
\]

\[
\boxed{
\|r_-(\ell-\cdot)\|_{L^2(0,\ell)}
=
o(\ell^N)
\qquad
\forall N.
}
\]

So the entry-zone old-exterior contribution is superflat.

The mirror statement holds on the opposite edge.

---

# IX. Uniformity along the compressed orbit

## 13. Operator superflatness

QA-3 already showed that the canonical collar Gramian is superflat in operator
norm on the finite-dimensional edge quotient.

Equivalently, there are scalar functions

\[
q_N(\varepsilon)\to0
\]

such that uniformly for

\[
v\in E,
\]

\[
\Delta_{c,c+\varepsilon}(v)
\le
q_N(\varepsilon)\varepsilon^N\|v\|.
\]

The compressed shifts satisfy

\[
\|A_\ell^k\|\le1.
\]

Therefore for every

\[
0\le k<d,
\]

the collar residuals of

\[
A_\ell^k v
\]

are uniformly superflat.

Sections VI--VIII then imply that their:

- mean corrections;
- raw exterior residuals;
- shifted entry residuals

are uniformly superflat as well.

Thus the entire finite compressed orbit from GERM-11 has superflat entry
residuals.

---

# X. Where the linear mismatch must live

## 14. Compare the two results

For a nonzero obstruction:

### Source/moment side

There is a fixed finite chart with

\[
\boxed{
\|R_J(\ell)\|
\ge
c_J\ell.
}
\]

### Old-exterior entry side

For every compressed-orbit vector,

\[
\boxed{
\text{entry residual}
=
o(\ell^N)
\qquad
\forall N.
}
\]

Therefore the unavoidable finite-order moment mismatch cannot be explained by
the shifted old-exterior residual alone.

It must be carried by the remaining custody channels:

\[
\boxed{
\text{boundary-prefix strip}
+
\text{projection/ejection}.
}
\]

This is the sharpest transfer localization presently available.

---

# XI. Why this still does not close \(\mathcal E_c\)

## 15. Different observables

The collar residual and the moment mismatch are different linear observations
of the source.

Superflatness of one does not automatically imply superflatness of the other.

GERM-1 and GERM-5 already supplied local smooth-flat mechanisms showing that a
Volterra edge output can be infinitely flat while the underlying source
retains nontrivial interior information.

The present pass now shows that the source-side translation/moment detector
must in fact remain finite-order nonflat.

There is no contradiction unless the actual Weil equation identifies that
source-side mismatch with a bounded transform of the collar observation.

No such identity is currently established.

---

# XII. Local sharpness model for the missing transfer

## 16. One-dimensional Volterra model

The lack of an automatic transfer persists even in a smooth
one-dimensional local model.

Choose an interior hinge location

\[
s_0\in(0,L)
\]

and a small radius \(\rho>0\).

Let

\[
h(t)=e^{-1/t^2}
\qquad
(t>0)
\]

with a smooth cutoff inside \((0,\rho)\), and set

\[
f(s_0-t)=h''(t)
\]

on the left side of the hinge, with \(f\) smooth and compactly supported
there.

Then the corresponding hinge Volterra observation is

\[
\int_0^\delta
(\delta-t)f(s_0-t)\,dt
=
h(\delta)
\]

for sufficiently small \(\delta\).

Thus the edge output is nonzero and infinitely flat.

But the one-dimensional source space

\[
V=\operatorname{span}\{f\}
\]

has ordinary truncated-translation compression and archimedean moments, whose
finite-chart mismatch is not forced to be superflat and is subject to the
finite-order translation bounds above.

This model is **not** an actual Weil kernel vector.

Its role is only to show that:

\[
\boxed{
\text{finite dimensionality}
+
\text{local Volterra structure}
+
\text{superflat edge output}
}
\]

do not imply superflat source-shift mismatch.

The missing transfer must use the global first-kind Weil equation in a new
way.

---

# XIII. Result of this NF pass

The superflat-to-defect problem now has a precise split.

A nonzero edge obstruction satisfies simultaneously:

\[
\boxed{
\text{raw exterior/entry residuals are superflat},
}
\]

while for a fixed finite separating moment chart,

\[
\boxed{
\|R_J(\ell)\|
\ge
c_J\ell.
}
\]

Therefore the mismatch detected in GERM-11 is quantitatively finite-order and
cannot come from the already-superflat shifted old-exterior term.

It must reside in the boundary-prefix/projection channel.

This is a structural advance, but not a contradiction.

---

# XIV. Next traversal target

The next genuinely new target is

\[
\boxed{
\text{SZ-KERNEL-EDGE-GERM-13 / EJECTION-EDGE IDENTITY}.
}
\]

The next pass should derive the exterior/collar observation of the canonical
ejection

\[
Q S_\ell f
\]

and compare it directly with:

\[
D_\ell^+\mathcal J_\ell f.
\]

The target is an operator identity or estimate of the form

\[
\boxed{
\text{moment mismatch}
=
\mathcal L_\ell
\left(
\text{collar observations of }
f,\,
A_\ell f,\,
QS_\ell f
\right)
}
\]

with controlled \(\mathcal L_\ell\).

If the boundary/projection mismatch were a bounded transform of quantities
already known to be superflat, the linear lower bound of this pass would force

\[
\mathcal E_c=0.
\]

Conversely, failure of such an identity would identify support ejection as the
terminal independent carrier of the edge obstruction.

No ejection-edge identity is proved here.

---

# XV. Cursor status

The canonical theorem cursor remains

\[
\boxed{\text{SZ-CROSS-COLLAR-3}}.
\]

This is an unratified quantitative-transfer / no-go residue.

No public promotion and no canonical cursor movement are asserted.
