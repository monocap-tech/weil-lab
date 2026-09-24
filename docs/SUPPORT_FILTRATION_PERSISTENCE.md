# Support Filtration and Persistence Limits
## H1-P1.2 — Right limits, endpoint jumps, and representative blow-up

This pass abstracts the support/observation-filtration mechanism that remained after H1-P1.0 and H1-P1.1.

No theorem below uses zeta-specific arithmetic.

---

## 0. Coefficient-space filtration

Let

\[
K=K_+\oplus K_-
\]

be a Hilbert space with fundamental symmetry

\[
J=
\begin{pmatrix}
I&0\\
0&-I
\end{pmatrix}.
\]

Let

\[
\{\mathcal A_t\}_{t\ge c}
\]

be a family of closed subspaces of \(K\) satisfying

\[
\boxed{
c\le s<t
\Longrightarrow
\mathcal A_s\subseteq\mathcal A_t.
}
\]

Thus larger observation/support parameter gives a larger analysis space.

Define the right-limit space at \(c\) by

\[
\boxed{
\mathcal A_{c+}
:=
\bigcap_{t>c}\mathcal A_t.
}
\]

Since

\[
\mathcal A_c\subseteq\mathcal A_{c+},
\]

define the endpoint jump space

\[
\boxed{
\mathcal J_c
:=
\mathcal A_{c+}\ominus\mathcal A_c.
}
\]

A vector in

\[
\mathcal A_{c+}\setminus\mathcal A_c
\]

is called a **new right-persistent coefficient vector** at the endpoint.

---

## WD-C1 — Monotone projection limit

Let \(P_t\) be the orthogonal projection onto \(\mathcal A_t\).

As

\[
t\downarrow c,
\]

the projections converge strongly to the projection onto the right-limit space:

\[
\boxed{
P_t
\longrightarrow
P_{c+}
}
\]

in the strong operator topology.

### Proof

Choose any sequence

\[
t_n\downarrow c.
\]

Then

\[
\mathcal A_{t_{n+1}}\subseteq\mathcal A_{t_n},
\]

so the projections \(P_{t_n}\) form a decreasing sequence of orthogonal projections.

For every \(x\in K\),

\[
\|P_{t_n}x\|^2
=
\langle P_{t_n}x,x\rangle
\]

decreases and the standard monotone-projection argument gives a strong limit \(P\).

The range of \(P\) is exactly

\[
\bigcap_n\mathcal A_{t_n}.
\]

Because the filtration is monotone and \(t_n\downarrow c\),

\[
\bigcap_n\mathcal A_{t_n}
=
\bigcap_{t>c}\mathcal A_t
=
\mathcal A_{c+}.
\]

The limit is independent of the chosen sequence.

**Standing:** PROVED.

---

## WD-C2 — Right-limit gap duality

Define the gap spaces

\[
G_t:=\mathcal A_t^\perp.
\]

Then

\[
s<t
\Longrightarrow
G_s\supseteq G_t.
\]

Define

\[
\boxed{
G_{c+}
:=
\overline{\bigcup_{t>c}G_t}.
}
\]

Because the \(G_t\) are nested in the reverse direction,

\[
\boxed{
\mathcal A_{c+}
=
G_{c+}^\perp.
}
\]

### Proof

For any family of closed subspaces,

\[
\left(\bigcap_i M_i\right)^\perp
=
\overline{\operatorname{span}\bigcup_i M_i^\perp}.
\]

Here the \(G_t\) form a nested family, so the linear span of their union is just their union. Hence

\[
\mathcal A_{c+}^\perp
=
\overline{\bigcup_{t>c}G_t}
=
G_{c+}.
\]

**Standing:** PROVED.

### Interpretation

Right persistence is equivalently an orthogonality law against every limiting gap relation.

This is the abstract source of relations of the form

\[
\langle a,x\rangle+\langle u,w\rangle=0.
\]

---

## WD-C3 — Fixed finite negative-sector compactness

Assume now

\[
K=K_+\oplus M,
\qquad
\dim M<\infty.
\]

Let

\[
t_n\downarrow c
\]

and let

\[
y_n=(a_n,u_n)\in\mathcal A_{t_n}
\]

satisfy

\[
\|y_n\|=1.
\]

After passing to a subsequence,

\[
a_n\rightharpoonup a
\]

weakly in \(K_+\), while

\[
u_n\to u
\]

strongly in \(M\).

Then

\[
\boxed{
y:=(a,u)\in\mathcal A_{c+}.
}
\]

If additionally

\[
[y_n,y_n]_J\to q_*\le0,
\]

then

\[
\boxed{
y\ne0
}
\]

and

\[
\boxed{
[y,y]_J\le q_*.
}
\]

### Proof

For any fixed \(s>c\), eventually

\[
t_n<s.
\]

By monotonicity,

\[
\mathcal A_{t_n}\subseteq\mathcal A_s,
\]

so eventually \(y_n\in\mathcal A_s\).

Closed subspaces are weakly closed, hence the weak limit \(y\) belongs to every \(\mathcal A_s\), \(s>c\). Therefore

\[
y\in\mathcal A_{c+}.
\]

Since

\[
\|a_n\|^2+\|u_n\|^2=1
\]

and

\[
\|a_n\|^2-\|u_n\|^2\to q_*,
\]

we have

\[
\|u_n\|^2\to\frac{1-q_*}{2}.
\]

Because \(M\) is finite dimensional,

\[
\|u\|^2=\frac{1-q_*}{2}\ge\frac12,
\]

so \(y\ne0\).

Weak lower semicontinuity gives

\[
\|a\|^2
\le
\lim\|a_n\|^2.
\]

Thus

\[
[y,y]_J
=
\|a\|^2-\|u\|^2
\le
\lim
\left(
\|a_n\|^2-\|u_n\|^2
\right)
=
q_*.
\]

**Standing:** PROVED.

---

## WD-C4 — Critical-sequence dichotomy

Under the hypotheses of WD-C3, suppose

\[
[y_n,y_n]_J\to0.
\]

Then

\[
\|a_n\|^2\to\frac12,
\qquad
\|u_n\|^2\to\frac12.
\]

The right-limit vector \(y=(a,u)\) satisfies exactly one of the following:

### N — compact critical limit

If

\[
\|a\|^2=\frac12,
\]

then

\[
[y,y]_J=0
\]

and weak convergence plus convergence of norms implies

\[
a_n\to a
\]

strongly.

Hence

\[
y_n\to y
\]

strongly and \(y\) is an actual nonzero neutral vector in \(\mathcal A_{c+}\).

### L — positive-mass loss

If

\[
\|a\|^2<\frac12,
\]

then

\[
\boxed{
[y,y]_J<0.
}
\]

Thus loss of positive coefficient norm in the limit converts an approximately neutral sequence into a strictly negative right-persistent vector.

### Consequence

For a fixed finite negative sector,

\[
\boxed{
\text{approximate criticality}
\Longrightarrow
\text{actual nonpositive right-limit ray}.
}
\]

There is no third possibility in which all coefficient mass disappears.

**Standing:** PROVED.

---

## WD-C5 — Uniform negative margins produce persistent negative rays

Under the hypotheses of WD-C3, suppose there is

\[
\kappa>0
\]

such that

\[
[y_n,y_n]_J\le-\kappa
\]

for all \(n\).

Then after passage to a subsequence there exists

\[
0\ne y\in\mathcal A_{c+}
\]

such that

\[
\boxed{
[y,y]_J\le-\kappa.
}
\]

If the endpoint space \(\mathcal A_c\) is \(J\)-nonnegative, then automatically

\[
\boxed{
y\in\mathcal A_{c+}\setminus\mathcal A_c.
}
\]

Thus a uniformly negative right-approaching sequence in a fixed finite negative sector forces a genuine negative endpoint jump.

**Standing:** PROVED.

---

## WD-C6 — Endpoint jump controls new negative index

Assume

\[
\mathcal A_c
\]

is \(J\)-nonnegative.

Then every \(J\)-negative subspace

\[
L\subseteq\mathcal A_{c+}
\]

satisfies

\[
L\cap\mathcal A_c=\{0\}.
\]

Therefore the quotient map

\[
L\to
\mathcal A_{c+}/\mathcal A_c
\]

is injective, and hence

\[
\boxed{
\operatorname{ind}_-(\mathcal A_{c+},J)
\le
\dim(\mathcal A_{c+}/\mathcal A_c)
}
\]

whenever the quotient dimension is finite.

Equivalently, using the Hilbert-space jump representative,

\[
\boxed{
\operatorname{ind}_-(\mathcal A_{c+},J)
\le
\dim\mathcal J_c.
}
\]

### Interpretation

New right-limit negative index requires an endpoint discontinuity in the analysis space.

A one-dimensional endpoint jump can carry at most one new negative direction.

**Standing:** PROVED.

---

# Physical realization

The preceding results are purely coefficient-space statements.

Representative blow-up requires an additional physical realization.

Let \(\mathscr H\) be a Hilbert space with a monotone family of closed physical subspaces

\[
\mathscr H_s\subseteq\mathscr H_t
\qquad
(c\le s<t),
\]

and assume right continuity at the physical level:

\[
\boxed{
\mathscr H_c
=
\bigcap_{t>c}\mathscr H_t.
}
\]

Let

\[
T:\mathscr H\to K
\]

be bounded, and define

\[
\boxed{
\mathcal A_t
=
\overline{T(\mathscr H_t)}.
}
\]

---

## WD-C7 — Endpoint representative blow-up principle

Let

\[
y\in
\mathcal A_{c+}\setminus\mathcal A_c.
\]

Let

\[
t_n\downarrow c,
\qquad
\varepsilon_n\downarrow0,
\]

and choose any

\[
h_n\in\mathscr H_{t_n}
\]

such that

\[
\|Th_n-y\|\le\varepsilon_n.
\]

Then

\[
\boxed{
\|h_n\|\to\infty.
}
\]

### Proof

Suppose instead that a subsequence is bounded.

By weak compactness in Hilbert space,

\[
h_{n_k}\rightharpoonup h.
\]

For every fixed \(s>c\), eventually

\[
t_{n_k}<s,
\]

hence

\[
h_{n_k}\in\mathscr H_s.
\]

Because \(\mathscr H_s\) is weakly closed,

\[
h\in\mathscr H_s
\]

for every \(s>c\).

Thus

\[
h\in
\bigcap_{s>c}\mathscr H_s
=
\mathscr H_c.
\]

Boundedness of \(T\) gives

\[
Th_{n_k}\rightharpoonup Th.
\]

But

\[
Th_{n_k}\to y
\]

strongly, so

\[
Th=y.
\]

Hence

\[
y\in T(\mathscr H_c)\subseteq\mathcal A_c,
\]

contradiction.

**Standing:** PROVED.

### Interpretation

A genuinely new endpoint coefficient vector can persist arbitrarily close to the endpoint only by losing physical compactness.

---

## WD-C8 — Boundary amplification functional

For

\[
y\in\mathcal A_{c+},
\]

define

\[
\boxed{
\mathfrak B_y(t,\varepsilon)
:=
\inf
\left\{
\|h\|:
h\in\mathscr H_t,\ 
\|Th-y\|\le\varepsilon
\right\}.
}
\]

If

\[
y\in\mathcal A_{c+}\setminus\mathcal A_c,
\]

then

\[
\boxed{
\mathfrak B_y(t,\varepsilon)\to\infty
\quad
\text{as }
(t,\varepsilon)\to(c+,0).
}
\]

More explicitly: for every \(M>0\), there exist

\[
\delta>0,
\qquad
\eta>0
\]

such that

\[
c<t<c+\delta,
\qquad
0<\varepsilon<\eta
\]

imply

\[
\mathfrak B_y(t,\varepsilon)>M.
\]

### Proof

If not, one can choose

\[
t_n\downarrow c,
\qquad
\varepsilon_n\downarrow0
\]

and \(h_n\in\mathscr H_{t_n}\) with

\[
\|h_n\|\le M
\]

and

\[
\|Th_n-y\|\le\varepsilon_n,
\]

contradicting WD-C7.

**Standing:** PROVED.

### Scope warning

Blow-up is necessary for a new endpoint vector, but it is not sufficient to prove that the vector lies outside \(\mathcal A_c\): nonclosed-range phenomena can also produce large inverse cost inside an endpoint closure.

---

## WD-C9 — Vanishing coefficient amplitude and normalized blow-up

Suppose

\[
g_n\in\mathscr H_{t_n},
\qquad
\|g_n\|=1,
\]

and

\[
Tg_n=\varepsilon_n z_n,
\qquad
\varepsilon_n\downarrow0,
\qquad
z_n\to y\ne0.
\]

Define

\[
h_n:=\varepsilon_n^{-1}g_n.
\]

Then

\[
Th_n=z_n\to y
\]

while

\[
\boxed{
\|h_n\|
=
\varepsilon_n^{-1}
\to\infty.
}
\]

If \(y\in\mathcal A_{c+}\setminus\mathcal A_c\), this is exactly the endpoint blow-up morphology of WD-C7.

**Standing:** PROVED.

---

# Moving-sector escape

The finite-dimensional compactness in WD-C3 depends on using one fixed finite negative sector.

It fails if the selected negative coordinate itself moves through an infinite coefficient space.

---

## WD-E5 — Moving finite sectors can lose every persistent ray

Let

\[
K_+=\ell^2(\mathbb N),
\qquad
K_-=\ell^2(\mathbb N),
\]

with the standard \(J\)-form.

Let

\[
r_n>1,
\qquad
r_n\downarrow1,
\]

and define normalized vectors

\[
y_n
=
\frac{(e_n,r_ne_n)}
{\sqrt{1+r_n^2}}.
\]

Then

\[
[y_n,y_n]_J
=
\frac{1-r_n^2}{1+r_n^2}
<0
\]

and

\[
[y_n,y_n]_J\to0.
\]

Define the decreasing filtration

\[
\boxed{
\mathcal A_n
:=
\overline{\operatorname{span}}
\{y_k:k\ge n\}.
}
\]

Because the \(y_k\) are Hilbert-orthonormal,

\[
\boxed{
\bigcap_{n=1}^\infty\mathcal A_n
=
\{0\}.
}
\]

Thus every stage contains a finite one-dimensional negative direction with margin tending to zero, but no nonzero persistent right-limit vector survives.

The negative coordinate itself moves through the orthogonal directions \(e_n\).

**Standing:** PROVED EXAMPLE.

### Consequence

\[
\boxed{
\text{moving finite packets}
\text{ can realize approximate neutrality without persistence}.
}
\]

This is the principal abstract mechanism excluded by WD-C3 for a fixed finite negative sector.

---

## WD-E6 — Positive-mass escape strengthens a fixed-sector limit

Let

\[
K_+=\ell^2(\mathbb N),
\qquad
M=\mathbb C.
\]

Define

\[
y_n
=
\left(
\frac1{\sqrt2}e_n,
\frac1{\sqrt2}
\right).
\]

Then

\[
\|y_n\|=1
\]

and

\[
[y_n,y_n]_J=0.
\]

But

\[
y_n\rightharpoonup
\left(
0,\frac1{\sqrt2}
\right)
=:y,
\]

and

\[
\boxed{
[y,y]_J=-\frac12.
}
\]

If

\[
\mathcal A_n
=
\overline{\operatorname{span}}
\{y_k:k\ge n\},
\]

then \(y\in\mathcal A_n\) for every \(n\), since each \(\mathcal A_n\) is weakly closed and contains the tail of the sequence.

Hence

\[
y\in\bigcap_n\mathcal A_n.
\]

This explicitly realizes the positive-mass-loss branch of WD-C4.

**Standing:** PROVED EXAMPLE.

---

# H1-P1.2 determination

The remaining support-filtration mechanism is now abstractly classified.

## 1. Right persistence is an endpoint jump

\[
\mathcal A_{c+}
=
\bigcap_{t>c}\mathcal A_t
\]

and

\[
\mathcal J_c
=
\mathcal A_{c+}\ominus\mathcal A_c.
\]

New negative index cannot appear without a nontrivial endpoint jump when \(\mathcal A_c\) is nonnegative.

## 2. Fixed finite negative sectors force a nonpositive right-limit ray

For unit right-approaching vectors in a fixed finite negative sector,

\[
[y_n,y_n]_J\to q_*\le0
\]

forces a nonzero

\[
y\in\mathcal A_{c+}
\]

with

\[
[y,y]_J\le q_*.
\]

Approximate neutrality becomes either:

- an actual neutral right-limit vector; or
- a stricter negative persistent vector caused by positive-coordinate mass loss.

## 3. Moving sectors are the genuine escape

If the selected negative direction itself moves through an infinite coefficient field, the whole sequence may escape weakly and leave no persistent ray.

Thus the non-attained approximate-neutral morphology from H1-P1.0 is now localized to:

\[
\boxed{
\text{infinite-sector or moving-sector noncompactness}.
}
\]

## 4. New endpoint vectors require physical blow-up

Under a common bounded physical realization,

\[
y\in\mathcal A_{c+}\setminus\mathcal A_c
\]

forces every increasingly accurate inward/right-endpoint representation to have norm tending to infinity.

This is the abstract representative-blow-up theorem previously encountered in the Weil traversal.

---

# H1-P1 completion

The abstract defect calculus now contains:

1. synthesis/defect/index equivalence;
2. Douglas screening and graph normal form;
3. selected/background shared budget;
4. recursive background elimination;
5. finite-sector singular-value inertia;
6. complement shorting;
7. monotone support filtration;
8. right-limit gap duality;
9. persistent-ray compactness;
10. endpoint jump/index control;
11. representative blow-up;
12. moving-sector escape.

Therefore

\[
\boxed{
\textbf{H1-P1 — ABSTRACT DEFECT CALCULUS: COMPLETE.}
}
\]

## Next Horizon cursor

\[
\boxed{
\texttt{H1-P2.0 / ZETA-WEIL SPECIALIZATION MAP}
}
\]

The next phase should map each zeta-Weil object to its precise H1-P1 abstract carrier before importing any arithmetic strengthening:

- positive and negative quartet channels \(\to S_+,S_-\);
- selected packet \(\to M\);
- unselected negative divisor \(\to B\);
- support window \(\to\mathcal A_t\);
- persistent ray \(\to\mathcal J_c\);
- zero-moment residue law \(\to\) genuinely new zeta-specific structure;
- explicit formula and next jets \(\to\) post-abstraction arithmetic attachments.
