# SZ-MV-ROUGH-ENDPOINT-0 — Variance growth and kernel-restricted quasi-analyticity

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Immediate parent residue:** SZ_MARGIN_MV_FIRST_ORDER_0_20260926.md  
**Uses:** ratified SZ-CROSS-COLLAR-1/2; Suzuki arXiv:2606.09096v3,
Theorem 1.1, Theorem 1.3, §§2.1–2.2 and 8.4–8.5.

## 0. Objective

The remaining MV question is:

> For a nonzero regular endpoint mode
> \[
> u\in\ker G_c,
> \]
> can the collar residual
> \[
> \Delta_{c,c+\varepsilon}(u)
> \]
> be flatter than every explicit power/logarithmic scale?

The answer from the currently available structure is:

\`\`\`text
the generic exterior Cauchy/Stieltjes mechanism does not force a lower jet.
\`\`\`

A quantitative lower jet can only come from an additional theorem about the
**special finite-dimensional kernel \(\ker G_c\)**.

---

## 1. The regular zero kernel is finite dimensional

Suzuki proves that

\[
D=i\,\frac{d}{dx}:
H_0^1(-c,c)\to L_0^2(-c,c)
\]

is an isometric isomorphism when \(H_0^1\) is equipped with the derivative
norm, and

\[
B_c=D^*G_cD.
\]

Take

\[
u\in\ker G_c
\]

and let

\[
v=D^{-1}u\in H_0^1(-c,c).
\]

Then

\[
B_cv
=
D^*G_cu
=
0.
\]

Since Suzuki's \(A_c\) is the Friedrichs extension of \(B_c\),

\[
v\in\ker A_c.
\]

Thus

\[
\boxed{
D^{-1}(\ker G_c)
\subseteq
\ker A_c.
}
\]

The spectrum of \(A_c\) is discrete with finite-multiplicity eigenspaces.
Therefore

\[
\boxed{
\dim\ker G_c<\infty.
}
\]

This is useful but does not by itself give an asymptotic collar order.

---

## 2. Exact variance-growth identity for the collar residual

Fix

\[
0\ne u\in\ker G_c.
\]

Let

\[
F(x)
=
F_u(x)
=
\int_{-c}^{c}g(x-y)u(y)\,dy.
\]

On \((-c,c)\),

\[
F(x)=C_u.
\]

For \(b\ge c\), define the interval mean

\[
m(b)
:=
\frac1{2b}
\int_{-b}^{b}F(x)\,dx.
\]

The ratified residual is

\[
\Delta(b)^2
=
\|G_bJ_{c,b}u\|_2^2
=
\int_{-b}^{b}|F(x)-m(b)|^2\,dx.
\]

Since \(F\) is continuous, this function is differentiable for \(b>c\).
A direct differentiation gives

\[
\boxed{
\frac{d}{db}\Delta(b)^2
=
|F(b)-m(b)|^2
+
|F(-b)-m(b)|^2.
}
\]

Indeed, differentiating

\[
\Delta(b)^2
=
\int_{-b}^{b}|F(x)|^2dx
-
\frac1{2b}
\left|
\int_{-b}^{b}F(x)\,dx
\right|^2
\]

produces exactly the displayed sum of two squares.

Therefore

\[
\boxed{
\Delta(b)^2
\text{ is nondecreasing in }b.
}
\]

Since \(\Delta(c)=0\),

\[
\boxed{
\Delta(c+\varepsilon)^2
=
\int_0^\varepsilon
\Big(
|F(c+s)-m(c+s)|^2
+
|F(-c-s)-m(c+s)|^2
\Big)\,ds.
}
\]

So the entire lower-jet question is a boundary-germ problem.

---

## 3. Recovery of the ratified first-order flatness

Ratified SZ-CROSS-COLLAR-2 gives

\[
F\in C^1_{\mathrm{loc}},
\qquad
F'(\pm c)=0.
\]

Hence

\[
F(c+s)-C_u=o(s),
\qquad
F(-c-s)-C_u=o(s).
\]

The mean satisfies the same first-order flatness. Thus the derivative identity
immediately reproduces

\[
\Delta(c+\varepsilon)^2=o(\varepsilon^3),
\]

or

\[
\boxed{
\Delta(c+\varepsilon)
=
o(\varepsilon^{3/2}).
}
\]

But the identity supplies no lower scale unless one knows that the boundary
germ cannot be superflat.

---

## 4. The exterior singular term is a Stieltjes transform

On the right collar write

\[
s=c-y,
\qquad
f(s):=u(c-s),
\qquad
0<s<2c.
\]

The singular term in the ratified exterior second-derivative equation is

\[
\boxed{
(\mathcal C f)(\delta)
:=
\int_0^{2c}
\frac{f(s)}{s+\delta}\,ds,
\qquad
\delta>0.
}
\]

This is a finite-interval Stieltjes/Cauchy transform.

The conditional endpoint-trace calculation corresponds to the special case
where

\[
f(s)\to u(c-)
\]

as \(s\downarrow0\), which produces the logarithm

\[
(\mathcal C f)(\delta)
=
u(c-)\log(1/\delta)+O(1).
\]

Without a trace, the Stieltjes transform has much more freedom.

---

## 5. Explicit superflat Stieltjes profiles exist in \(L^2\)

The absence of a generic lower jet is not merely a logical possibility.

Let

\[
L:=2c
\]

and consider the slit plane

\[
\Omega
=
\mathbb C\setminus[-L,0].
\]

A standard conformal map from \(\Omega\) to the exterior unit disk is

\[
w(z)
=
\frac{
2z+L+2\sqrt{z(z+L)}
}{L},
\]

with the branch chosen so that \(w(z)\to\infty\) as \(z\to\infty\).

For \(z>0\) and \(z\downarrow0\),

\[
w(z)-1
\sim
2\sqrt{\frac zL}.
\]

Define on \(|w|>1\)

\[
H(w)
=
w^{-2}
\exp\!\left(
-\frac{w+1}{w-1}
\right).
\]

The Möbius factor

\[
\frac{w+1}{w-1}
\]

has positive real part on the exterior disk, so \(H\) is bounded there.

Set

\[
S(z)
:=
H(w(z)).
\]

Then:

1. \(S\) is analytic on \(\Omega\);
2. \(S(z)=O(z^{-2})\) as \(z\to\infty\);
3. as \(z\downarrow0\) on the positive axis,
   \[
   \boxed{
   S(z)
   =
   O\!\left(
   e^{-\sqrt{L/z}}
   \right),
   }
   \]
   hence \(S(z)=o(z^N)\) for every \(N\);
4. \(S\not\equiv0\).

The boundary values on the two sides of the slit are bounded. By the Cauchy
jump representation, there exists a nonzero density

\[
f\in L^2(0,L)
\]

such that, up to a fixed nonzero normalization,

\[
\boxed{
S(z)
=
\int_0^L
\frac{f(s)}{s+z}\,ds.
}
\]

Because \(S(z)=O(z^{-2})\) at infinity, the \(z^{-1}\) coefficient vanishes:

\[
\boxed{
\int_0^L f(s)\,ds=0.
}
\]

Thus even within the zero-mean \(L^2\) class there are nonzero endpoint
profiles whose exterior Stieltjes transform is flatter than every power.

---

## 6. What this example proves—and what it does not

The construction in Section 5 proves

\[
\boxed{
\text{no quantitative lower jet follows from }
L^2
+
\text{zero mean}
+
\text{the Stieltjes structure alone}.
}
\]

It does **not** prove that such an \(f\) occurs as the endpoint profile of a
vector in

\[
\ker G_c.
\]

That is precisely the missing information.

The prime-translation and smooth archimedean terms in the full exterior
equation do not repair this generic lack of quasi-analyticity by themselves;
they provide additional equations only after the kernel condition is used.

---

## 7. Finite dimensionality does not create a rate automatically

Let

\[
K_c:=\ker G_c.
\]

Section 1 gives

\[
\dim K_c<\infty.
\]

For each \(\varepsilon>0\), define the collar map

\[
T_\varepsilon:
K_c
\to
L_0^2(-c-\varepsilon,c+\varepsilon),
\qquad
T_\varepsilon u
=
G_{c+\varepsilon}J u.
\]

Then

\[
\Delta_{c,c+\varepsilon}(u)
=
\|T_\varepsilon u\|.
\]

If no nonzero vector in \(K_c\) persists to the support \(c+\varepsilon\),
finite dimensionality gives a positive smallest singular value

\[
\nu_c(\varepsilon)
:=
\inf_{\substack{u\in K_c\\\|u\|=1}}
\|T_\varepsilon u\|
>
0.
\]

However,

\[
\boxed{
\nu_c(\varepsilon)>0
\text{ for each }\varepsilon
}
\]

does not imply any power-law lower bound as \(\varepsilon\downarrow0\).

Even a one-dimensional continuous family can behave like

\[
\nu_c(\varepsilon)
=
e^{-1/\varepsilon}.
\]

A rate requires additional regularity or quasi-analyticity in the support
parameter.

---

## 8. The exact missing theorem

The rough-endpoint problem has therefore reduced to

\`\`\`text
SZ-KERNEL-ENDPOINT-QA
\`\`\`

with the following target.

### Kernel-restricted quasi-analyticity

For

\[
0\ne u\in\ker G_c,
\]

prove that

\[
\Delta_{c,c+\varepsilon}(u)
=
o(\varepsilon^N)
\qquad
\forall N
\]

forces

\[
\Delta_{c,c+\varepsilon}(u)
\equiv0
\]

on some nontrivial right collar.

Equivalently:

\[
\boxed{
\text{a leaking actual kernel mode cannot have a flat exterior germ.}
}
\]

This is strictly stronger than ordinary Stieltjes uniqueness.

It uses the fact that \(u\) solves the full first-kind integral equation

\[
G_cu=0,
\]

not merely that \(u\in L^2\).

---

## 9. Threshold-aware form

Away from a prime-power threshold, the exterior equation contains only the
already-active finite translations.

At a threshold

\[
2c=\log n_0,
\]

the strict right collar activates the corresponding equality-threshold
translation, which samples the opposite endpoint.

Therefore a complete kernel quasi-analyticity theorem must be formulated
for the **right-limit exterior operator**, including this finite threshold
correction.

The threshold does not change the generic Stieltjes no-go; it changes the
special kernel equation to which quasi-analyticity would have to be applied.

---

## 10. Consequence for the same-source margin

The preceding margin pass gave

\[
\mathfrak m_{c+\varepsilon}(u)
\gtrsim
\Delta_{c,c+\varepsilon}(u)^2.
\]

Thus a kernel-restricted lower jet

\[
\Delta_{c,c+\varepsilon}(u)
\gtrsim
\varepsilon^\alpha
(\log(1/\varepsilon))^\beta
\]

would immediately imply

\[
\boxed{
\mathfrak m_{c+\varepsilon}(u)
\gtrsim
\varepsilon^{2\alpha}
(\log(1/\varepsilon))^{2\beta}.
}
\]

Without SZ-KERNEL-ENDPOINT-QA, no such universal lower order is justified.

---

## 11. Result of this NF pass

The rough-endpoint lower-jet problem does **not** close from the local
Cauchy/Stieltjes singularity alone.

The pass establishes three sharper facts:

\[
\boxed{
\dim\ker G_c<\infty,
}
\]

\[
\boxed{
\frac{d}{db}\Delta_{c,b}(u)^2
=
|F_u(b)-m(b)|^2
+
|F_u(-b)-m(b)|^2,
}
\]

and

\[
\boxed{
\text{nonzero zero-mean }L^2
\text{ Stieltjes profiles can be superflat at the endpoint.}
}
\]

Therefore any theorem excluding arbitrarily flat MV leakage must exploit the
**kernel equation itself**, not merely endpoint \(L^2\) regularity or the
Cauchy singularity.

The surviving seam is exactly

\`\`\`text
SZ-KERNEL-ENDPOINT-QA
\`\`\`

—kernel-restricted endpoint quasi-analyticity.

---

## 12. Candidate follow-on if ratified

\`\`\`text
SZ-KERNEL-ENDPOINT-QA / FIRST-KIND RIGIDITY
\`\`\`

A future NF should use the full equation

\[
G_cu=0
\]

together with the threshold-aware exterior distribution equation to test
whether a flat exterior germ forces actual collar persistence.

**No canonical cursor movement is asserted by this residue.**
