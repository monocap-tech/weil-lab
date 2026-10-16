# RPB-56 — Cumulative boundary-mass leakage and cancellation test

**Date:** 2026-09-28  
**Branch:** research/reflected-packet-bridge  
**Status:** **PASS AS EXACT RETYPING / EXTERIOR STIELTJES TRANSFORM IS THE TRUE BOUNDARY LEAKAGE OBJECT / CUMULATIVE MASS IS EQUIVALENT MODULO \(O(1)\) FOR BOUNDED BOUNDARY GERMS / NONTHRESHOLD PERSISTENCE FORCES BOUNDED STIELTJES DATA / THRESHOLD PERSISTENCE GIVES A TWO-ENDPOINT STIELTJES COUPLING / BOUNDED STIELTJES DATA DO NOT BY THEMSELVES FORCE CORE REGULARITY**  
**Dependencies:** RPB-31, RPB-43, RPB-54, RPB-55; RPB-EXT-A7 Chen--Weth logarithmic-Laplacian integral representation.  
**Promotion status:** none.

## 0. Objective

RPB-55 proposed the cumulative boundary masses

~~~math
M_+(s;h)
=
\int_s^\delta
\frac{h(c-r)}r\,dr,
~~~

and

~~~math
M_-(s;h)
=
\int_s^\delta
\frac{h(-c+r)}r\,dr
~~~

as a more robust replacement for a classical logarithmic trace coefficient.

RPB-56 asks whether \(M_\pm\) are the exact objects seen by the exterior Weil
operator and whether bounded cumulative mass forces any stronger regularity.

The answer is:

1. the exact exterior object is a Stieltjes transform;
2. cumulative mass differs from it by only \(O(1)\) when the boundary germ is
   bounded;
3. without a boundary boundedness hypothesis, cumulative mass is only a proxy;
4. bounded Stieltjes data do not, by boundary geometry alone, imply
   \(H_0^1\) core regularity.

---

## 1. Exact right and left boundary Stieltjes transforms

Let

~~~math
f_+(r)
=
h(c-r),
\qquad
f_-(r)
=
h(-c+r),
\qquad
0<r<\delta.
~~~

Define

~~~math
\boxed{
\Sigma_+(s;h)
=
\int_0^\delta
\frac{f_+(r)}{s+r}\,dr
}
~~~

and

~~~math
\boxed{
\Sigma_-(s;h)
=
\int_0^\delta
\frac{f_-(r)}{s+r}\,dr.
}
~~~

RPB-54's exact exterior logarithmic-Laplacian formula gives

~~~math
L_\Delta\widetilde h(c+s)
=
-\Sigma_+(s;h)
+
R_+(s),
~~~

and

~~~math
L_\Delta\widetilde h(-c-s)
=
-\Sigma_-(s;h)
+
R_-(s),
~~~

where the far-support remainders satisfy

~~~math
R_\pm(s)=O(1).
~~~

Therefore \(\Sigma_\pm\), not \(M_\pm\), are the exact near-boundary leakage
functionals.

---

## 2. Logarithmic-coordinate representation

Put

~~~math
s=e^{-T},
\qquad
r=e^{-t},
~~~

and define

~~~math
H_+(t)
=
h(c-e^{-t}).
~~~

Then

~~~math
\boxed{
\Sigma_+(e^{-T};h)
=
\int_{t_0}^{\infty}
\frac{
H_+(t)
}{
1+e^{t-T}
}\,dt,
}
~~~

where

~~~math
t_0=\log(1/\delta).
~~~

Meanwhile,

~~~math
\boxed{
M_+(e^{-T};h)
=
\int_{t_0}^{T}
H_+(t)\,dt.
}
~~~

Thus the Stieltjes transform is a Fermi/logistic smoothing of the sharp
primitive.

The kernel

~~~math
\frac1{1+e^{t-T}}
~~~

is a smoothed version of the step function
\(\mathbf1_{t<T}\).

This explains why \(M_+\) gives the correct leading behavior for slowly varying
logarithmic boundary species, but also why it need not be exact for arbitrary
oscillatory or unbounded germs.

---

## 3. Bounded germs: cumulative mass and Stieltjes leakage differ by \(O(1)\)

Assume

~~~math
|f_+(r)|
\le
C
\qquad
(0<r<\delta).
~~~

Then

~~~math
\Sigma_+(s)-M_+(s)
=
\int_0^s
\frac{f_+(r)}{s+r}\,dr
+
\int_s^\delta
f_+(r)
\left(
\frac1{s+r}
-
\frac1r
\right)\,dr.
~~~

The first term satisfies

~~~math
\left|
\int_0^s
\frac{f_+(r)}{s+r}\,dr
\right|
\le
C\log2.
~~~

For the second term,

~~~math
\begin{aligned}
s\int_s^\delta
\frac{dr}{
r(s+r)
}
&=
\log\frac{2\delta}{s+\delta}
\\
&\le
\log2.
\end{aligned}
~~~

Hence

~~~math
\boxed{
|\Sigma_+(s)-M_+(s)|
\le
2C\log2.
}
~~~

The same estimate holds at the left endpoint.

Therefore, for bounded boundary germs,

~~~math
\boxed{
|M_\pm(s)|\to\infty
\Longrightarrow
|\Sigma_\pm(s)|\to\infty
}
~~~

provided the cumulative divergence is not itself canceled by the bounded
\(O(1)\) difference.

In particular all of the bounded optimal-log classes considered in RPB-54
and RPB-55 may use \(M_\pm\) or \(\Sigma_\pm\) interchangeably at the level of
unbounded leakage.

---

## 4. Recovery of the known logarithmic examples

If

~~~math
h(c-r)
\sim
b\ell^{1/2}(r),
~~~

then

~~~math
M_+(s)
\sim
2b\sqrt{\log(1/s)},
~~~

and Section 3 recovers

~~~math
\Sigma_+(s)
\sim
2b\sqrt{\log(1/s)}.
~~~

If

~~~math
h(c-r)
\sim
\frac b{\log(1/r)},
~~~

then

~~~math
M_+(s)
\sim
b\log\log(1/s),
~~~

and therefore

~~~math
\boxed{
\Sigma_+(s)
=
b\log\log(1/s)
+
O(1).
}
~~~

So the exterior leakage mechanism extends strictly beyond the leading
\(\ell^{1/2}\) amplitude class.

---

## 5. Actual archimedean exterior output in terms of \(\Sigma_\pm\)

RPB-49 gives

~~~math
\mathcal A_\infty
=
\frac12L_\Delta
-
\log(2\pi)I
+
\mathcal S_{-2}.
~~~

Outside the support,

~~~math
I\widetilde h=0,
~~~

and the \(\mathcal S_{-2}\) output is locally bounded.

Hence

~~~math
\boxed{
\mathcal A_\infty\widetilde h(c+s)
=
-\frac12\Sigma_+(s;h)
+
O(1),
}
~~~

and similarly

~~~math
\boxed{
\mathcal A_\infty\widetilde h(-c-s)
=
-\frac12\Sigma_-(s;h)
+
O(1).
}
~~~

These formulas require no classical pointwise logarithmic trace coefficient.

---

## 6. Nonthreshold persistence forces bounded Stieltjes data

Assume

~~~math
2c
\notin
\{\log(p^m)\}.
~~~

For sufficiently small \(s>0\), every active prime translation at the right
exterior point samples either:

- outside the old support, where \(\widetilde h=0\); or
- a fixed interior point a positive distance from the endpoint.

By the RPB-43 interior analytic-ellipticity argument, the latter samples are
bounded and analytic in \(s\).

The pole/evaluation terms and smoother archimedean remainder are also bounded.

Therefore, if the zero extension satisfied the strict right-limit null
equation on an exterior collar, necessarily

~~~math
\boxed{
\Sigma_+(s;h)=O(1)
\qquad
(s\downarrow0).
}
~~~

Likewise,

~~~math
\boxed{
\Sigma_-(s;h)=O(1).
}
~~~

Consequently, at a nonthreshold support,

~~~math
\boxed{
|\Sigma_+(s;h)|\to\infty
\text{ or }
|\Sigma_-(s;h)|\to\infty
\Longrightarrow
\text{strict null extension is impossible}.
}
~~~

This is the coefficient-free exterior leakage theorem.

---

## 7. Threshold persistence gives a coupled Stieltjes boundary system

Now suppose

~~~math
2c
=
\log n_0.
~~~

Let

~~~math
a_0
=
\frac{\Lambda(n_0)}{\sqrt{n_0}}.
~~~

The strict right-limit operator activates the equality-threshold translation.

At the right exterior point \(x=c+s\), its only nonzero equality sample is

~~~math
h(-c+s).
~~~

At the left exterior point \(x=-c-s\), the corresponding sample is

~~~math
h(c-s).
~~~

Thus strict threshold persistence forces relations of the form

~~~math
\boxed{
\frac12\Sigma_+(s;h)
+
a_0h(-c+s)
=
O(1),
}
~~~

and

~~~math
\boxed{
\frac12\Sigma_-(s;h)
+
a_0h(c-s)
=
O(1),
}
~~~

where the \(O(1)\) terms collect the strict-endpoint active primes, pole range,
far-support logarithmic contribution, and smoother archimedean remainder.

The exact overall sign depends only on the fixed translation convention and is
irrelevant to the growth separation.

This is the **threshold Stieltjes coupling**.

---

## 8. Growth separation at a threshold

The threshold system immediately yields a coefficient-free exclusion criterion.

If

~~~math
\frac{
|\Sigma_+(s;h)|
}{
1+|h(-c+s)|
}
\to\infty,
~~~

then the first coupled equation cannot hold.

Likewise, if

~~~math
\frac{
|\Sigma_-(s;h)|
}{
1+|h(c-s)|
}
\to\infty,
~~~

the second cannot hold.

Therefore

~~~math
\boxed{
\max\left\{
\frac{|\Sigma_+(s;h)|}{1+|h(-c+s)|},
\frac{|\Sigma_-(s;h)|}{1+|h(c-s)|}
\right\}
\to\infty
}
~~~

excludes strict threshold persistence.

RPB-54's two-sided optimal-log result is a special case:

~~~math
|\Sigma_\pm(s)|
\asymp
\sqrt{\log(1/s)},
~~~

while

~~~math
|h(\mp c\pm s)|
=
O((\log(1/s))^{-1/2}).
~~~

The same criterion also handles slower logarithmic leakage whenever the
Stieltjes transform dominates the opposite endpoint sample.

---

## 9. Why unbounded cumulative mass is not the universal theorem without boundary control

The estimate in Section 3 used boundedness of the boundary germ.

For an arbitrary boundary-untyped Friedrichs mode, RPB-31 does not currently
supply

~~~math
h\in L^\infty.
~~~

Thus an unbounded \(M_\pm\) cannot be silently promoted to an unbounded
\(\Sigma_\pm\) without additional control on the local correction.

The exact coefficient-free theorem is therefore stated in terms of
\(\Sigma_\pm\).

Cumulative mass remains a useful asymptotic proxy on bounded boundary classes.

---

## 10. Bounded Stieltjes data do not imply core regularity

There is a simple local counterexample.

Let

~~~math
h(c-r)
=
\sin\!\left(
\log\frac1r
\right)
~~~

near the endpoint.

Then in logarithmic coordinates

~~~math
H(t)=\sin t.
~~~

The cumulative mass is

~~~math
M_+(e^{-T})
=
\int_{t_0}^{T}
\sin t\,dt,
~~~

which is bounded.

The Stieltjes transform is

~~~math
\Sigma_+(e^{-T})
=
\int_{t_0}^{\infty}
\frac{\sin t}{1+e^{t-T}}\,dt.
~~~

Since the logistic kernel differs from
\(\mathbf1_{t<T}\) by an \(L^1\)-localized function of \(t-T\), this expression
is also uniformly bounded in \(T\).

However,

~~~math
\partial_r
\sin\!\left(
\log\frac1r
\right)
=
-\frac{
\cos(\log(1/r))
}{r},
~~~

so

~~~math
\int_0^\delta
|\partial_r h(c-r)|^2\,dr
=
\infty.
~~~

Thus

~~~math
\boxed{
\text{bounded }M_+ \text{ and bounded }\Sigma_+
\not\Longrightarrow
H_0^1.
}
~~~

This is a boundary-geometry counterexample only; it is not claimed to satisfy
the actual Weil zero equation.

---

## 11. The interior zero equation is now the only remaining discriminator

The preceding counterexample is real analytic for every \(r>0\), so interior
analyticity alone does not exclude it.

What it fails is the logarithmic endpoint normal equation: for

~~~math
H(t)=\sin t,
~~~

~~~math
2tH(t)-\int^tH(w)\,dw
~~~

has size \(t\), not bounded endpoint residual size.

Therefore the bounded-Stieltjes residue must now be tested against the
**actual interior endpoint equation**, not against generic boundary regularity
or analyticity.

This is a strictly narrower problem than RPB-55.

---

## 12. RPB-56 determination

~~~math
\boxed{
\textbf{RPB-56 — THE EXTERIOR STIELTJES TRANSFORM, NOT CUMULATIVE MASS ALONE, IS THE EXACT BOUNDARY LEAKAGE OBJECT.}
}
~~~

Exact coefficient-free nonthreshold criterion:

~~~math
\boxed{
|\Sigma_+(s;h)|\to\infty
\text{ or }
|\Sigma_-(s;h)|\to\infty
\Longrightarrow
\text{no strict null extension}.
}
~~~

Threshold persistence must satisfy the coupled boundary system

~~~math
\boxed{
\frac12\Sigma_+(s)+a_0h(-c+s)=O(1),
\qquad
\frac12\Sigma_-(s)+a_0h(c-s)=O(1).
}
~~~

For bounded boundary germs,

~~~math
\boxed{
\Sigma_\pm(s)-M_\pm(s)=O(1),
}
~~~

so the cumulative-mass criterion is recovered.

The remaining residue is:

~~~text
NONTHRESHOLD:
    bounded right and left Stieltjes boundary transforms

THRESHOLD:
    coupled Stieltjes/opposite-endpoint cancellation class

NEITHER RESIDUE:
    known to imply screw-core regularity
~~~

## Next cursor

~~~text
RPB-57 / BOUNDED STIELTJES RESIDUE VS INTERIOR ENDPOINT EQUATION
~~~

The next pass should combine the exact interior logarithmic endpoint equation
with bounded Stieltjes data.

Priority order:

1. rewrite the interior right-endpoint equation in logarithmic coordinates for
   the broadest class justified by the Friedrichs operator domain;
2. determine whether bounded \(\Sigma_+\) forces the \(t^{-1/2}\) homogeneous
   coefficient to vanish;
3. classify the next admissible endpoint species and test its Stieltjes
   transform;
4. at thresholds, incorporate the coupled opposite-endpoint equations only
   after the one-endpoint interior classification is established.
