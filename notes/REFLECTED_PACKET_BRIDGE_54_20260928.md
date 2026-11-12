# RPB-54 — Noncore logarithmic boundary-layer exterior leakage test

**Date:** 2026-09-28  
**Branch:** research/reflected-packet-bridge  
**Status:** **PASS CONDITIONALLY ON AN OPTIMAL LOGARITHMIC BOUNDARY TRACE / NONZERO \(\ell^{1/2}\) AMPLITUDE CREATES AN UNCANCELLABLE \(\sqrt{\log(1/s)}\) EXTERIOR LEAK / NONTHRESHOLD CASE NEEDS ONE ENDPOINT TRACE ONLY / THRESHOLD EQUALITY PRIME IS LOWER ORDER UNDER TWO-SIDED OPTIMAL TRACE CONTROL / RESIDUE = LOG-FLAT OR BOUNDARY-UNTYPED NONCORE MODES**  
**Dependencies:** RPB-31, RPB-43, RPB-49, RPB-53; RPB-EXT-A7 Chen--Weth logarithmic-Laplacian integral representation.  
**Promotion status:** none.

## 0. Objective

RPB-53 showed that a Friedrichs zero mode may carry the generic logarithmic
boundary species

~~~math
h(c-r)
\sim
b_+\,
\ell^{1/2}(r),
\qquad
\ell(r)
=
\frac1{\log(1/r)}.
~~~

RPB-54 asks whether a nonzero coefficient \(b_+\) itself obstructs strict
null extension.

It does.

The key point is that the logarithmic Laplacian is nonlocal across the support
boundary.  Just outside the old support, the zero extension produces a
singular integral of the boundary layer.  For the optimal
\(\ell^{1/2}\)-profile, this integral grows like

~~~math
\sqrt{\log(1/s)}.
~~~

The remaining actual-Weil terms are bounded or strictly smaller in endpoint
order and therefore cannot cancel it.

---

## 1. Exterior logarithmic-Laplacian formula

Let

~~~math
\widetilde h
=
0
\qquad
\text{on }
\mathbb R\setminus[-c,c].
~~~

Chen--Weth give, in dimension one,

~~~math
L_\Delta u(x)
=
\int_{\mathbb R}
\frac{
u(x)\mathbf 1_{|x-y|<1}
-
u(y)
}{
|x-y|
}
\,dy
+
\rho_1u(x),
~~~

because the dimensional constant is

~~~math
c_1
=
\pi^{-1/2}\Gamma(1/2)
=
1.
~~~

For

~~~math
x=c+s,
\qquad
s>0,
~~~

we have

~~~math
\widetilde h(c+s)=0.
~~~

Hence the formula simplifies exactly to

~~~math
\boxed{
L_\Delta\widetilde h(c+s)
=
-
\int_{-c}^{c}
\frac{h(y)}{c+s-y}\,dy.
}
~~~

No principal value is needed outside the support.

---

## 2. Separate the right endpoint

Fix a small

~~~math
0<\delta<\min(1,2c).
~~~

Put

~~~math
y=c-r.
~~~

Then

~~~math
L_\Delta\widetilde h(c+s)
=
-
\int_0^\delta
\frac{h(c-r)}{s+r}\,dr
+
R_{\rm far}(s),
~~~

where

~~~math
R_{\rm far}(s)
=
-
\int_{-c}^{c-\delta}
\frac{h(y)}{c+s-y}\,dy.
~~~

Since the far denominator is bounded below by \(\delta\) and
\(h\in L^2(-c,c)\subset L^1(-c,c)\),

~~~math
\boxed{
R_{\rm far}(s)=O(1)
\qquad
(s\downarrow0).
}
~~~

Thus the entire unbounded exterior behavior is owned by the right endpoint.

---

## 3. Model boundary integral

Define

~~~math
J(s)
=
\int_0^\delta
\frac{dr}{
(s+r)\sqrt{\log(1/r)}
}.
~~~

Split at \(r=s\).

For \(0<r<s\),

~~~math
\int_0^s
\frac{dr}{
(s+r)\sqrt{\log(1/r)}
}
=
O\!\left(
\frac1{\sqrt{\log(1/s)}}
\right).
~~~

For \(s<r<\delta\),

~~~math
\frac1{s+r}
=
\frac1r
+
\left(
\frac1{s+r}-\frac1r
\right),
~~~

and the difference contributes

~~~math
O\!\left(
\frac1{\sqrt{\log(1/s)}}
\right)
+
O(1).
~~~

The principal piece is explicit:

~~~math
\begin{aligned}
\int_s^\delta
\frac{dr}{
r\sqrt{\log(1/r)}
}
&=
2
\left(
\sqrt{\log(1/s)}
-
\sqrt{\log(1/\delta)}
\right).
\end{aligned}
~~~

Therefore

~~~math
\boxed{
J(s)
=
2\sqrt{\log(1/s)}
+
O(1).
}
~~~

The \(O(1)\) precision is more than enough for the separation argument below.

---

## 4. Stability under an \(o(\ell^{1/2})\) remainder

Assume the actual mode has the right boundary expansion

~~~math
\boxed{
h(c-r)
=
b_+
\frac1{\sqrt{\log(1/r)}}
+
o\!\left(
\frac1{\sqrt{\log(1/r)}}
\right),
\qquad
b_+\ne0.
}
~~~

Write

~~~math
h(c-r)
=
b_+\ell^{1/2}(r)
+
q(r),
~~~

with

~~~math
q(r)
=
o(\ell^{1/2}(r)).
~~~

For every \(\varepsilon>0\), choose \(\delta_\varepsilon\) so that

~~~math
|q(r)|
\le
\varepsilon\ell^{1/2}(r)
\qquad
(0<r<\delta_\varepsilon).
~~~

Then the near contribution of \(q\) is bounded by

~~~math
\varepsilon J(s),
~~~

while the part on
\([\delta_\varepsilon,\delta]\) is \(O(1)\).

Letting \(\varepsilon\downarrow0\) gives

~~~math
\boxed{
\int_0^\delta
\frac{q(r)}{s+r}\,dr
=
o\!\left(
\sqrt{\log(1/s)}
\right).
}
~~~

Consequently,

~~~math
\boxed{
L_\Delta\widetilde h(c+s)
=
-2b_+\sqrt{\log(1/s)}
+
o\!\left(
\sqrt{\log(1/s)}
\right).
}
~~~

This is the exact noncore logarithmic-layer exterior leakage.

---

## 5. Transfer to the actual archimedean Weil operator

RPB-49 gives

~~~math
\mathcal A_\infty
=
\frac12L_\Delta
-
\log(2\pi)I
+
\mathcal S_{-2},
~~~

where \(\mathcal S_{-2}\) is two orders smoother at high frequency.

Outside the old support,

~~~math
I\widetilde h(c+s)=0.
~~~

Moreover,

~~~math
\mathcal S_{-2}:
L^2(\mathbb R)
\longrightarrow
H^2_{\rm loc}(\mathbb R),
~~~

after absorbing the smooth low-frequency part into the smoothing remainder.

In one dimension this gives a continuous, locally bounded output.

Therefore

~~~math
\boxed{
\mathcal A_\infty\widetilde h(c+s)
=
-b_+\sqrt{\log(1/s)}
+
o\!\left(
\sqrt{\log(1/s)}
\right).
}
~~~

The coefficient is nonzero whenever \(b_+\ne0\).

---

## 6. Interior analyticity extends beyond the screw core

RPB-43 stated interior analyticity for a screw-core neutral mode, but the
analytic-ellipticity proof uses only:

1. compact support;
2. the scalar interior equation
   \[
   A_ch=0;
   \]
3. analytic ellipticity of the full compact-window scalar symbol at high
   frequency;
4. analytic finite-rank pole range.

It does not use \(Dh\in L^2\).

Therefore the same argument applies to every Friedrichs zero mode

~~~math
h\in\ker A_c.
~~~

Hence

~~~math
\boxed{
h\in C^\omega(-c,c).
}
~~~

This extension is important because active prime translations sample fixed
interior points as the exterior edge is approached.

---

## 7. Active prime translations are bounded away from thresholds

Let

~~~math
\ell_n=\log n<2c
~~~

be an active prime-power delay.

At

~~~math
x=c+s,
~~~

the outward translate satisfies

~~~math
\widetilde h(c+s+\ell_n)=0.
~~~

The inward translate is

~~~math
\widetilde h(c+s-\ell_n).
~~~

For fixed

~~~math
0<\ell_n<2c,
~~~

and sufficiently small \(s>0\),

~~~math
c+s-\ell_n
~~~

lies a fixed positive distance inside \((-c,c)\).

By Section 6,

~~~math
\boxed{
\widetilde h(c+s-\ell_n)
=
O(1)
}
~~~

and in fact is analytic in \(s\).

Since only finitely many delays are active,

~~~math
\boxed{
\text{the entire strict-endpoint prime sum is }O(1)
}
~~~

near \(x=c+\).

Thus away from an equality threshold no arithmetic translation can cancel the
\(\sqrt{\log(1/s)}\) archimedean leakage.

---

## 8. Pole/evaluation terms are bounded

The pole/evaluation contribution has finite-dimensional range spanned by fixed
analytic exponential functions.

Hence

~~~math
\boxed{
\mathcal R_{\rm pole}\widetilde h(c+s)
=
O(1).
}
~~~

Any fixed finite selected correction, when present in a laboratory
decomposition, likewise has finite-dimensional smooth range and is \(O(1)\).

These terms cannot cancel the exterior logarithmic divergence.

---

## 9. Nonthreshold exterior exclusion

Suppose

~~~math
2c
\notin
\{\log(p^m)\}.
~~~

For sufficiently small strict right enlargement, the right-limit operator has
the same active prime set as the endpoint operator.

Combining Sections 5, 7, and 8 gives

~~~math
\boxed{
\mathcal W_c^{\rm ext}\widetilde h(c+s)
=
-b_+\sqrt{\log(1/s)}
+
o\!\left(
\sqrt{\log(1/s)}
\right).
}
~~~

Therefore

~~~math
\boxed{
b_+\ne0
\Longrightarrow
\mathcal W_c^{\rm ext}\widetilde h
\not\equiv0
\text{ on every right exterior collar.}
}
~~~

So strict null extension is impossible.

This proves the nonthreshold noncore exclusion from a single nonzero endpoint
amplitude.

---

## 10. Equality-threshold correction

Now suppose

~~~math
2c
=
\log n_0.
~~~

The strict right-limit operator contains the equality-threshold translation
absent from the endpoint strict-\(<\) operator.

At the right exterior point \(x=c+s\), its nonzero translated sample is

~~~math
\widetilde h(c+s-2c)
=
h(-c+s).
~~~

Assume the mode belongs to the **two-sided optimal logarithmic boundary
class**, namely

~~~math
h(c-r)
=
b_+\ell^{1/2}(r)
+
o(\ell^{1/2}(r)),
~~~

and

~~~math
h(-c+r)
=
b_-\ell^{1/2}(r)
+
o(\ell^{1/2}(r)).
~~~

Then the equality-threshold prime contribution has size only

~~~math
O(\ell^{1/2}(s))
=
O\!\left(
\frac1{\sqrt{\log(1/s)}}
\right).
~~~

This is smaller by an entire factor of

~~~math
\log(1/s)
~~~

than the archimedean exterior leakage

~~~math
\sqrt{\log(1/s)}.
~~~

Therefore

~~~math
\boxed{
\mathcal W_{c+}^{\rm ext}\widetilde h(c+s)
=
-b_+\sqrt{\log(1/s)}
+
o\!\left(
\sqrt{\log(1/s)}
\right)
}
~~~

also at a prime-power threshold.

The same argument applies at the left endpoint using \(b_-\).

---

## 11. Two-sided amplitude criterion

For a Friedrichs zero mode admitting the two-sided optimal expansions, define

~~~math
\mathbf b(h)
=
(b_+(h),b_-(h)).
~~~

If

~~~math
\mathbf b(h)\ne(0,0),
~~~

choose an endpoint with nonzero coefficient.

Sections 9 and 10 give, uniformly across the threshold convention,

~~~math
\boxed{
\mathbf b(h)\ne0
\Longrightarrow
\text{strict null extension is impossible}.
}
~~~

Thus every amplitude-bearing noncore logarithmic mode is excluded from the
canonical null-extension branch.

---

## 12. Relation to the core route

The screw-core route and the log-layer route are complementary.

### Core mode

If

~~~math
0\ne h\in
\ker A_c\cap H_0^1(-c,c),
~~~

then RPB-32 identifies

~~~math
Dh\in\ker_{L^2}G_c,
~~~

and RPB-34--49 exclude strict null extension.

### Noncore amplitude-bearing mode

If \(h\) has a nonzero optimal logarithmic boundary amplitude, RPB-54 excludes
strict null extension directly from the exterior archimedean singularity.

Thus the unresolved modes are no longer "all noncore modes."

They are the much thinner residual class for which the leading logarithmic
boundary amplitude is unavailable or vanishes.

---

## 13. Residual class

Define, where the two-sided optimal trace exists,

~~~math
\mathcal N_c^{\rm flat}
=
\left\{
h\in\ker A_c:
b_+(h)=b_-(h)=0
\right\}.
~~~

These are the **log-flat Friedrichs zero modes**.

There is also a currently untyped residue

~~~math
\mathcal N_c^{\rm untyped},
~~~

consisting of zero modes for which the current theory has not established a
two-sided classical \(\ell^{1/2}\) trace coefficient.

RPB-54 therefore reduces the unresolved canonical interface to

~~~math
\boxed{
\mathcal N_c^{\rm flat}
\cup
\mathcal N_c^{\rm untyped},
}
~~~

after removing:

- all core modes by RPB-34--49;
- all optimal-trace modes with nonzero boundary amplitude by RPB-54.

No claim is made yet that
\(\mathcal N_c^{\rm untyped}\) is nonempty.

---

## 14. RPB-54 determination

~~~math
\boxed{
\textbf{RPB-54 — A NONZERO OPTIMAL LOGARITHMIC BOUNDARY AMPLITUDE FORCES AN UNCANCELLABLE \(\sqrt{\log(1/s)}\) EXTERIOR WEIL LEAK.}
}
~~~

Exact right-edge asymptotic:

~~~math
\boxed{
h(c-r)
=
b_+\ell^{1/2}(r)
+
o(\ell^{1/2}(r))
\Longrightarrow
\mathcal A_\infty\widetilde h(c+s)
=
-b_+\sqrt{\log(1/s)}
+
o(\sqrt{\log(1/s)}).
}
~~~

Away from thresholds, every other actual-Weil term is \(O(1)\).

At an equality threshold, under the two-sided optimal logarithmic trace,
the new equality-prime term is only

~~~math
O(\ell^{1/2}(s)).
~~~

Therefore any nonzero endpoint amplitude excludes strict null extension.

Current branch-local partition:

~~~text
CORE ZERO MODE:
    excluded by RPB-34–49

NONCORE MODE WITH NONZERO OPTIMAL LOG AMPLITUDE:
    excluded by RPB-54

LOG-FLAT OR BOUNDARY-UNTYPED NONCORE ZERO MODE:
    OPEN
~~~

## Next cursor

~~~text
RPB-55 / OPTIMAL LOG-TRACE EXISTENCE AND FLAT-RESIDUE TEST
~~~

The next pass should determine whether every actual Friedrichs zero mode admits
a two-sided optimal logarithmic trace

~~~math
h(\pm c\mp r)
=
b_\pm(h)\ell^{1/2}(r)
+
o(\ell^{1/2}(r)).
~~~

If yes, the untyped residue disappears and the problem reduces to log-flat
zero modes.  Then test whether simultaneous vanishing

~~~math
b_+(h)=b_-(h)=0
~~~

forces screw-core membership, triviality, or a strictly smaller next boundary
species.
