# NJDG-3 — derivative-to-RENJET value/jet and resolvent-order audit

**Date:** 2026-09-30  
**Repository:** monocap-tech/weil-lab  
**Branch:** research/nextjet-derivative-geometry  
**Status:** **COMPLETE INTERFACE REDUCTION / ONE ORDINARY ZETA-PRIME OR XI-PRIME ZERO SUPPLIES ONLY A VALUE ROW FOR THE POLE-REMOVED LOGARITHMIC DERIVATIVE / THE FIRST CANONICAL RENJET REQUIRES A FIRST JET PLUS A SECOND-RESOLVENT NEAR STATISTIC / TWO CRITICAL POINTS CAN RECOVER THE FIRST JET ONLY WITH INVERSE-SPACING CONDITIONING / A MULTIPLE CRITICAL POINT CAN LIFT ONE JET ORDER BUT IS NOT FORCED / NO DIRECT DERIVATIVE-TO-RENJET THEOREM LOCATED / NEXTJET NOT PROVED**  
**Parent:** NJDG-2  
**Canonical Key-C status:** unchanged

## 0. Objective

NJDG-2 established that derivative geometry is load-bearing only if it controls the canonical collision-safe joint renormalized jet

[
mathfrak J_{F,Omega}[psi]
=
rac n2psi''(c)
+
(psi A_{F,Omega})'(c)
+
sum_{muinOmega}m_mu K_psi(mu-c).
	ag{1}
]

NJDG-3 asks what an actual zero of (zeta') or (Xi') determines about the field

[
A_{F,Omega}(z)
=
rac{Xi'}{Xi}(z)
-
sum_{hoin F}rac1{z-ho}
-
sum_{muinOmega}rac{m_mu}{z-mu}.
	ag{2}
]

The answer is one jet order too weak in the generic simple critical-point case.

## 1. Zeta-prime critical-value row

Write

[
Xi(s)=H(s)zeta(s),
]

where (H) is the standard nonzero completion factor in the local nontrivial-zero region.

At a point (	au) with

[
zeta'(	au)=0,
qquad
zeta(	au)
e0,
]

we have

[
rac{zeta'}{zeta}(	au)=0
]

and therefore

[
oxed{
rac{Xi'}{Xi}(	au)
=
rac{H'}H(	au).
}
	ag{3}
]

Substituting into (2),

[
oxed{
A_{F,Omega}(	au)
=
rac{H'}H(	au)
-
sum_{hoin F}rac1{	au-ho}
-
sum_{muinOmega}rac{m_mu}{	au-mu}.
}
	ag{4}
]

Thus one ordinary (zeta')-zero supplies one exact **critical-value row**.

It determines a value of the pole-removed field, not its derivative.

## 2. Xi-prime critical-value row

At a point (	au) with

[
Xi'(	au)=0,
qquad
Xi(	au)
e0,
]

we have

[
rac{Xi'}{Xi}(	au)=0,
]

hence

[
oxed{
A_{F,Omega}(	au)
=
-
sum_{hoin F}rac1{	au-ho}
-
sum_{muinOmega}rac{m_mu}{	au-mu}.
}
	ag{5}
]

Again the information is a value row.

The completion term disappears in this version, but the jet order does not improve.

## 3. The first RENJET needs a derivative row

Expanding the native field term in (1),

[
oxed{
(psi A_{F,Omega})'(c)
=
psi'(c)A_{F,Omega}(c)
+
psi(c)A_{F,Omega}'(c).
}
	ag{6}
]

The ordinary critical-point identities (4) or (5) do not determine

[
A_{F,Omega}'(c).
]

This is the **value-to-jet gap**.

At the level of analytic data, one value condition cannot control the derivative functional without an additional theorem.

A simple functional-data control makes the point precise. If (A) is any local analytic field satisfying

[
A(	au)=a,
]

then

[
widetilde A_lambda(z)
=
A(z)+lambda(z-	au)
]

has the same critical-value row

[
widetilde A_lambda(	au)=a
]

while

[
widetilde A_lambda'(c)
=
A'(c)+lambda.
]

This is not a deformation of actual zeta and is not an actual-zeta counterexample. It proves only that the critical-value row, as a datum type, does not algebraically determine the first jet.

## 4. Two critical points and interpolation conditioning

Suppose two critical points

[
	au_1,	au_2
]

supply exact field values

[
A(	au_i)=a_i.
]

Let

[
d_i=	au_i-c
]

and suppose

[
|d_i|le r.
]

Taylor expansion gives

[
a_i
=
A(c)+A'(c)d_i+R_i,
]

with

[
|R_i|
le
rac12 M_2|d_i|^2,
qquad
M_2=sup_U|A''|.
]

Subtracting the two equations,

[
oxed{
A'(c)
=
rac{a_1-a_2}{	au_1-	au_2}
-
rac{R_1-R_2}{	au_1-	au_2}.
}
	ag{7}
]

Hence

[
oxed{
|A'(c)|
le
rac{|a_1-a_2|}{|	au_1-	au_2|}
+
rac{M_2r^2}{|	au_1-	au_2|}.
}
	ag{8}
]

Therefore two critical points can form a **critical-point frame**, but its first-jet reconstruction has inverse-spacing cost

[
|	au_1-	au_2|^{-1}.
]

A useful every-packet theorem must therefore provide at least:

1. two lawful critical points in a controlled packet-scale neighborhood;
2. a projective lower separation between them or an equivalent confluent/Hermite replacement;
3. a projective bound on the relevant critical-value difference;
4. a projective (A'') bound on the interpolation region.

Existence or density of critical points alone does not provide this package.

## 5. Symmetry does not supply a uniform frame

The functional equation can generate reflected critical-point symmetry for (Xi').

But a reflected pair may approach the symmetry axis, making

[
|	au_1-	au_2|
	o0.
]

Equation (8) then loses exactly through the inverse-spacing factor.

Thus symmetry can provide two rows without providing a uniformly conditioned frame.

This is the derivative-zero analogue of the interpolation-conditioning problem already seen in Cauchy/Hermite packet geometry.

## 6. Multiple critical points lift one jet order

There is one exact special case.

If

[
zeta'(	au)=0,
qquad
zeta''(	au)=0,
qquad
zeta(	au)
e0,
]

then

[
left(rac{zeta'}{zeta}ight)'(	au)
=
rac{zeta''}{zeta}(	au)
-
left(rac{zeta'}{zeta}(	au)ight)^2
=
0.
]

Hence

[
oxed{
left(rac{Xi'}{Xi}ight)'(	au)
=
left(rac{H'}Hight)'(	au).
}
	ag{9}
]

Differentiating (2),

[
A_{F,Omega}'(	au)
=
left(rac{Xi'}{Xi}ight)'(	au)
+
sum_{hoin F}rac1{(	au-ho)^2}
+
sum_{muinOmega}
rac{m_mu}{(	au-mu)^2}.
]

Therefore

[
oxed{
A_{F,Omega}'(	au)
=
left(rac{H'}Hight)'(	au)
+
sum_{hoin F}rac1{(	au-ho)^2}
+
sum_{muinOmega}
rac{m_mu}{(	au-mu)^2}.
}
	ag{10}
]

Likewise, if

[
Xi'(	au)=Xi''(	au)=0,
qquad
Xi(	au)
e0,
]

then

[
oxed{
A_{F,Omega}'(	au)
=
sum_{hoin F}rac1{(	au-ho)^2}
+
sum_{muinOmega}
rac{m_mu}{(	au-mu)^2}.
}
	ag{11}
]

Thus a multiple critical point supplies a **multiple-critical-point lift** of one jet order.

But no retained theorem forces such a multiple critical point for every admitted KPH-dangerous packet.

So (10)--(11) are exact interfaces, not progress on the canonical gate.

## 7. The second mismatch: resolvent order

Even if (A_{F,Omega}'(c)) were controlled, the full first RENJET also contains

[
sum_{muinOmega}
m_mu K_psi(mu-c).
	ag{12}
]

In the equivalent finite-part form,

[
mathfrak J_{F,Omega}[psi]
=
rac n2psi''(c)
+
(psi B_F)'(c)
+
sum_{muinOmega}
m_mu
rac{psi(mu)}{(mu-c)^2}.
	ag{13}
]

A critical-value equation such as (4) naturally sees first-resolvent data

[
sum_
u rac{m_
u}{	au-
u}.
]

Equation (13) contains a second-resolvent / second-divided-difference statistic.

Therefore there is also a **resolvent-order gap**:

[
oxed{
	ext{critical-point value equation}

otRightarrow
	ext{second-resolvent RENJET control}
}
	ag{14}
]

without an additional differentiated or interpolated theorem.

This is independent of the value-to-jet gap.

## 8. Consequence for higher derivative towers

One might try to iterate

[
zeta',
zeta'',
zeta''',
ldots
]

or

[
Xi',
Xi'',
Xi''',
ldots
]

to obtain progressively higher rows.

The exact lesson is:

- a zero of the first derivative gives a zeroth-order logarithmic-derivative value row;
- a common zero of the first two derivatives can give a first-jet row;
- higher simultaneous derivative vanishing can supply still higher local jets.

But ordinary zeros of successive derivative functions at unrelated points do not automatically form a uniformly conditioned jet frame at the original packet center.

Thus a derivative tower becomes useful only through a theorem that controls:

[
oxed{
	ext{location}
+
	ext{separation/confluence}
+
	ext{jet order}
+
	ext{uniform conditioning}.
}
	ag{15}
]

No such every-dangerous-packet theorem was located in the GitHub source sweep used for NJDG-3.

## 9. Relation to the frozen multiplier order

The critical-point frame, if supplied externally, may be read after the multiplier

[
psi_*^{m tot}
]

is frozen.

That does not violate SOURCE-II selection order.

However the theorem may not use the observed critical-point configuration to choose a new multiplier and then import the old selected-only source margin.

So the lawful order would be:

1. selected packet/channel fixed;
2. selected-only multiplier fixed;
3. derivative-critical geometry read;
4. critical-point frame theorem applied to the already-fixed (psi_*);
5. RENJET/tower estimate obtained.

This leaves the route logically open but prevents adaptive critical-point interpolation from being used to redesign the source.

## 10. External-source disposition

The NJDG GitHub sweep found:

- classical/global Speiser-type derivative-zero information;
- aggregate and form-factor information for (Xi'), (Xi''), and higher derivatives;
- numerical zero-location infrastructure;
- hostile audits explicitly identifying microscopic local-density and conditioning as the missing layer.

It did not locate a theorem with the package (15) for every admitted actual packet.

This is a bounded source determination for the present sweep, not a literature-exhaustion theorem.

## 11. NJDG-3 determination

- One ordinary (zeta')-zero gives an exact value row for (A_{F,Omega}): **YES**.
- One ordinary (Xi')-zero gives an exact value row: **YES**.
- One such row determines (A_{F,Omega}'(c)): **NO**.
- Two critical points can reconstruct a first jet with inverse-spacing conditioning: **YES**.
- Symmetry guarantees a uniformly separated critical-point frame: **NO**.
- A multiple critical point can lift one jet order exactly: **YES**.
- Every dangerous packet forces such a multiple critical point: **NO**.
- Critical-point equations directly control the second-resolvent RENJET term: **NO**.
- A derivative tower is useful without a conditioned local frame theorem: **NO**.
- Frozen multiplier order is compatible with a future external critical-point-frame theorem: **YES**.
- Direct derivative-to-RENJET transfer proved: **NO**.
- NEXTJET proved: **NO**.
- KPH floor proved: **NO**.
- RH proved: **NO**.

## 12. Route consequence

The derivative-zero route is now reduced to a precise external theorem class.

A successful theorem must provide either:

### CPF — critical-point frame

A uniformly conditioned local set of derivative-critical rows strong enough to reconstruct the required RENJET jets and second-resolvent statistic at projective cost.

or:

### MCP — multiple-critical-point / confluent lift

A forced confluent derivative configuration carrying enough jet information directly, with every-packet control.

or:

### DIRECT

A theorem using derivative-zero geometry to bound the full joint RENJET/tower without reconstructing its components.

Anything that supplies only existence, density, pair correlation, or one critical point remains insufficient.

## 13. Next cursor

[
oxed{	ext{NJDG-4 / CRITICAL-POINT FRAME SOURCE AUDIT}}
]

Priority order:

1. search specifically for pointwise local theorems linking a zeta zero cluster to two or more nearby (zeta')/(Xi') critical points;
2. require explicit scale and separation, not only existence;
3. inspect confluent/multiple-critical-point theorems as an alternative to separation;
4. test whether any theorem controls the second-resolvent order needed by RENJET;
5. stop if all located results remain average, density, or RH-conditional in a way unusable inside the false-RH reductio.
