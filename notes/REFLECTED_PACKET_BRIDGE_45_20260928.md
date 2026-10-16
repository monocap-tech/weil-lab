# RPB-45 — Base-endpoint \(t=0\) screw-singularity matching

**Date:** 2026-09-28  
**Branch:** \`research/reflected-packet-bridge\`  
**Status:** **PASS / NONTHRESHOLD STRICT COLLAR EXCLUDED / STRICT PERSISTENCE QUANTIZED TO PRIME-POWER THRESHOLDS / THRESHOLD BRANCH REDUCED TO A CARLEMAN--STIELTJES ENDPOINT EQUATION**  
**Dependencies:** RPB-35, RPB-43, RPB-44; RPB-EXT-A3 Suzuki base singularity; RPB-EXT-A4 Sokhotskii--Plemelj.  
**Promotion status:** none.

## 0. Objective

RPB-44 eliminated every prime-endpoint activation strictly above the original
support edge \(x=c\).

The only remaining place where a strict constant screw collar could begin is
the original boundary itself.

That point is qualitatively different because the non-prime screw kernel
reaches the diagonal singularity

\`\`\`math
t=x-y=0.
\`\`\`

RPB-45 analyzes this base singularity.

The result is a sharp dichotomy.

If

\`\`\`math
2c
\ne
\log n
\`\`\`

for every prime power \(n\), then no strict collar can exist.

If a strict collar exists, necessarily

\`\`\`math
\boxed{
2c=\log n_0
}
\`\`\`

for a prime power \(n_0\), and the endpoint source must satisfy one exact
parity-dependent Carleman--Stieltjes equation.

Thus strict neutral persistence is quantized to the prime-power threshold set.

---

## 1. Suzuki's small-\(t\) formula

For

\`\`\`math
0<t<\log2,
\`\`\`

the prime sum in Suzuki's explicit screw formula is empty.

In the proof of Theorem 4.1, Suzuki gives

\`\`\`math
\Psi'(t)
=
2(e^{t/2}-e^{-t/2})
+
c_0
-
\arctan(e^{t/2})
+
\operatorname{arctanh}(e^{-t/2}),
\`\`\`

with

\`\`\`math
c_0
=
\frac{\pi}{4}
-
\frac{\gamma_0+3\log2}{2}.
\`\`\`

As \(t\downarrow0\),

\`\`\`math
\operatorname{arctanh}(e^{-t/2})
=
-\frac12\log t
+
\log2
+
O(t^2),
\`\`\`

\`\`\`math
\arctan(e^{t/2})
=
\frac{\pi}{4}
+
\frac t4
+
O(t^3),
\`\`\`

and

\`\`\`math
2(e^{t/2}-e^{-t/2})
=
2t
+
O(t^3).
\`\`\`

Hence

\`\`\`math
\Psi'(t)
=
-\frac12\log t
-
\frac{\gamma_0+\log2}{2}
+
O(t).
\`\`\`

Integrating from \(0\), using \(\Psi(0)=0\),

\`\`\`math
\Psi(t)
=
-\frac t2\log t
+
\frac{1-\gamma_0-\log2}{2}t
+
O(t^2).
\`\`\`

Since

\`\`\`math
g=-\Psi,
\`\`\`

we obtain

\`\`\`math
\boxed{
g(t)
=
\frac t2\log t
+
\frac{\gamma_0+\log2-1}{2}t
+
O(t^2)
}
\qquad
(t\downarrow0).
\`\`\`

Therefore

\`\`\`math
\boxed{
g''(t)
=
\frac1{2t}
+
O(1)
}
\qquad
(t\downarrow0).
\`\`\`

The coefficient \(1/2\) is exact and load-bearing.

---

## 2. Endpoint coordinates

Let

\`\`\`math
0\ne u
\in
L_0^2(-c,c)
\`\`\`

be the screw-visible neutral source, with

\`\`\`math
F_u
=
g*u.
\`\`\`

By RPB-43,

\`\`\`math
u
\in
C^\omega(-c,c).
\`\`\`

Write a right-exterior point as

\`\`\`math
x=c+s,
\qquad
s>0,
\`\`\`

and parameterize the source from the right endpoint by

\`\`\`math
r=c-y,
\qquad
0<r<2c.
\`\`\`

Define

\`\`\`math
\boxed{
f(r)
=
u(c-r).
}
\`\`\`

Then

\`\`\`math
x-y
=
s+r.
\`\`\`

The base singularity in Section 1 therefore contributes to
\(F_u''(c+s)\) the Stieltjes term

\`\`\`math
\boxed{
\frac12
S_f(s),
\qquad
S_f(s)
=
\int_0^{2c}
\frac{f(r)}{s+r}\,dr.
}
\`\`\`

---

## 3. Analyticity of every nonthreshold remainder

Fix \(s\) in a sufficiently small neighborhood of \(0\).

After subtracting

\`\`\`math
\frac1{2t}
\`\`\`

from \(g''(t)\) near \(t=0+\), the remaining non-prime kernel is real analytic
there.

For source points bounded away from \(y=c\), the separation \(x-y\) stays
bounded away from \(0\), so the non-prime kernel is real analytic in \(s\).

Now consider a prime-power term.

Its second derivative contributes

\`\`\`math
\frac{\Lambda(n)}{\sqrt n}
u(c+s-\log n).
\`\`\`

If

\`\`\`math
\log n<2c,
\`\`\`

then at \(s=0\)

\`\`\`math
c-\log n
\in
(-c,c),
\`\`\`

strictly inside the source interval.

RPB-43 therefore makes this shifted source a real-analytic function of \(s\)
near \(0\).

If

\`\`\`math
\log n>2c,
\`\`\`

then the shifted point stays outside the support for all sufficiently small
positive \(s\), so the term vanishes identically there.

Thus the only prime term that can fail to be analytic through \(s=0\) is an
equality-threshold term satisfying

\`\`\`math
\boxed{
\log n_0=2c.
}
\`\`\`

The pole/evaluation range is analytic as in RPB-43.

---

## 4. Nonthreshold exterior equation

Assume

\`\`\`math
2c
\ne
\log n
\`\`\`

for every prime power \(n\).

Suppose, for contradiction, that the neutral screw potential extends
constantly to a strict right collar:

\`\`\`math
F_u(x)=C
\qquad
(c<x<c+\varepsilon).
\`\`\`

Then

\`\`\`math
F_u''(c+s)=0
\qquad
(0<s<\varepsilon).
\`\`\`

Sections 2 and 3 give

\`\`\`math
\boxed{
\frac12S_f(s)
+
A(s)
=
0,
}
\`\`\`

where \(A\) is real analytic through \(s=0\).

Equivalently,

\`\`\`math
S_f(s)
=
-2A(s).
\`\`\`

---

## 5. Holomorphic continuation through the end of the cut

Define the Cauchy/Stieltjes transform

\`\`\`math
S_f(z)
=
\int_0^{2c}
\frac{f(r)}{z+r}\,dr.
\`\`\`

Since

\`\`\`math
f\in L^2(0,2c),
\`\`\`

this is holomorphic on

\`\`\`math
\mathbb C\setminus[-2c,0].
\`\`\`

The analytic function \(A(s)\) in Section 4 has a holomorphic extension to a
complex neighborhood of \(0\).

The equality

\`\`\`math
S_f(s)
=
-2A(s)
\`\`\`

holds on a nonempty positive real interval.

By the identity theorem, the holomorphic function \(S_f\) on the right side of
the cut coincides there with the holomorphic extension of \(-2A\).

Therefore \(S_f\) admits a holomorphic continuation through a nonempty
subinterval

\`\`\`math
(-\delta,0)
\subset
[-2c,0].
\`\`\`

---

## 6. Plemelj jump kills the endpoint source

The Sokhotskii--Plemelj jump formula recovers the \(L^2\) density of a Cauchy
transform from the difference of its two boundary values across the cut.

If \(S_f\) is holomorphic through

\`\`\`math
(-\delta,0),
\`\`\`

its jump there is zero.

Hence

\`\`\`math
\boxed{
f(r)=0
}
\qquad
\text{for a.e. }
0<r<\delta.
\`\`\`

Equivalently,

\`\`\`math
u(y)=0
\`\`\`

on an open interval adjacent to the right endpoint \(c\).

But RPB-43 proved

\`\`\`math
u
\in
C^\omega(-c,c)
\`\`\`

and \(u\ne0\).

The analytic identity theorem therefore forces

\`\`\`math
u\equiv0,
\`\`\`

contradiction.

Thus:

\`\`\`math
\boxed{
2c\ne\log n
\text{ for every prime power}
\Longrightarrow
\text{no strict constant collar exists}.
}
\`\`\`

This is the nonthreshold base-crossing exclusion.

---

## 7. Strict persistence is quantized to a prime-power threshold

Section 6 proves the contrapositive:

\`\`\`math
\boxed{
\text{strict collar persistence}
\Longrightarrow
2c=\log n_0
}
\`\`\`

for some prime power \(n_0\).

Equivalently,

\`\`\`math
\boxed{
e^{2c}
=
n_0
=
p^m.
}
\`\`\`

Thus strict null-extension, if it occurs at all, is confined to the discrete
support set

\`\`\`math
\left\{
\frac12\log(p^m)
\right\}.
\`\`\`

This is prime-power threshold quantization of strict persistence.

---

## 8. Equality-threshold prime term

Now assume

\`\`\`math
\boxed{
2c=\log n_0
}
\`\`\`

for one prime power \(n_0\).

Under the endpoint strict-\(<\) convention, this prime term is absent from the
endpoint compact-window sum but becomes active for every strict right
enlargement.

Its second-derivative contribution on the right collar is

\`\`\`math
a_0
u(c+s-\log n_0),
\`\`\`

where

\`\`\`math
\boxed{
a_0
=
\frac{\Lambda(n_0)}{\sqrt{n_0}}.
}
\`\`\`

Since

\`\`\`math
\log n_0=2c,
\`\`\`

this is

\`\`\`math
a_0u(-c+s).
\`\`\`

Resolve the source into one parity block:

\`\`\`math
u(-x)
=
\varepsilon_u u(x),
\qquad
\varepsilon_u\in\{+1,-1\}.
\`\`\`

Then

\`\`\`math
u(-c+s)
=
\varepsilon_u u(c-s)
=
\varepsilon_u f(s).
\`\`\`

So the equality-threshold prime term has exactly the same endpoint source
density as the Stieltjes singularity.

---

## 9. Exact threshold base-endpoint equation

All other contributions are analytic across \(s=0\).

Therefore a strict constant collar at a threshold forces

\`\`\`math
\boxed{
\frac12
\int_0^{2c}
\frac{f(r)}{s+r}\,dr
+
\varepsilon_u a_0 f(s)
+
A(s)
=
0,
\qquad
0<s<\varepsilon,
}
\`\`\`

where

\`\`\`math
A
\in
C^\omega((-\varepsilon,\varepsilon)).
\`\`\`

Equivalently,

\`\`\`math
\boxed{
\frac12S_f(s)
+
\varepsilon_u a_0 f(s)
\in
C^\omega
}
\`\`\`

through the endpoint.

This is the threshold base-endpoint Carleman equation.

Unlike the nonthreshold case, Plemelj continuation does not force
\(f=0\), because the equality-threshold prime term carries exactly the
endpoint density that can absorb the Cauchy jump.

This is the only surviving local crossing mechanism.

---

## 10. Formal Mellin indicial equation

To identify the endpoint singular species, consider the singular model

\`\`\`math
\frac12
\int_0^\delta
\frac{f(r)}{s+r}\,dr
+
\varepsilon_u a_0 f(s)
=
\text{analytic}.
\`\`\`

Insert the formal nonanalytic mode

\`\`\`math
f(s)
\sim
s^\beta.
\`\`\`

The nonanalytic Mellin coefficient of the Stieltjes term is

\`\`\`math
-\frac{\pi}{2\sin(\pi\beta)}
s^\beta.
\`\`\`

Therefore the formal indicial equation is

\`\`\`math
\boxed{
-\frac{\pi}{2\sin(\pi\beta)}
+
\varepsilon_u a_0
=
0,
}
\`\`\`

or

\`\`\`math
\boxed{
\sin(\pi\beta)
=
\frac{\pi}{2\varepsilon_u a_0}.
}
\`\`\`

For prime powers,

\`\`\`math
0<a_0<1,
\`\`\`

so

\`\`\`math
\left|
\frac{\pi}{2a_0}
\right|
>
1.
\`\`\`

Thus the formal roots are nonreal.

If

\`\`\`math
\varepsilon_u=+1,
\`\`\`

the first \(L^2\)-compatible branch is of the species

\`\`\`math
\beta
=
\frac12
\pm
i\tau
\`\`\`

modulo even integers.

If

\`\`\`math
\varepsilon_u=-1,
\`\`\`

the branch with real part \(-1/2\) is borderline non-\(L^2\), so the first
\(L^2\)-compatible representative is of the species

\`\`\`math
\beta
=
\frac32
\pm
i\tau.
\`\`\`

Here formally

\`\`\`math
\cosh(\pi\tau)
=
\frac{\pi}{2a_0}.
\`\`\`

These modes are compatible with interior analyticity for every \(s>0\) while
remaining nonanalytic at the endpoint.

### Scope

RPB-45 does **not** promote a full Mellin asymptotic theorem from this formal
indicial calculation.

The exact threshold equation of Section 9 is proved.

The realization/classification of its \(L^2\) endpoint germs is the next
problem.

---

## 11. Compatibility with the core domain

The threshold model does not contradict the screw-core regularity.

For a formal source mode

\`\`\`math
f(s)
\sim
s^\beta
\`\`\`

with

\`\`\`math
\Re\beta>\!-\frac12,
\`\`\`

we have

\`\`\`math
f\in L^2(0,\delta).
\`\`\`

Since

\`\`\`math
u=ih',
\`\`\`

the corresponding physical mode behaves after one integration like

\`\`\`math
h(c-s)
\sim
s^{\beta+1}.
\`\`\`

This is compatible with

\`\`\`math
h\in H_0^1(-c,c).
\`\`\`

Therefore core regularity alone does not eliminate the threshold Carleman
branch.

---

## 12. Relation to RPB-44

RPB-44 proved that once a strict collar has crossed the base endpoint, every
later prime-endpoint activation is uncrossable.

RPB-45 now shows that the base endpoint itself can be crossed only at a
prime-power threshold.

Thus, if strict persistence exists at all, the geometry is completely
quantized:

\`\`\`math
\boxed{
2c=\log n_0
}
\`\`\`

at the starting edge, and then

\`\`\`math
\boxed{
a_{\max}
=
\min
\left\{
c+\log2,\,
\log n_+(c)-c
\right\}
}
\`\`\`

by RPB-44.

The only remaining issue is whether the threshold endpoint equation of
Section 9 actually admits a nonzero source germ compatible with the global
neutral mode.

---

## 13. Consequence for the neutral null-extension interface

The broad interface

\`\`\`text
AZ-FIN-WEIL-NULL-EXTENSION
\`\`\`

has now collapsed to a discrete threshold problem.

Away from prime-power thresholds:

\`\`\`math
\boxed{
\text{strict null extension is impossible}.
}
\`\`\`

At a threshold:

\`\`\`math
\boxed{
\text{strict null extension}
\Longrightarrow
\text{threshold Carleman--Stieltjes endpoint compatibility}.
}
\`\`\`

So the original support-rigidity question is no longer a continuum of support
values.

It is a family of local boundary integral equations indexed by prime powers.

---

## 14. RPB-45 determination

\`\`\`math
\boxed{
\textbf{RPB-45 — THE BASE }t=0\textbf{ SCREW SINGULARITY EXCLUDES ALL NONTHRESHOLD STRICT COLLARS; ONLY PRIME-POWER THRESHOLD CARLEMAN MATCHING SURVIVES.}
}
\`\`\`

Exact nonthreshold theorem:

\`\`\`math
\boxed{
2c\notin\{\log(p^m)\}
\Longrightarrow
\text{no strict neutral collar}.
}
\`\`\`

Exact threshold equation:

\`\`\`math
\boxed{
\frac12
\int_0^{2c}
\frac{f(r)}{s+r}\,dr
+
\varepsilon_u
\frac{\Lambda(n_0)}{\sqrt{n_0}}
f(s)
+
A(s)
=
0,
}
\`\`\`

with

\`\`\`math
2c=\log n_0,
\qquad
A\in C^\omega.
\`\`\`

Formal Mellin symbol:

\`\`\`math
\boxed{
\sin(\pi\beta)
=
\frac{\pi}{
2\varepsilon_u
\Lambda(n_0)/\sqrt{n_0}
}.
}
\`\`\`

Next cursor:

\`\`\`text
RPB-46 / THRESHOLD CARLEMAN-MELLIN ENDPOINT REALIZATION
\`\`\`

The next pass should analyze the exact singular integral equation at a
prime-power threshold:

1. identify the Mellin/Carleman operator on the endpoint \(L^2\) germ;
2. determine its point/continuous spectrum in the two parity sectors;
3. prove or disprove realization of the formal exponents above;
4. test compatibility with the global interior-neutral equation and the
   zero-mean/source normalization;
5. decide whether any threshold support can actually admit strict neutral
   persistence.
