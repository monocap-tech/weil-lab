# Abstract Defect Calculus
## H1-P1.0 — Hilbert/Krein screening normal form

This document extracts the first zeta-independent theorem package of Horizon 1.

No statement below uses \(\zeta\), \(\Xi\), primes, functional-equation quartets, or the explicit formula.

## 0. Setup

Let

\[
\mathcal H,\qquad K_+,\qquad K_-
\]

be complex Hilbert spaces and let

\[
S_+\in\mathcal B(K_+,\mathcal H),
\qquad
S_-\in\mathcal B(K_-,\mathcal H).
\]

Define the synthesis operator

\[
E:K_+\oplus K_-\to\mathcal H,
\qquad
E(x,u)=S_+x+S_-u.
\]

Equip the coefficient space with the fundamental symmetry

\[
J=
\begin{pmatrix}
I&0\\
0&-I
\end{pmatrix},
\]

so that

\[
[(x,u),(y,v)]_J
=
\langle x,y\rangle-\langle u,v\rangle.
\]

Define the analysis space

\[
\boxed{
\mathcal A:=(\ker E)^\perp
=
\overline{\operatorname{Ran}E^*}.
}
\]

Finally define the physical defect operator

\[
\boxed{
D:=EJE^*
=
S_+S_+^*-S_-S_-^*.
}
\]

The point of H1-P1.0 is that the sign geometry of \(\mathcal A\) is exactly the sign geometry of \(D\).

---

## WD-A1 — Defect identity and index transfer

For every \(h\in\mathcal H\),

\[
E^*h=(S_+^*h,S_-^*h),
\]

and therefore

\[
\boxed{
[E^*h,E^*h]_J
=
\langle Dh,h\rangle.
}
\]

Consequently,

\[
\boxed{
\mathcal A\text{ is }J\text{-nonnegative}
\iff
D\succeq0.
}
\]

More generally,

\[
\boxed{
\operatorname{ind}_-(\mathcal A,J)
=
\operatorname{ind}_-(D),
}
\]

where each side denotes the supremum of the dimensions of negative-definite subspaces.

### Proof

The identity is immediate:

\[
[E^*h,E^*h]_J
=
\|S_+^*h\|^2-\|S_-^*h\|^2
=
\langle
(S_+S_+^*-S_-S_-^*)h,h
\rangle.
\]

If \(D\succeq0\), the \(J\)-form is nonnegative on \(\operatorname{Ran}E^*\), hence by continuity on its closure \(\mathcal A\).

Conversely, if \(\mathcal A\) is \(J\)-nonnegative, then \(E^*h\in\mathcal A\) for every \(h\), so the displayed identity gives \(\langle Dh,h\rangle\ge0\).

For the index statement, a negative-definite subspace for \(D\) cannot meet \(\ker E^*\) nontrivially, and \(E^*\) maps it injectively to a \(J\)-negative subspace of \(\mathcal A\). In the other direction, every finite-dimensional \(J\)-negative subspace of \(\mathcal A\) can be approximated by vectors from the dense subspace \(\operatorname{Ran}E^*\); negative definiteness is stable under sufficiently small finite-dimensional perturbation. Taking suprema over finite dimensions gives equality.

**Standing:** PROVED.

---

## WD-A2 — Contractive screening equivalence

The following are equivalent:

1. \(\mathcal A\) is \(J\)-nonnegative;
2. \(D\succeq0\);
3. 
   \[
   S_-S_-^*\preceq S_+S_+^*;
   \]
4. there exists a contraction
   \[
   X:K_-\to K_+
   \]
   such that
   \[
   \boxed{
   S_-=-S_+X.
   }
   \]

Among all exact solutions of \(S_+X=-S_-\), there is a unique Douglas reduced solution satisfying

\[
\operatorname{Ran}X
\subseteq
(\ker S_+)^\perp.
\]

### Proof

The equivalence of 1–3 is WD-A1.

The equivalence of 3 and 4 is Douglas' factorization theorem applied to \(S_-\) and \(S_+\). The sign is absorbed into \(X\).

**Standing:** PROVED using the imported Douglas factorization theorem.

### Interpretation

A nonnegative analysis space is exactly the statement that every negative synthesis channel can be reproduced through the positive synthesis map **within unit coefficient norm**.

Thus the “unit screening budget” is an abstract Hilbert-space factorization condition, not an arithmetic phenomenon.

---

## WD-A3 — Reduced-screening graph normal form

Assume only exact range inclusion

\[
\operatorname{Ran}S_-
\subseteq
\operatorname{Ran}S_+.
\]

Let \(X:K_-\to(\ker S_+)^\perp\) be the Douglas reduced solution of

\[
S_+X=-S_-.
\]

No contractivity assumption is made.

Then

\[
\boxed{
\ker E
=
(\ker S_+\oplus\{0\})
\ \widehat\oplus\
\{(Xu,u):u\in K_-\},
}
\]

where the sum is orthogonal in \(K_+\oplus K_-\).

Consequently,

\[
\boxed{
\mathcal A
=
\{(a,-X^*a):
a\in(\ker S_+)^\perp\}.
}
\]

On this graph,

\[
\boxed{
[(a,-X^*a),(a,-X^*a)]_J
=
\|a\|^2-\|X^*a\|^2.
}
\]

The physical defect operator also factors as

\[
\boxed{
D
=
S_+(I-XX^*)S_+^*.
}
\]

### Proof

Every \((x,u)\in\ker E\) satisfies

\[
S_+x=-S_-u=S_+Xu,
\]

hence \(x-Xu\in\ker S_+\). Since \(Xu\perp\ker S_+\), the stated orthogonal decomposition follows.

A vector \((a,v)\) is orthogonal to \(\ker S_+\oplus\{0\}\) exactly when \(a\perp\ker S_+\). Orthogonality to every \((Xu,u)\) then gives

\[
\langle a,Xu\rangle+\langle v,u\rangle=0
\]

for every \(u\), hence \(v=-X^*a\).

Finally,

\[
S_-S_-^*
=
S_+XX^*S_+^*,
\]

which gives the defect factorization.

**Standing:** PROVED.

---

## WD-A4 — Complete abstract screening morphology

The reduced solution gives a complete first sign classification.

### R — Range defect

If

\[
\operatorname{Ran}S_-
\not\subseteq
\operatorname{Ran}S_+,
\]

then no exact screening operator exists.

By Douglas' theorem,

\[
S_-S_-^*\npreceq \lambda S_+S_+^*
\]

for every finite factorization constant adequate to the failed inclusion, and in particular contractive screening is impossible. Since \(D\succeq0\) would imply range inclusion, \(D\not\succeq0\), so \(\mathcal A\) contains a strictly negative direction.

This is an **unscreened negative defect**.

### B — Over-budget defect

Assume range inclusion and let \(X\) be the reduced solution.

If

\[
\|X\|>1,
\]

then there exists \(a\in(\ker S_+)^\perp\) with

\[
\|X^*a\|>\|a\|,
\]

so

\[
(a,-X^*a)\in\mathcal A
\]

is strictly \(J\)-negative.

This is an **exactly screenable but over-budget negative defect**.

### P — Strictly screened regime

If

\[
\|X\|=r<1,
\]

then every \(y=(a,-X^*a)\in\mathcal A\) satisfies

\[
[y,y]_J
\ge
(1-r^2)\|a\|^2.
\]

Since

\[
\|y\|^2
=
\|a\|^2+\|X^*a\|^2
\le
(1+r^2)\|a\|^2,
\]

we obtain the uniform estimate

\[
\boxed{
[y,y]_J
\ge
\frac{1-r^2}{1+r^2}\|y\|^2.
}
\]

This is the **uniformly positive screened regime**.

### N — Attained critical screening

Suppose

\[
\|X\|=1
\]

and the norm of \(X^*\) is attained: there exists \(a\ne0\) with

\[
\|X^*a\|=\|a\|.
\]

Then

\[
\boxed{
(a,-X^*a)\ne0
}
\]

is a neutral vector in \(\mathcal A\).

This is the **neutral-mode boundary**.

### AN — Non-attained critical screening

Suppose

\[
\|X\|=1
\]

but there is no nonzero \(a\) satisfying

\[
\|X^*a\|=\|a\|.
\]

Then every nonzero vector of \(\mathcal A\) is strictly \(J\)-positive, but there exists a sequence \(\|a_n\|=1\) such that

\[
\|X^*a_n\|\to1.
\]

Hence, for

\[
y_n=(a_n,-X^*a_n),
\]

the normalized \(J\)-margin tends to zero:

\[
\frac{[y_n,y_n]_J}{\|y_n\|^2}
\longrightarrow0.
\]

This is the **approximate-neutral boundary**.

### Consequence

The abstract screening boundary is not a simple negative/neutral dichotomy.

At minimum it contains

\[
\boxed{
\text{range defect},
\quad
\text{over-budget negative defect},
\quad
\text{attained neutral mode},
\quad
\text{non-attained approximate-neutral boundary},
\quad
\text{strict positive screening}.
}
\]

**Standing:** PROVED.

---

## WD-A5 — Rank-one defect specialization

Let

\[
K_-=\mathbb C
\]

and let

\[
S_-\alpha=\alpha g
\]

for a fixed \(g\in\mathcal H\).

Then

\[
S_-S_-^*
=
g\otimes g,
\]

so

\[
\boxed{
D
=
S_+S_+^*
-
g\otimes g.
}
\]

Therefore the following are equivalent:

\[
D\succeq0,
\]

\[
g\otimes g\preceq S_+S_+^*,
\]

and the existence of \(c\in K_+\) with

\[
g=-S_+c,
\qquad
\|c\|\le1.
\]

Thus the rank-one positivity defect used in the Weil traversal is the one-negative-channel specialization of WD-A1–A4.

**Standing:** PROVED.

---

## WD-A6 — Monotone positive screening

Let \(P_N\) be an increasing sequence of orthogonal projections on \(K_+\) with

\[
P_N\to I
\]

strongly.

Define

\[
S_{+,N}=S_+P_N
\]

and

\[
D_N
=
S_+P_NS_+^*
-
S_-S_-^*.
\]

Then

\[
\boxed{
D_N\preceq D_{N+1}\preceq D
}
\]

and

\[
D_N\to D
\]

strongly.

Consequently,

\[
\langle D_Nh,h\rangle
\uparrow
\langle Dh,h\rangle
\]

for every \(h\in\mathcal H\), and

\[
\boxed{
\operatorname{ind}_-(D_N)
\ge
\operatorname{ind}_-(D_{N+1}).
}
\]

Finite negative index can therefore shrink under restoration of the positive complement.

It need not survive in the limit.

**Standing:** PROVED.

---

## WD-E1 — Complete spectral screening is possible

Take

\[
\mathcal H=\mathbb C,
\qquad
K_-=\mathbb C,
\qquad
S_-=1.
\]

Let

\[
K_+=\ell^2(\mathbb N)
\]

and define

\[
c_j=\frac1{\sqrt{j(j+1)}},
\qquad
S_+x=\sum_{j\ge1}c_jx_j.
\]

Because

\[
\sum_{j=1}^\infty c_j^2
=
\sum_{j=1}^\infty\frac1{j(j+1)}
=
1,
\]

the full defect is

\[
D=0.
\]

For \(P_N\) the projection onto the first \(N\) coordinates,

\[
\sum_{j=1}^N c_j^2
=
1-\frac1{N+1},
\]

so

\[
\boxed{
D_N=-\frac1{N+1}.
}
\]

Thus every finite truncation has one strictly negative direction, but

\[
D_N\uparrow0.
\]

This gives an exact abstract model of complete spectral screening.

**Standing:** PROVED EXAMPLE.

---

## WD-E2 — Critical screening need not produce a neutral vector

Take

\[
\mathcal H=K_+=K_-=L^2(0,1),
\]

let

\[
S_+=I,
\qquad
X=M_t,
\qquad
S_-=-X,
\]

where

\[
(M_tf)(t)=t f(t).
\]

Then

\[
\|X\|=1,
\]

but \(X\) does not attain its norm on a nonzero vector because

\[
|t|<1
\]

almost everywhere on \((0,1)\).

The defect is

\[
D
=
I-M_{t^2}.
\]

For every nonzero \(f\),

\[
\langle Df,f\rangle
=
\int_0^1(1-t^2)|f(t)|^2\,dt
>
0,
\]

so there is no neutral vector.

However, unit vectors supported increasingly close to \(t=1\) satisfy

\[
\langle Df_n,f_n\rangle\to0.
\]

Hence the system is positive but not uniformly positive and lies on the non-attained approximate-neutral boundary.

**Standing:** PROVED EXAMPLE.

---

## H1-P1.0 determination

The first abstraction pass succeeds.

The following objects are now independent of zeta arithmetic:

\[
\boxed{
D=S_+S_+^*-S_-S_-^*,
}
\]

\[
\boxed{
\operatorname{ind}_-(\mathcal A,J)
=
\operatorname{ind}_-(D),
}
\]

\[
\boxed{
D\succeq0
\iff
\text{contractive Douglas screening},
}
\]

and, under exact range inclusion,

\[
\boxed{
\mathcal A
=
\operatorname{graph}(-X^*).
}
\]

The abstract sign problem is therefore a reduced-screening norm problem.

The pass also corrects the earlier public morphology map:

\[
\boxed{
\text{critical screening}
\not\Rightarrow
\text{actual neutral mode}.
}
\]

There is a distinct non-attained approximate-neutral boundary.

## Next H1-P1 cursor

\[
\boxed{
\texttt{H1-P1.1 / RESTRICTED-CHANNEL AND FINITE-INDEX TRANSFER}
}
\]

The next pass should determine how WD-A1–A6 behave when:

1. only a selected finite-dimensional negative subspace is tracked;
2. the remaining negative channels are treated as background;
3. the negative index is finite but larger than one;
4. screening is compressed or Schur-complemented through nested channel decompositions.

That is the correct bridge from the abstract calculus back toward the finite-index Weil setting.
