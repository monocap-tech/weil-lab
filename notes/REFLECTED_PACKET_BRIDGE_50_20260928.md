# RPB-50 — Null-extension discharge and neutral-plateau collapse audit

**Date:** 2026-09-28  
**Branch:** `research/reflected-packet-bridge`  
**Status:** **PASS / EVERY SCREW-CORE ENDPOINT NULL DIRECTION LEAKS / ONE LEAKING CORE DIRECTION COLLAPSES EVERY POSITIVE-LENGTH NEUTRAL PLATEAU / CORE-RESTRICTED AZ-FIN-WEIL-NULL-EXTENSION IS DISCHARGED NEGATIVELY / FULL FRIEDRICHS MODE-WISE INTERFACE REMAINS OPEN ONLY THROUGH THE CORE-LIFT MULTIPLICITY DEFECT**  
**Dependencies:** RPB-30, RPB-32 through RPB-35, RPB-49; WD-T38 / H1-P3.1 neutral morphology.  
**Promotion status:** none.

## 0. Objective

RPB-49 proved the core strict-null-extension exclusion

```math
0
e uinker G_c
Longrightarrow
G_aJ_{c,a}u
e0
qquad
(a>c)
```

for every screw-visible/core neutral source in the branch hypotheses.

RPB-50 is an audit pass.  It asks what this already-proved statement does to:

1. the possibility of a positive-length neutral support plateau;
2. the full Friedrichs neutral nullspace;
3. the selected unit-gain/Birman--Schwinger representation;
4. the canonical `AZ-FIN-WEIL-NULL-EXTENSION` stop line.

No new endpoint parametrix is introduced here.

---

## 1. RPB-34 converts every nonzero leakage into strict negativity

RPB-34 gives the exact nested-support compression

```math
J_{c,a}^{*}G_aJ_{c,a}=G_c.
```

Hence for (uinker G_c),

```math
G_aJ_{c,a}u
perp
J_{c,a}H_c.
```

Write

```math
L_{c,a}(u)
=
G_aJ_{c,a}u.
```

If (L_{c,a}(u)
e0), RPB-34 uses

```math
w_t
=
J_{c,a}u-tL_{c,a}(u)
```

and obtains

```math
langle G_aw_t,w_tangle
=
-2t|L_{c,a}(u)|^2
+
O(t^2).
```

Therefore, for all sufficiently small (t>0),

```math
oxed{
L_{c,a}(u)
e0
Longrightarrow
G_a
otsucceq0.
}
```

This conclusion is pointwise in the enlargement (a>c).  It does not require a derivative in (a), a spectral gap above zero, or a sign condition on the collar block.

---

## 2. RPB-49 removes the persistent-kernel alternative

RPB-49 proved that for every nonzero screw-core neutral source,

```math
oxed{
L_{c,a}(u)
=
G_aJ_{c,a}u

e0
qquad
(a>c).
}
```

Combining with Section 1 gives

```math
oxed{
0
e uinker G_c
Longrightarrow
G_a
otsucceq0
qquad
	ext{for every }a>c.
}
```

Thus any one nonzero endpoint screw-kernel direction is sufficient to force a strict negative direction at every strict enlargement.

The argument is stronger than an infinitesimal crossing statement: the old kernel vector has exactly zero diagonal form under zero extension, but its unavoidable off-diagonal collar leakage produces the negative test vector.

---

## 3. Positive-length neutral plateaus collapse

Suppose

```math
G_csucceq0,
qquad
ker G_c
e{0}.
```

A positive-length right neutral plateau would require some (b>c) such that the family remains nonnegative on the support interval immediately to the right of (c).

But choose any

```math
0
e uinker G_c.
```

Section 2 gives, for every (ain(c,b]),

```math
G_a
otsucceq0.
```

Contradiction.

Therefore

```math
oxed{
G_csucceq0,
quad
ker G_c
e0
Longrightarrow
	ext{there is no positive-length nonnegative/neutral right plateau from }c.
}
```

This is the **neutral-plateau collapse**.

It does not say that zero can never reappear as an eigenvalue at a later support after negativity has already appeared.  The statement is the support-filtration statement needed here: the endpoint cannot sit at the left edge of a nontrivial interval of continued nonnegativity.

---

## 4. Apply the collapse at the actual neutral edge

RPB-33 proved that at the actual neutral edge (c_*),

```math
G_{c_*}succeq0,
qquad
ker G_{c_*}
e{0}.
```

Therefore RPB-50 yields

```math
oxed{
G_a
otsucceq0
qquad
	ext{for every }a>c_*.
}
```

within the RPB support family.

So the neutral edge is an actual boundary of nonnegativity in the screw carrier.

No separate post-edge compact-tail mechanism is needed to prove the existence of right-side negativity once RPB-49 is available.

The endpoint attained-neutral vector may still exist at (c_*); what collapses is its interpretation as the beginning of a positive-length neutral plateau.

---

## 5. Exact selected-space subspace carried by the core

RPB-30 gives the neutral-resolvent isomorphism

```math
J_*:
E_*
=
ker(mathsf K_{c_*}-I)
overset{sim}{longrightarrow}
ker A_{c_*}.
```

RPB-32 gives

```math
ker A_{c_*}cap H_0^1(-c_*,c_*)
=
D^{-1}(ker G_{c_*}).
```

Define the selected core eigenspace

```math
oxed{
E_*^{m core}
:=
J_*^{-1}
left(
D^{-1}(ker G_{c_*})
ight)
subseteq
E_*.
}
```

RPB-33 implies

```math
oxed{
E_*^{m core}
e{0}.
}
```

For every nonzero (vin E_*^{m core}), its physical representative

```math
h_v
=
J_*v
```

lies in (H_0^1), and

```math
u_v
=
Dh_v
in
ker G_{c_*}setminus{0}.
```

RPB-49 therefore excludes strict null extension of this fixed physical representative.

Thus the unit-gain selected space contains an actual nonzero direction on which the null-extension question is already answered negatively.

---

## 6. What happens to the Birman--Schwinger budget on the right

On any right neighborhood where the RPB complementary-background decomposition remains valid with

```math
A_{B,a}succ0
```

and the same fixed finite selected packet is retained,

```math
A_{{m full},a}
=
A_{B,a}
-
Phi_a^*Phi_a.
```

The Birman--Schwinger operator is

```math
mathsf K_a
=
Phi_aA_{B,a}^{-1}Phi_a^*.
```

Section 4 supplies a negative direction of the full operator:

```math
A_{{m full},a}
otsucceq0.
```

Under the strict background gap this is equivalent to failure of the unit budget,

```math
oxed{
lambda_{max}(mathsf K_a)>1.
}
```

Hence the right-side branch enters the over-budget/negative morphology immediately wherever the fixed selected/background decomposition remains in force.

What is **not** proved is that the zero-extended endpoint selected vector itself remains an eigenvector of (mathsf K_a), or that the post-edge top eigenvector is frozen to one endpoint coordinate.  The selected eigendirection may rotate after the collar opens.

Therefore the custody conclusion is:

```math
oxed{
	ext{same fixed selected packet can carry immediate over-budget negativity,}
}
```

not

```math
oxed{
	ext{same endpoint selected eigenvector remains the post-edge eigenvector.}
}
```

---

## 7. Exact status of AZ-FIN-WEIL-NULL-EXTENSION

The canonical Horizon-1 interface is mode-wise.

It starts from a particular nonzero finite-exception unit-gain neutral physical mode

```math
kinker A_c
```

and asks whether the same zero-extended fixed relation satisfies the correct right-limit compact-window equation on a strict enlargement.

RPB-50 now separates two statements.

### 7.1 Core-restricted interface

If

```math
0
e k
in
ker A_ccap H_0^1(-c,c),
```

then by RPB-32

```math
Dkinker G_csetminus{0},
```

and RPB-49/RPB-35 give

```math
oxed{
widetilde k

otin
ker A_a
qquad
(a>c).
}
```

with the threshold-aware right-limit convention already built into the RPB-45--49 argument.

Therefore the **core-restricted** version of

```text
AZ-FIN-WEIL-NULL-EXTENSION
```

is discharged negatively.

### 7.2 Full Friedrichs mode-wise interface

RPB-33 proved existence of a nonzero core direction but deliberately did not prove

```math
dimker A_c
=
dimker G_c.
```

The residual defect is

```math
oxed{
delta_{m core}(c)
=
dimker A_c
-
dimker G_c
ge0.
}
```

If (delta_{m core}(c)>0), there can be Friedrichs zero modes outside (H_0^1) to which the screw-core exclusion has not yet been transferred.

Consequently the canonical interface, **as stated for an arbitrary carrier-identified Friedrichs neutral mode**, remains open.

Its open content has been sharply reduced:

```math
oxed{
	ext{the only remaining mode-wise gap is the zero-eigenspace core-lift/multiplicity defect.}
}
```

---

## 8. Why the remaining defect does not restore a neutral plateau

Suppose a noncore Friedrichs zero mode exists and even suppose, for the sake of the audit, that its zero extension remained a null vector at some larger support.

That would not restore nonnegativity.

RPB-33 supplies a nonzero core direction at the same endpoint, and RPB-49 forces that core direction to leak.  RPB-34 then produces a strict negative direction at the enlargement.

Therefore a larger support could at most be **indefinite with a surviving zero mode**.

It cannot be a continuation of the endpoint nonnegative neutral plateau.

Hence the two questions are now distinct:

```math
oxed{
egin{array}{ll}
	ext{plateau-level question:} & 	ext{closed negatively;}\[2mm]
	ext{arbitrary-mode null-extension question:} & 	ext{open only through }delta_{m core}.
end{array}
}
```

This distinction is the main bookkeeping result of RPB-50.

---

## 9. Consequence for the H1 neutral morphology

WD-T38/H1-P3.1 reaches an attained neutral endpoint mode and stops at the null-extension interface.

RPB-50 changes the experimental branch interpretation as follows.

The attained endpoint geometry remains valid:

```math
W_ck=0
```

under the WD-T38 hypotheses.

But at an actual neutral edge the existence of the screw-visible core kernel already forces strict right-side negativity.

Therefore the support-filtration morphology is no longer

```math
	ext{neutral endpoint}
longrightarrow
	ext{possibly positive-length neutral plateau}
longrightarrow
	ext{unknown exit}.
```

It is instead

```math
oxed{
	ext{neutral endpoint}
longrightarrow
	ext{immediate strict-right negative branch}.
}
```

This branch-level statement does not identify every endpoint neutral vector with a screw-core vector and therefore does not by itself rewrite the canonical WD-T38 theorem.

Promotion requires a separate audit.

---

## 10. RPB-50 determination

```math
oxed{
	extbf{RPB-50 — ONE NONZERO SCREW-CORE NEUTRAL DIRECTION IS ENOUGH TO COLLAPSE EVERY POSITIVE-LENGTH NEUTRAL PLATEAU; THE CORE-RESTRICTED NULL-EXTENSION INTERFACE IS DISCHARGED NEGATIVELY.}
}
```

Plateau collapse:

```math
oxed{
G_csucceq0,
quad
ker G_c
e0
Longrightarrow
G_a
otsucceq0
quad
(a>c).
}
```

Selected core subspace:

```math
oxed{
E_*^{m core}
=
J_*^{-1}
left(
D^{-1}ker G_{c_*}
ight)

e0.
}
```

Core-restricted null-extension discharge:

```math
oxed{
0
e kin
ker A_ccap H_0^1
Longrightarrow
widetilde k
otinker A_a
quad
(a>c).
}
```

Residual universal caveat:

```math
oxed{
delta_{m core}(c)
=
dimker A_c-dimker G_c
}
```

is the only remaining obstruction to promoting the negative answer from the core subspace to every Friedrichs neutral mode.

The canonical `AZ-FIN-WEIL-NULL-EXTENSION` entry is therefore **not promoted or closed in the stable theorem ledger by this pass**.  Its branch-local status is:

```text
CORE-RESTRICTED: DISCHARGED NEGATIVELY
FULL FRIEDRICHS MODE-WISE FORM: OPEN ONLY AT CORE-LIFT MULTIPLICITY
PLATEAU-LEVEL SUPPORT QUESTION: CLOSED NEGATIVELY
```

## Next cursor

```text
RPB-51 / ZERO-EIGENSPACE MULTIPLICITY AND CORE-LIFT AUDIT
```

The next pass should test the remaining equality

```math
dimker A_c
stackrel{?}{=}
dimker G_c
```

at the actual neutral edge, using Suzuki's generalized eigenvalue equivalence with full multiplicity bookkeeping rather than domain inclusion alone.

If equality is available, the full Friedrichs mode-wise null-extension interface is discharged negatively.  If not, the noncore zero-mode quotient must be isolated as the final irreducible residue.
