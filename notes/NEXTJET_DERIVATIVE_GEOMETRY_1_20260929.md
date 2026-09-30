# NJDG-1 — local collision-to-derivative transfer trichotomy and quartet-axis no-go

**Date:** 2026-09-29  
**Repository:** monocap-tech/weil-lab  
**Branch:** research/nextjet-derivative-geometry  
**Status:** **COMPLETE LOCAL REDUCTION / ISOLATED SELECTED-EXTERIOR PAIR FORCES EITHER A PAIR-SCALE DERIVATIVE ZERO OR AN INVERSE-GAP COFACTOR FIELD / HIGHER CLUSTER IS THE ONLY FACTORIZATION ESCAPE / FUNCTIONAL-EQUATION QUARTET GEOMETRY DOES NOT FORCE A FORBIDDEN DERIVATIVE ZERO / EXISTING SPEISER-CLASS INPUTS REMAIN QUANTIFIER-MISMATCHED / NEXTJET NOT PROVED**  
**Parent:** NJDG-0  
**Canonical Key-C status:** unchanged

## 0. Objective

NJDG-0 opened the derivative-geometry route:

[
	ext{selected/exterior collision}
longrightarrow
	ext{derivative-zero geometry}
longrightarrow
	ext{possible actual-zeta exclusion}.
]

NJDG-1 asks the first local question exactly:

> If two actual zeta zeros approach at the scale that makes the weighted NEXTJET response large, what must the local derivative geometry do?

The pass separates the local analytic consequence from the much stronger global theorem that would be needed to close NEXTJET.

## 1. Local pair normalization

Let (f) denote either (zeta) in a high nontrivial-zero neighborhood or the completed (Xi) carrier in a corresponding local coordinate.

Suppose two simple zeros are

[
a=m-d,
qquad
b=m+d,
qquad
d
eq0.
]

Assume first that there is no other zero of (f) in the pair-scale disk and write

[
f(m+w)
=
(w^2-d^2)G(w),
]

where (G) is holomorphic and nonzero on a neighborhood of

[
|w|le |d|.
]

Set

[
h(w)
=
rac{G'(w)}{G(w)},
qquad
M
=
sup_{|w|le |d|}
|h(w)|.
]

Differentiating gives

[
rac{f'(m+w)}{G(w)}
=
2w
+
(w^2-d^2)h(w).
	ag{1}
]

Thus local derivative zeros away from (a,b) are zeros of the right side of (1).

## 2. Pair-capture lemma

### Lemma NJDG-1.1

If

[
M|d|<rac45,
	ag{2}
]

then (f') has exactly one zero in

[
|w|<rac{|d|}{2}.
	ag{3}
]

### Proof

On the circle

[
|w|=rac{|d|}{2},
]

the main term in (1) has modulus

[
|2w|=|d|.
]

The perturbation satisfies

[
|(w^2-d^2)h(w)|
le
Mleft(|w|^2+|d|^2ight)
=
rac54 M|d|^2.
]

Under (2),

[
rac54 M|d|^2
<
|d|
=
|2w|.
]

Rouché therefore gives the same number of zeros as (2w) inside the circle, namely one. Because the original pair lies at (|w|=|d|), this zero is a genuine derivative zero and not an original zero. (square)

## 3. Exact local trichotomy

Let the full selected/exterior gap be

[
Delta=|a-b|=2|d|.
]

For any close selected/exterior pair, one of the following occurs.

### Branch C1 — higher cluster

There is another zero of (f) in the pair-scale disk, so the two-zero cofactor (G) is not zero-free there.

This means the NEXTJET collision is part of a higher local cluster rather than an isolated pair.

### Branch C2 — derivative capture

The pair is isolated and

[
M|d|<rac45.
]

Then NJDG-1.1 gives a derivative zero in the midpoint disk

[
|z-m|<rac{Delta}{4}.
]

### Branch C3 — cofactor blow-up

The pair is isolated but derivative capture is not licensed by the lemma. Then necessarily

[
M
ge
rac{4}{5|d|}
=
rac{8}{5Delta}.
	ag{4}
]

Thus the zero-free cofactor logarithmic derivative is itself of inverse-gap size.

Therefore:

[
oxed{
	ext{close selected/exterior pair}
Longrightarrow
	ext{higher cluster}
 lor	ext{pair-scale derivative zero}
 lorsupleft|rac{G'}Gight|
gtrsim
Delta^{-1}.
}
	ag{5}
]

Equation (5) is the **collision-transfer trichotomy**.

## 4. Relation to NEXTJET scale

For a selected dangerous coefficient (v_j
eq0), canonical Key-C custody gives the local response

[
R_v(mu)
=
rac{v_j}{mu-ho_j}
+
O(1).
]

Hence a selected/exterior gap (Delta) contributes at scale

[
|R_v(mu)|
asymp
Delta^{-1}
]

unless compensated by the remaining selected packet.

The cofactor blow-up branch (4) therefore lands at the same inverse-gap scale:

[
oxed{
	ext{NEXTJET collision size}
sim
	ext{cofactor logarithmic-derivative size}.
}
	ag{6}
]

This is not a contradiction. It is a localization of where the same microscopic debt can move.

## 5. Why derivative capture is not yet a forbidden event

Derivative capture in (3) gives a nearby zero of (f'), but several tempting conclusions are invalid.

### 5.1 Functional-equation reflected pair

For the same-height reflected pair about the critical line, write the centered coordinate (w) so that the pair is

[
w=pm a.
]

The pair factor is

[
p(w)=w^2-a^2,
]

and

[
p'(w)=2w.
]

Its derivative zero is exactly

[
w=0,
]

on the critical line.

So even perfect local derivative capture can land on the symmetry axis rather than in a forbidden off-axis region.

### 5.2 Full quartet hostile control

The externally located hostile audit
`ashaffer/riemann-zeta@ca617bed2607aec5dd0c7e2664d7ecbbdd0c1778`
records the exact polynomial

[
Q_{a,gamma}(z)
=
((z-igamma)^2-a^2)
((z+igamma)^2-a^2),
]

whose zeros are the off-axis quartet

[
pm apm igamma,
]

while

[
Q'_{a,gamma}(z)
=
4z(z^2+gamma^2-a^2)
]

has only axial critical points when (gamma>a).

Thus:

[
oxed{
	ext{off-axis quartet}

otRightarrow
	ext{off-axis derivative zero}.
}
	ag{7}
]

This is the **quartet-axis countercontrol**.

### 5.3 (Xi') versus (zeta')

If the local factor is taken in (Xi), a zero of (Xi') is not a zero of (zeta').

Writing

[
Xi=Hzeta,
]

one has

[
rac{Xi'}{Xi}
=
rac{H'}H
+
rac{zeta'}zeta.
]

Therefore

[
zeta'(s)=0
]

requires

[
rac{Xi'}{Xi}(s)
=
rac{H'}H(s),
]

not (Xi'(s)=0).

The gamma/completion field is of logarithmic size at high height and cannot be silently discarded.

For NJDG purposes it is therefore cleaner to apply the local pair lemma directly to (zeta) when testing Speiser-type consequences.

## 6. Speiser-class quantifier audit

The external hostile audit also records the classical derivative-zero route in the form

[
N_1^-(T)
=
N^-(T)
+
O(log T),
]

together with Speiser's qualitative equivalence.

For NJDG the key point is quantifier, not the exact historical constant.

One selected/exterior collision contributes only a bounded amount of zero multiplicity. An (O(log T)) global count discrepancy can absorb that event at arbitrarily large height.

Likewise, long-interval derivative-zero density estimates remain compatible with one sparse derivative zero.

Therefore:

[
oxed{
	ext{one captured derivative zero}

otRightarrow
	ext{contradiction with current aggregate derivative-zero counts}.
}
	ag{8}
]

NJDG-1 does not import the external audit as canonical theorem custody; it uses it as a hostile search-space control consistent with the direct local calculation above.

## 7. What would actually close one branch

The trichotomy (5) shows that derivative geometry can help only if one of the following new actual-zeta inputs exists.

### DGT-A — pair-scale derivative exclusion

A pointwise theorem forbidding the derivative-capture configuration produced by an admitted dangerous selected/exterior pair.

It must act at the unfolded (O(1)), equivalently physical (O(1/log T)), scale and cannot merely be average in height.

### DGT-B — cofactor field bound

A pointwise projective upper bound

[
sup_{	ext{pair disk}}
left|rac{G'}Gight|
le
H^{O(1)}
]

strong enough that a superprojectively small selected/exterior gap forces Branch C2.

This still requires DGT-A or another contradiction after capture.

### DGT-C — cluster replication / rigidity

A theorem saying the higher-cluster branch C1 cannot occur on an admitted KPH-dangerous packet, or that it forces enough derivative/original zeros to violate an independent local density law.

The theorem must be multiplicity-aware and worst-packet, not density-one.

### DGT-D — direct signed cancellation

A theorem allowing C1-C3 individually but controlling the final signed weighted NEXTJET combination anyway.

This bypasses derivative-zero location entirely.

## 8. Comparison with the original hope

The initial NJDG hope was

[
	ext{NEXTJET collision}
	o
	ext{forbidden derivative zero}.
]

NJDG-1 replaces it by the exact weaker statement

[
oxed{
	ext{NEXTJET collision}
	o
left[
	ext{higher cluster}
lor
	ext{nearby derivative zero}
lor
	ext{inverse-gap cofactor field}
ight].
}
	ag{9}
]

The missing theorem has not disappeared. It has been localized.

This is useful because the three exits are now mathematically distinct and can be screened separately.

## 9. Determination

- Pair-scale local factorization obtained: **YES**.
- Isolated close pair with moderate cofactor forces a derivative zero: **YES**.
- Explicit constant (4/5) obtained by Rouché on the half-gap circle: **YES**.
- Failure of derivative capture forces inverse-gap cofactor size: **YES**.
- Another nearby zero is the only factorization escape: **YES**.
- Functional-equation quartet alone forces an off-axis derivative zero: **NO**.
- A captured (Xi')-zero is automatically a (zeta')-zero: **NO**.
- Existing aggregate Speiser/derivative-density input excludes one captured offender: **NO**.
- NEXTJET proved: **NO**.
- KPH floor proved: **NO**.
- RH proved: **NO**.

## 10. Next cursor

[
oxed{	ext{NJDG-2 / COFACTOR BLOW-UP AND CLUSTER-BRANCH AUDIT}}
]

Priority order:

1. express the cofactor field (G'/G) in canonical zero/pole/completion coordinates after removing the selected/exterior pair;
2. determine whether existing local logarithmic-derivative estimates already control it at projective scale on admitted packets;
3. test whether the higher-cluster branch is already covered by G2C collision/reblocking or is genuinely an unselected-complement phenomenon;
4. identify any exact implication from cofactor blow-up to the existing SOURCE-II jet tower;
5. stop if the result only renames NEXTJET in logarithmic-derivative coordinates.
