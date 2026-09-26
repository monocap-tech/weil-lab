# SZ-BG-RELATIVE-GAP-0 — Support-transport no-go

**Date:** 2026-09-26  
**Branch:** `sz-cross-collar`  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** `SZ-CROSS-COLLAR-3`  
**Immediate parent residue:** `SZ_BG_GAP_0_20260926.md`

## 0. Objective

The preceding gap audit proved that at a jointly screened endpoint the
background residual budget

```math
R_B(c)=I-X_B(c)X_B(c)^*
```

has a strict positive lower bound on the finite selected-active range

```math
W_M(c)=\operatorname{Ran}X_M(c).
```

The proposed continuation was to transport that relative gap to (b>c).

This pass tests whether the continuity already available on the **physical
synthesis/covariance side** is sufficient.

It is not.

---

## 1. Compact positive synthesis

Take

```math
K_+=H=\ell^2(\mathbb N),
\qquad
M=B=\mathbb C.
```

Let ((e_j)) be the standard orthonormal basis and define the compact
injective positive synthesis

```math
S_+e_j
=
\frac1j e_j.
```

Thus

```math
S_+
=
\operatorname{diag}
\left(
1,\frac12,\frac13,\ldots
\right).
```

Its kernel is zero, but its inverse on the range is unbounded.

This is the basic geometry responsible for instability of Douglas
coefficients despite stability of their physical images.

---

## 2. Endpoint selected/background screens

Set

```math
a:=\frac1{\sqrt2}.
```

At the endpoint define

```math
X_M(0)z
=
az e_1,
\qquad
X_B(0)z
=
az e_1.
```

Both maps have norm

```math
\frac1{\sqrt2}<1.
```

Their joint budget is exactly saturated in the (e_1) direction:

```math
X_M(0)X_M(0)^*
+
X_B(0)X_B(0)^*
=
P_{e_1}.
```

Define the physical selected and background syntheses by

```math
S_M(0)=-S_+X_M(0),
\qquad
S_B(0)=-S_+X_B(0).
```

The background residual budget is

```math
R_B(0)
=
I-\frac12P_{e_1}.
```

The selected-active range is

```math
W_M(0)=\mathbb Ce_1.
```

Hence

```math
\boxed{
\langle R_B(0)x,x\rangle
=
\frac12\|x\|^2
\qquad
(x\in W_M(0)).
}
```

So the endpoint relative gap is exactly (1/2).

After background elimination, the selected channel is critical: the residual
positive covariance in the (e_1) direction and the selected covariance both
have weight (1/2).

---

## 3. Nearby screens invisible in the physical norm

For (n\ge2), define the unit vector

```math
y_n
:=
\frac1{\sqrt2}e_1
+
\frac1{\sqrt2}e_n.
```

Set

```math
X_M(n)z
=
zy_n,
\qquad
X_B(n)z
=
zy_n.
```

Then

```math
\boxed{
\|X_M(n)\|
=
\|X_B(n)\|
=
1.
}
```

Because (S_+) is injective, these are the unique reduced exact solutions for
their physical channels.

Define

```math
S_M(n)=-S_+X_M(n),
\qquad
S_B(n)=-S_+X_B(n).
```

Now

```math
S_+y_n
=
\frac1{\sqrt2}e_1
+
\frac1{\sqrt2 n}e_n.
```

Therefore

```math
\boxed{
\|S_M(n)-S_M(0)\|
=
\frac1{\sqrt2 n}
\longrightarrow0,
}
```

and identically

```math
\boxed{
\|S_B(n)-S_B(0)\|
\longrightarrow0.
}
```

Consequently their rank-one physical covariances also converge in trace norm,
hence in operator norm.

So the physical channel family is extremely well behaved.

---

## 4. The Douglas maps do not converge

On the coefficient side,

```math
X_M(n)1-X_M(0)1
=
\frac1{\sqrt2}e_n,
```

so

```math
\boxed{
\|X_M(n)-X_M(0)\|
=
\frac1{\sqrt2}
}
```

for every (n).

The same holds for (X_B).

Thus physical operator-norm convergence of the synthesis maps does **not**
imply norm continuity of their Douglas reduced solutions, even when

- the negative domain is one-dimensional;
- the positive synthesis is fixed;
- the positive synthesis is injective;
- exact factorization holds at every parameter;
- every individual screen is contractive.

The obstruction is the unbounded inverse geometry of the compact
(S_+).

---

## 5. The selected-active subspace jumps

At the endpoint,

```math
W_M(0)=\mathbb Ce_1.
```

For every (n\ge2),

```math
W_M(n)=\mathbb Cy_n.
```

Since

```math
|\langle y_n,e_1\rangle|
=
\frac1{\sqrt2},
```

the one-dimensional orthogonal projections satisfy

```math
\boxed{
\|P_{W_M(n)}-P_{W_M(0)}\|
=
\frac1{\sqrt2}.
}
```

Hence the moving selected-active subspace is not norm continuous.

Finite selected dimension does not repair this.

---

## 6. The relative background gap collapses

For (n\ge2), the background map is an isometry from (mathbb C) onto
(mathbb Cy_n). Therefore

```math
X_B(n)X_B(n)^*
=
P_{y_n}
```

and

```math
R_B(n)
=
I-P_{y_n}.
```

But

```math
W_M(n)=\mathbb Cy_n.
```

Therefore

```math
\boxed{
R_B(n)|_{W_M(n)}=0.
}
```

The endpoint relative gap

```math
\frac12
```

has collapsed to zero at every nearby index, despite norm convergence of the
physical selected/background syntheses and their covariances.

Thus

```math
\boxed{
\text{physical covariance continuity}
\not\Rightarrow
\text{support transport of the selected-active residual gap}.
}
```

---

## 7. What the collapse means

The background itself remains individually screenable:

```math
\|X_B(n)\|=1.
```

So this example is **not** a failure of background elimination.

Instead, after background elimination there is no residual positive budget in
the selected-active direction (y_n), while the selected physical channel is
nonzero.

Hence the residual selected problem has become unscreenable there.

The collapse of the relative gap is therefore already a **selected residual
defect**, not a mysterious third obstruction.

This is consistent with SZ-CROSS-COLLAR-5R.

---

## 8. Consequence for the proposed support-transport route

The interface

```text
SZ-BG-RELATIVE-GAP / SUPPORT TRANSPORT
```

cannot be discharged from

- finite selected dimension;
- norm-continuous physical synthesis;
- trace/operator-norm continuous physical covariances;
- individual contractivity of the background.

One needs genuinely stronger control of the **coefficient-side reduced
factorizations**, such as a bounded-below condition excluding approximate
positive-synthesis kernels on the relevant moving coefficient sector.

But that stronger condition is precisely the type of inverse/coercivity
information Horizon 1 repeatedly refuses to assume for free.

Therefore coefficient-side continuity should not be made a new hidden premise.

---

## 9. Correct remaining fork

This pass removes relative-gap transport as a necessary intermediate goal.

At each enlarged support (b), the logically correct test remains:

### Background screen admissible

If

```math
S_{B,b}=-S_{+,b}X_{B,b},
\qquad
\|X_{B,b}\|\le1,
```

then WD-T10 eliminates the background **at that support**.

Any full negative value is then a negative residual selected defect.

### Background screen inadmissible

If no such contractive exact background factorization exists, the obstruction
is background range/over-budget failure.

Thus the robust collar statement is pointwise in (b):

```math
\boxed{
\text{Suzuki collar leakage at }b
\Longrightarrow
\begin{cases}
\text{negative residual selected defect at }b,
&
\text{if background screening is admissible},\\
\text{background screening defect at }b,
&
\text{otherwise}.
\end{cases}
}
```

No continuity of the Douglas maps is needed for this dichotomy.

---

## 10. Result of this NF pass

The moving-selected-active-gap route is a dead end without extra coercivity.

The explicit compact diagonal example proves that the desired coefficient
transport can fail maximally while the physical channel family converges in
norm.

Accordingly:

```text
SZ-BG-RELATIVE-GAP / SUPPORT TRANSPORT — NO-GO from existing continuity data.
```

The useful invariant is the **pointwise background-screening status** at each
strict support, not continuity of its chosen Douglas coordinates.

This returns the traversal to the clean background-or-selected dichotomy of
SZ-CROSS-COLLAR-5R without adding an unjustified inverse-stability premise.

---

## 11. Candidate follow-on if ratified

```text
SZ-COLLAR-BRANCH-CLASSIFICATION
```

A future NF should combine the ratified cross-collar theorem with the
pointwise WD-T10 background test and classify the two resulting strict-support
branches against the existing Horizon-1 negative/noncompact morphologies,
without assuming continuity of reduced screening maps.

**No canonical cursor movement is asserted by this residue.**
