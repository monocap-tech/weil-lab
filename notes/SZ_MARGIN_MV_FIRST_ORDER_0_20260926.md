# SZ-MARGIN-MV-FIRST-ORDER-0 — Residual-square lower law and no universal first exponent

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Immediate parent residue:** SZ_SAME_SOURCE_MARGIN_0_20260926.md  
**Uses:** ratified SZ-CROSS-COLLAR-1/2, same-source correction residue,
regular screw-carrier channel map, exact affine-fiber margin law.

## 0. Objective

In the vanishing-margin branch

~~~math
\mathfrak m_{c+\varepsilon}(u)\to0,
~~~

determine whether the existing Suzuki collar information forces a first
nonzero asymptotic order.

The answer has two layers.

1. On the regular screw carrier, the same-source margin is bounded below by
   the **square of the Suzuki collar residual**.
2. The present hypotheses do not force a nonzero asymptotic order for that
   residual. Hence there is no universal first exponent without an additional
   lower-jet theorem.

Under the conditional endpoint-trace hypotheses of SZ-CROSS-COLLAR-2, the
residual-square scale is

~~~math
\varepsilon^5\log^2(1/\varepsilon).
~~~

---

## 1. Regular endpoint setup

Assume the endpoint neutral mode is in the regular Suzuki branch:

~~~math
0\ne u\in\ker G_c
\subset
L_0^2(-c,c).
~~~

For

~~~math
b=c+\varepsilon>c,
~~~

let

~~~math
J=J_{c,b}
~~~

be zero extension and define the canonical residual

~~~math
\boxed{
r_b:=G_bJu,
\qquad
\Delta_b:=\|r_b\|_2.
}
~~~

Ratified SZ-CROSS-COLLAR-1 gives

~~~math
\Delta_b>0
\Longrightarrow
\lambda_b<0.
~~~

Let

~~~math
\sigma_b:
L_0^2(-b,b)\to M_\Pi
~~~

be the bounded selected-coordinate map from the regular screw-carrier custody
construction.

Zero extension preserves the selected coordinate.

---

## 2. A bounded old-domain correction operator

The old selected-coordinate map

~~~math
\sigma_c:
L_0^2(-c,c)\to M_\Pi
~~~

is surjective for the fixed finite packet.

Because \(M_\Pi\) is finite dimensional, choose a bounded linear right inverse

~~~math
R_c:
M_\Pi\to L_0^2(-c,c)
~~~

such that

~~~math
\boxed{
\sigma_cR_c=I_{M_\Pi}.
}
~~~

Define the corrected residual direction

~~~math
\boxed{
d_b
:=
r_b
-
J R_c(\sigma_b r_b).
}
~~~

Then

~~~math
\sigma_b(d_b)=0.
~~~

Thus \(d_b\) is an admissible selected-preserving direction for the
same-source affine fiber.

---

## 3. The correction does not change the cross coupling

Because \(JR_c(\sigma_b r_b)\) is an old-support direction and \(Ju\) is the
zero extension of the endpoint null mode,

~~~math
\langle
G_bJu,
JR_c(\sigma_b r_b)
\rangle
=
0.
~~~

Therefore

~~~math
\begin{aligned}
L_b(d_b)
&=
\langle
G_bJu,d_b
\rangle\\
&=
\langle r_b,r_b\rangle\\
&=
\Delta_b^2.
\end{aligned}
~~~

Hence

~~~math
\boxed{
L_b(d_b)=\Delta_b^2.
}
~~~

This is the key quantitative same-source identity.

---

## 4. The corrected direction is \(O(\Delta_b)\)

On a fixed small right collar

~~~math
c<b\le A,
~~~

the selected-coordinate maps are uniformly bounded:

~~~math
\|\sigma_b\|
\le
C_{\sigma,A}.
~~~

The old right inverse \(R_c\) is fixed.

Thus

~~~math
\begin{aligned}
\|d_b\|
&\le
\|r_b\|
+
\|R_c\|\,\|\sigma_b r_b\|\\
&\le
\left(
1+\|R_c\|C_{\sigma,A}
\right)\Delta_b.
\end{aligned}
~~~

Set

~~~math
C_d
:=
1+\|R_c\|C_{\sigma,A}.
~~~

Then

~~~math
\boxed{
\|d_b\|\le C_d\Delta_b.
}
~~~

Likewise, the bounded screw operators \(G_b\) have a uniform norm bound on a
fixed compact support collar:

~~~math
\|G_b\|\le M_A.
~~~

Therefore

~~~math
|q_b(d_b)|
=
|\langle G_bd_b,d_b\rangle|
\le
M_A C_d^2\Delta_b^2.
~~~

---

## 5. Residual-square lower law for the same-source margin

Recall

~~~math
\mathfrak m_b(u)
=
-\inf_{\sigma_b(x)=u}q_b(x).
~~~

There are three possibilities for the corrected direction \(d_b\).

### If \(q_b(d_b)<0\)

The same-source affine fiber contains a negative selected-preserving ray, so

~~~math
\mathfrak m_b(u)=+\infty.
~~~

### If \(q_b(d_b)=0\)

Since

~~~math
L_b(d_b)=\Delta_b^2>0,
~~~

the coupled-null case again gives

~~~math
\mathfrak m_b(u)=+\infty.
~~~

### If \(q_b(d_b)>0\)

The exact affine-fiber law gives

~~~math
\mathfrak m_b(u)
\ge
\frac{|L_b(d_b)|^2}{q_b(d_b)}.
~~~

Using Sections 3–4,

~~~math
\mathfrak m_b(u)
\ge
\frac{\Delta_b^4}
{M_A C_d^2\Delta_b^2}.
~~~

Hence

~~~math
\boxed{
\mathfrak m_b(u)
\ge
C_*\,\Delta_b^2,
\qquad
C_*:=
\frac1{M_A C_d^2}>0.
}
~~~

whenever the finite-margin branch applies.

With the convention \(+\infty\ge C_*\Delta_b^2\), the estimate holds uniformly
through all three cases:

~~~math
\boxed{
\Delta_b>0
\Longrightarrow
\mathfrak m_b(u)
\ge
C_*\Delta_b^2.
}
~~~

This is the basic quantitative collar-to-margin transfer law.

---

## 6. When the residual-square law is two-sided

Assume additionally that the selected-preserving restriction has a uniform
positive lower bound

~~~math
\boxed{
q_b(h)
\ge
\alpha\|h\|^2
\qquad
(h\in\ker\sigma_b)
}
~~~

for some \(\alpha>0\) on the right collar.

Then for every \(h\in\ker\sigma_b\),

~~~math
|L_b(h)|
=
|\langle r_b,h\rangle|
\le
\Delta_b\|h\|.
~~~

Therefore

~~~math
\frac{|L_b(h)|^2}{q_b(h)}
\le
\frac{\Delta_b^2}{\alpha}.
~~~

Taking the supremum,

~~~math
\boxed{
C_*\Delta_b^2
\le
\mathfrak m_b(u)
\le
\alpha^{-1}\Delta_b^2.
}
~~~

Thus under selected-preserving coercivity,

~~~math
\boxed{
\mathfrak m_b(u)
\asymp
\Delta_b^2.
}
~~~

No such coercivity is presently canonical.

---

## 7. What the ratified native collar flatness gives

Ratified SZ-CROSS-COLLAR-2 proves at native regularity

~~~math
\boxed{
\Delta_{c,c+\varepsilon}(u)
=
o(\varepsilon^{3/2}).
}
~~~

The residual-square lower law therefore reads

~~~math
\mathfrak m_{c+\varepsilon}(u)
\ge
C_*
\Delta_{c,c+\varepsilon}(u)^2.
~~~

But

~~~math
\Delta^2
=
o(\varepsilon^3)
~~~

is only information about the **size of this lower-bound scale**.

It does not imply

~~~math
\mathfrak m_{c+\varepsilon}(u)
=
o(\varepsilon^3),
~~~

because no matching upper estimate is available without coercivity.

Nor does it give a positive lower power of \(\varepsilon\), because
\(o(\varepsilon^{3/2})\) permits arbitrarily faster decay.

Thus native \(C^1\) collar flatness alone supplies no first nonzero exponent.

---

## 8. Conditional endpoint-trace scale

Under the additional endpoint-trace and translated-sample regularity
hypotheses retained conditionally in SZ-CROSS-COLLAR-2, if at least one
endpoint trace is nonzero then

~~~math
\Delta_{c,c+\varepsilon}(u)^2
=
C_{\rm tr}
\varepsilon^5
\log^2\frac1\varepsilon
+
o\!\left(
\varepsilon^5
\log^2\frac1\varepsilon
\right),
~~~

where

~~~math
C_{\rm tr}
=
\frac{
|u(c-)|^2+|u(-c+)|^2
}{80}
>0.
~~~

The residual-square law immediately yields

~~~math
\boxed{
\mathfrak m_{c+\varepsilon}(u)
\gtrsim
\varepsilon^5
\log^2\frac1\varepsilon.
}
~~~

If the selected-preserving coercivity hypothesis of Section 6 also holds,
then

~~~math
\boxed{
\mathfrak m_{c+\varepsilon}(u)
\asymp
\varepsilon^5
\log^2\frac1\varepsilon.
}
~~~

So the conditional logarithmic collar jet does determine the first margin
scale once a matching denominator bound is available.

---

## 9. Arbitrarily flat decay is not excluded by present axioms

The existing abstract/canonical data do not force a polynomial or
polylogarithmic lower order.

For any positive function

~~~math
a(\varepsilon)\downarrow0,
~~~

consider the two-dimensional Hermitian family

~~~math
Q_\varepsilon
=
\begin{pmatrix}
0&-a(\varepsilon)\\
-a(\varepsilon)&1
\end{pmatrix}.
~~~

Take the selected coordinate to be the first coordinate.

Then the endpoint vector \(e_1\) is neutral at \(a=0\), the cross functional
is nonzero whenever \(a(\varepsilon)>0\), and

~~~math
\boxed{
\mathfrak m_\varepsilon
=
a(\varepsilon)^2.
}
~~~

Choosing, for example,

~~~math
a(\varepsilon)
=
e^{-1/\varepsilon}
~~~

gives

~~~math
\boxed{
\mathfrak m_\varepsilon
=
e^{-2/\varepsilon},
}
~~~

which is flatter than every power of \(\varepsilon\).

This is an abstract sharpness model. It does **not** assert that Suzuki's
actual screw kernel realizes such a flat branch.

It proves only that the current structural axioms cannot rule one out.

---

## 10. Interpretation of the MV branch

The vanishing-margin problem has now separated into two independent analytic
questions.

### Numerator question

How small can

~~~math
\Delta_{c,c+\varepsilon}(u)
~~~

be for an actual nonzero endpoint kernel vector?

The ratified answer is only

~~~math
\Delta=o(\varepsilon^{3/2}).
~~~

The conditional trace calculation gives a definite logarithmic second-jet
scale when a nonzero endpoint trace exists.

### Denominator question

How degenerate can

~~~math
q_b|_{\ker\sigma_b}
~~~

be relative to the ambient screw norm?

Without a positive lower bound, the affine-fiber margin may be much larger
than \(\Delta^2\), including \(+\infty\).

Thus a true first-order theorem for \(\mathfrak m_b(u)\) requires controlling
both the collar residual and the selected-preserving denominator geometry.

---

## 11. Result of this NF pass

The sharp unconditional regular-carrier statement is

~~~math
\boxed{
\mathfrak m_b(u)
\gtrsim
\Delta_{c,b}(u)^2.
}
~~~

A matching upper bound—and hence an exact margin order—requires additional
coercivity on the selected-preserving form.

Therefore:

~~~text
SZ-MARGIN-MV / FIRST NONZERO ORDER
~~~

does **not** close to a universal exponent from the current canonical data.

Under the conditional nonzero endpoint-trace regime, the natural margin scale
is

~~~math
\boxed{
\varepsilon^5\log^2(1/\varepsilon),
}
~~~

at least as a lower bound, and as a two-sided order if selected-preserving
coercivity is supplied.

At native regularity, arbitrarily flat decay remains structurally possible
from the information currently proved.

---

## 12. Candidate follow-on if ratified

~~~text
SZ-MV / ROUGH-ENDPOINT LOWER JET
~~~

A future NF should attack the numerator question directly:

> can a nonzero \(u\in\ker G_c\) have
> \(\Delta_{c,c+\varepsilon}(u)\) flatter than every explicit
> power/logarithmic scale, or does the exterior Cauchy/Stieltjes term force a
> quantitative lower jet even without endpoint traces?

That is now the cleanest route for shrinking the MV branch.

**No canonical cursor movement is asserted by this residue.**
