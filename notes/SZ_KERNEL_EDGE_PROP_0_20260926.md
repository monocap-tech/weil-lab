# SZ-KERNEL-EDGE-PROP-0 — Threshold-aware edge-delay normal form and zero-eigenvalue nonbootstrap

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Immediate parent residue:** SZ_KERNEL_ENDPOINT_QA_0_20260926.md  
**External comparison:** Chen–Hauer–Weth, arXiv:2312.15689;
Harrach–Lin–Weth, arXiv:2412.17775.  
**Suzuki pin:** Masatoshi Suzuki, arXiv:2606.09096v3,
especially §§2.1, 2.5, 8.1–8.5.

## 0. Objective

Work directly with the first-kind equation

~~~math
G_cu=0
~~~

and the threshold-aware exterior distribution equation to test whether
infinite collar flatness propagates to actual persistence.

The pass does not prove such propagation.

It produces instead:

1. an exact local decomposition of the prime-delay terms at each endpoint;
2. a sharp distinction between ordinary supports and prime-power thresholds;
3. a zero-eigenvalue nonbootstrap obstruction showing why the regularity of
   the kernel vector cannot be inferred from the smoothing property of \(G_c\);
4. a refined statement of the remaining edge-propagation theorem.

---

## 1. Exterior equation at the right edge

Fix

~~~math
0\ne u\in K_c:=\ker G_c.
~~~

Let

~~~math
F_u(x)
=
\int_{-c}^{c}g(x-y)u(y)\,dy.
~~~

On \((-c,c)\),

~~~math
F_u(x)=C_u.
~~~

For

~~~math
x=c+\delta,
\qquad
\delta>0,
~~~

the ratified distributional exterior identity is

~~~math
F_u''(c+\delta)
=
\frac12
\int_{-c}^{c}
\frac{u(y)}{c+\delta-y}\,dy
+
\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}
u(c+\delta-\log n)
+
\mathcal R_{+,u}(\delta),
~~~

with \(u\) zero-extended outside \((-c,c)\).

The term with \(u(c+\delta+\log n)\) vanishes identically on the right
exterior collar.

---

## 2. Which prime delays can actually occur?

A shifted sample

~~~math
u(c+\delta-\log n)
~~~

can be nonzero only if

~~~math
-c<c+\delta-\log n<c.
~~~

Equivalently,

~~~math
\boxed{
\delta<\log n<2c+\delta.
}
~~~

Choose a collar width

~~~math
0<\varepsilon_0<\log2.
~~~

Then the lower inequality is automatic for every prime power \(n\ge2\) and
every \(0<\delta<\varepsilon_0\).

Because the prime-power logarithms are discrete, shrink \(\varepsilon_0\) if
necessary so that no prime-power logarithm lies in

~~~math
(2c,2c+\varepsilon_0)
~~~

except a possible equality value

~~~math
\log n_0=2c.
~~~

Therefore, throughout this fixed collar, the right-edge prime term consists
exactly of

~~~math
\boxed{
\{\log n<2c\}
}
~~~

plus, when it exists, the single threshold prime power \(n_0\) with

~~~math
\log n_0=2c.
~~~

The threshold is unique by WD-T34.

---

## 3. Away from a threshold, every delay samples the strict interior

Assume

~~~math
\operatorname{primePowerThreshold}(c)=\varnothing.
~~~

The active set

~~~math
\mathcal P_c
=
\{n=p^m:\log n<2c\}
~~~

is finite.

Define the positive endpoint separation

~~~math
\eta_c
:=
\min_{n\in\mathcal P_c}
\min
\{
\log n,\,
2c-\log n
\}
>0,
~~~

with the obvious convention if \(\mathcal P_c\) is empty.

Take

~~~math
0<\varepsilon_0<\frac{\eta_c}{2}.
~~~

For every \(n\in\mathcal P_c\) and \(0<\delta<\varepsilon_0\),

~~~math
c+\delta-\log n
\in
[-c+\eta_c/2,\,
c-\eta_c/2].
~~~

Hence

~~~math
\boxed{
\text{all prime delays in the right collar sample one fixed compact
subinterval strictly inside }(-c,c).
}
~~~

Define the interior-delay germ

~~~math
\mathcal D_{+,c}u(\delta)
:=
\sum_{\log n<2c}
\frac{\Lambda(n)}{\sqrt n}
u(c-\log n+\delta).
~~~

Then, away from thresholds,

~~~math
\boxed{
F_u''(c+\delta)
=
\frac12\mathcal C_{+,c}u(\delta)
+
\mathcal D_{+,c}u(\delta)
+
\mathcal R_{+,u}(\delta),
}
~~~

where

~~~math
\mathcal C_{+,c}u(\delta)
=
\int_{-c}^{c}
\frac{u(y)}{c+\delta-y}\,dy.
~~~

There is no direct arithmetic coupling to the opposite endpoint.

---

## 4. At a threshold, exactly one delay couples the two edges

Assume now that

~~~math
2c=\log n_0
~~~

for a prime power \(n_0\).

The newly active strict-right term is

~~~math
\frac{\Lambda(n_0)}{\sqrt{n_0}}
u(c+\delta-2c)
=
\frac{\Lambda(n_0)}{\sqrt{n_0}}
u(-c+\delta).
~~~

Thus the right edge directly samples the left-edge germ.

Similarly, on the left exterior collar,

~~~math
x=-c-\delta,
~~~

the same threshold shift samples

~~~math
u(c-\delta).
~~~

Hence the threshold contribution has the exact two-edge form

~~~math
\boxed{
\frac{\Lambda(n_0)}{\sqrt{n_0}}
\begin{pmatrix}
u(-c+\delta)\\
u(c-\delta)
\end{pmatrix}.
}
~~~

All strictly active prime powers with

~~~math
\log n<2c
~~~

still sample compact interior points separated from both endpoints.

Therefore:

~~~text
nonthreshold endpoint:
    Stieltjes edge term + interior delays + regular remainder;

threshold endpoint:
    Stieltjes edge term + interior delays
    + one direct opposite-edge coupling + regular remainder.
~~~

There is no larger arithmetic edge graph on a sufficiently small collar.

---

## 5. The corresponding left-edge equation

Define

~~~math
\mathcal C_{-,c}u(\delta)
=
\int_{-c}^{c}
\frac{u(y)}{c+\delta+y}\,dy.
~~~

Up to the fixed signs supplied by the even screw kernel, the left exterior
equation has the analogous structure

~~~math
F_u''(-c-\delta)
=
\frac12\mathcal C_{-,c}u(\delta)
+
\mathcal D_{-,c}u(\delta)
+
\mathcal R_{-,u}(\delta),
~~~

where

~~~math
\mathcal D_{-,c}u(\delta)
=
\sum_{\log n<2c}
\frac{\Lambda(n)}{\sqrt n}
u(-c+\log n-\delta).
~~~

Away from threshold, every sample point again lies in one fixed compact
interior set.

At threshold the additional term is proportional to

~~~math
u(c-\delta).
~~~

So the two boundary equations form a \(2\times2\) edge system only at an exact
prime-power threshold.

---

## 6. Why the first-kind equation does not bootstrap the source

Suzuki proves that \(G_c\) is an integral operator with continuous kernel and
that

~~~math
G_c:
L_0^2(-c,c)\to H^1(-c,c).
~~~

For a nonzero eigenvalue

~~~math
G_cu=\lambda u,
\qquad
\lambda\ne0,
~~~

this immediately yields

~~~math
u=\lambda^{-1}G_cu\in H^1.
~~~

At the zero eigenvalue, however,

~~~math
G_cu=0
~~~

gives no representation of \(u\) in terms of the smoothed output.

Thus

~~~math
\boxed{
\text{the smoothing property of }G_c
\text{ provides no generic regularity bootstrap on }\ker G_c.
}
~~~

This is intrinsic to a homogeneous Fredholm equation of the first kind.

It explains why endpoint traces of \(u\) cannot be imported from the
regularity of \(G_cu\).

Suzuki explicitly emphasizes the first-kind Fredholm nature of the integral
equations associated with \(G_a\); the compact operator is analytically easier
than \(A_a\), but the zero-eigenspace remains a first-kind nullspace problem.

---

## 7. Abstract sharpness: even a smooth integral kernel may have a rough zero mode

The preceding point is not merely a limitation of one proof.

Let

~~~math
H=L^2(-c,c)
~~~

and choose any unit vector

~~~math
u_0\in H,
~~~

with no prescribed Sobolev regularity.

The smooth functions orthogonal to \(u_0\) are dense in \(u_0^\perp\):

given a smooth approximation to a vector in \(u_0^\perp\), subtract a fixed
smooth function having nonzero pairing with \(u_0\) to restore orthogonality.

Choose an orthonormal basis

~~~math
(e_j)_{j\ge1}
~~~

of \(u_0^\perp\) consisting of smooth functions.

Choose positive numbers

~~~math
\lambda_j\downarrow0
~~~

so rapidly that, for every derivative order \(r,s\),

~~~math
\sum_j
\lambda_j
\|e_j^{(r)}\|_\infty
\|e_j^{(s)}\|_\infty
<
\infty.
~~~

Then

~~~math
K(x,y)
=
\sum_{j\ge1}
\lambda_j
e_j(x)\overline{e_j(y)}
~~~

is a \(C^\infty\) Hermitian kernel, and the corresponding compact
self-adjoint integral operator satisfies

~~~math
Te_j=\lambda_je_j,
\qquad
Tu_0=0.
~~~

Therefore

~~~math
\boxed{
\ker T=\mathbb C u_0,
}
~~~

even though \(u_0\) may be arbitrarily rough.

So neither

- smoothness of the integral kernel;
- compactness;
- self-adjointness;
- nor finite-dimensionality of the zero eigenspace

can, by themselves, produce endpoint regularity of a zero mode.

Any bootstrap for the actual Weil kernel must use its special
difference/arithmetic structure.

---

## 8. Why ordinary logarithmic-Laplacian UCP is still insufficient

Chen–Hauer–Weth prove a weak unique-continuation theorem for the logarithmic
Laplacian of the following type:

~~~text
u = 0 on a nonempty open set
and
L_Δ u = 0 there
    => u = 0 globally.
~~~

Harrach–Lin–Weth use the corresponding nonlocal UCP in the logarithmic
Schrödinger inverse problem.

Our flat-but-leaking branch supplies no such open set.

The exterior residual is assumed only to be asymptotically flat as the collar
width shrinks; it is nonzero on every strict collar.

Moreover, the Weil edge equation contains finite translations in addition to
the logarithmic principal species.

Thus

~~~math
\boxed{
\text{open-set logarithmic UCP}
\text{ does not close the edge-flatness problem.}
}
~~~

This is a strict logical mismatch, not merely a missing citation.

---

## 9. What infinite flatness would have to cancel

Away from threshold, a superflat leaking mode would have to produce an
all-orders cancellation in the right-edge system

~~~math
\frac12\mathcal C_{+,c}u
+
\mathcal D_{+,c}u
+
\mathcal R_{+,u},
~~~

and simultaneously in the left-edge system

~~~math
\frac12\mathcal C_{-,c}u
+
\mathcal D_{-,c}u
+
\mathcal R_{-,u}.
~~~

The Cauchy terms are genuine edge transforms.

The arithmetic terms depend only on finitely many **strict-interior germs** of
the same kernel vector.

At a threshold, one additional pair of opposite-edge germs enters.

Therefore the possible superflat defect is now localized to a finite
delay-germ cancellation problem.

---

## 10. But residual flatness does not automatically imply second-derivative flatness

There is one further regularity warning.

The collar residual controls

~~~math
F_u(c+\delta)-m(c+\delta)
~~~

and its left-edge analogue in an integrated \(L^2\) sense.

The first-kind delay equation is an identity for

~~~math
F_u''.
~~~

At native regularity we have only

~~~math
F_u\in C^1.
~~~

Infinite-order smallness of the residual norm does not, by itself, justify
differentiating the asymptotic infinitely many times.

Thus one cannot simply conclude that the Stieltjes term and the finite-delay
term cancel to infinite differential order.

A successful edge-propagation proof must either

1. upgrade the boundary germ to a quasi-analytic differentiability class; or
2. work directly with an integral/extension formulation that does not
   differentiate the flatness hypothesis.

This is another reason the existing distributional equation alone does not
close the argument.

---

## 11. Refined finite-dimensional edge-germ operator

Let

~~~math
K_c=\ker G_c,
\qquad
P_c^+\subseteq K_c
~~~

be the stabilized persistence space from the preceding pass.

For a sufficiently small nonthreshold collar, package the two exterior
potentials as

~~~math
\mathfrak G_c(u)
=
\left(
F_u(c+\cdot)-m(c+\cdot),
F_u(-c-\cdot)-m(c+\cdot)
\right).
~~~

At a threshold, include the two directly coupled opposite-edge source germs
in the same package.

Then

~~~math
\mathfrak G_c:
K_c\to
C^1_{\mathrm{loc}}([0,\varepsilon_0))^2
~~~

is linear, and

~~~math
\boxed{
\ker\mathfrak G_c
=
P_c^+.
}
~~~

The flat-edge obstruction is exactly the possibility that the induced map

~~~math
K_c/P_c^+
\longrightarrow
\{\text{edge germs}\}
~~~

contains a nonzero germ flat to every order permitted by the chosen topology.

This is the first-kind/delay realization of the finite-dimensional
edge-defect space

~~~math
\mathcal E_c.
~~~

---

## 12. Result of this NF pass

The first-kind delay system does **not** yet prove

~~~math
\mathcal E_c=0.
~~~

It does sharpen the problem substantially.

### Nonthreshold support

All arithmetic delays near either endpoint sample a fixed compact interior
region. The only genuine edge singularity is the exterior Stieltjes term.

### Threshold support

Exactly one prime-power delay can directly couple the two endpoints.

### Zero-eigenvalue obstruction

Membership in

~~~math
\ker G_c
~~~

does not inherit the smoothing regularity of \(G_c\). Generic smooth compact
integral operators can have arbitrarily rough finite-dimensional kernels.

Therefore the missing theorem must exploit the **specific Weil
difference/arithmetic kernel**, not generic Fredholm smoothing.

The surviving target is:

~~~text
SZ-KERNEL-EDGE-QA / WEIL-SPECIFIC GERM RIGIDITY
~~~

> prove that the finite-dimensional edge-germ family generated by
> \(\ker G_c\) is quasi-analytic modulo the stabilized persistence subspace,
> using the special screw-function / arithmetic-delay structure.

Standard logarithmic-Laplacian open-set UCP is insufficient for this target.

---

## 13. Candidate follow-on if ratified

~~~text
SZ-KERNEL-EDGE-QA / SCREW-KERNEL TRANSFORM
~~~

A future NF should avoid differentiating the flatness hypothesis and instead
seek an integral-transform representation of the two edge germs whose
analytic continuation or moment structure uses the **specific explicit screw
function \(g\)**. The aim is to decide whether a nonzero class in
\(K_c/P_c^+\) can have a superflat transform at the slit endpoints.

**No canonical cursor movement is asserted by this residue.**
