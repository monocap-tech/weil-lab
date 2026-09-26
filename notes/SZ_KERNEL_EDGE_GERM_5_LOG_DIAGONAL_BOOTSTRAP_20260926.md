# SZ-KERNEL-EDGE-GERM-5 — Log-diagonal bootstrap ceiling and quasi-analyticity gate

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Immediate residue:** SZ-KERNEL-EDGE-GERM-4  
**Target tested:** LOG-DIAGONAL BOOTSTRAP  
**Public promotion:** forbidden

## 0. Objective

GERM-4 showed that movable-center arithmetic elimination is triangular in
prime-delay length, but every recentering imports the archimedean diagonal
singularity.

The surviving core is therefore the logarithmic principal species.

This pass asks whether stronger regularity for that principal operator could
close the edge problem.

The conclusion is sharply negative at the level of ordinary regularity
scales:

\[
\boxed{
\text{even all logarithmic orders, all finite Sobolev orders, or }C^\infty
\text{ regularity do not exclude infinite-order edge flatness.}
}
\]

The missing property is not “more smoothness.”

It is **quasi-analyticity** or an equivalent finite-order rigidity statement.

This pass also isolates one source gate that would be needed before even an
all-log bootstrap could be used canonically: the localized differentiated
Weil equation must be normalized as a logarithmic principal operator plus
lower channels that preserve every logarithmic domain.

---

# I. Principal logarithmic species

## 1. Local diagonal singularity

Suzuki's local expansion near the origin has the form

\[
g(t)
=
\frac12|t|\log|t|
+
\text{less singular terms}.
\]

After two distributional derivatives, the principal local kernel is of
finite-part type

\[
\operatorname{Pf}\frac1{|t|},
\]

up to local normalization terms.

Thus the interior differentiated equation has logarithmic pseudodifferential
principal behavior.

---

## 2. Whole-line logarithmic scale

For the whole-line logarithmic Laplacian, the Fourier symbol is

\[
2\log|\xi|
\]

up to the standard normalization at low frequency.

More generally, the \(m\)-order logarithmic Laplacian has symbol

\[
\boxed{
(2\log|\xi|)^m.
}
\]

External source pin:

- Huyuan Chen, *On m-order logarithmic Laplacians and related properties*,
  arXiv:2307.06198;
- Huyuan Chen, Daniel Hauer, Tobias Weth,
  *An extension problem for the logarithmic Laplacian*,
  arXiv:2312.15689.

For regularity bookkeeping it is convenient to use the positive weight

\[
\Lambda_{\log}(\xi)
=
1+\log(1+|\xi|).
\]

Define the logarithmic Sobolev scale

\[
\boxed{
H_{\log}^m
=
\left\{
u\in L^2:
\Lambda_{\log}^m\widehat u\in L^2
\right\}.
}
\]

---

# II. What is already canonical

## 3. Current ratified regularity

The canonical bridge supplies one logarithmic form-domain estimate of the form

\[
\int_{\mathbb R}
\log(e+|t|)
|\widehat f(t)|^2\,dt<\infty.
\]

This is sufficient for the closed zero-side form decomposition.

It is explicitly **not** a positive-Sobolev bootstrap.

Nor does the current canonical package assert

\[
u\in H_{\log}^m
\qquad
\forall m.
\]

Thus an iterated log bootstrap is not presently canonical.

---

# III. Conditional all-log bootstrap mechanism

## 4. What would be needed

A standard logarithmic elliptic iteration would require a localized operator
identity of the schematic form

\[
\boxed{
L_{\log}u
=
B_cu
+
r,
}
\]

where:

1. \(L_{\log}\) is the normalized logarithmic principal operator;
2. \(B_c\) consists of finite translations, zeroth-order local terms, and
   sufficiently regular archimedean remainders;
3. for every \(m\),
   \[
   B_c:H_{\log}^m\to H_{\log}^m;
   \]
4. cutoff commutators with \(L_{\log}\) gain enough ordinary order to remain
   harmless in every logarithmic scale.

If this package is source-pinned, then induction would give

\[
u\in H_{\log}^m_{\rm loc}
\qquad
\forall m.
\]

Finite translations themselves are harmless here because in Fourier space
they are unimodular multipliers and commute with every function of
\(|D|\).

The unclosed point is the exact localized normalization and commutator custody
for the full differentiated Weil equation.

Therefore:

\[
\boxed{
\text{ALL-LOG BOOTSTRAP IS PLAUSIBLE BUT NOT YET RATIFIED.}
}
\]

The rest of this pass shows that even proving it would not close the edge
problem.

---

# IV. All logarithmic orders do not imply any positive Sobolev order

## 5. Spectral counterexample

Consider the one-dimensional torus and Fourier coefficients

\[
|\widehat f(n)|^2
=
\frac1{
n\,\exp(\sqrt{\log n})
},
\qquad
n\ge3,
\]

with the negative-frequency coefficients chosen symmetrically.

Then

\[
\sum_{n\ge3}
|\widehat f(n)|^2
<\infty,
\]

because under

\[
t=\log n
\]

the integral test reduces to

\[
\int^\infty e^{-\sqrt t}\,dt<\infty.
\]

For every integer \(m\ge0\),

\[
\sum_{n\ge3}
(\log n)^{2m}
|\widehat f(n)|^2
<\infty,
\]

since

\[
\int^\infty
t^{2m}e^{-\sqrt t}\,dt
<\infty.
\]

Hence

\[
\boxed{
f\in\bigcap_{m\ge0}H_{\log}^m.
}
\]

But for every

\[
s>0,
\]

\[
\sum_{n\ge3}
n^{2s}
|\widehat f(n)|^2
=
\sum_{n\ge3}
n^{2s-1}
e^{-\sqrt{\log n}}
=
\infty.
\]

Thus

\[
\boxed{
f\notin H^s
\qquad
\forall s>0.
}
\]

Therefore

\[
\boxed{
\bigcap_{m\ge0}H_{\log}^m
\not\subset
\bigcup_{s>0}H^s.
}
\]

Arbitrarily many logarithmic derivatives do not manufacture one positive
power derivative.

---

# V. Even positive Sobolev bootstrap would not be enough

## 6. Smooth flat Volterra germ

The edge obstruction is stronger than lack of Sobolev regularity.

Let

\[
h(\delta)
=
\begin{cases}
e^{-1/\delta^2}, & \delta>0,\\
0, & \delta\le0.
\end{cases}
\]

Then

\[
h\in C^\infty(\mathbb R),
\]

and

\[
h^{(k)}(0)=0
\qquad
\forall k\ge0,
\]

while

\[
h(\delta)>0
\qquad
(\delta>0).
\]

Choose a smooth cutoff that equals \(1\) near \(0\) and remains inside a fixed
small collar; continue to denote the resulting flat function by \(h\).

Set

\[
f(t)=h''(t).
\]

Then

\[
f\in C_c^\infty
\]

locally in the one-sided collar, and because

\[
h(0)=h'(0)=0,
\]

we have

\[
\boxed{
h(\delta)
=
\int_0^\delta
(\delta-t)f(t)\,dt
}
\]

for sufficiently small \(\delta>0\).

This is exactly the second-order Volterra germ occurring at a prime hinge.

Therefore a prime-hinge leakage channel may be:

- nonzero;
- infinitely flat;
- generated by a \(C^\infty\) local source germ.

So even the hypothetical bootstrap

\[
u\in H^s
\qquad
\forall s
\]

would not by itself exclude flat leakage.

---

# VI. The actual regularity threshold is quasi-analytic

## 7. Smoothness versus quasi-analyticity

The implication needed by the edge program is

\[
\boxed{
\text{all edge jets vanish}
\Longrightarrow
\text{edge germ vanishes identically}.
}
\]

That implication fails in \(C^\infty\).

It also fails in every ordinary non-quasi-analytic Denjoy-Carleman class.

What is required is a quasi-analytic class, or a substitute such as:

- a finite-order lower bound;
- an analytic continuation principle;
- a moment uniqueness theorem;
- a nonvanishing finite Plücker coefficient;
- or a determinant estimate that forbids common flat divisors.

Thus the correct hierarchy is

\[
\boxed{
L^2
\;<\;
\text{all-log}
\;<\;
C^\infty
\;<\;
\text{quasi-analytic rigidity}
}
\]

for the purpose of this endpoint problem.

The inequalities here refer to logical strength for flatness exclusion, not
literal embeddings in every setting.

---

# VII. Finite-dimensionality does not repair the gap

## 8. One-dimensional counterspace

The obstruction remains even on a one-dimensional space.

Let

\[
V=\operatorname{span}\{f\},
\]

where \(f=h''\) is the smooth flat Volterra source above.

Then \(V\) is finite dimensional and every element is \(C^\infty\), yet its
Volterra observation is a scalar multiple of

\[
h(\delta)=e^{-1/\delta^2}
\]

near zero.

Hence

\[
\boxed{
\text{finite dimensionality}
+
C^\infty
\not\Rightarrow
\text{quasi-analyticity}.
}
\]

So the finite dimension of

\[
K_c
\]

or

\[
\mathcal E_c
\]

cannot by itself convert a regularity bootstrap into edge rigidity.

What matters is a **uniform quantitative derivative law** on that particular
finite-dimensional family.

---

# VIII. Quantitative growth is the missing datum

## 9. Why mere membership in every domain is insufficient

Suppose one proves

\[
u\in H_{\log}^m
\qquad
\forall m.
\]

This gives finite numbers

\[
M_m(u)
=
\|\Lambda_{\log}^m u\|_2,
\]

but no useful restriction on the growth of

\[
M_m(u)
\]

as \(m\to\infty\).

Quasi-analyticity requires quantitative control of the sequence of derivative
or moment norms, not merely finiteness term-by-term.

The torus counterexample above has every \(M_m<\infty\) while the sequence
grows too rapidly to imply any power regularity.

The smooth-flat Volterra example is stronger still: all ordinary derivatives
exist, but their growth permits a flat nonzero germ.

---

## 10. Exponential log-moment growth would be too strong globally

There is also a useful ceiling.

For a positive logarithmic multiplier \(A\), if a compactly supported
nonzero function satisfied

\[
\|A^m u\|
\le
CR^m
\qquad
\forall m,
\]

then the spectral measure of \(A\) would be supported in

\[
[0,R].
\]

For

\[
A\sim\log(1+|D|),
\]

this would force bounded Fourier support.

A nonzero function cannot be both compactly supported and band-limited.

Therefore a nonzero compactly supported kernel vector cannot satisfy such a
global exponential analytic-vector bound.

The useful quasi-analytic estimate, if it exists, must therefore be a **local
edge estimate**, not a global band-limit surrogate.

---

# IX. Result of this NF pass

The logarithmic diagonal is not closed by regularity iteration alone.

Even granting the strongest plausible qualitative bootstrap

\[
\boxed{
u\in H_{\log}^m_{\rm loc}
\qquad
\forall m,
}
\]

one still cannot infer:

\[
u\in H^\varepsilon,
\]

let alone endpoint quasi-analyticity.

More sharply,

\[
\boxed{
C^\infty
\text{ local source germs can generate nonzero infinitely-flat hinge leakage}.
}
\]

Therefore

\[
\boxed{
\text{LOG-DIAGONAL BOOTSTRAP}
\not\Rightarrow
\text{EDGE RIGIDITY}
}
\]

unless the bootstrap carries quantitative quasi-analytic growth information.

The current canonical logarithmic form-domain result is consequently below
the true rigidity threshold.

---

# X. Next traversal target

The next genuinely new target is

\[
\boxed{
\text{SZ-KERNEL-EDGE-GERM-6 / LOCAL QUASI-ANALYTIC MOMENT CONTROL}.
}
\]

The next pass should stop asking for generic regularity and instead seek a
quantitative finite-dimensional law on the actual kernel family.

Promising interfaces are:

1. use the explicit archimedean exponential moments from GERM-2 to derive
   growth bounds on the Schur-reduced family;
2. test whether the interior identity gives a recurrence among those moments;
3. search for a Carleman/Denjoy-Carleman sequence attached specifically to
   \(K_c\);
4. alternatively, derive a finite-order nonzero moment directly from the
   minimal-hinge / endpoint subsystem.

A successful result must distinguish the actual Weil kernel family from the
smooth flat Volterra counterspace.

No such quasi-analytic estimate is proved in this pass.

---

# XI. Cursor status

The canonical theorem cursor remains

\[
\boxed{\text{SZ-CROSS-COLLAR-3}}.
\]

This is an unratified regularity-ceiling/no-go residue.

No public promotion and no canonical cursor movement are asserted.
