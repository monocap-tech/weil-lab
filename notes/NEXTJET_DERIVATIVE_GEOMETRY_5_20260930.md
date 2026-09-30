# NJDG-5 — critical-value enrichment at simple derivative zeros

**Date:** 2026-09-30  
**Repository:** monocap-tech/weil-lab  
**Branch:** `research/nextjet-derivative-geometry`  
**Status:** **COMPLETE ENRICHMENT AUDIT / SECOND-DERIVATIVE VALUE AT A SIMPLE DERIVATIVE ZERO DOES LIFT THE POLE-REMOVED FIELD BY ONE JET ORDER / NO TWO-CRITICAL-POINT INTERPOLATION IS THEN NEEDED FOR THAT FIELD JET / THE CURVATURE VALUE IS ITSELF SECOND-RESOLVENT DATA AND NO UNCONDITIONAL EVERY-CRITICAL-POINT BOUND WAS LOCATED / TRANSPORT TO THE PACKET CENTER AND THE MODE-WEIGHTED NEAR KERNEL REMAIN INDEPENDENT RESIDUALS / NEXTJET NOT PROVED**  
**Parent:** NJDG-4  
**Canonical Key-C status:** unchanged

## 0. Objective

NJDG-4 found no every-packet critical-point frame or forced confluent critical point.

NJDG-5 tests a narrower idea:

> If one simple derivative critical point is already available, can the value of the second derivative at that same point provide the missing first jet directly, avoiding the need for a second separated critical point?

For the pole-removed logarithmic-derivative field, the answer is **yes**.

For the full canonical RENJET, the answer is **not by itself**.

## 1. Zeta-prime critical curvature

Write

[
Xi(s)=H(s)zeta(s)
]

and

[
D(s)=rac{zeta'}{zeta}(s).
]

Let (	au) satisfy

[
zeta'(	au)=0,
qquad
zeta(	au)
e0.
]

Then

[
D(	au)=0.
]

Differentiate:

[
D'(s)
=
rac{zeta''}{zeta}(s)
-
left(rac{zeta'}{zeta}(s)ight)^2.
]

Hence at the critical point,

[
oxed{
D'(	au)
=
rac{zeta''(	au)}{zeta(	au)}.
}
	ag{1}
]

For the completed logarithmic derivative

[
U(s)=rac{Xi'}{Xi}(s)
=
rac{H'}H(s)+D(s),
]

we therefore obtain

[
oxed{
U'(	au)
=
left(rac{H'}Hight)'(	au)
+
rac{zeta''(	au)}{zeta(	au)}.
}
	ag{2}
]

Thus a second-derivative value at one simple (zeta')-zero supplies one exact first-jet row.

## 2. Exact pole-removed field jet at the critical point

Recall

[
A_{F,Omega}(z)
=
rac{Xi'}{Xi}(z)
-
sum_{hoin F}rac1{z-ho}
-
sum_{muinOmega}rac{m_mu}{z-mu}.
]

Differentiating,

[
A'_{F,Omega}(z)
=
left(rac{Xi'}{Xi}ight)'(z)
+
sum_{hoin F}rac1{(z-ho)^2}
+
sum_{muinOmega}
rac{m_mu}{(z-mu)^2}.
]

Using (2),

[
oxed{
A'_{F,Omega}(	au)
=
left(rac{H'}Hight)'(	au)
+
rac{zeta''(	au)}{zeta(	au)}
+
sum_{hoin F}rac1{(	au-ho)^2}
+
sum_{muinOmega}
rac{m_mu}{(	au-mu)^2}.
}
	ag{3}
]

The zeroth-order field value is already supplied by the critical-point equation:

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

Therefore the pair

[
left(
A_{F,Omega}(	au),
A'_{F,Omega}(	au)
ight)
]

is determined exactly from:

- the critical point (	au);
- selected and near zero locations;
- the completion factor;
- the single enriched value (zeta''(	au)/zeta(	au)).

This removes NJDG-3's need for a second critical point **for the field first jet at (	au)**.

## 3. Completed-Xi version

If instead

[
Xi'(	au)=0,
qquad
Xi(	au)
e0,
]

then

[
rac{Xi'}{Xi}(	au)=0
]

and

[
left(rac{Xi'}{Xi}ight)'(	au)
=
rac{Xi''(	au)}{Xi(	au)}.
]

Hence

[
oxed{
A'_{F,Omega}(	au)
=
rac{Xi''(	au)}{Xi(	au)}
+
sum_{hoin F}rac1{(	au-ho)^2}
+
sum_{muinOmega}
rac{m_mu}{(	au-mu)^2}.
}
	ag{5}
]

Again one enriched critical point gives one field first jet.

## 4. The curvature datum is already second-resolvent order

The gain in Sections 1–3 is real, but it is not free.

The logarithmic derivative of a canonical product has the schematic form

[
rac{Xi'}{Xi}(z)
=
sum_ho
left(
rac{m_ho}{z-ho}
+
	ext{canonical regularization}
ight)
+
	ext{entire term}.
]

Differentiating gives

[
oxed{
left(rac{Xi'}{Xi}ight)'(z)
=
-
sum_ho
rac{m_ho}{(z-ho)^2}
+
	ext{canonical regularized/completion term}.
}
	ag{6}
]

Thus the critical-curvature value

[
rac{zeta''(	au)}{zeta(	au)}
]

or

[
rac{Xi''(	au)}{Xi(	au)}
]

is itself second-resolvent information.

This is the **curvature–resolvent identity**.

Consequently a theorem giving a strong pointwise bound for critical curvature may already contain essentially the same local zero-interaction information that RENJET needs.

It must not be counted as a cheap lower-order input without an implication-strength audit.

## 5. Transport from the critical point to the packet center

The canonical first RENJET is evaluated at the selected packet center (c), not at (	au).

Since (A_{F,Omega}) is analytic after selected and near poles are removed,

[
A'_{F,Omega}(c)
-
A'_{F,Omega}(	au)
=
int_	au^c
A''_{F,Omega}(z),dz.
]

Therefore

[
oxed{
|A'_{F,Omega}(c)
-
A'_{F,Omega}(	au)|
le
|c-	au|
sup_U|A''_{F,Omega}|.
}
	ag{7}
]

Unlike the two-critical-point interpolation formula, (7) has no inverse-spacing denominator.

That is a genuine improvement.

However, the inherited SOURCE-II local derivative bounds are only projective. On the fixed physical window, the previously used second-derivative control is of logarithmic/projective size.

Thus packet-scale proximity

[
|c-	au|=O(L^{-1})
]

yields at best a bounded-order transport error from the existing generic estimate; it does not automatically produce the subordinate scale required by the final frozen source margin.

A useful theorem must improve at least one of:

1. proximity of (	au) to (c);
2. the pole-removed (A'') bound;
3. the final cancellation after transport.

## 6. The full first RENJET still contains another datum

The collision-safe first RENJET is

[
oxed{
mathfrak J_{F,Omega}[psi]
=
rac n2psi''(c)
+
(psi A_{F,Omega})'(c)
+
sum_{muinOmega}
m_mu K_psi(mu-c).
}
	ag{8}
]

Even if (3) or (5) controls the field jet perfectly, one still has

[
oxed{
mathcal K_{Omega,psi}
=
sum_{muinOmega}
m_mu K_psi(mu-c).
}
	ag{9}
]

For an exponential mode,

[
K_t(w)
=
rac{e^{tw}-1-tw}{w^2}.
]

This is an entire second-divided-difference kernel.

It is not determined by the unweighted critical-curvature value at (	au).

Equivalently, in the finite-part form,

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
	ag{10}
]

Critical curvature samples an unweighted second-resolvent field at (	au); equation (10) requires a **mode-weighted** second-resolvent statistic at (c).

Therefore enrichment removes one mismatch but not the whole RENJET deficit.

## 7. No pointwise critical-curvature theorem located

The NJDG-5 source sweep searched specifically for pointwise bounds on

[
rac{zeta''(ho')}{zeta(ho')},
qquad
zeta'(ho')=0,
]

or the corresponding completed-(Xi) quantity.

No unconditional theorem with an every-critical-point upper bound suitable for the dangerous-packet quantifier was located.

Neighboring source classes were:

- distribution/location of (zeta')-zeros;
- values of (zeta) at critical points;
- moments of (zeta) and its derivatives at critical-line extrema;
- zeros of higher derivatives;
- contour counts using (zeta''/zeta').

None supplies the required pointwise curvature row.

## 8. Pearce-Crump near miss

Pearce-Crump (2025) evaluates first moments of (zeta) and its derivatives at local extrema on the critical line.

This is notable because it shows that enriched derivative data at critical-type points can be treated analytically.

But the main extrema theorems:

- assume RH;
- average over many extrema;
- use zeros of the derivative of Hardy's (Z)-function / an auxiliary extrema function rather than arbitrary strip zeros of (zeta').

Thus this source does not provide NJDG's every-packet critical-curvature row.

## 9. Chorge near miss

Chorge studies extreme values of

[
|zeta(ho')|
]

where

[
zeta'(ho')=0
]

in the right half of the critical strip.

This uses the correct critical object, but it controls (zeta)-values rather than the curvature quotient

[
rac{zeta''(ho')}{zeta(ho')}.
]

No direct RENJET transfer follows.

## 10. Exact enrichment theorem interface

The successful part of NJDG-5 suggests a narrower possible external theorem.

### PCC — pointwise critical curvature

For every derivative critical point (	au) lawfully attached to an admitted dangerous selected packet, prove a projective pointwise estimate for

[
oxed{
rac{zeta''(	au)}{zeta(	au)}
}
]

or

[
oxed{
rac{Xi''(	au)}{Xi(	au)}.
}
]

The theorem must then be accompanied by:

1. packet-scale attachment of (	au);
2. transport control from (	au) to (c);
3. control or cancellation of the mode-weighted near kernel (9).

PCC alone does not close RENJET.

## 11. Implication-strength warning

Because of (6), a sufficiently strong PCC theorem may be equivalent in difficulty to a pointwise second-resolvent theorem for the actual zero divisor.

Therefore:

[
oxed{
	ext{critical-curvature bound}

ot	ext{ automatically weaker than}
	ext{ RENJET control}.
}
	ag{11}
]

The useful question is not whether the curvature can be named, but whether the critical-point equation gives additional arithmetic structure making that second-resolvent statistic easier than at a generic point.

No such theorem was located in this pass.

## 12. NJDG-5 determination

- (zeta''(	au)/zeta(	au)) at a simple (zeta')-zero gives the first logarithmic-derivative jet at (	au): **YES**.
- (Xi''(	au)/Xi(	au)) at a simple (Xi')-zero gives the completed first jet: **YES**.
- A second critical point is needed to reconstruct that field jet once curvature is known: **NO**.
- Transport to the packet center has an inverse-spacing loss: **NO**.
- Transport to the packet center has a higher-derivative/proximity loss: **YES**.
- Critical curvature is lower resolvent order than RENJET: **NO; it is second-resolvent order**.
- Critical curvature determines the mode-weighted near kernel: **NO**.
- Unconditional every-critical-point curvature bound located: **NO HIT**.
- Averaged enriched derivative results located: **YES**.
- They have the every-packet quantifier: **NO**.
- PCC alone closes RENJET: **NO**.
- NEXTJET proved: **NO**.
- KPH floor proved: **NO**.
- RH proved: **NO**.

## 13. Route consequence

Critical-value enrichment is a real structural improvement over NJDG-4:

[
oxed{
	ext{one critical point + curvature value}
Rightarrow
	ext{one full field first jet}.
}
]

But the remaining deficit is now specifically **mode-weighted curvature**:

[
	ext{unweighted second-resolvent critical curvature}
quad	ext{vs}quad
	ext{selected-mode-weighted second-resolvent RENJET}.
]

This is the next legitimate derivative-geometry seam.

## 14. Next cursor

[
oxed{
	ext{NJDG-6 / MODE-WEIGHTED CRITICAL-CURVATURE TRANSFER}
}
]

Priority order:

1. write the fixed two-mode RENJET kernel as a transform of second-resolvent curvature data;
2. determine whether the critical equation (D(	au)=0) gives a useful weighted identity after differentiation or interpolation in mode depth;
3. test whether two fixed SOURCE-II modes (t,u) allow elimination of the unweighted curvature debt without choosing modes from complement data;
4. compare with the multiplier-free complement wedge already extracted in LOTUS-SHADOW-7;
5. stop if the weighted curvature identity is merely the same complement wedge in new notation.
