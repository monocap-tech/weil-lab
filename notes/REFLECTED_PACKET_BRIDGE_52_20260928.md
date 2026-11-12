# RPB-52 — Completed-to-\(L^2\) screw core-lift test

**Date:** 2026-09-28  
**Branch:** research/reflected-packet-bridge  
**Status:** **NO-GO FROM THE COMPLETED GENERALIZED ZERO EQUATION ALONE / ZERO EIGENVALUE DOES NOT FORCE AN \(L^2\) SCREW REPRESENTATIVE / SHARP ABSTRACT FRIEDRICHS-CORE COUNTERMODEL / THE REMAINING ACTUAL-WEIL PROBLEM IS A GENUINE EXTRA-REGULARITY THEOREM**  
**Dependencies:** RPB-31, RPB-32, RPB-51; Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v3, §§8.2–8.5.  
**Promotion status:** none.

## 0. Objective

RPB-51 corrected the ambient space of Suzuki's generalized zero problem.

The actual question is now

~~~math
\mathcal N_c^S
\cap
L_0^2(-c,c)
\stackrel{?}{\ne}
\{0\},
~~~

where

~~~math
\mathcal N_c^S
=
\left\{
u\in\mathcal H(S_c):
G_cu=0
\text{ in the completed generalized realization}
\right\}.
~~~

RPB-52 asks whether the special value \(\lambda=0\), the inverse Neumann
Laplacian \(K_c\), compactness of \(G_c\), or the Friedrichs construction
forces such a completed zero mode back into the ordinary \(L^2\) screw carrier.

It does not, from the currently available structure alone.

The obstruction is not merely absence of a cited theorem.  There is a sharp
abstract model with the same structural features in which the Friedrichs
operator has a true zero eigenvector, while the ordinary compact screw operator
has trivial kernel.

---

## 1. What Suzuki's zero equation does and does not contain

For a shift

~~~math
\mu<\lambda_c,
~~~

Suzuki defines

~~~math
S_c
=
G_c-\mu K_c,
\qquad
K_c=(-\Delta_N)^{-1},
~~~

and completes the ordinary zero-mean carrier in the norm induced by \(S_c\).

He explicitly records

~~~math
\mathcal H(S_c)\not\subset L^2(-c,c).
~~~

The generalized eigenvalue equation is

~~~math
G_cu
=
\lambda K_cu,
\qquad
u\in\mathcal H(S_c).
~~~

At

~~~math
\lambda=0,
~~~

the \(K_c\)-term disappears:

~~~math
\boxed{
G_cu=0
\quad
\text{in the completed generalized realization.}
}
~~~

Therefore the exceptional zero equation itself contains no explicit
\(K_c\)-smoothing term from which ordinary \(L^2\) regularity could be read off.

One may rewrite

~~~math
G_c
=
S_c+\mu K_c,
~~~

but on the completion the resulting equation is a form/operator identity in
\(\mathcal H(S_c)\).  It does not justify replacing the completed \(K_c\)-form
by the ordinary integral operator

~~~math
K_c:L_0^2\to L_0^2
~~~

before \(u\in L^2\) has already been established.

Thus the inverse Neumann Laplacian does not provide a free regularity bootstrap.

---

## 2. Suzuki explicitly separates ordinary attainment from completed spectral attainment

The ordinary compact carrier satisfies

~~~math
G_c:
L_0^2(-c,c)
\to
L_0^2(-c,c),
~~~

and Bombieri's \(H_0^1\) problem becomes the ordinary compact-operator Rayleigh
problem for \(G_c\).

Suzuki also emphasizes the distinction:

~~~text
the relevant bottom of the spectrum can agree while the infimum may or may not
be attained on the ordinary compact carrier.
~~~

This is exactly the phenomenon relevant at zero.

A completed generalized zero eigenvector can encode spectral attainment of the
Friedrichs problem without forcing the ordinary \(L^2\) screw Rayleigh
infimum to be attained by a nonzero vector.

So the source itself leaves room for

~~~math
\ker A_c\ne0,
\qquad
\ker_{L^2}G_c=\{0\}.
~~~

RPB-52 now shows that this possibility is structurally real.

---

## 3. Abstract countermodel: physical Hilbert space and core

Let

~~~math
H
=
\ell^2(\mathbb N).
~~~

Define the core

~~~math
V
=
\left\{
v=(v_n):
\sum_{n\ge1}n^2|v_n|^2<\infty
\right\}.
~~~

Let

~~~math
D:V\to H,
\qquad
(Dv)_n
=
n v_n.
~~~

Then

~~~math
\boxed{
D:V\overset{\sim}{\longrightarrow}H
}
~~~

is an isometric isomorphism when \(V\) is given the derivative norm.

Its inverse is

~~~math
(D^{-1}u)_n
=
\frac{u_n}{n},
~~~

which is compact as a map from \(H\) into the ambient \(\ell^2\) topology.

This is the sequence-space analogue of

~~~math
D:H_0^1(-c,c)\overset{\sim}{\longrightarrow}L_0^2(-c,c).
~~~

---

## 4. Choose a noncore zero eigenvector

Choose a unit vector

~~~math
v_0
=
C\left(
1,\frac12,\frac13,\ldots
\right)
\in H,
~~~

with normalizing constant \(C>0\).

Then

~~~math
v_0\in\ell^2,
~~~

but

~~~math
\sum_{n\ge1}
n^2
\left|
\frac{C}{n}
\right|^2
=
\infty.
~~~

Hence

~~~math
\boxed{
v_0\in H\setminus V.
}
~~~

Let

~~~math
P_0
=
|v_0\rangle\langle v_0|
~~~

and define the bounded nonnegative self-adjoint operator

~~~math
\boxed{
A
=
I-P_0.
}
~~~

Then

~~~math
\boxed{
\ker A
=
\mathbb C v_0,
}
~~~

while

~~~math
\boxed{
\ker A\cap V
=
\{0\}.
}
~~~

Thus \(A\) has a genuine zero eigenvalue, but its zero eigenspace contains no
core vector.

---

## 5. Construct the compact screw operator

Define

~~~math
\boxed{
G
=
(D^{-1})^*
A
D^{-1}
:
H\to H.
}
~~~

Since \(D^{-1}\) is compact and \(A\) is bounded,

~~~math
\boxed{
G
\text{ is compact, self-adjoint, and nonnegative.}
}
~~~

For every \(v\in V\),

~~~math
\begin{aligned}
\langle GDv,Dv\rangle_H
&=
\langle
A D^{-1}Dv,
D^{-1}Dv
\rangle_H
\\
&=
\langle Av,v\rangle_H.
\end{aligned}
~~~

Therefore

~~~math
\boxed{
q(v)
:=
\langle Av,v\rangle_H
=
\langle GDv,Dv\rangle_H
\qquad
(v\in V).
}
~~~

This is exactly the structural relation used by the screw-core realization.

---

## 6. The ordinary compact screw kernel is trivial

Suppose

~~~math
Gu=0.
~~~

Then

~~~math
0
=
\langle Gu,u\rangle
=
\left\langle
A D^{-1}u,
D^{-1}u
\right\rangle.
~~~

Since \(A\ge0\),

~~~math
D^{-1}u
\in
\ker A
=
\mathbb C v_0.
~~~

But

~~~math
D^{-1}u
\in V
~~~

for every \(u\in H\), while

~~~math
v_0\notin V.
~~~

Hence

~~~math
D^{-1}u=0,
~~~

and therefore

~~~math
u=0.
~~~

Thus

~~~math
\boxed{
\ker_H G
=
\{0\}.
}
~~~

We have obtained

~~~math
\boxed{
\ker A\ne0
\qquad\text{but}\qquad
\ker_HG=0.
}
~~~

---

## 7. Friedrichs interpretation

Restrict the quadratic form

~~~math
q(v)
=
\langle Av,v\rangle
~~~

to the dense core \(V\).

Because \(A\) is bounded and \(V\) is dense in \(H\), the closure of this
nonnegative form has form domain all of \(H\), and its associated self-adjoint
operator is precisely \(A\).

Equivalently, if \(B\) denotes the symmetric core operator/form generated by

~~~math
D^*GD,
~~~

then its Friedrichs realization is \(A\).

Therefore this model has all of the structural features relevant to the
RPB-52 implication:

- a dense \(H_0^1\)-type core \(V\);
- an isomorphism \(D:V\to H\);
- a compact nonnegative screw operator \(G\);
- the identity
  \[
  q(v)=\langle GDv,Dv\rangle;
  \]
- a Friedrichs operator \(A\);
- an attained zero eigenvalue of \(A\);
- no nonzero ordinary screw-kernel vector.

Hence the implication

~~~math
\boxed{
0\in\sigma_p(A)
\Longrightarrow
\ker_HG\ne0
}
~~~

is false at the level of this abstract architecture.

---

## 8. Completed zero modes are therefore not automatically regularized

The countermodel shows that the completion can genuinely add a zero spectral
direction that is invisible to the ordinary core carrier.

In RPB terminology,

~~~math
\boxed{
\mathcal N_c^S\ne0
}
~~~

does not structurally imply

~~~math
\boxed{
\mathcal N_c^S
\cap
L_0^2(-c,c)
\ne0.
}
~~~

Nor does simplicity of the completed zero eigenspace help: the countermodel
already has

~~~math
\dim\ker A=1.
~~~

Parity information alone also cannot repair the issue; one may place \(v_0\)
inside either parity sector in a doubled symmetric model while keeping it
outside the chosen core.

Thus neither zero-eigenvalue exceptionalism, one-dimensionality, nor symmetry
forces the completed zero vector into the ordinary screw carrier.

---

## 9. What an actual-Weil core-lift theorem would have to add

The remaining actual-Weil question must use information absent from the
abstract Friedrichs/screw architecture.

A successful theorem would need a statement of the form

~~~math
\boxed{
v\in\ker A_c
\Longrightarrow
v\in H_0^1(-c,c),
}
~~~

or at least

~~~math
\boxed{
\ker A_c
\cap
H_0^1(-c,c)
\ne
\{0\}.
}
~~~

Equivalent completed-screw forms are

~~~math
\boxed{
\mathcal N_c^S
\subseteq
L_0^2(-c,c)
}
~~~

for full lift, or

~~~math
\boxed{
\mathcal N_c^S
\cap
L_0^2(-c,c)
\ne
\{0\}
}
~~~

for existence of one core direction.

Such a theorem must exploit actual zeta-Weil endpoint structure, for example:

- a boundary regularity theorem for the zero mode stronger than the generic
  logarithmic form domain;
- an actual-kernel cancellation law that removes the noncore endpoint layer;
- an independent ordinary \(G_c\)-kernel existence theorem;
- or a source-specific domain identity at the zero spectral point.

None of these is supplied by Suzuki §§8.2–8.5 alone.

---

## 10. Consequence for the RPB line

RPB-52 closes the proposed "zero itself regularizes" route negatively.

The surviving conditional theorem remains

~~~math
0\ne u\in\ker_{L^2}G_c
\Longrightarrow
\text{RPB-34--50 collar/null-extension exclusion}.
~~~

But there is currently no structural bridge from

~~~math
0\ne v\in\ker A_c
~~~

to such a \(u\).

Therefore the full canonical interface remains open for exactly the reason
identified in RPB-51, and that reason cannot be removed by abstract
Friedrichs/generalized-eigenvalue theory.

---

## 11. RPB-52 determination

~~~math
\boxed{
\textbf{RPB-52 — THE COMPLETED GENERALIZED ZERO EQUATION DOES NOT FORCE AN ORDINARY \(L^2\) SCREW-CORE REPRESENTATIVE.}
}
~~~

Sharp abstract separation:

~~~math
\boxed{
\ker A\ne0,
\qquad
\ker A\cap V=0,
\qquad
\ker G=0.
}
~~~

Therefore:

~~~text
ZERO-EIGENVALUE REGULARIZATION: NO-GO FROM ABSTRACT STRUCTURE
COMPLETED-TO-L2 CORE LIFT: STILL OPEN FOR THE ACTUAL WEIL OPERATOR
RPB-34–50 CORE MECHANISM: INTACT CONDITIONALLY
FULL AZ-FIN-WEIL-NULL-EXTENSION: OPEN
~~~

## Next cursor

~~~text
RPB-53 / ACTUAL ZERO-MODE ENDPOINT REGULARITY TEST
~~~

The next pass should return to the actual localized Weil zero mode rather than
the generalized compact pencil.

Priority order:

1. derive the sharp endpoint class forced by \(A_cv=0\) in the Friedrichs
   domain;
2. determine whether the zero spectral value cancels the generic
   \((\log(1/s))^{-1/2}\)-type boundary layer or permits it;
3. test whether parity, the exact prime-delay structure, or the pole term
   removes the leading noncore boundary coefficient;
4. stop if the result is only generic logarithmic regularity already known from
   RPB-31, and record that the core-lift route is exhausted without a new
   actual-Weil boundary theorem.
