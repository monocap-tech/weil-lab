# RPB-55 — Optimal log-trace existence and flat-residue test

**Date:** 2026-09-28  
**Branch:** research/reflected-packet-bridge  
**Status:** **NO UNIVERSAL TRACE-COEFFICIENT THEOREM FROM CURRENT LOG-LAPLACIAN REGULARITY / OPTIMAL BOUNDARY CONTROL IS AN ENVELOPE, NOT AN ASYMPTOTIC EXPANSION / HOPF LOWER BOUNDS APPLY ONLY TO SIGN-CONTROLLED CLASSES / LOG-FLATNESS DOES NOT IMPLY SCREW-CORE REGULARITY / RESIDUE RETYPED BY CUMULATIVE BOUNDARY MASS**  
**Dependencies:** RPB-31, RPB-53, RPB-54; Hernández-Santamaría--López Ríos--Saldaña optimal boundary regularity/Hopf theorem; Feulefack--Jarohs--Weth eigenfunction regularity.  
**Promotion status:** none.

## 0. Objective

RPB-54 excluded strict null extension for every Friedrichs zero mode for which a
two-sided optimal logarithmic expansion exists and has nonzero amplitude:

~~~math
h(c-r)
=
b_+\ell^{1/2}(r)
+
o(\ell^{1/2}(r)),
~~~

~~~math
h(-c+r)
=
b_-\ell^{1/2}(r)
+
o(\ell^{1/2}(r)),
~~~

with

~~~math
(b_+,b_-)\ne(0,0).
~~~

RPB-55 asks:

1. does current logarithmic-Laplacian boundary theory give such coefficients
   \(b_\pm\) for every actual Friedrichs zero mode?
2. if the coefficients exist and both vanish, does that force the mode into
   the screw core?

The answer to both questions is **no at the current theorem level**.

This pass therefore does not close the canonical null-extension interface.  It
retypes the boundary residue more accurately.

---

## 1. The sharp general boundary theorem is an upper envelope

For the pure Dirichlet logarithmic Laplacian,

~~~math
L_\Delta u=f
\quad\text{in }\Omega,
\qquad
u=0
\quad\text{in }\mathbb R^N\setminus\Omega,
~~~

Hernández-Santamaría--López Ríos--Saldaña prove that, under an exterior uniform
sphere condition, for

~~~math
f\in L^\infty(\Omega),
\qquad
u\in\mathbb H(\Omega)\cap L^\infty(\mathbb R^N),
~~~

one has

~~~math
\boxed{
|u(x)|
\le
C\ell^{1/2}(d(x,\partial\Omega)).
}
~~~

This is the optimal exponent.

But the theorem does **not** assert the existence of a boundary quotient limit

~~~math
\lim_{r\downarrow0}
\frac{
u(x_0-r\nu)
}{
\ell^{1/2}(r)
}.
~~~

Thus optimal regularity does not by itself produce a scalar boundary trace
coefficient.

---

## 2. Optimality is proved on special positive classes

The same paper proves sharp lower behavior for special sign-controlled
solutions.

For the torsion function in a sufficiently small ball,

~~~math
L_\Delta\tau=1,
~~~

one has two-sided comparability

~~~math
c^{-1}\ell^{1/2}(d(x,\partial B))
\le
\tau(x)
\le
c\ell^{1/2}(d(x,\partial B)).
~~~

The Hopf-type theorem likewise gives a positive lower quotient for nontrivial
nonnegative supersolutions under the stated maximum-principle hypotheses.

These statements prove that the exponent \(1/2\) is sharp.

They still do not provide a general linear boundary trace operator

~~~math
u
\mapsto
b_{\partial}(u)
~~~

for arbitrary sign-changing weak solutions.

In particular, an arbitrary neutral eigenfunction need not satisfy the sign
hypotheses required for the Hopf lower bound.

---

## 3. Pure logarithmic eigenfunctions are bounded, but this still does not create a coefficient

Feulefack--Jarohs--Weth prove that Dirichlet eigenfunctions of the pure
logarithmic Laplacian are bounded and locally continuous; under an exterior
sphere condition they are continuous up to the boundary.

Combining boundedness with the sharp boundary theorem gives, for a pure
logarithmic eigenfunction,

~~~math
|\phi(x)|
\le
C\ell^{1/2}(d(x,\partial\Omega)).
~~~

Again this is only an envelope.

Even for the pure eigenvalue problem, the cited results do not supply a
two-sided asymptotic expansion

~~~math
\phi(x_0-r\nu)
=
b(x_0)\ell^{1/2}(r)
+
o(\ell^{1/2}(r))
~~~

for every eigenfunction and every boundary point.

Therefore the existence of \(b_\pm\) cannot be imported from the current pure
logarithmic spectral theory.

---

## 4. The actual Weil zero mode has an additional hypothesis gap

For the actual compact-window Weil operator,

~~~math
A_c
=
\frac12L_\Delta
+
B_c,
~~~

RPB-31 gives

~~~math
h\in\ker A_c
\Longrightarrow
h\in\mathfrak D(A_{\log,c}).
~~~

At this level the lower-order equation yields an \(L^2\) right-hand side for
the logarithmic principal operator.

The sharp boundary theorem quoted in Section 1 assumes both:

~~~math
u\in L^\infty,
\qquad
f\in L^\infty.
~~~

Those hypotheses are not consequences of logarithmic operator-domain
membership alone.

The finite translations preserve \(L^p\) classes but do not improve them.

Thus, before even asking for a boundary coefficient, there is a separate
actual-Weil endpoint regularity gap:

~~~math
\boxed{
\ker A_c
\stackrel{?}{\subset}
L^\infty(-c,c).
}
~~~

RPB-43 gives interior analyticity, but that does not control the boundary
norm.

Hence current boundary theory does not eliminate the
**boundary-untyped** class.

---

## 5. Even an optimal envelope does not give a coefficient

Suppose, more strongly, that an actual zero mode is already known to satisfy

~~~math
|h(c-r)|
\le
C\ell^{1/2}(r).
~~~

This still permits:

- oscillation of
  \[
  h(c-r)/\ell^{1/2}(r);
  \]
- different subsequential boundary quotients;
- quotient tending to zero without any next asymptotic coefficient;
- sign changes on logarithmic scales.

Therefore

~~~math
h
=
O(\ell^{1/2})
~~~

does not imply

~~~math
h
=
b\ell^{1/2}
+
o(\ell^{1/2}).
~~~

RPB-54's scalar-amplitude theorem is consequently a conditional theorem on a
strictly stronger boundary class than current general regularity provides.

---

## 6. Log-flatness does not imply \(H_0^1\)

Now suppose a classical optimal coefficient does exist and vanishes:

~~~math
h(c-r)
=
o(\ell^{1/2}(r)).
~~~

This condition alone is far weaker than screw-core regularity.

For example, define near the endpoint

~~~math
h(c-r)
=
\ell(r)
=
\frac1{\log(1/r)}.
~~~

Then

~~~math
\frac{
h(c-r)
}{
\ell^{1/2}(r)
}
=
\ell^{1/2}(r)
\to0.
~~~

So this germ is log-flat.

But

~~~math
\partial_r h(c-r)
=
\frac1{
r\log^2(1/r)
},
~~~

and therefore

~~~math
\int_0^\delta
|\partial_r h(c-r)|^2\,dr
=
\infty.
~~~

Thus

~~~math
\boxed{
\text{log-flat}
\not\Longrightarrow
H_0^1.
}
~~~

This is a regularity counterexample only; it is not asserted to solve the
actual Weil null equation.

Its purpose is to prevent a silent promotion from vanishing leading
logarithmic amplitude to screw-core membership.

---

## 7. The endpoint normal equation suggests a smaller flat hierarchy, but does not yet classify it

Let

~~~math
t=\log(1/r),
\qquad
H(t)=h(c-e^{-t}).
~~~

The leading logarithmic normal operator is

~~~math
\mathcal N_{\log}H
=
2tH
-
\int^t H.
~~~

Write

~~~math
F(t)
=
\int_{t_0}^tH(w)\,dw.
~~~

If one has an endpoint equation of the model form

~~~math
2tH(t)-F(t)=g(t)
~~~

with

~~~math
g(t)=O(1),
~~~

then

~~~math
2tF'(t)-F(t)=g(t).
~~~

Solving the first-order equation gives

~~~math
F(t)
=
C\sqrt t
+
O(1),
~~~

and therefore

~~~math
H(t)
=
\frac{C}{2\sqrt t}
+
O(t^{-1}).
~~~

The coefficient \(C\) is precisely the leading logarithmic homogeneous
amplitude in this normal model.

If the leading amplitude vanishes,

~~~math
C=0,
~~~

the model only gives

~~~math
\boxed{
H(t)=O(t^{-1}),
}
~~~

not \(H_0^1\) regularity.

This calculation is recorded as a normal-model guide only.  RPB-55 does not
claim that every actual Friedrichs zero mode satisfies a pointwise normal
equation with bounded \(g\).

---

## 8. Exterior leakage does not fundamentally require a point trace coefficient

At the right endpoint, define the cumulative boundary mass

~~~math
\boxed{
M_+(s;h)
=
\int_s^\delta
\frac{
h(c-r)
}{
r
}
\,dr.
}
~~~

For the zero extension, RPB-54's exact exterior formula shows that the
logarithmic principal output is governed, up to bounded and near-\(r<s\)
corrections, by

~~~math
-M_+(s;h).
~~~

The amplitude case

~~~math
h(c-r)
\sim
b_+\ell^{1/2}(r)
~~~

is only one special situation:

~~~math
M_+(s;h)
\sim
2b_+\sqrt{\log(1/s)}.
~~~

If instead

~~~math
h(c-r)
\sim
\frac{b}{\log(1/r)},
~~~

then

~~~math
M_+(s;h)
\sim
b\log\log(1/s).
~~~

Thus a log-flat mode can still have an unbounded exterior leakage.

The pointwise coefficient \(b_+\) is not the fundamental object for
null-extension rigidity.

The more robust object is the cumulative boundary mass.

---

## 9. Cancellation caveat

For sign-changing or oscillatory boundary germs, it is possible for

~~~math
h(c-r)
=
o(\ell^{1/2}(r))
~~~

while the cumulative mass

~~~math
M_+(s;h)
~~~

remains bounded because of cancellation.

Therefore RPB-55 does not promote

~~~math
\text{noncore}
\Longrightarrow
|M_+(s;h)|\to\infty.
~~~

The next pass must distinguish:

1. cumulative-mass divergent modes, which should leak directly;
2. cumulative-mass bounded modes, which represent a genuinely thinner
   cancellation class.

This distinction does not require existence of a classical
\(\ell^{1/2}\) coefficient.

---

## 10. RPB-55 determination

~~~math
\boxed{
\textbf{RPB-55 — CURRENT BOUNDARY REGULARITY DOES NOT PRODUCE A UNIVERSAL OPTIMAL LOG TRACE COEFFICIENT, AND VANISHING OF SUCH A COEFFICIENT DOES NOT FORCE SCREW-CORE MEMBERSHIP.}
}
~~~

Current theorem-level information:

~~~text
GENERAL SHARP LOG BOUNDARY THEOREM:
    O(ell^{1/2}) envelope under bounded-solution/bounded-forcing hypotheses

TORSION / NONNEGATIVE HOPF CLASSES:
    matching positive lower bound

ARBITRARY ACTUAL WEIL FRIEDRICHS ZERO MODE:
    no universal classical b_± trace theorem currently available

LOG-FLATNESS b_+=b_-=0:
    does not imply H_0^1
~~~

The canonical residue is therefore better expressed through cumulative
boundary mass than through a mandatory scalar trace coefficient.

## Next cursor

~~~text
RPB-56 / CUMULATIVE BOUNDARY-MASS LEAKAGE AND CANCELLATION TEST
~~~

The next pass should work directly with

~~~math
M_\pm(s;h)
=
\int_s^\delta
\frac{
h(\pm c\mp r)
}{
r
}
\,dr.
~~~

Priority order:

1. derive the exterior Weil asymptotic in terms of \(M_\pm\) without assuming a
   pointwise trace coefficient;
2. show that any unbounded \(M_\pm\) dominating the lower actual-Weil terms
   excludes strict null extension;
3. characterize how bounded cumulative mass can occur under the interior zero
   equation;
4. determine whether the bounded-mass residue forces stronger endpoint
   cancellation, core regularity, or a new explicitly typed boundary quotient.
