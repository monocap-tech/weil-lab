# SZ-KERNEL-EDGE-GERM-14 — Fixed-width strip coercivity and the no-rate barrier

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Immediate residue:** SZ-KERNEL-EDGE-GERM-13  
**Target tested:** BOUNDARY-PREFIX COERCIVITY  
**Public promotion:** forbidden

## 0. Objective

GERM-13 decomposed the canonical translation ejection into:

\[
\boxed{
\text{endpoint-prefix source}
\;+\;
\text{persistent kernel}
\;+\;
\text{nonflat kernel}
\;+\;
\text{nonkernel ejection}.
}
\]

The remaining proposed route was a quantitative small-strip estimate converting
the discarded boundary-prefix source into its smaller-support screw field.

This pass establishes the exact fixed-width statement and then proves the
relevant no-go.

For every fixed sufficiently small strip width \(\ell\), the prime-free
exterior screw field determines the discarded strip source, and therefore
finite-dimensional coercivity holds on the restriction image of the edge
obstruction.

However:

\[
\boxed{
\text{neither finite dimensionality nor small-window positivity supplies
a controlled power-law lower bound as }\ell\downarrow0.
}
\]

A one-dimensional moving-prefix example can make the fixed-width coercivity
constant decay faster than every algebraic power along a sequence.

Thus the missing estimate must exploit additional regularity/rigidity of the
**actual Weil kernel family near the endpoint**.

---

# I. Boundary-prefix source

## 1. Right-oriented prefix

Let

\[
L=2c,
\qquad
f(s)=u(c-s),
\qquad
0<s<L.
\]

For

\[
0<\ell<L,
\]

the discarded physical strip

\[
(c-\ell,c)
\]

corresponds to the prefix

\[
(0,\ell).
\]

Write

\[
\boxed{
R_\ell f
=
f|_{(0,\ell)}.
}
\]

For the canonical edge representative \(E_+\subset L^2(0,L)\), define its
restriction image

\[
\boxed{
V_\ell
=
R_\ell(E_+)
\subset
L^2(0,\ell).
}
\]

This is finite dimensional, with

\[
\dim V_\ell\le d:=\dim E_+.
\]

No injectivity of \(R_\ell:E_+\to V_\ell\) is asserted; an obstruction vector
may vanish near the physical endpoint while remaining nontrivial at another
singular site.

---

# II. Recentered strip

## 2. Symmetric coordinate

Set

\[
a=\frac{\ell}{2}.
\]

For

\[
g_\ell:=R_\ell f,
\]

define the recentered strip source

\[
\boxed{
w(r)=g_\ell(a-r),
\qquad
-a<r<a.
}
\]

Then the screw potential of the strip is

\[
F_w(z)
=
\int_{-a}^{a}
g(z-r)w(r)\,dr.
\]

At the right exterior point

\[
z=a+\delta,
\]

the change of variables

\[
s=a-r
\]

gives

\[
\boxed{
F_w(a+\delta)
=
\int_0^\ell
g(\delta+s)g_\ell(s)\,ds.
}
\]

---

# III. Prime-free exterior window

## 3. Choose the window

Assume

\[
\boxed{
0<\ell<\frac{\log2}{3}.
}
\]

Take

\[
\delta\in(\ell,2\ell).
\]

Then for

\[
0<s<\ell,
\]

\[
0<\delta+s<3\ell<\log2.
\]

Therefore no prime-power hinge is active in the kernel argument

\[
\delta+s.
\]

On this entire observation window,

\[
g(\delta+s)
=
a_\infty(\delta+s),
\]

the Suzuki archimedean component.

---

# IV. Exact prefix-moment expansion

## 4. Differentiate outside the support

Because

\[
\delta>0,
\]

the observation point remains a positive distance from the strip support.

Hence differentiation under the integral is legitimate.

GERM-2 derived

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

Thus

\[
\boxed{
\frac{d^2}{d\delta^2}F_w(a+\delta)
=
-
e^{\delta/2}J_{\ell,+}(g_\ell)
+
\sum_{m=1}^{\infty}
e^{-\lambda_m\delta}
J_{\ell,m}(g_\ell),
}
\]

where

\[
\boxed{
J_{\ell,+}(g_\ell)
=
\int_0^\ell
e^{s/2}g_\ell(s)\,ds,
}
\]

and

\[
\boxed{
J_{\ell,m}(g_\ell)
=
\int_0^\ell
e^{-\lambda_m s}g_\ell(s)\,ds.
}
\]

These are exactly the endpoint-prefix archimedean moments from the
GERM-10/13 defect decomposition.

---

# V. Fixed-width injectivity

## 5. Constant exterior field implies zero strip source

Suppose

\[
F_w(a+\delta)
\]

is constant on a nonempty open subinterval of

\[
(\ell,2\ell).
\]

Then

\[
F_w''(a+\delta)=0
\]

there.

By real analyticity in \(\delta>0\), this identity extends through the
prime-free connected exterior window.

Set

\[
q=e^{-\delta/2}.
\]

Then

\[
e^{\delta/2}=q^{-1},
\qquad
e^{-\lambda_m\delta}=q^{4m+1}.
\]

The zero second derivative becomes the Laurent identity

\[
-
J_{\ell,+}q^{-1}
+
\sum_{m=1}^{\infty}
J_{\ell,m}q^{4m+1}
=
0.
\]

Uniqueness of Laurent coefficients gives

\[
J_{\ell,+}=0
\]

and

\[
J_{\ell,m}=0
\qquad
\forall m\ge1.
\]

The change of variables

\[
x=e^{-2s}
\]

takes \((0,\ell)\) to

\[
(e^{-2\ell},1).
\]

As in GERM-2, polynomial density implies

\[
g_\ell=0.
\]

Therefore:

\[
\boxed{
\text{the exterior strip potential modulo constants is injective on }
L^2(0,\ell).
}
\]

No small-window kernel hypothesis is required for this injectivity; it follows
from the explicit prime-free Suzuki archimedean transform.

---

# VI. Fixed-width finite-dimensional coercivity

## 6. Exterior oscillation map

Fix, for example, the reference point

\[
\delta_0=\frac32\ell
\]

and define

\[
\boxed{
\mathcal B_\ell g_\ell(\delta)
=
F_w(a+\delta)-F_w(a+\delta_0),
\qquad
\ell<\delta<2\ell.
}
\]

Section V gives

\[
\ker\mathcal B_\ell=\{0\}.
\]

Restrict to the finite-dimensional image

\[
V_\ell=R_\ell(E_+).
\]

Then compactness of the unit sphere gives a number

\[
\boxed{
\kappa_E(\ell)>0
}
\]

such that

\[
\boxed{
\|\mathcal B_\ell g_\ell\|_{L^2(\ell,2\ell)}
\ge
\kappa_E(\ell)
\|g_\ell\|_{L^2(0,\ell)}
\qquad
(g_\ell\in V_\ell).
}
\]

Thus boundary-prefix coercivity is valid at every fixed sufficiently small
strip width.

---

# VII. Fixed-width moment/field equivalence

## 7. Finite moment chart on the restriction image

The full prefix moment family

\[
\{
J_{\ell,m}
\}_{m\ge1}
\]

separates \(V_\ell\).

Hence one can choose

\[
r_\ell\le\dim V_\ell
\]

indices

\[
m_1(\ell),\ldots,m_{r_\ell}(\ell)
\]

such that

\[
\boxed{
g_\ell
\longmapsto
\left(
J_{\ell,m_j(\ell)}(g_\ell)
\right)_{j=1}^{r_\ell}
}
\]

is injective.

Consequently, for each fixed \(\ell\), there are positive finite constants
relating:

- the \(L^2\) norm of the prefix source;
- a finite prefix-moment vector;
- the prime-free exterior strip field.

This is a complete fixed-width statement.

What is missing is control of those constants as

\[
\ell\downarrow0.
\]

---

# VIII. Small-window positivity does not give an \(L^2\) spectral gap

## 8. Positivity versus coercivity

For

\[
a\le\frac{\log2}{2},
\]

Bombieri--Yoshida positivity implies triviality of the regular zero kernel on
the small centered support.

That is an injectivity statement for the relevant small-window Weil/screw
operator.

It is **not** a uniform \(L^2\) coercivity statement.

Suzuki's screw operator \(G_a\) is compact.

Even when a compact self-adjoint operator is injective, its positive
eigenvalues may accumulate at zero.

Therefore:

\[
\boxed{
K_a=\{0\}
\not\Rightarrow
G_a\succeq\eta(a)I
\text{ on the full infinite-dimensional carrier}.
}
\]

Small-window positivity alone cannot supply a global source-norm lower bound.

---

# IX. Why finite dimensionality still gives no power rate

## 9. The restriction family moves with \(\ell\)

At each fixed \(\ell\),

\[
V_\ell
=
R_\ell(E_+)
\]

is finite dimensional.

But the normalized restricted directions

\[
\frac{R_\ell f}{\|R_\ell f\|}
\]

may vary arbitrarily rapidly as

\[
\ell\downarrow0.
\]

Finite dimensionality of the *ambient source family* \(E_+\) does not make
this normalized moving restriction family compact in a topology stronger than
\(L^2\) with a controlled modulus.

No endpoint trace or finite vanishing order is presently available.

---

# X. Sharpness construction for the rate

## 10. A one-dimensional moving-prefix family

The absence of a power-rate theorem is not merely formal.

Choose a decreasing sequence

\[
\ell_k\downarrow0
\]

with

\[
3\ell_k<\log2.
\]

Choose pairwise disjoint intervals

\[
I_k
=
(\ell_k-\delta_k,\ell_k)
\subset
(0,L),
\]

where

\[
0<\delta_k\ll\ell_k.
\]

Let

\[
\phi_k\in C_c^\infty(I_k)
\]

be \(L^2\)-normalized.

Choose positive coefficients \(b_k\) decreasing sufficiently rapidly that:

1. 
   \[
   \sum_k b_k^2<\infty;
   \]
2. in the prefix \((0,\ell_k)\), the \(k\)-th bump dominates the \(L^2\) norm;
3. the \(L^1\) contribution of all later bumps is negligible compared with
   \[
   b_k\sqrt{\delta_k}.
   \]

Set

\[
\boxed{
f
=
\sum_{k\ge1}
b_k\phi_k.
}
\]

Then

\[
V=\operatorname{span}\{f\}
\]

is one dimensional.

For the normalized prefix

\[
w_k
=
\frac{f|_{(0,\ell_k)}}{
\|f\|_{L^2(0,\ell_k)}
},
\]

one can arrange

\[
\boxed{
\|w_k\|_{L^1(0,\ell_k)}
\lesssim
\sqrt{\delta_k}.
}
\]

---

## 11. Exterior field upper bound

Suzuki's origin expansion gives, for sufficiently small positive \(t\),

\[
|g(t)|
\lesssim
t|\log t|.
\]

For

\[
\delta\in(\ell_k,2\ell_k),
\qquad
0<s<\ell_k,
\]

we have

\[
0<\delta+s<3\ell_k.
\]

Hence

\[
|g(\delta+s)|
\lesssim
\ell_k|\log\ell_k|.
\]

Therefore the normalized strip potential satisfies

\[
\sup_{\ell_k<\delta<2\ell_k}
|F_{w_k}(a_k+\delta)|
\lesssim
\ell_k|\log\ell_k|
\|w_k\|_1.
\]

Thus

\[
\boxed{
\|\mathcal B_{\ell_k}w_k\|_{L^2(\ell_k,2\ell_k)}
\lesssim
\ell_k^{3/2}
|\log\ell_k|
\sqrt{\delta_k}.
}
\]

---

## 12. Arbitrarily fast degeneration

Choose

\[
\delta_k
\]

so rapidly decreasing that

\[
\ell_k^{3/2}
|\log\ell_k|
\sqrt{\delta_k}
=
o(\ell_k^N)
\]

for every fixed \(N\) as \(k\to\infty\).

For example, one may take a superalgebraically small sequence such as

\[
\delta_k
=
\exp(-2/\ell_k).
\]

Then

\[
\boxed{
\|\mathcal B_{\ell_k}w_k\|
=
o(\ell_k^N)
\qquad
\forall N.
}
\]

Since

\[
\|w_k\|_2=1,
\]

the fixed-width coercivity constants satisfy

\[
\boxed{
\kappa_V(\ell_k)
=
o(\ell_k^N)
\qquad
\forall N
}
\]

along this sequence.

The coefficients \(b_k\) may be chosen even faster decreasing if one wants
the resulting fixed source \(f\) to have an arbitrarily regular or flat
endpoint representative.

This is an **abstract local source-family sharpness model**, not a construction
of an actual Weil kernel vector.

---

# XI. Consequence for the proposed power estimate

## 13. No abstract polynomial coercivity

From the currently available ingredients

\[
\text{finite dimension}
+
\text{prime-free small-strip injectivity}
+
\text{small-window positivity},
\]

one cannot infer constants

\[
C,\alpha>0
\]

such that

\[
\boxed{
\|g_\ell\|_2
\le
C\ell^{-\alpha}
\|\mathcal B_\ell g_\ell\|
}
\]

uniformly for all sufficiently small \(\ell\).

Nor can one infer an analogous uniform power estimate recovering the prefix
moment vector from the strip field.

The sharpness construction defeats every prescribed algebraic rate.

---

# XII. Relation to GERM-13's nonkernel ejection

## 14. Fixed-\(\ell\) recovery

GERM-13 gives on the core zone

\[
F_{n_\ell}(x)
=
\text{constant}
-
B_{\ell,+}u(x).
\]

Therefore, for each fixed \(\ell\), the strip source carried by

\[
R_\ell f
\]

is recoverable from the nonconstant interior field of \(n_\ell\).

On the finite-dimensional restriction image this gives a fixed-\(\ell\)
estimate.

But the constant may degenerate superalgebraically as

\[
\ell\downarrow0.
\]

Thus GERM-13's exact field identity does not provide the rate needed to
contradict GERM-12's linear mismatch floor.

---

# XIII. The kernel-ejection blocks remain independent

## 15. Persistent and nonflat kernel components

Even a hypothetical quantitative estimate for the nonkernel block

\[
n_\ell
\]

would leave the two kernel-ejection components from GERM-13:

\[
p_\ell\in P_c^+,
\qquad
h_\ell\in K_c\cap F_\infty^\perp.
\]

They have constant old-interior screw potential and are therefore invisible to
the strip-field identity.

Their moment contributions

\[
\mathcal M p_\ell,
\qquad
\mathcal M h_\ell
\]

remain independent custody channels.

So boundary-prefix coercivity cannot by itself close the entire GERM-12
mismatch.

---

# XIV. Result of this NF pass

The small-strip boundary problem now has a complete fixed-width
classification.

For every fixed sufficiently small \(\ell\):

\[
\boxed{
\text{endpoint prefix}
\longleftrightarrow
\text{prime-free exterior strip field}
}
\]

is injective, and on the finite-dimensional restriction image one has a
positive coercivity constant

\[
\boxed{
\kappa_E(\ell)>0.
}
\]

But:

\[
\boxed{
\text{no algebraic lower rate for }\kappa_E(\ell)
\text{ follows from the current structure}.
}
\]

A one-dimensional moving-prefix family can make

\[
\kappa_E(\ell_k)
\]

smaller than every power along a shrinking sequence.

Therefore the sought boundary-prefix rate is itself another
kernel-restricted endpoint regularity statement.

The route has not escaped the original quasi-analyticity barrier; it has
reexpressed it in singular-value form.

---

# XV. Next traversal target

The next genuinely new target is

\[
\boxed{
\text{SZ-KERNEL-EDGE-GERM-15 / PREFIX-MASS FILTRATION}.
}
\]

The next pass should use finite dimensionality of the actual edge obstruction
to classify the possible decay of

\[
\|f\|_{L^2(0,\ell)}
\]

and of finite prefix-moment vectors as

\[
\ell\downarrow0.
\]

The aim is to separate:

1. obstruction directions with a finite-order endpoint-prefix mass;
2. directions superflat at the physical endpoint but forced to remain visible
   at interior prime singular sites;
3. directions whose translation ejection enters \(H^{\rm nf}\) at finite
   collar order.

A successful filtration comparison could show that every nonzero obstruction
must expose a finite-order channel somewhere, even if the endpoint prefix
itself is superflat.

No such filtration comparison is proved in this pass.

---

# XVI. Cursor status

The canonical theorem cursor remains

\[
\boxed{\text{SZ-CROSS-COLLAR-3}}.
\]

This is an unratified fixed-width coercivity / no-rate residue.

No public promotion and no canonical cursor movement are asserted.
