# SZ-CROSS-COLLAR-2 — First nonzero collar jet

**Date:** 2026-09-25  
**Branch:** `sz-cross-collar`  
**Status:** PRIVATE LAB / INTERNAL DERIVATION  
**Depends on:** `SZ_CROSS_COLLAR_0_20260925.md`,
`SZ_CROSS_COLLAR_1_20260925.md`

## 0. Objective

Study the small-collar behavior

```math
\Delta_{c,c+\varepsilon}(u)
\qquad
(\varepsilon\downarrow0)
```

for a nonzero endpoint source

```math
u\in\ker G_c.
```

The first question is whether the cross-collar residual leaks at first order.
The second is what extra information forces a nonzero leading term.

---

## 1. Source regularity supplied by Suzuki

Suzuki, Section 2.1, records that the screw kernel (g) is continuous and its
first derivative is piecewise continuous apart from the discrete singular set;
the local expansion

```math
g(t)
=
\frac12|t|\log|t|
+
A|t|
+
\text{prime hinges}
+
r(t)
```

shows in particular that

```math
g'\in L^2_{\mathrm{loc}}(\mathbb R).
```

For compactly supported

```math
u\in L^2(-c,c),
```

define

```math
F_u(x)
=
\int_{-c}^{c}g(x-y)u(y)\,dy.
```

On any bounded (x)-interval, the derivative is represented by the local
(L^2)-convolution

```math
F_u'(x)
=
\int_{-c}^{c}g'(x-y)u(y)\,dy.
```

Translation continuity in (L^2) therefore gives

```math
\boxed{
F_u\in C^1_{\mathrm{loc}}(\mathbb R).
}
```

This slightly sharpens the (H^1) regularity explicitly recorded for the
projected operator output in Suzuki.

---

## 2. Native collar flatness

Assume

```math
u\in\ker G_c.
```

Then

```math
F_u(x)=C_u
\qquad
(|x|<c).
```

Since (F_u\in C^1),

```math
F_u'(c)=F_u'(-c)=0.
```

Hence, on the right collar,

```math
r_+(\delta)
:=
F_u(c+\delta)-C_u
=
\int_0^\delta F_u'(c+s)\,ds,
```

and similarly on the left.

Because (F_u') is continuous and vanishes at both endpoint traces,

```math
\sup_{0<s<\varepsilon}|F_u'(c+s)|\to0,
```

so

```math
\boxed{
\|r_{c,c+\varepsilon;u}\|_{L^2(\mathcal C)}
=
o(\varepsilon^{3/2}).
}
```

The mean-removal term in the definition of (Delta) cannot increase this
order. Therefore

```math
\boxed{
\Delta_{c,c+\varepsilon}(u)
=
o(\varepsilon^{3/2}).
}
```

Thus a neutral endpoint mode is automatically **first-order clamped** to the
support boundary in Suzuki coordinates.

A nonzero cross-collar coupling, if present, begins beyond the ordinary
first-order collar jet.

---

## 3. Exterior second-derivative equation

Suzuki gives, distributionally,

```math
-g''(t)
=
-\frac12\operatorname{Pf}\frac1{|t|}
-(2A+1)\delta(t)
-
\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}
\bigl(
\delta(t-\log n)+\delta(t+\log n)
\bigr)
-r''(t).
```

For

```math
x=c+\delta>c,
```

the local delta term does not meet the support of (u), and
(x-y>0) for every (y\in[-c,c]). Hence the singular principal-value term
becomes the ordinary exterior Cauchy/Stieltjes transform.

In distributions on the right collar,

```math
\boxed{
F_u''(x)
=
\frac12\int_{-c}^{c}\frac{u(y)}{x-y}\,dy
+
\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\,
u(x-\log n)
+
\mathcal R_u(x),
}
```

where (u) is zero-extended and (mathcal R_u) denotes the remaining
archimedean convolution.

The (u(x+\log n)) terms vanish for (x>c).

On any fixed compact collar only finitely many prime-power translates can meet
the old support.

This identity is the rigorous distributional target for the collar; pointwise
interpretation of the translated terms requires the corresponding regularity
of (u).

---

## 4. Conditional boundary-trace asymptotic

Assume now, additionally, that (u) has a continuous right endpoint trace

```math
u(c-)=u_c.
```

Assume also enough local regularity at the finitely many translated sampling
points for the prime-shift terms to remain bounded as
(delta\downarrow0).

Then the exterior Cauchy term satisfies

```math
\int_{-c}^{c}
\frac{u(y)}{c+\delta-y}\,dy
=
u_c\log\frac1\delta
+
O(1).
```

The finite prime-shift contribution and the smooth archimedean remainder are
only (O(1)) at this scale. Therefore

```math
F_u''(c+\delta)
=
\frac{u_c}{2}\log\frac1\delta
+
O(1).
```

Using

```math
F_u(c)=C_u,
\qquad
F_u'(c)=0,
```

two integrations give

```math
\boxed{
F_u(c+\delta)-C_u
=
\frac{u_c}{4}
\delta^2\log\frac1\delta
+
O(\delta^2).
}
```

Thus

```math
u(c-)\ne0
```

forces immediate nonzero right-collar leakage.

The analogous left-boundary statement holds with the endpoint trace
(u(-c+)).

---

## 5. Necessary clamped-boundary condition

Under the trace hypotheses above, exact null persistence to any nontrivial
strict collar requires

```math
\boxed{
u(c-)=u(-c+)=0.
}
```

If

```math
u=Dk=ik'
```

with enough regularity for boundary traces, while

```math
k\in H_0^1(-c,c),
```

then (k(\pm c)=0) already.

Collar persistence additionally forces

```math
\boxed{
k'(c-)=k'(-c+)=0.
}
```

So a persistent regular neutral mode must satisfy an overdetermined
**clamped endpoint condition**:

```math
\boxed{
k(\pm c)=0,
\qquad
k'(\pm c)=0.
}
```

This condition is not available at the native logarithmic-form regularity and
must not be imported into the public neutral theorem.

---

## 6. Conditional leading collar norm

If at least one endpoint trace is nonzero, the mean-removal term is one order
smaller than the collar (L^2) mass, and the two sides give

```math
\Delta_{c,c+\varepsilon}(u)^2
=
\frac{
|u(c-)|^2+|u(-c+)|^2
}{80}
\,
\varepsilon^5
\log^2\frac1\varepsilon
+
o\!\left(
\varepsilon^5\log^2\frac1\varepsilon
\right).
```

Equivalently,

```math
\boxed{
\Delta_{c,c+\varepsilon}(u)
\sim
\frac{1}{4\sqrt5}
\sqrt{
|u(c-)|^2+|u(-c+)|^2
}
\,
\varepsilon^{5/2}
\log\frac1\varepsilon.
}
```

This is a **conditional logarithmic collar jet**, not a theorem at native
(L^2) source regularity.

Combined with SZ-CROSS-COLLAR-1, any nonzero endpoint trace forces

```math
\lambda_{c+\varepsilon}<0
```

for every sufficiently small strict enlargement.

---

## 7. What remains

The actual hard case has now narrowed again.

At native regularity we know:

```math
F_u\in C^1,
\qquad
F_u=C_u\text{ on }[-c,c],
```

but (u) need not possess boundary traces.

Therefore the remaining seam is not the ordinary first collar jet. It is:

```math
\boxed{
\text{Can }u\in\ker G_c
\text{ be sufficiently rough at the support edge to avoid the logarithmic
Cauchy leakage mechanism?}
}
```

Equivalently: can the first-kind integral equation (G_cu=0) support a
nonzero kernel vector with no usable endpoint trace while its screw potential
remains constant on a strict larger interval?

---

## 8. Next cursor

```text
SZ-CROSS-COLLAR-3 / ENDPOINT REGULARITY BOOTSTRAP
```

Targets:

1. determine the strongest endpoint regularity forced by (G_cu=0);
2. test whether the first-kind equation gives any trace information despite
   the zero eigenvalue;
3. if no regularity bootstrap is available, formulate a trace-free version of
   the Cauchy-leakage argument using boundary averages or Hardy/Stieltjes
   transforms;
4. keep generic radii and prime-power threshold radii separate.

**Do not promote to the public repository.**
