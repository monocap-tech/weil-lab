# RPB-36 — Finite-delay unique continuation for a core-neutral Weil mode

**Date:** 2026-09-28  
**Branch:** \`research/reflected-packet-bridge\`  
**Status:** **NO BLACK-BOX UCP TRANSFER / FINITE DELAYS DESTROY THE LOG-LAPLACIAN CAUCHY TRIGGER / ARITHMETIC DELAY-ORBIT STRUCTURE IS NOW THE MISSING INPUT**  
**Dependencies:** RPB-33 through RPB-35; compact-window explicit operator; Chen--Hauer--Weth weak UCP for the whole-space logarithmic Laplacian.  
**Promotion status:** none.

## 0. Objective

RPB-35 identified screw-potential collar persistence with the core-regular
compact-window Weil null-extension problem.

For a nonzero screw-visible neutral mode

\`\`\`math
h\in H_0^1(-c,c),
\qquad
\operatorname{supp}h\subseteq[-c,c],
\`\`\`

suppose its zero extension satisfies

\`\`\`math
\mathcal W^{\rm ext}h=0
\`\`\`

on a strict enlargement \((-a,a)\), \(a>c\).

Then on each exterior collar

\`\`\`math
I_+=(c,a),
\qquad
I_-=(-a,-c),
\`\`\`

we have

\`\`\`math
h=0,
\qquad
\mathcal W^{\rm ext}h=0.
\`\`\`

RPB-36 asks whether known weak unique continuation for the logarithmic
Laplacian can be transferred to this finite-delay Weil equation.

It cannot be transferred as a black box.

The obstruction is exact: local vanishing of \(h\) does not kill the inward
prime translations, so the second logarithmic Cauchy datum is absent.

---

## 1. The logarithmic-Laplacian UCP trigger

Chen, Hauer, and Weth prove a weak unique-continuation theorem for the
whole-space logarithmic Laplacian \(L_\Delta\).

In the form consumed here, their theorem says that if

\`\`\`math
u\in L_0^1(\mathbb R^N)
\`\`\`

and, on a nonempty open set \(D\),

\`\`\`math
u=0,
\qquad
L_\Delta u=0,
\`\`\`

then

\`\`\`math
u\equiv0.
\`\`\`

Their extension construction represents \(L_\Delta\) as boundary data of a
local weighted extension and uses the simultaneous vanishing to obtain the
Cauchy-type zero data needed for harmonic unique continuation after the
doubling argument.

### External source

Huyuan Chen, Daniel Hauer, Tobias Weth,
*An extension problem for the logarithmic Laplacian*,
arXiv:2312.15689, Theorem 5.1.

The same theorem is quoted as the UCP input in later work on the logarithmic
Schrödinger Calderón problem.

---

## 2. The core mode lies in the logarithmic UCP regularity regime

The RPB-33 screw-visible mode satisfies

\`\`\`math
h\in H_0^1(-c,c).
\`\`\`

Therefore its zero extension is compactly supported and belongs to

\`\`\`math
H^1(\mathbb R)
\cap
L_0^1(\mathbb R).
\`\`\`

Moreover

\`\`\`math
\log^2|\xi|
\lesssim
1+|\xi|^2
\`\`\`

away from the integrable low-frequency logarithmic singularity, so

\`\`\`math
L_\Delta h\in L^2(\mathbb R).
\`\`\`

Thus lack of basic regularity is no longer what prevents application of the
logarithmic UCP.

The missing item is the local equation

\`\`\`math
L_\Delta h=0
\`\`\`

on the collar.

---

## 3. Fixed-support decomposition of the archimedean operator

The exact archimedean multiplier is

\`\`\`math
m_\infty(\xi)
=
\Re\psi\!\left(
\frac14+\frac{i\xi}{2}
\right)
-
\log\pi.
\`\`\`

At high frequency,

\`\`\`math
m_\infty(\xi)
=
\log|\xi|
-
\log(2\pi)
+
O(|\xi|^{-2}).
\`\`\`

Near \(\xi=0\), \(m_\infty\) is regular whereas \(\log|\xi|\) has only an
integrable logarithmic singularity.

On the fixed support class

\`\`\`math
\operatorname{supp}h\subseteq[-c,c],
\`\`\`

the Fourier bound

\`\`\`math
|\widehat h(\xi)|
\le
\sqrt{2c}\,\|h\|_2
\`\`\`

controls the low-frequency logarithmic difference.

Consequently, on this fixed compact-support carrier, one may write

\`\`\`math
\boxed{
\mathcal A_\infty h
=
\frac12L_\Delta h
+
\mathcal B_{\infty,c}h,
}
\`\`\`

where

\`\`\`math
\mathcal B_{\infty,c}
:
L^2(-c,c)
\to
L^2_{\rm loc}(\mathbb R)
\`\`\`

is bounded on the fixed-support class.

No claim is made that the multiplier difference is globally \(L^\infty\) on
unrestricted whole-line \(L^2\).

---

## 4. Exact collar equation

Let

\`\`\`math
\mathcal D_{c+}
=
\left\{
\ell=\log n:
n=p^m,
\quad
\ell\le2c
\right\}
\`\`\`

with the equality case included according to the strict-right threshold
convention.

Shrink the collar width

\`\`\`math
\varepsilon=a-c
\`\`\`

so that

\`\`\`math
0<\varepsilon<\log2
\`\`\`

and no additional prime-power threshold occurs inside the collar.

For

\`\`\`math
x\in I_+=(c,c+\varepsilon),
\`\`\`

we have

\`\`\`math
h(x)=0,
\qquad
h(x+\ell)=0
\quad
(\ell>0).
\`\`\`

But

\`\`\`math
h(x-\ell)
\`\`\`

may lie inside \((-c,c)\).

Therefore the right-collar null equation is

\`\`\`math
\boxed{
\frac12L_\Delta h(x)
=
\sum_{\ell\in\mathcal D_{c+}}
a_\ell h(x-\ell)
-
\mathcal B_{\infty,c}h(x)
-
\mathcal R_{\rm pole}h(x),
}
\`\`\`

with

\`\`\`math
a_{\log n}
=
\frac{\Lambda(n)}{\sqrt n}.
\`\`\`

The left collar has the reflected equation with the inward samples
\(h(x+\ell)\).

Thus

\`\`\`math
\boxed{
h=0
\text{ on the collar}
\not\Rightarrow
L_\Delta h=0
\text{ there}.
}
\`\`\`

This is the finite-delay Cauchy-data defect.

---

## 5. Why local zeroth-order perturbations would be different

Suppose instead one had an equation

\`\`\`math
L_\Delta h
+
V(x)h
=
0
\`\`\`

with a local multiplication potential \(V\).

On any open set where

\`\`\`math
h=0,
\`\`\`

one automatically has

\`\`\`math
Vh=0,
\`\`\`

hence

\`\`\`math
L_\Delta h=0.
\`\`\`

The Chen--Hauer--Weth UCP trigger is then recovered.

Finite translations behave differently:

\`\`\`math
h(x)=0
\`\`\`

does not imply

\`\`\`math
h(x-\ell)=0.
\`\`\`

Therefore the prime terms are not ordinary lower-order potentials from the
point of view of unique continuation.

Their order is low in Fourier regularity, but their **support action is
nonlocal**.

---

## 6. Finite rank is also not harmless for black-box UCP

Weak UCP for a self-adjoint operator is not stable under an arbitrary bounded
finite-rank perturbation.

Let \(A\) be self-adjoint, and choose

\`\`\`math
0\ne h\in\mathfrak D(A)
\`\`\`

that vanishes on a prescribed nonempty open set.

Set

\`\`\`math
e
=
\frac{h}{\|h\|},
\qquad
r
=
-\frac{Ah}{\|h\|}.
\`\`\`

Using the rank-one convention

\`\`\`math
(x\otimes y)z
=
\langle z,y\rangle x,
\`\`\`

define

\`\`\`math
\boxed{
R
=
r\otimes e
+
e\otimes r
-
\langle r,e\rangle
e\otimes e.
}
\`\`\`

Because \(A\) is self-adjoint,

\`\`\`math
\langle r,e\rangle
\in\mathbb R,
\`\`\`

so \(R\) is bounded, finite rank, and self-adjoint.

Moreover

\`\`\`math
Re=r,
\`\`\`

hence

\`\`\`math
\boxed{
(A+R)h=0.
}
\`\`\`

Thus a nonzero function may vanish on an open set and solve a globally
homogeneous equation after a bounded self-adjoint finite-rank perturbation.

This example is not the actual Weil pole term.

Its role is a sharp scope statement:

\`\`\`math
\boxed{
\text{UCP for the actual Weil operator cannot follow merely from}
\;
\text{"logarithmic principal part + bounded/finite-rank perturbation."}
}
\`\`\`

The specific structure of the arithmetic perturbation must be used.

---

## 7. Two exterior collars do not double the information after parity reduction

The compact-window Weil operator commutes with reflection.

Therefore any persistent neutral mode decomposes as

\`\`\`math
h=h_++h_-,
\`\`\`

where

\`\`\`math
h_+(x)=h_+(-x),
\qquad
h_-(x)=-h_-(-x),
\`\`\`

and each nonzero parity component separately satisfies the same null-extension
equation.

Hence one may reduce to a definite parity mode.

For such a mode, the left-collar equation is the reflected copy of the
right-collar equation.

Thus simultaneous left and right collar vanishing does not provide two
independent scalar Cauchy constraints.

It supplies one arithmetic delay relation together with its parity image.

---

## 8. The one-delay regime still does not trigger logarithmic UCP

Suppose, exceptionally, that the strict-right active set contains a single
delay

\`\`\`math
\mathcal D_{c+}
=
\{\ell\}.
\`\`\`

Then on the right collar

\`\`\`math
a_\ell h(x-\ell)
=
\frac12L_\Delta h(x)
+
\mathcal B_{\infty,c}h(x)
+
\mathcal R_{\rm pole}h(x).
\`\`\`

This determines one translated interior germ from the exterior nonlocal field.

But it does not imply

\`\`\`math
h(x-\ell)=0
\`\`\`

or

\`\`\`math
L_\Delta h(x)=0.
\`\`\`

Therefore even a single active prime delay does not by itself recover the
Chen--Hauer--Weth hypothesis.

The obstruction is qualitative, not merely caused by having too many delays.

---

## 9. Multiple delays give an underdetermined germ relation

When

\`\`\`math
\mathcal D_{c+}
=
\{\ell_1,\dots,\ell_N\},
\qquad
N\ge2,
\`\`\`

choose the collar small enough that the translated intervals

\`\`\`math
(c-\ell_j,c-\ell_j+\varepsilon)
\`\`\`

are pairwise disjoint.

Then the right-collar equation is one functional relation

\`\`\`math
\boxed{
\sum_{j=1}^{N}
a_j
h(c-\ell_j+s)
=
\mathcal E_+(s),
\qquad
0<s<\varepsilon,
}
\`\`\`

where \(\mathcal E_+\) is the exterior archimedean/pole field.

This is one relation among \(N\) distinct interior germs.

Support ordering alone is therefore not triangular.

The left collar gives the reflected relation after parity reduction.

No direct elimination of all interior germs follows.

---

## 10. Why the extension proof cannot simply be coupled to the delays

The Chen--Hauer--Weth extension converts the logarithmic Laplacian into a local
weighted equation in one higher dimension.

For pure logarithmic UCP, simultaneous vanishing of

\`\`\`math
h
\quad\text{and}\quad
L_\Delta h
\`\`\`

on an open boundary piece supplies the zero boundary data needed for the
doubled harmonic unique-continuation argument.

For the Weil equation, the same boundary piece has

\`\`\`math
h=0,
\`\`\`

but

\`\`\`math
L_\Delta h
=
\text{inward delayed source}
+
\text{global remainder}.
\`\`\`

Thus the extension has nonzero inhomogeneous boundary data on precisely the
collar where the trace vanishes.

Introducing extensions of the translated functions does not automatically
make these data vanish: the translated traces live on interior pieces of the
old support.

The original Cauchy-zero mechanism is therefore absent.

---

## 11. Applying the Dirichlet operator does not close the gap at current regularity

The project already uses

\`\`\`math
L
=
-\partial_x^2
+
\frac14
\`\`\`

to remove the homogeneous \(e^{\pm x/2}\) directions in finite Problem-1
relations.

In a pole realization whose range is spanned by those homogeneous modes,
applying \(L\) also removes that finite-rank contribution.

Because \(L\) commutes with translations and Fourier multipliers, this would
leave a pole-free finite-delay equation.

However the transformed unknown is

\`\`\`math
q=Lh.
\`\`\`

From the currently proved core regularity

\`\`\`math
h\in H_0^1,
\`\`\`

one only obtains

\`\`\`math
q\in H^{-1}
\`\`\`

in general.

Thus this maneuver trades the finite-rank term for a loss of regularity and
does not place the transformed source into the currently pinned logarithmic
UCP class.

No closure is obtained.

---

## 12. Literature audit

The current logarithmic-Laplacian literature supplies:

1. the whole-space extension formulation;
2. weak UCP for the pure logarithmic Laplacian;
3. logarithmic Schrödinger applications with local multiplication potentials;
4. boundary regularity and spectral theory.

The RPB-36 search found no theorem covering

\`\`\`math
L_\Delta
+
\sum_{j=1}^{N}
a_j\tau_{\ell_j}
+
\text{global finite-rank term}
\`\`\`

with unique continuation from a collar on which the unknown itself vanishes.

Therefore no external finite-delay UCP theorem is imported.

---

## 13. Exact surviving arithmetic problem

The missing information is now more specific than generic UCP.

For the actual strict-right delay set

\`\`\`math
\mathcal D_{c+}
=
\{\log n:n=p^m,\ \log n\le2c\},
\`\`\`

one must exploit simultaneously:

- the exact arithmetic coefficients
  \`\`\`math
  \Lambda(n)/\sqrt n;
  \`\`\`
- the additive relations among prime-power logarithms;
- the interior equation on all of \((-c,c)\);
- the right exterior delay relation;
- its parity-reflected left counterpart;
- compact support;
- screw-kernel/core-neutral origin.

This is the **two-sided arithmetic delay-orbit problem**.

It is not supplied by the general logarithmic UCP theorem.

---

## 14. RPB-36 determination

\`\`\`math
\boxed{
\textbf{RPB-36 — STANDARD LOGARITHMIC UCP DOES NOT EXTEND TO THE WEIL COLLAR BY A LOWER-ORDER PERTURBATION ARGUMENT.}
}
\`\`\`

The decisive obstruction is

\`\`\`math
\boxed{
h=0
\text{ on }I
\quad\text{but}\quad
L_\Delta h
=
\text{nonzero inward-delay/global data on }I.
}
\`\`\`

Finite translations are lower order in regularity but nonlocal in support, so
they destroy the Cauchy-zero trigger used by the known weak UCP.

Arbitrary bounded finite-rank perturbations are likewise not UCP-safe in
general, as shown by the explicit rank-two construction above.

Thus any closure theorem for the actual Weil neutral mode must consume the
special arithmetic delay structure rather than only perturbation size/order.

Next cursor:

\`\`\`text
RPB-37 / TWO-SIDED ARITHMETIC DELAY-ORBIT CLOSURE
\`\`\`

The next pass should build the orbit generated by the active delays
\(\log p^m\) on the compact support interval, use parity to quotient the
left/right duplication, and determine whether repeated use of the interior and
collar equations yields a finite triangular subsystem, a dense arithmetic
orbit, or another explicit nonclosure mechanism.
