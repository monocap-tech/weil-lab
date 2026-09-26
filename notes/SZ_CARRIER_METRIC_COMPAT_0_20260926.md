# SZ-CARRIER-METRIC-COMPAT-0 — Preconditioned form bridge, not operator equivalence

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Immediate parent residue:** SZ_COLLAR_BRANCH_CLASSIFICATION_0_20260926.md  
**Uses:** ZW1-T9 / WD-T28, WD-T35/36, the H1-P2 specialization map,
and the explicit carrier-identification hypothesis retained in WD-T38.

## 0. Objective

The previous collar classification is formulated in the native zero-side
selected/background defect language.

The ratified Suzuki theorem is formulated in the closed localized Weil form

~~~math
q_b
~~~

on \(L^2(-b,b)\), with associated self-adjoint operator \(A_b\).

The question is whether these are literally the same support-\(b\) operator
after identifying their Hilbert carriers.

They are not.

The correct bridge must be a **preconditioned form identity**.

---

## 1. The two carrier layers have different operator order

### Native Problem-1 layer

Horizon 1 uses the Dirichlet Green metric

~~~math
L_b
=
-\partial_u^2+\frac14,
\qquad
G_b^{\rm Dir}=L_b^{-1},
~~~

and the negative-order carrier

~~~math
\mathscr H_b^{\rm P1}
=
H^{-1}_{L_b}(-b,b).
~~~

The actual zero-side synthesis

~~~math
E_b:\ell^2(\Gamma)\to\mathscr H_b^{\rm P1}
~~~

is Hilbert-Schmidt by WD-T28.

Therefore every fixed positive/negative channel restriction is compact, and
the corresponding covariance operators

~~~math
S_{+,b}S_{+,b}^*,
\qquad
S_{-,b}S_{-,b}^*
~~~

are trace class.

Hence the signed native defect

~~~math
D_b^{\rm P1}
=
S_{+,b}S_{+,b}^*
-
S_{-,b}S_{-,b}^*
~~~

is a bounded compact operator on the native Problem-1 carrier.

### Suzuki closed-form layer

The compact-window Weil form has logarithmic Fourier order:

~~~math
q_b(f)+C_b\|f\|_2^2
\asymp_b
\int
\log(e+|t|)
|\widehat f(t)|^2\,dt.
~~~

Thus its associated self-adjoint operator \(A_b\) is an unbounded
logarithmic-order operator on \(L^2(-b,b)\).

Therefore the two operator realizations have fundamentally different order.

---

## 2. Boundedly invertible equivalence is impossible

Suppose there were a boundedly invertible map

~~~math
U_b:
\mathscr H_b^{\rm P1}
\to
L^2(-b,b)
~~~

such that, as operators,

~~~math
A_b
=
(U_b^{-1})^*
D_b^{\rm P1}
U_b^{-1}.
~~~

The right-hand side would be bounded because

- \(D_b^{\rm P1}\) is bounded;
- \(U_b^{-1}\) is bounded.

Hence \(A_b\) would be bounded.

This contradicts the logarithmic-order realization.

So

~~~math
\boxed{
\text{no boundedly invertible/unitary carrier identification can identify }
D_b^{\rm P1}\text{ with }A_b.
}
~~~

In particular, SZ-CARRIER-METRIC-COMPAT must not be formulated as an
operator-unitary equivalence.

---

## 3. Why this is expected

The Problem-1 realization deliberately inserts Green preconditioning.

The physical Problem-1 columns solve

~~~math
L_bF_\gamma=e^{-i\gamma u},
~~~

with the reciprocal factor

~~~math
\left(\frac14+\gamma^2\right)^{-1}.
~~~

The native metric is correspondingly

~~~math
\|f\|_{H^{-1}_{L_b}}^2
=
\langle f,L_b^{-1}f\rangle.
~~~

This smoothing is exactly what makes the infinite zero synthesis
Hilbert-Schmidt.

By contrast, Suzuki keeps the localized Weil form at its natural logarithmic
order.

Thus compactness on the Problem-1 side and unbounded logarithmic order on the
Suzuki side are not inconsistent. They signal a preconditioned realization of
the same underlying Weil geometry at different analytic orders.

The exact preconditioning map and normalization must still be proved; they
must not be guessed from this heuristic.

---

## 4. What Horizon 1 actually establishes

The H1-P2 specialization map records

~~~math
D
=
S_+S_+^*-S_-S_-^*
~~~

as the zero-side compact-window Weil defect/operator.

Separately, H1-P2.2/H1-P3.1 identifies the compact-window Weil form with the
prime/pole/archimedean logarithmic-order representation.

But the project deliberately retained an explicit **carrier-identification
hypothesis** when WD-T38 passed from the finite-exception physical null mode
to that compact-window arithmetic form.

Likewise, the WD-T28 audit explicitly warns that Bombieri's matrix is not being
identified with an ordinary Hilbert Gram matrix merely from the
Dirichlet-resolvent estimate.

Therefore there is currently no internal theorem of the form

~~~math
D_b^{\rm P1}
\simeq
A_b
~~~

between the two Hilbert realizations.

This is a real missing bridge, not a notation gap.

---

## 5. The correct common-core target

Let

~~~math
\mathcal C_b
~~~

be a dense regular core for Suzuki's localized form, for example the regular
compact-support/Dirichlet class on which both the zero-side and
explicit-formula polarizations are defined.

The correct target is to construct an explicit densely defined smoothing map

~~~math
T_b:
\mathscr H_b^{\rm P1}
\supset
\mathcal D(T_b)
\to
L^2(-b,b)
~~~

or its inverse-direction equivalent, together with a polarized identity of the
form

~~~math
\boxed{
q_b(T_bx,T_by)
=
\langle
D_b^{\rm P1}x,
y
\rangle_{\mathscr H_b^{\rm P1}}
}
~~~

for \(x,y\) in a common dense core.

Equivalent formulations may place the preconditioner on the Suzuki side, e.g.

~~~math
\boxed{
D_b^{\rm P1}
=
T_b^* A_b T_b
}
~~~

in the sense of closed forms.

The exact direction and power of the Green operator must be derived from the
Problem-1 normalization.

---

## 6. Closure requirement

A core identity alone is insufficient unless it determines the closed forms.

The bridge must establish:

1. the proposed core is a form core for the Suzuki form;
2. the preconditioned native form is closable;
3. the two closures agree under the proposed map.

Only then can a sign statement proved in one realization be transported to
the other without a domain leak.

So the bridge has two layers:

~~~text
CORE IDENTITY
+
CLOSURE COMPATIBILITY.
~~~

This is the exact analytic content hidden inside the former generic phrase
“carrier identification.”

---

## 7. Channelwise compatibility is an additional requirement

Even equality of the **total** quadratic form does not automatically transfer
the owner classification

~~~math
\text{SR-R},\ \text{SR-B},\ \text{BG-R},\ \text{BG-B}.
~~~

Those labels depend on the selected/background channel decomposition.

Therefore one additionally needs the preconditioner to intertwine the
polarized channel covariances, schematically

~~~math
\boxed{
q_{+,b}(T_bx,T_by)
=
\langle
S_{+,b}S_{+,b}^*x,y
\rangle,
}
~~~

~~~math
\boxed{
q_{M,b}(T_bx,T_by)
=
\langle
S_{M,b}S_{M,b}^*x,y
\rangle,
}
~~~

and similarly for \(B_\Pi\).

Without this channelwise identification, equality of the full Weil form would
transfer negativity but not selected/background ownership.

This is precisely the custody distinction enforced throughout Horizon 1.

---

## 8. Metric dependence of Douglas budgets

There is a further reason not to identify the screening maps across carriers
naively.

Douglas contractivity

~~~math
\|X\|\le1
~~~

is a Hilbert-metric statement.

A general bounded invertible congruence preserves the sign of a quadratic
form but does **not** preserve the unit coefficient budget or the norm of the
reduced screening map.

Thus even after a form congruence is found, the WD-A4 labels must be transferred
through the **channelwise preconditioned covariance identities**, not by
asserting that the Douglas maps themselves are unchanged.

This separates:

- invariant form sign;
- channel ownership;
- metric-specific screening norms.

---

## 9. Refined bridge interface

Replace the broad

~~~text
SZ-CARRIER-METRIC-COMPAT
~~~

by the more precise

~~~text
SZ-PRECOND-FORM-BRIDGE
~~~

with three obligations.

### PFB-1 — Core polarization

Construct the exact Problem-1 preconditioner and prove the polarized full-form
identity on a common dense core.

### PFB-2 — Closure

Prove that the common-core identity extends to the closed localized Suzuki
form and the corresponding preconditioned native form.

### PFB-3 — Channel custody

Prove that the same preconditioner respects the positive, selected-negative,
and background-negative polarizations needed for the pointwise branch
classification.

Only PFB-1/PFB-2 are needed to transport **sign**.

PFB-3 is additionally required to transport **owner labels**.

---

## 10. Consequence for the collar program

The previous branch classification remains valid internally on the native
zero-side defect carrier.

The ratified Suzuki cross-collar theorem remains valid internally on the
closed \(L^2\) form carrier.

What is not yet justified is the inference

~~~math
\boxed{
\Lambda_{c,b;k}\ne0
\Longrightarrow
\text{SR-R/SR-B/BG-R/BG-B}
}
~~~

for the actual same support-\(b\) object, because that inference crosses the
unproved preconditioning bridge.

After PFB-1/PFB-2, one may transport strict negativity.

After PFB-3, one may transport the selected/background ownership taxonomy.

So the real seam is now exact and modular.

---

## 11. Result of this NF pass

SZ-CARRIER-METRIC-COMPAT is **not** a missing bounded metric equivalence.

Such an equivalence is structurally impossible because one realization is
bounded/compact while the other is unbounded of logarithmic order.

The correct unresolved interface is

~~~text
SZ-PRECOND-FORM-BRIDGE
~~~

consisting of:

~~~text
PFB-1 core polarized identity
PFB-2 closure compatibility
PFB-3 channelwise custody compatibility.
~~~

This is narrower and correctly typed.

No claim is made in this pass that the exact Green power or normalization in
\(T_b\) has been identified.

---

## 12. Candidate follow-on if ratified

~~~text
SZ-PRECOND-FORM-BRIDGE / PFB-1
~~~

A future NF should derive the exact preconditioning map directly from the
Bombieri Problem-1 Green kernel and compare its polarized zero-side form with
Suzuki's regular \(H_0^1/L_0^2\) identity before attempting closure.

**No canonical cursor movement is asserted by this residue.**
