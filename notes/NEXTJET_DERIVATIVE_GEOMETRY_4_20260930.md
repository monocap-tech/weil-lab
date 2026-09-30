# NJDG-4 — critical-point-frame source audit

**Date:** 2026-09-30  
**Repository:** monocap-tech/weil-lab  
**Branch:** research/nextjet-derivative-geometry  
**Status:** **SOURCE AUDIT COMPLETE / NO HIT FOR EVERY-PACKET CRITICAL-POINT FRAME OR FORCED CONFLUENT LIFT / STRONGEST UNCONDITIONAL POINTWISE INPUT IS ONE-WAY DERIVATIVE-TO-ZETA PROXIMITY / STRONGEST MICROSCOPIC LOCAL LOG-DERIVATIVE INPUT LOCATED IS RH-CONDITIONAL / HIGHER-DERIVATIVE INPUTS REMAIN DENSITY OR MEAN-VALUE / NEXTJET NOT PROVED**  
**Parent:** NJDG-3  
**Canonical Key-C status:** unchanged

## 0. Admission test

NJDG-3 reduces a useful derivative-zero theorem to one of three forms.

### CPF — critical-point frame

For every admitted dangerous selected packet, produce derivative-critical points

[
	au_1,ldots,	au_q
]

in a controlled packet-scale neighborhood such that their critical-value rows recover the required RENJET jets with projective condition number.

At minimum for the first jet, two separated rows are needed unless a confluent substitute is supplied.

### MCP — multiple-critical/confluent lift

Force a configuration such as

[
zeta'(	au)=zeta''(	au)=0
]

or the corresponding completed-(Xi) condition, so the first logarithmic-derivative jet is fixed directly.

### DIRECT

Bound the canonical RENJET or frozen tower directly from derivative geometry without reconstructing its components.

The source must be compatible with the false-RH reductio and the complement-oblivious multiplier order.

## 1. Garaev–Yıldırım: pointwise but wrong direction

Garaev and Yıldırım prove unconditionally that for every zero

[
ho'=eta'+igamma'
]

of (zeta'), there exists a zero

[
ho=eta+igamma
]

of (zeta) such that

[
oxed{
|gamma-gamma'|
ll
sqrt{|eta'-1/2|}.
}
	ag{1}
]

This is genuinely pointwise and stronger than a density statement.

However its logical direction is

[
oxed{
zeta'	ext{-zero}
Longrightarrow
	ext{nearby zeta-zero ordinate}.
}
	ag{2}
]

NJDG needs essentially the inverse direction:

[
oxed{
	ext{prescribed dangerous zeta packet}
Longrightarrow
	ext{enough nearby derivative-critical rows}.
}
	ag{3}
]

Equation (1) does not invert.

Even if a derivative zero is independently known to exist, it supplies only one critical-value row and no lower bound on separation from a second row.

**Disposition:** POINTWISE / WRONG DIRECTION / ONE ROW.

## 2. Ki: exact microscopic scale but RH-conditional

Haseo Ki proves, assuming RH, that

[
liminf
(eta'-1/2)loggamma'

e0
]

is equivalent to the microscopic nearest-zero approximation

[
oxed{
rac{zeta'}{zeta}(s)
=
rac1{s-ho}
+
O(log t)
}
	ag{4}
]

uniformly for

[
|sigma-1/2|<c/log t,
]

where (ho) is the closest zeta zero.

This is extremely close to the scale required by NJDG:

[
	ext{physical spacing}asymp 1/log T.
]

But:

1. RH is an explicit hypothesis;
2. the theorem does not attach two derivative-critical points to every selected packet;
3. it does not give a projective critical-point-frame conditioning floor;
4. it does not directly control the second-resolvent RENJET statistic.

Therefore (4) is a structural control on the correct scale, not an admissible false-RH source input.

**Disposition:** MICROSCOPIC / HIGHLY RELEVANT / RH-CONDITIONAL.

## 3. Farmer–Ki: aggregate implication

Farmer and Ki prove that sufficiently many zeros of (zeta') close to the critical line force many closely spaced zeros of (zeta).

This is a global distribution implication:

[
	ext{many derivative zeros}
Longrightarrow
	ext{many close zeta zeros}.
]

It neither begins from one prescribed dangerous selected packet nor yields a local conditioned derivative frame.

**Disposition:** AGGREGATE / WRONG PACKET QUANTIFIER.

## 4. Levinson–Montgomery / Speiser lineage

The classical derivative-zero theory relates global counts of zeros of (zeta) and (zeta') on the left of the critical line and yields Speiser's equivalence.

Its strength is global topology/counting.

It does not provide:

- assignment of derivative zeros to one selected packet;
- packet-scale location;
- two-row separation;
- confluent multiplicity;
- second-resolvent jet data.

Thus it cannot cross CPF or MCP.

**Disposition:** GLOBAL COUNTING / NO FRAME.

## 5. Higher derivative sources

The higher-derivative source sweep located work including Das–Pujahari, which uses mollified mean values in short intervals and refines density estimates for zeros of higher derivatives.

The relevant outputs remain of types:

- mean value;
- zero density;
- almost-all clustering;
- asymptotic distribution.

None of the located statements forces, for every adversarial dangerous packet, a finite conditioned local derivative tower with the required jet order.

**Disposition:** HIGHER-DERIVATIVE / WRONG QUANTIFIER.

## 6. Guo / Feng / Zhang near-line lineage

The source sweep located the principal near-line bibliographic lineage:

- C. R. Guo, Proc. London Math. Soc. 72 (1996);
- Yitang Zhang, Duke Math. J. 110 (2001);
- Shaoji Feng, Acta Arith. 120 (2005);
- Haseo Ki, 2007.

This literature studies the horizontal/vertical distribution of (zeta')-zeros and their relation to zeta-zero spacing.

No located theorem in the present audit has the form

[
oxed{
	ext{every prescribed dangerous zeta packet}
Longrightarrow
	ext{two derivative-critical points with}
quad
|	au_1-	au_2|ge L^{-A}
}
	ag{5}
]

inside a controlled packet-scale neighborhood.

Nor did the audit locate a theorem forcing

[
zeta'(	au)=zeta''(	au)=0
]

or another confluent derivative configuration on every such packet.

**Disposition:** NEAREST LITERATURE / FRAME-SOURCE GATE NOT CROSSED.

## 7. Exact theorem matrix

| Source class | Pointwise? | Starts from prescribed zeta packet? | Produces 2+ critical rows? | Conditioning floor? | RENJET order? | NJDG result |
|---|---:|---:|---:|---:|---:|---|
| Garaev–Yıldırım proximity | YES | NO | NO | NO | NO | NO HIT |
| Speiser / Levinson–Montgomery | NO / global | NO | NO | NO | NO | NO HIT |
| Ki microscopic law | YES | partially local | NO | NO | first-resolvent | RH-CONDITIONAL |
| Farmer–Ki | NO / aggregate | NO | NO | NO | NO | NO HIT |
| Guo/Feng/Zhang distribution | distributional | NO located theorem | NO located theorem | NO | NO | NO HIT |
| Higher derivatives / density | NO / almost-all | NO | NO uniform frame | NO | higher derivative but averaged | NO HIT |
| Forced multiple critical point | would be YES | would need YES | confluent | n/a | potentially YES | NOT LOCATED |

## 8. Why one-way proximity cannot be inverted for free

Suppose a theorem says

[
orallho'in Z(zeta'),
quad
existshoin Z(zeta):
quad
|gamma-gamma'|lePhi(ho').
]

This implies a covering statement for the image of derivative zeros inside the zeta-zero set.

It does not imply surjectivity onto every chosen zeta zero or packet.

A single zeta zero may receive no derivative zero under such a relation while many derivative zeros attach to other zeta zeros.

Thus the quantifier reversal

[
orallho'existsho
quad
otRightarrowquad
orallhoexistsho'
]

is not licensed.

NJDG cannot use (1) to manufacture critical rows around the selected packet.

## 9. Why density of critical points does not provide a frame

Even a theorem giving the correct number of derivative zeros in a long window does not control the local interpolation condition number.

Two rows at

[
	au_1,	au_2
]

recover a first jet with cost

[
|	au_1-	au_2|^{-1}.
]

A density theorem permits severe local clustering and long local holes unless it includes a pointwise lower/upper spacing theorem at the packet scale.

Therefore:

[
oxed{
	ext{critical-point density}

otRightarrow
	ext{critical-point frame}.
}
	ag{6}
]

## 10. Why higher derivatives do not automatically solve confluence

A zero of (zeta'') near a zero of (zeta') is not the same as a common zero

[
zeta'(	au)=zeta''(	au)=0.
]

The latter directly lifts the logarithmic-derivative jet order; the former merely supplies another value at another point and reintroduces an interpolation-conditioning problem.

Thus an MCP source theorem must control actual simultaneous vanishing or an equivalent Hermite/confluent relation.

No such every-packet theorem was located.

## 11. NJDG-4 determination

- Unconditional pointwise derivative-to-zeta proximity theorem found: **YES**.
- It has the packet-to-derivative direction required by NJDG: **NO**.
- It supplies two conditioned critical rows: **NO**.
- Microscopic (1/log T)-scale logarithmic-derivative theorem found: **YES / Ki**.
- It is unconditional in a false-RH world: **NO / assumes RH**.
- Global Speiser/Levinson–Montgomery input supplies a packet-local frame: **NO**.
- Higher-derivative mean/density input supplies a packet-local confluent lift: **NO**.
- Located near-line literature supplies an every-packet separation floor for two critical rows: **NO HIT**.
- Located literature forces a multiple critical point on every dangerous packet: **NO HIT**.
- CPF gate crossed: **NO**.
- MCP gate crossed: **NO**.
- DIRECT derivative-to-RENJET theorem found: **NO**.
- NEXTJET proved: **NO**.
- KPH floor proved: **NO**.
- RH proved: **NO**.

## 12. Route consequence

The generic derivative-zero location route is at a source stop.

Do not repeat broad searches for:

- zeros of (zeta') near the line;
- Speiser equivalences;
- derivative-zero density;
- higher-derivative pair correlation;

unless a new source explicitly changes the packet-local quantifier or supplies jet conditioning.

The remaining derivative route is narrower:

[
oxed{
	ext{critical-value enrichment}
}
]

namely whether values of (zeta''), (Xi''), or logarithmic-derivative derivatives evaluated **at already located simple critical points** can provide the missing RENJET jet without requiring a second separated critical point.

This is not the same as searching for zeros of higher derivatives.

## 13. Next cursor

[
oxed{	ext{NJDG-5 / CRITICAL-VALUE ENRICHMENT AT SIMPLE DERIVATIVE ZEROS}}
]

Priority order:

1. derive exactly what (zeta''(	au)/zeta(	au)) or (Xi''(	au)/Xi(	au)) at a simple derivative zero determines about (A'_{F,Omega}(	au));
2. determine whether any unconditional pointwise theorem bounds these values at derivative zeros;
3. test transport from (	au) to the packet center (c) without introducing an uncontrolled separation denominator;
4. compare directly with the second-resolvent term in RENJET;
5. stop if the required (zeta'')-value estimate is merely another form of the missing RENJET bound.
