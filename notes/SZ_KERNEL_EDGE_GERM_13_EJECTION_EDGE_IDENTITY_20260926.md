# SZ-KERNEL-EDGE-GERM-13 — Ejection-edge identity and kernel-escape decomposition

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Immediate residue:** SZ-KERNEL-EDGE-GERM-12  
**Target tested:** EJECTION-EDGE IDENTITY  
**Public promotion:** forbidden

## 0. Objective

GERM-12 proved a sharp split:

- the old exterior/entry residual of every superflat obstruction is
  superflat;
- the canonical finite moment mismatch has an unavoidable linear lower bound.

The remaining finite-order mismatch was therefore forced into the
boundary-prefix / projection-ejection channel.

This pass identifies that channel exactly.

The canonical ejection from the edge quotient splits into three geometrically
different pieces:

\[
\boxed{
\text{persistent kernel}
\;\oplus\;
\text{nonflat kernel}
\;\oplus\;
\text{nonkernel ejection}.
}
\]

Only the nonkernel piece carries the nonconstant interior screw field of the
discarded boundary strip.

The two kernel pieces are annihilated by the interior screw equation but remain
visible to the archimedean moment map.

Therefore there is no direct factorization of the GERM-11/12 moment mismatch
through the ejection screw field alone.

The next missing input is quantitative custody of the boundary-prefix and
kernel-escape blocks.

---

# I. Canonical orthogonal decomposition of the regular kernel

## 1. Nested stabilized spaces

Let

\[
K=K_c=\ker G_c,
\qquad
F=F_\infty,
\qquad
P=P_c^+.
\]

The canonical inclusions are

\[
P\subseteq F\subseteq K.
\]

Define

\[
\boxed{
E
=
F\cap P^\perp
}
\]

and

\[
\boxed{
H^{\rm nf}
=
K\cap F^\perp.
}
\]

Then

\[
\boxed{
K
=
P\oplus^\perp E\oplus^\perp H^{\rm nf}.
}
\]

The space \(E\) is the canonical Hilbert representative of

\[
\mathcal E_c=F/P.
\]

The superscript “nf” means **nonflat-kernel complement**.

---

## 2. Flatness meaning of \(H^{\rm nf}\)

The endpoint filtration stabilizes at a finite index

\[
N_c
\]

with

\[
F_\infty=F_{N_c}.
\]

Hence for every nonzero

\[
h\in H^{\rm nf},
\]

we have

\[
h\notin F_{N_c}.
\]

Therefore

\[
\boxed{
\Delta_{c,c+\varepsilon}(h)
\ne
o(\varepsilon^{N_c})
}
\]

as \(\varepsilon\downarrow0\).

No uniform lower coefficient is asserted.

The point is only that a nonzero \(H^{\rm nf}\)-component is a
**finite-order non-superflat kernel channel**.

---

# II. Source-coordinate form

## 3. Right-oriented source space

Set

\[
L=2c,
\qquad
\mathcal H=L^2(0,L),
\]

and let

\[
U_+u(s)=u(c-s).
\]

Transport the four orthogonal blocks into \(\mathcal H\):

\[
P_+=U_+P,
\qquad
E_+=U_+E,
\qquad
H_+^{\rm nf}=U_+H^{\rm nf},
\qquad
K_+=U_+K.
\]

Let the corresponding orthogonal projections be

\[
\Pi_P,\Pi_E,\Pi_H,\Pi_K.
\]

Then

\[
\Pi_K=\Pi_P+\Pi_E+\Pi_H.
\]

---

# III. Translate a superflat obstruction

## 4. Compressed shift

For

\[
f\in E_+,
\]

let

\[
S_\ell f
\]

be the truncated left shift from GERM-10 and define the canonical compressed
obstruction component

\[
\boxed{
a_\ell
=
A_\ell f
=
\Pi_E S_\ell f.
}
\]

The total ejection is

\[
\boxed{
q_\ell
=
Q S_\ell f
=
(I-\Pi_E)S_\ell f.
}
\]

---

## 5. Three-block ejection

Define

\[
\boxed{
p_\ell
=
\Pi_P S_\ell f,
}
\]

\[
\boxed{
h_\ell
=
\Pi_H S_\ell f,
}
\]

and

\[
\boxed{
n_\ell
=
(I-\Pi_K)S_\ell f.
}
\]

Then

\[
\boxed{
S_\ell f
=
a_\ell+p_\ell+h_\ell+n_\ell
}
\]

orthogonally, and

\[
\boxed{
q_\ell
=
p_\ell+h_\ell+n_\ell.
}
\]

Thus the GERM-10 projection term

\[
Q S_\ell f
\]

contains three distinct carriers.

---

# IV. Physical-space version

## 6. Return to \((-c,c)\)

Let

\[
u=U_+^{-1}f\in E,
\]

\[
v_\ell=U_+^{-1}a_\ell\in E,
\]

\[
p_\ell^{\rm phys}=U_+^{-1}p_\ell\in P,
\]

\[
h_\ell^{\rm phys}=U_+^{-1}h_\ell\in H^{\rm nf},
\]

and

\[
n_\ell^{\rm phys}=U_+^{-1}n_\ell\in K^\perp.
\]

To simplify notation below, suppress the superscript “phys”.

Then

\[
\boxed{
T_{\ell,c}u
=
v_\ell+p_\ell+h_\ell+n_\ell.
}
\]

The first three terms except \(n_\ell\) lie in \(K_c\).

Therefore their screw potentials are constant throughout the old interval.

---

# V. Exact core-zone ejection identity

## 7. Boundary-strip potential

GERM-8 defined

\[
\boxed{
B_{\ell,+}u(x)
=
\int_{c-\ell}^{c}
g(x-\ell-z)u(z)\,dz.
}
\]

For

\[
-c+\ell<x<c,
\]

GERM-8 gives

\[
F_{T_{\ell,c}u}(x)
=
C_u-B_{\ell,+}u(x).
\]

On the other hand,

\[
F_{v_\ell}(x)=C_{v_\ell},
\]

\[
F_{p_\ell}(x)=C_{p_\ell},
\]

and

\[
F_{h_\ell}(x)=C_{h_\ell}
\]

throughout the same old-interior region.

Subtracting gives

\[
\boxed{
F_{n_\ell}(x)
=
C_{\ell,u}
-
B_{\ell,+}u(x),
\qquad
-c+\ell<x<c,
}
\]

where

\[
C_{\ell,u}
=
C_u-C_{v_\ell}-C_{p_\ell}-C_{h_\ell}.
\]

Thus the entire nonconstant core-zone field of the boundary commutator is
carried by the nonkernel ejection \(n_\ell\).

---

## 8. Constant-free form

For any two points

\[
x_1,x_2\in(-c+\ell,c),
\]

the constant disappears:

\[
\boxed{
F_{n_\ell}(x_1)-F_{n_\ell}(x_2)
=
-
\left(
B_{\ell,+}u(x_1)-B_{\ell,+}u(x_2)
\right).
}
\]

This is the canonical ejection-edge identity.

It requires no convention for the additive constant in the screw potential.

---

# VI. Entry-zone identity

## 9. Shifted old exterior residual

Write

\[
x=-c+s,
\qquad
0<s<\ell.
\]

GERM-8 gives

\[
F_{T_{\ell,c}u}(-c+s)
=
C_u
+
r_-^u(\ell-s)
-
B_{\ell,+}u(-c+s).
\]

Subtracting the three kernel constants again yields

\[
\boxed{
F_{n_\ell}(-c+s)
=
C_{\ell,u}
+
r_-^u(\ell-s)
-
B_{\ell,+}u(-c+s).
}
\]

Choose any core reference point

\[
x_0\in(-c+\ell,c).
\]

Then

\[
\boxed{
F_{n_\ell}(-c+s)-F_{n_\ell}(x_0)
=
r_-^u(\ell-s)
-
\left[
B_{\ell,+}u(-c+s)-B_{\ell,+}u(x_0)
\right].
}
\]

For

\[
u\in E\subset F_\infty,
\]

GERM-12 proves

\[
\boxed{
\|r_-^u(\ell-\cdot)\|_{L^2(0,\ell)}
=
o(\ell^N)
\qquad
\forall N.
}
\]

Hence the entry-zone nonkernel ejection field equals the boundary-strip field,
up to a superflat remainder.

---

# VII. The boundary commutator is a smaller-support field

## 10. Recenter the strip

Set

\[
a=\frac{\ell}{2},
\qquad
y_0=c-a,
\]

and define

\[
w_\ell(r)
=
u(y_0+r),
\qquad
-a<r<a.
\]

GERM-8 gives

\[
\boxed{
B_{\ell,+}u(x)
=
F_{w_\ell}(x-c-a).
}
\]

Therefore Section V can be rewritten as

\[
\boxed{
F_{n_\ell}(x)
=
\text{constant}
-
F_{w_\ell}(x-c-a)
}
\]

on the core zone.

So the nonkernel ejection is exactly the carrier of the smaller-strip screw
field created by support loss.

---

# VIII. Moment defect decomposition

## 11. Full GERM-10 defect

GERM-10 gives

\[
\mathfrak R_\ell
=
-D_\ell^+\mathcal J_\ell
-
\mathcal M Q S_\ell
\]

on \(E_+\).

Using

\[
Q S_\ell
=
p_\ell+h_\ell+n_\ell,
\]

we obtain the canonical four-term split

\[
\boxed{
\mathfrak R_\ell
=
-D_\ell^+\mathcal J_\ell
-
\mathcal M p_\ell
-
\mathcal M h_\ell
-
\mathcal M n_\ell.
}
\]

The four carriers are:

1. endpoint-prefix source moments;
2. persistent-kernel moments;
3. nonflat-kernel moments;
4. nonkernel-ejection moments.

---

# IX. Edge visibility of the four carriers

## 12. Persistent block

For

\[
p_\ell\in P,
\]

the zero extension persists through a strict collar.

Hence its collar observation vanishes there.

But in general

\[
\boxed{
\mathcal M p_\ell\ne0.
}
\]

So \(p_\ell\) is:

\[
\boxed{
\text{edge-invisible but moment-visible}.
}
\]

This alone prevents reconstruction of the full moment mismatch from collar
data without additional persistent custody.

---

## 13. Nonflat kernel block

If

\[
h_\ell\ne0,
\]

then

\[
h_\ell\in H^{\rm nf}
\]

and therefore

\[
\Delta_{c,c+\varepsilon}(h_\ell)
\ne
o(\varepsilon^{N_c}).
\]

Thus \(h_\ell\) is a finite-order kernel-escape channel.

It is killed by the old-interior kernel equation but is **not** superflat at
the collar.

So translation can eject a superflat obstruction into an ordinary
finite-order leaking kernel direction.

---

## 14. Nonkernel block

The nonkernel component

\[
n_\ell\in K^\perp
\]

is the only block whose old-interior potential is nonconstant.

Sections V--VII identify that nonconstant field exactly with the discarded
boundary-strip potential.

Thus \(n_\ell\) is:

\[
\boxed{
\text{the interior screw-field carrier of support loss}.
}
\]

---

# X. No direct factorization through the ejection screw field

## 15. Kernel blindness of the screw equation

The old-interior screw equation annihilates every vector in

\[
K=P\oplus E\oplus H^{\rm nf}.
\]

In particular it cannot distinguish the two ejection blocks

\[
p_\ell,
\qquad
h_\ell.
\]

The moment map does distinguish them.

Therefore no identity of the form

\[
\boxed{
\mathfrak R_\ell
=
\mathcal L_\ell
\left(
\text{old-interior screw field of }q_\ell
\right)
}
\]

can follow from the screw field alone without separately recovering the
kernel-ejection coordinates.

The exact ejection-edge identity controls only \(n_\ell\).

---

# XI. Why invertibility of \(G_c\) on \(K^\perp\) is not enough

## 16. No global spectral gap

The regular screw operator is compact with finite-dimensional kernel.

On

\[
K^\perp,
\]

it is injective, but a compact infinite-dimensional operator does not have a
bounded inverse on its range in general; its nonzero eigenvalues may
accumulate at zero.

Therefore smallness of the interior screw field of \(n_\ell\) would not, by
itself, imply comparable smallness of

\[
\|n_\ell\|_2
\]

or of its moment vector.

For each fixed finite-dimensional ejection image one may obtain a positive
singular-value constant, but no uniform lower bound as

\[
\ell\downarrow0
\]

has been established.

Thus even the nonkernel block still requires a quantitative small-strip
coercivity estimate to transfer field flatness into source/moment flatness.

---

# XII. Small-\(\ell\) qualitative behavior

## 17. All ejection blocks vanish in norm, with no known rate

Since the translation semigroup is strongly continuous on \(L^2\),

\[
S_\ell f\to f
\qquad
(\ell\downarrow0).
\]

Because \(E_+\) is finite dimensional, this convergence is uniform on its unit
sphere.

Since

\[
f\in E_+,
\]

we obtain uniformly on \(E_+\):

\[
\boxed{
\|p_\ell\|
+
\|h_\ell\|
+
\|n_\ell\|
\to0.
}
\]

However, current regularity gives no algebraic rate.

In particular, these norms are not known to be

\[
o(\ell^N)
\]

for any prescribed \(N\).

So qualitative translation continuity does not conflict with the linear
moment-defect floor of GERM-12.

---

# XIII. Result of this NF pass

The ejection-edge interface is now exact.

For a translated superflat obstruction,

\[
\boxed{
Q S_\ell f
=
p_\ell+h_\ell+n_\ell
}
\]

with:

\[
p_\ell\in P_c^+,
\]

\[
h_\ell\in K_c\cap F_\infty^\perp,
\]

\[
n_\ell\in K_c^\perp.
\]

The nonkernel block satisfies

\[
\boxed{
F_{n_\ell}(x_1)-F_{n_\ell}(x_2)
=
-
\left(
B_{\ell,+}u(x_1)-B_{\ell,+}u(x_2)
\right)
}
\]

on the core zone, and the entry-zone correction differs from the same
boundary-strip field only by the already-superflat old exterior residual.

Meanwhile the moment mismatch is

\[
\boxed{
\mathfrak R_\ell
=
-D_\ell^+\mathcal J_\ell
-
\mathcal M p_\ell
-
\mathcal M h_\ell
-
\mathcal M n_\ell.
}
\]

Therefore the linear mismatch floor from GERM-12 has three independent escape
routes not controlled by collar superflatness:

1. endpoint-prefix moments;
2. moment-visible kernel ejection;
3. source moments of the nonkernel ejection.

The direct ejection-edge identity controls the screw field of route 3, but not
its source norm or moment vector.

So the hoped-for one-step superflat-to-defect factorization does not close.

---

# XIV. Next traversal target

The next genuinely new target is

\[
\boxed{
\text{SZ-KERNEL-EDGE-GERM-14 / BOUNDARY-PREFIX COERCIVITY}.
}
\]

The next pass should test whether the special finite-dimensional family of
boundary strips generated by \(E\) admits a quantitative estimate relating:

\[
\mathcal J_\ell f,
\qquad
\mathcal M n_\ell,
\qquad
\mathcal M h_\ell,
\]

to the smaller-strip screw field

\[
B_{\ell,+}u.
\]

A useful theorem would need a rate as

\[
\ell\downarrow0,
\]

not merely fixed-\(\ell\) injectivity.

Candidate forms are:

\[
\|\mathcal J_\ell f\|
\lesssim
\ell^{-\alpha}
\|\operatorname{osc}B_{\ell,+}u\|,
\]

or a finite-dimensional singular-value lower bound on the boundary-strip
potential map with controlled \(\ell\)-dependence.

Without such a rate, support ejection remains an independent carrier of the
linear mismatch.

No boundary-prefix coercivity estimate is proved in this pass.

---

# XV. Cursor status

The canonical theorem cursor remains

\[
\boxed{\text{SZ-CROSS-COLLAR-3}}.
\]

This is an unratified ejection-identity / transfer-no-go residue.

No public promotion and no canonical cursor movement are asserted.
