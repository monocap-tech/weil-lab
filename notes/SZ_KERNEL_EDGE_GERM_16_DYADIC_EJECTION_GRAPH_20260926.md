# SZ-KERNEL-EDGE-GERM-16 — Dyadic visible-germ ejection graph

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Immediate residue:** SZ-KERNEL-EDGE-GERM-15  
**Target tested:** VISIBLE-GERM EJECTION GRAPH  
**Public promotion:** forbidden

## 0. Objective

GERM-15 isolated the terminal local-mass obstruction

\[
E_{\rm vis}^\infty
\subseteq
E_+
\]

consisting of edge-obstruction directions whose \(L^2\)-mass is superflat on:

- the physical endpoint-visible half-collar;
- every right-visible prime-hinge half-collar.

The remaining question was whether these jointly-superflat visible germs can
cycle indefinitely through the finite arithmetic delay graph without exposing
a finite-order carrier.

The first-prime chain gives an exact answer at the level of custody.

Let

\[
a=\log2.
\]

Because every power

\[
2^j
\]

is a prime power, the source points

\[
ja=\log(2^j)
\]

form a canonical arithmetic spine through the active hinge set until the
support length

\[
L=2c
\]

is exhausted.

On a nonzero jointly-superflat visible family, repeated \(a\)-translation
cannot remain inside the regular kernel forever.

More strongly, the family has a finite **dyadic escape filtration**, and every
nonzero filtration layer injects canonically into \(K_c^\perp\) at its first
escape step.

Thus the jointly-superflat obstruction admits a finite acyclic escape graph.

This does not yet prove that the obstruction is zero.

It identifies a finite nonkernel carrier for every surviving layer.

---

# I. Nontriviality forces the first-prime regime

## 1. Small-window exclusion

Let

\[
W
=
E_{\rm vis}^\infty.
\]

If

\[
W\ne0,
\]

then in particular

\[
K_c\ne0.
\]

GERM-8 uses the Bombieri--Yoshida small-window positivity input to give

\[
K_c=\{0\}
\qquad
\left(
2c\le\log2
\right).
\]

Therefore a nonzero \(W\) requires

\[
\boxed{
L=2c>a=\log2.
}
\]

So the first-prime truncated shift is genuinely active.

---

# II. The dyadic translation spine

## 2. Source-coordinate shift

Work in

\[
H=L^2(0,L)
\]

with right-oriented source coordinate

\[
f(s)=u(c-s).
\]

Let

\[
S=S_a
\]

be the truncated left shift by

\[
a=\log2:
\]

\[
(Sf)(s)
=
\begin{cases}
f(s+a), & 0<s<L-a,\\
0, & L-a<s<L.
\end{cases}
\]

Then

\[
S^j=S_{ja}.
\]

Let

\[
q
=
\min
\left\{
n\in\mathbb N:
na\ge L
\right\}.
\]

Then

\[
\boxed{
S^q=0.
}
\]

---

## 3. Dyadic hinges are visible sites

For every integer

\[
1\le j<q,
\]

we have

\[
ja<L.
\]

Since

\[
ja=\log(2^j)
\]

and \(2^j\) is a prime power, \(ja\) is an active right-oriented prime hinge.

Therefore, for

\[
f\in W=E_{\rm vis}^\infty,
\]

\[
\boxed{
\|f\|_{L^2(ja,ja+\varepsilon)}
=
o(\varepsilon^N)
\qquad
\forall N.
}
\]

Equivalently,

\[
\boxed{
S^jf
\text{ has endpoint-prefix mass }
o(\varepsilon^N)
\text{ for every }N.
}
\]

Thus every dyadic relocation of \(W\) is endpoint-superflat as long as the
corresponding hinge lies inside the support.

---

# III. Injectivity of the first-prime shift on the kernel

## 4. GERM-8 input

GERM-8 proved

\[
\boxed{
K_c\cap\ker S=\{0\}.
}
\]

Equivalently,

\[
\boxed{
S|_{K_c}
\text{ is injective}.
}
\]

This is the exact small-support consequence needed below.

It is stronger than mere non-invariance.

---

# IV. Dyadic escape filtration

## 5. Definition

Define

\[
\boxed{
C_j
=
\left\{
f\in W:
S^kf\in K_c
\text{ for }0\le k\le j
\right\},
}
\]

for

\[
0\le j\le q-1.
\]

Then

\[
\boxed{
W=C_0\supseteq C_1\supseteq\cdots\supseteq C_{q-1}.
}
\]

This is the dyadic escape filtration registered in the terminology registry.

---

# V. The filtration terminates at zero

## 6. Terminal step

Take

\[
f\in C_{q-1}.
\]

Then

\[
S^{q-1}f\in K_c.
\]

But

\[
S^qf=0.
\]

Hence

\[
S(S^{q-1}f)=0.
\]

Injectivity of \(S|_{K_c}\) gives

\[
S^{q-1}f=0.
\]

Now

\[
S^{q-2}f\in K_c
\]

and

\[
S(S^{q-2}f)=0,
\]

so again injectivity gives

\[
S^{q-2}f=0.
\]

Iterating backward yields

\[
f=0.
\]

Therefore

\[
\boxed{
C_{q-1}=\{0\}.
}
\]

So every nonzero jointly-superflat visible vector leaves the regular kernel
after finitely many dyadic relocations.

---

# VI. First-escape operator

## 7. Nonkernel projection

Let

\[
\Pi_K
\]

be the orthogonal projection in \(H\) onto the right-oriented regular kernel

\[
K_+=U_+K_c.
\]

For

\[
0\le j\le q-2,
\]

define

\[
\boxed{
\mathcal N_j:
C_j\to K_+^\perp,
\qquad
\mathcal N_j f
=
(I-\Pi_K)S^{j+1}f.
}
\]

---

## 8. Exact kernel

For

\[
f\in C_j,
\]

all iterates through

\[
S^jf
\]

already lie in \(K_+\).

Therefore

\[
\mathcal N_jf=0
\]

if and only if

\[
S^{j+1}f\in K_+.
\]

But that is exactly the extra condition defining

\[
C_{j+1}.
\]

Hence

\[
\boxed{
\ker\mathcal N_j=C_{j+1}.
}
\]

Therefore \(\mathcal N_j\) descends to an injective map

\[
\boxed{
\overline{\mathcal N}_j:
C_j/C_{j+1}
\hookrightarrow
K_+^\perp.
}
\]

Every nonzero escape layer is faithfully represented by a nonkernel
translation component.

---

# VII. Orthogonal escape layers

## 9. Canonical Hilbert realization

Define

\[
\boxed{
L_j
=
C_j\cap C_{j+1}^\perp
}
\]

inside \(W\).

Since

\[
C_{q-1}=0,
\]

the nested orthogonal decomposition gives

\[
\boxed{
W
=
\bigoplus_{j=0}^{q-2}
L_j.
}
\]

Some \(L_j\) may be zero.

For nonzero \(L_j\),

\[
\mathcal N_j|_{L_j}
\]

is injective.

Hence finite dimensionality gives

\[
\boxed{
\|\mathcal N_jf\|
\ge
\nu_j\|f\|
\qquad
(f\in L_j)
}
\]

for some fixed

\[
\nu_j>0.
\]

Thus each nonzero layer has fixed-scale quantitative nonkernel escape.

---

# VIII. Dyadic escape depth

## 10. Interpretation

A nonzero vector in

\[
L_j
\]

has the following exact custody history:

\[
f\in K_c,
\]

\[
Sf\in K_c,
\]

\[
\cdots,
\]

\[
S^jf\in K_c,
\]

but

\[
\boxed{
S^{j+1}f\notin K_c.
}
\]

The integer

\[
\boxed{
j+1
}
\]

is its dyadic escape depth.

Because the original family is jointly visible-superflat, every surviving
kernel iterate

\[
S^kf,
\qquad
0\le k\le j,
\]

has superflat endpoint-prefix mass.

So a vector may remain endpoint-superflat through several arithmetic
relocations, but it must eventually leave the regular kernel.

---

# IX. The escape is a boundary-strip screw field

## 11. Apply GERM-13 at the escape step

Take

\[
f\in L_j
\]

and set

\[
g=S^jf.
\]

Then

\[
g\in K_+.
\]

Its next shift is

\[
Sg=S^{j+1}f.
\]

The nonkernel component is exactly

\[
\mathcal N_jf.
\]

Return to physical coordinates and write the corresponding kernel vector as
\(u_j\).

GERM-13 gives, on the first-prime core zone,

\[
\boxed{
F_{\mathcal N_jf}(x_1)
-
F_{\mathcal N_jf}(x_2)
=
-
\left[
B_{a,+}u_j(x_1)
-
B_{a,+}u_j(x_2)
\right].
}
\]

Thus the first nonkernel escape is precisely the carrier of the screw field
generated by the dyadic source cell discarded at that step.

---

# X. Dyadic cell interpretation

## 12. Which original source cell escapes?

For

\[
g=S^jf,
\]

its discarded endpoint strip under the next \(a\)-shift is

\[
g|_{(0,a)}.
\]

In terms of the original source \(f\), this is

\[
\boxed{
f|_{(ja,(j+1)a)}.
}
\]

So the escape layer at depth \(j+1\) is detected by the screw field of the
original dyadic cell

\[
\boxed{
(ja,(j+1)a).
}
\]

This is a fixed-width cell, not merely an infinitesimal endpoint germ.

The visible-superflat condition controls only the germ at its left endpoint

\[
ja.
\]

It does not make the full cell small.

That is why the escape theorem does not yet contradict collar superflatness.

---

# XI. Dimension-growth bound before full-subspace escape

## 13. Translate the whole family

Set

\[
W_j=S^jW.
\]

Suppose

\[
W_0,\ldots,W_r
\subseteq K_+.
\]

Define

\[
V_j
=
\operatorname{span}
(W_0,\ldots,W_j)
\subseteq K_+.
\]

If for some \(j<r\),

\[
W_{j+1}\subseteq V_j,
\]

then

\[
SV_j
=
\operatorname{span}
(W_1,\ldots,W_{j+1})
\subseteq V_j.
\]

Thus \(V_j\) would be a nonzero \(S\)-invariant subspace of \(K_+\).

GERM-8 forbids this.

Therefore

\[
\boxed{
W_{j+1}\not\subseteq V_j.
}
\]

Hence

\[
\boxed{
\dim V_{j+1}\ge\dim V_j+1.
}
\]

---

## 14. Escape-depth bound for the full family

Let

\[
k=\dim K_c,
\qquad
d_W=\dim W.
\]

Starting from

\[
\dim V_0=d_W,
\]

the previous section gives

\[
\dim V_r\ge d_W+r
\]

as long as all \(W_0,\ldots,W_r\) remain in \(K_+\).

Since

\[
\dim V_r\le k,
\]

we obtain:

\[
\boxed{
W_r\not\subseteq K_+
\text{ for some }
r\le k-d_W+1.
}
\]

So the entire jointly-superflat family must develop a nonkernel component
within finitely many dyadic relocations bounded by the regular-kernel
dimension.

---

# XII. Acyclicity

## 15. No kernel cycle

The dyadic escape graph has no nonzero cycle contained entirely in \(K_+\).

Indeed, any finite return relation placing a later translate inside the span
of earlier kernel-contained translates would create a nonzero
\(S\)-invariant finite-dimensional subspace of \(K_+\).

GERM-8 excludes this.

Therefore:

\[
\boxed{
\text{the kernel-contained dyadic graph is acyclic.}
}
\]

Every nonzero path either:

1. creates a new independent kernel direction; or
2. exits into \(K_+^\perp\).

Finite kernel dimension forces the second alternative after finitely many
steps.

---

# XIII. What this resolves

## 16. The jointly-superflat visible family is not closed

GERM-15 left open the possibility that

\[
W=E_{\rm vis}^\infty
\]

might remain hidden at every visible singular germ.

The present pass shows that such a family cannot remain arithmetically closed
inside the regular kernel.

It admits the finite orthogonal decomposition

\[
\boxed{
W
=
\bigoplus_jL_j,
}
\]

and every nonzero layer has an injective fixed-scale detector

\[
\boxed{
\mathcal N_j:L_j\hookrightarrow K_c^\perp.
}
\]

So every jointly-superflat visible obstruction direction has a finite
nonkernel witness.

---

# XIV. What this does not resolve

## 17. Fixed-scale escape versus shrinking-collar flatness

The escape occurs at the fixed arithmetic step

\[
a=\log2.
\]

Its boundary source is the full dyadic cell

\[
(ja,(j+1)a).
\]

The original obstruction is defined by behavior as

\[
\varepsilon\downarrow0.
\]

No theorem currently transfers the nonzero fixed-scale escape field back into
a finite-order lower bound for the shrinking exterior collar of the original
vector.

Therefore the escape graph does not yet force

\[
W=0.
\]

---

# XV. Result of this NF pass

The visible-germ ejection graph closes structurally.

Assuming

\[
W=E_{\rm vis}^\infty\ne0,
\]

the first-prime shift

\[
S_{\log2}
\]

generates a finite dyadic escape filtration

\[
\boxed{
W=C_0\supseteq C_1\supseteq\cdots\supseteq C_{q-1}=0.
}
\]

Each layer satisfies

\[
\boxed{
C_j/C_{j+1}
\hookrightarrow
K_c^\perp
}
\]

through its first nonkernel translated component.

Equivalently,

\[
\boxed{
W
=
\bigoplus_jL_j
}
\]

with fixed constants

\[
\boxed{
\|\mathcal N_jf\|
\ge
\nu_j\|f\|
\qquad
(f\in L_j).
}
\]

Moreover, whole-family kernel containment can persist for at most

\[
\boxed{
\dim K_c-\dim W
}
\]

strict dyadic steps before a nonkernel component appears.

Thus no nonzero jointly-superflat visible family can form an arithmetic cycle
inside the regular kernel.

The remaining obstruction is the transfer from this fixed-scale nonkernel
escape back to the shrinking edge collar.

---

# XVI. Next traversal target

The next genuinely new target is

\[
\boxed{
\text{SZ-KERNEL-EDGE-GERM-17 / DYADIC ESCAPE FIELD TRANSFER}.
}
\]

The next pass should work layer by layer.

For

\[
f\in L_j,
\]

compare:

1. the nonzero escape source
   \[
   \mathcal N_jf\in K_c^\perp;
   \]
2. its exact dyadic-cell screw field from GERM-13;
3. the superflat endpoint germs of the surviving kernel iterates
   \[
   f,Sf,\ldots,S^jf;
   \]
4. the original centered edge observation.

The target is to determine whether a nonzero fixed-scale escape field can be
compatible with simultaneous all-orders flatness at every preceding dyadic
visible hinge.

A positive incompatibility theorem would eliminate

\[
E_{\rm vis}^\infty.
\]

No such transfer is proved in this pass.

---

# XVII. Cursor status

The canonical theorem cursor remains

\[
\boxed{\text{SZ-CROSS-COLLAR-3}}.
\]

This is an unratified dyadic ejection-graph result.

No public promotion and no canonical cursor movement are asserted.
