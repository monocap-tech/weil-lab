# SZ-KERNEL-EDGE-GERM-17 — Dyadic threshold equation and blind-side transfer

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Immediate residue:** SZ-KERNEL-EDGE-GERM-16  
**Target tested:** DYADIC ESCAPE FIELD TRANSFER  
**Public promotion:** forbidden

## 0. Objective

GERM-16 proved that every nonzero jointly-superflat visible obstruction
direction has finite dyadic escape depth under repeated translation by

\[
a=\log2.
\]

At its first escape step, a nonzero component enters \(K_c^\perp\).

The open question was whether that fixed-scale nonkernel escape forces a
finite-order signature back into one of the preceding shrinking edge collars.

This pass derives the exact local equation at every dyadic step.

The result is a precise transfer, but not yet a contradiction:

\[
\boxed{
\text{visible endpoint germ}
\longleftrightarrow
\text{blind-left archimedean transform at the next dyadic hinge}.
}
\]

If the next dyadic translate remains in \(K_c\), the two channels cancel
exactly.

If the next translate leaves \(K_c\), the first nonkernel escape field is
exactly the defect of that cancellation.

Because the visible endpoint germ is superflat on
\(E_{\rm vis}^\infty\), every finite-order or superflat property of the escape
field is inherited, up to a superflat error, by the blind-side archimedean
transform.

Thus the fixed-scale escape graph does transfer back to local edge data—but
to the **blind side** of the next hinge, not to its already-controlled visible
side.

This is the same one-sided seam isolated in GERM-1/3, now obtained as an exact
dyadic threshold equation.

---

# I. One dyadic kernel step

## 1. Setup

Let

\[
a=\log2.
\]

Take a right-oriented source

\[
g\in K_+
\]

such that its endpoint prefix is superflat:

\[
\boxed{
\|g\|_{L^2(0,\varepsilon)}
=
o(\varepsilon^N)
\qquad
\forall N.
}
\]

For the dyadic graph, \(g\) is typically

\[
g=S_a^jf
\]

for

\[
f\in E_{\rm vis}^\infty.
\]

Its next truncated shift is

\[
S_ag.
\]

---

# II. The first-prime boundary commutator

## 2. Core-zone formula

Return temporarily to physical coordinates and let \(u\in K_c\) correspond to
\(g\).

GERM-8 gives, for

\[
-c+a<x<c,
\]

\[
F_{T_{a,c}u}(x)
=
C_u-B_{a,+}u(x),
\]

where

\[
B_{a,+}u(x)
=
\int_{c-a}^{c}
g_{\rm screw}(x-a-z)u(z)\,dz.
\]

Write

\[
x=c-\eta,
\qquad
\eta>0.
\]

In source coordinates

\[
t=c-z,
\qquad
0<t<a,
\]

this becomes

\[
\boxed{
B_{a,+}u(c-\eta)
=
\int_0^a
g_{\rm screw}(a+\eta-t)\,g(t)\,dt.
}
\]

Set

\[
r=a-t.
\]

Then

\[
\boxed{
B_{a,+}u(c-\eta)
=
\int_0^a
g_{\rm screw}(\eta+r)\,g(a-r)\,dr.
}
\]

This is the key local form.

---

# III. Geometry of the two cell endpoints

## 3. Blind versus visible source sides

In

\[
\int_0^a
g_{\rm screw}(\eta+r)\,g(a-r)\,dr,
\]

the point

\[
r=0
\]

samples

\[
g(a-r)
\]

immediately to the **left** of the first-prime hinge

\[
s=a.
\]

This is the outward-blind side for the right-edge inward equation.

By contrast,

\[
r=a
\]

samples

\[
g(a-r)=g(0+),
\]

the current endpoint-visible germ.

Therefore the first-prime commutator couples exactly:

\[
\boxed{
\text{blind-left germ at }s=a
\quad\text{to}\quad
\text{visible endpoint germ at }s=0.
}
\]

For the \(j\)-th dyadic iterate of an original source \(f\), these correspond
to the original sites

\[
(j+1)a-
\]

and

\[
ja+,
\]

respectively.

---

# IV. Only the first prime is active locally

## 4. Choose a small \(\eta\)-window

Let

\[
\eta_0
<
\log3-\log2.
\]

For

\[
0<\eta<\eta_0
\]

and

\[
0<r<a,
\]

we have

\[
0<\eta+r<\log3.
\]

Hence the only positive prime-power hinge that can occur in the kernel
argument is

\[
a=\log2.
\]

Using Suzuki's decomposition,

\[
g_{\rm screw}(t)
=
a_\infty(t)
+
d_2(t-a)_+,
\qquad
0<t<\log3,
\]

where

\[
\boxed{
d_2
=
\frac{\log2}{\sqrt2}.
}
\]

---

# V. Differentiate the commutator twice

## 5. Archimedean plus threshold atom

For

\[
0<\eta<\eta_0,
\]

differentiate the local commutator in distributions.

The archimedean part gives

\[
\int_0^a
a_\infty''(\eta+r)g(a-r)\,dr.
\]

The prime hinge satisfies

\[
\frac{d^2}{dt^2}(t-a)_+
=
\delta_a.
\]

Therefore

\[
\int_0^a
\delta(\eta+r-a)
g(a-r)\,dr
=
g(\eta)
\]

for almost every \(\eta\in(0,\eta_0)\).

Hence

\[
\boxed{
\frac{d^2}{d\eta^2}
B_{a,+}u(c-\eta)
=
d_2g(\eta)
+
\int_0^a
a_\infty''(\eta+r)g(a-r)\,dr.
}
\]

This identity holds in the distributional/\(L^2_{\rm loc}\) sense required by
the source regularity.

---

# VI. Exact threshold equation when the next shift remains in the kernel

## 6. Kernel-contained next step

Suppose

\[
S_ag\in K_+.
\]

Then the physical translated vector \(T_{a,c}u\) has constant screw potential
on the whole old interval.

On the core zone,

\[
F_{T_{a,c}u}(c-\eta)
=
C_u-B_{a,+}u(c-\eta).
\]

Therefore

\[
B_{a,+}u(c-\eta)
\]

is constant for

\[
0<\eta<\eta_0.
\]

Its second derivative vanishes.

Section V gives the exact equation

\[
\boxed{
d_2g(\eta)
+
\int_0^a
a_\infty''(\eta+r)g(a-r)\,dr
=
0
}
\]

for almost every sufficiently small \(\eta>0\).

Thus a kernel-contained dyadic step forces exact cancellation between:

1. the threshold prime atom sampling the visible endpoint germ \(g(\eta)\);
2. the archimedean transform of the blind-left germ \(g(a-r)\).

---

# VII. Explicit exponential moment form

## 7. Insert GERM-2's archimedean expansion

GERM-2 gives

\[
a_\infty''(t)
=
-e^{t/2}
+
\sum_{m=1}^{\infty}
e^{-\lambda_m t},
\qquad
\lambda_m=2m+\frac12.
\]

Therefore the threshold equation becomes

\[
\boxed{
d_2g(\eta)
-
e^{\eta/2}A_+
+
\sum_{m=1}^{\infty}
e^{-\lambda_m\eta}A_m
=
0,
}
\]

where

\[
\boxed{
A_+
=
\int_0^a
e^{r/2}g(a-r)\,dr,
}
\]

and

\[
\boxed{
A_m
=
\int_0^a
e^{-\lambda_m r}g(a-r)\,dr.
}
\]

Equivalently, in the original cell coordinate \(t=a-r\),

\[
A_+
=
e^{a/2}
\int_0^a
e^{-t/2}g(t)\,dt,
\]

and

\[
A_m
=
e^{-\lambda_ma}
\int_0^a
e^{\lambda_mt}g(t)\,dt.
\]

The large-\(m\) moments emphasize the blind endpoint

\[
t=a^-.
\]

---

# VIII. Superflat visible germ forces a superflat blind transform

## 8. Transfer

Because

\[
g\in E_{\rm vis}^\infty
\]

after the appropriate dyadic relocation,

\[
\|g\|_{L^2(0,\varepsilon)}
=
o(\varepsilon^N)
\qquad
\forall N.
\]

Thus the threshold term

\[
d_2g(\eta)
\]

is superflat in local \(L^2\).

If the next dyadic step remains in \(K_c\), the exact threshold equation gives

\[
\boxed{
\left\|
\int_0^a
a_\infty''(\eta+r)g(a-r)\,dr
\right\|_{L^2(0,\varepsilon)}
=
o(\varepsilon^N)
\qquad
\forall N.
}
\]

Therefore kernel custody propagates visible superflatness into superflatness of
the blind-side archimedean transform.

It does **not** yet imply

\[
\|g\|_{L^2(a-\varepsilon,a)}
=
o(\varepsilon^N).
\]

That missing implication is precisely a one-sided quasi-analyticity/coercivity
problem.

---

# IX. First nonkernel escape equals the threshold-equation defect

## 9. Escape step

Now suppose

\[
g\in K_+
\]

but

\[
S_ag\notin K_+.
\]

Let

\[
n
=
(I-\Pi_K)S_ag
\in K_+^\perp
\]

be the first nonkernel escape.

GERM-13 gives on the core zone

\[
F_n(c-\eta)
=
\text{constant}
-
B_{a,+}u(c-\eta).
\]

Therefore

\[
\boxed{
\frac{d^2}{d\eta^2}F_n(c-\eta)
=
-
d_2g(\eta)
-
\int_0^a
a_\infty''(\eta+r)g(a-r)\,dr.
}
\]

Thus the first nonkernel escape field is exactly the defect of the
kernel-contained threshold equation.

---

# X. Escape-field transfer

## 10. Superflat threshold term

Since the visible endpoint term \(g(\eta)\) is superflat,

\[
d_2g(\eta)
\]

is superflat.

Hence

\[
\boxed{
F_n''(c-\eta)
+
\int_0^a
a_\infty''(\eta+r)g(a-r)\,dr
}
\]

is superflat.

Therefore:

- if the escape-field second derivative has a finite-order boundary germ,
  the blind-side archimedean transform has the same finite-order germ up to a
  superflat error;
- if the escape-field second derivative is superflat, then the blind-side
  archimedean transform is superflat as well.

So every dyadic escape transfers its local boundary behavior to the blind
side of the next hinge.

---

# XI. Why fixed nonzero escape does not force a finite boundary jet

## 11. Nonzero source versus flat boundary field

GERM-16 gives a fixed lower bound

\[
\|n\|
\ge
\nu_j\|f\|
\]

on each nonzero escape layer.

However, a nonzero compactly supported source may have an exterior
Cauchy/Stieltjes-type field flatter than every algebraic order at a boundary
point.

The earlier rough-endpoint/Stieltjes no-go and GERM-5 show that smooth or
\(L^2\) sources can support precisely this pattern.

Therefore:

\[
\boxed{
\|n\|>0
\not\Rightarrow
F_n''(c-\eta)
\text{ has finite nonzero boundary order}.
}
\]

Fixed-scale nonkernel escape cannot by itself close the shrinking-collar
problem.

---

# XII. Local sharpness of the blind-side transfer

## 12. Abstract cell model

Take a source profile \(b(r)\) on

\[
(0,a)
\]

whose archimedean transform

\[
\mathscr A_b(\eta)
=
\int_0^a
a_\infty''(\eta+r)b(r)\,dr
\]

is nonzero but superflat as

\[
\eta\downarrow0.
\]

Such behavior is compatible with the generic Stieltjes/Cauchy mechanism
already isolated in the earlier endpoint no-go chain.

Choose the visible endpoint contribution \(g(\eta)\) superflat as well.

Then the threshold-equation defect

\[
d_2g(\eta)+\mathscr A_b(\eta)
\]

may also be superflat and nonzero.

This supplies a local model of:

\[
\boxed{
\text{nonzero fixed escape}
+
\text{superflat local escape field}.
}
\]

It is not asserted to be an actual Weil kernel orbit.

Its purpose is to show that the dyadic graph plus local threshold geometry do
not automatically provide the missing finite-order transfer.

---

# XIII. Iterated dyadic consequence

## 13. Kernel-contained path

Take

\[
f\in E_{\rm vis}^\infty
\]

with dyadic escape depth

\[
j+1.
\]

Then for

\[
k=0,\ldots,j-1,
\]

both

\[
S^kf
\]

and

\[
S^{k+1}f
\]

lie in \(K_+\).

Hence each step satisfies an exact threshold equation:

\[
\boxed{
d_2(S^kf)(\eta)
+
\int_0^a
a_\infty''(\eta+r)
(S^kf)(a-r)\,dr
=
0.
}
\]

Every visible endpoint germ in this chain is superflat.

Therefore every corresponding blind-side archimedean transform is superflat.

At the terminal step \(k=j\), the same expression equals minus the second
derivative of the nonkernel escape field.

Thus the whole dyadic path propagates all-orders flatness through a sequence
of blind-side transforms until the first nonkernel escape.

---

# XIV. Result of this NF pass

The fixed-scale dyadic escape has now been transferred exactly to a local edge
equation.

For each kernel-contained dyadic step,

\[
\boxed{
\frac{\log2}{\sqrt2}\,g(\eta)
+
\int_0^{\log2}
a_\infty''(\eta+r)
g(\log2-r)\,dr
=
0.
}
\]

The visible term \(g(\eta)\) is superflat.

Therefore the blind-side archimedean transform at the next dyadic hinge is
superflat.

At the first nonkernel escape, the failure of this equation is exactly the
local screw field of the escaping \(K_c^\perp\) component.

Hence the scale-transfer problem does not disappear.

It moves from:

\[
\text{fixed nonkernel escape}
\]

to:

\[
\boxed{
\text{quasi-analyticity/coercivity of the blind-side archimedean transform}.
}
\]

This is a strict localization improvement, but not an elimination.

---

# XV. Next traversal target

The next genuinely new target is

\[
\boxed{
\text{SZ-KERNEL-EDGE-GERM-18 / BLIND-TRANSFORM FILTRATION}.
}
\]

The next pass should apply finite-dimensional stabilization directly to the
blind-side transforms

\[
g
\longmapsto
\int_0^{\log2}
a_\infty''(\eta+r)g(\log2-r)\,dr
\]

on the dyadic escape layers.

The target is to split each layer into:

1. directions with a finite-order blind-transform germ;
2. directions whose blind transform is superflat to every order.

For the second branch, the explicit exponential-moment expansion should be
used to determine whether all-orders transform flatness forces a further
finite-dimensional moment relation, reflection constraint, or dimension
drop.

No such blind-transform filtration is proved in this pass.

---

# XVI. Cursor status

The canonical theorem cursor remains

\[
\boxed{\text{SZ-CROSS-COLLAR-3}}.
\]

This is an unratified dyadic field-transfer / blind-side reduction.

No public promotion and no canonical cursor movement are asserted.
