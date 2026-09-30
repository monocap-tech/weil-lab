# SZ edge recurrence 103 — closure of the post-s15 formula window by seventeenth returns

**Date:** 2026-09-29  
**Branch:** sz-cross-collar  
**Standing:** UNRATIFIED RESIDUE / ONE NF PASS / SCOPED POSITIVE RESULT  
**Canonical parent:** SZ-CROSS-COLLAR-3, unchanged  
**Entry commit:** 26cc010882c02069da2d7298f530e710f116db58  
**Public promotion:** forbidden

## 0. Result and scope

The changed GERM-102 fifteenth map (J_2) is retained. Its complete sixteenth maps induce a (5/6)-return system on a new seventeenth section. Thirteen distinct complete returns admit two fixed-parameter rational cone charts. This closes the entire remaining GERM-102 formula window through (z=	au_{14}).

Write

[
arepsilon=z-s_{15}=e-e_{102}.
]

The new scalar-source result is

[
oxed{
0<arepsilonle t_{15}
quadLongrightarrowquad
x_{m source}=0
	ext{ in both scalar parity kernels}.
}
]

Under the inherited ambient equivalence and coverage,

[
oxed{
L_{103}=L_{102}+t_{15}
=log!left(rac{3^{616630565}}{2^{701561468}5^{118769764}}ight)
=1.711212516168914336902071568215382674601877004879ldots.
}
]

The increment is

[
t_{15}=0.000000000000027242875184250140717788943911118422ldots.
]

The endpoint is checked directly. This remains a scoped, unratified source-equation result.

## 1. Custody

GERM-102's verifier is pinned by SHA-256

```text
bc9f783b9c9c89072e5c6a468cf29d3dd98e85299bd9cf3cb274f078ea247a5e
```

and was replayed with assertions enabled. Its stdout matched the GERM-102 receipt byte for byte.

The GERM-103 verifier uses the inherited (10^{240}) rational grid and 800-term logarithm-series stack. No lower source equation is replaced by midpoint data or an assumed determinant value.

## 2. Four sixteenth maps

All (H_1,J_1,J_2) below retain their GERM-102 fifteenth definitions. Define the GERM-103-local sixteenth maps

[
A_0=H_1^3J_1,qquad
A_1=H_1^3J_2,qquad
B_0=H_1^4J_1,qquad
B_1=H_1^4J_2.
]

The (A)-maps are the four-step sixteenth returns and the (B)-maps the five-step returns. The suffix records whether the initial fifteenth source lies outside or inside the newly active interval (0<y<arepsilon).

All four are hyperbolic as complete sixteenth returns even though (J_2) itself enters from the changed source branch. Every intermediate fifteenth argument and first-return condition is checked on

[
0<arepsilonle t_{15}.
]

At (arepsilon=0), (A_0/B_0) recover the GERM-102 endpoint representation. At (arepsilon=t_{15}), only (A_1/B_1) survive.

## 3. Seventeenth section

Retain the GERM-102 sixteenth circle length (t_{15}) and put

[
c_{16}=t_{15}-ho_{16},
]

[
ho_{17}=t_{15}-5c_{16},
qquad
c_{17}=c_{16}-ho_{17}.
]

Exact arithmetic gives

[
0<ho_{17}<c_{16},
qquad
5c_{17}+6ho_{17}=t_{15}.
]

Use

[
K_{17}=(0,c_{16}).
]

The induced map is

[
oxed{
S_{17}(y)=y+ho_{17}pmod{c_{16}},
}
]

with return time five when (y<c_{17}) and six when (y>c_{17}). The two translation branches tile the section, hence the induced map is invertible and Lebesgue-measure preserving.

## 4. Complete legal words

For

[
0<arepsilonle c_{16},
]

all later pre-return sixteenth sources remain exterior. Only the initial source can switch:

[
oxed{
B_0^{N-1}A_i,
qquad iin{0,1},quad Nin{5,6}.
}
]

For

[
c_{16}learepsilonle t_{15},
]

the initial source always uses (A_1), while later sources descend and the internal (B_1)-visits form a final consecutive run:

[
oxed{
B_1^sB_0^{N-s-1}A_1,
qquad Nin{5,6},quad0le s<N.
}
]

The two (s=0) products are shared between the low and high libraries. Therefore there are **13 distinct temporal products and 15 parameter/chart tests**.

The chart junction (arepsilon=c_{16}) is checked in both charts. At the formula endpoint (arepsilon=t_{15}), the surviving complete returns are

[
B_1^4A_1,qquad B_1^5A_1.
]

Both endpoint faces pass directly. The chronology follows the actual source locations; no favorable matrices are inserted or reordered.

## 5. Two rational cone charts

Use

[
C_{m low}=
egin{pmatrix}
1&1\
-2827/2000&-27/20
end{pmatrix},
qquad
det C_{m low}=rac{127}{2000},
]

and

[
C_{m high}=
egin{pmatrix}
1&1\
-279/200&-283/200
end{pmatrix},
qquad
det C_{m high}=-rac1{50}.
]

The low chart is selected for (arepsilonle c_{16}), the high chart for (arepsilonge c_{16}), and the chosen chart remains fixed along each orbit. Both work at the junction.

After retaining the certified overall signs, every required conjugate is strictly positive. The weakest certified forward factor is

[
>21.2185157340,
]

and the weakest backward factor is

[
>20.5144189739.
]

Hence the deliberately weakened common estimate is

[
oxed{
|widehat Mv|_1ge20|v|_1
quad(vin C_+),
qquad
|widehat M^{-1}v|_1ge20|v|_1
quad(vin C_-).
}
]

The actual overall signs remain in the recurrence. Hyperbolicity alone is not used as the cone proof.

A five-step seventeenth return contains 2,271,842,500,980 original rotation steps; a six-step return contains 2,743,334,531,329. These are temporal product lengths of (2	imes2) matrices, not independent coordinates.

## 6. (L^2) exclusion

For an actual scalar source, restrict the inherited two-coordinate field to (K_{17}) and apply the fixed chart appropriate to the parameter. Restriction, translation, and the invertible chart preserve (L^2).

The source equations and checked substitutions give the signed seventeenth recurrence almost everywhere. Remove inherited exceptional sets and the required countable preimages before iteration. Forward same-sign and backward opposite-sign cone expansion, together with measure preservation, force the transformed field to vanish almost everywhere.

The seventeenth towers cover the sixteenth circle. Invertibility then propagates zero through the fifteenth, fourteenth, and lower return hierarchy and through the inherited finite reconstruction to the scalar source. No arbitrary-vector surjectivity is assumed.

## 7. Endpoint arithmetic and remaining scope

Exact arithmetic gives

[
L_{103}=(-701561468,616630565,-118769764)
]

in the ordered ((log2,log3,log5)) basis, and

[
e_{103}=147080066h-28310302k.
]

The GERM-102 fourteenth/fifteenth formula remainder is now **zero**.

The still-licensed GERM-100 eleventh formula remainder is

[
omega_{11}
=0.000000000020893371365682198926433019186282259509ldots.
]

The remaining width before (e=3h) is

[
3h-e_{103}
=0.000031477398428669305491066588424613339713993483ldots.
]

The full unresolved four-delay interval remains (L_{103}<Llelog6). None of those larger intervals is claimed closed.

## 8. Exact next source change

Immediately above (z=	au_{14}), equivalently above the GERM-101 formula endpoint (b=ho_{12}), the ten-step twelfth return acquires an interior final eleventh source.

On the first source strip

[
0<q<b-ho_{12},
]

the chronological word changes to nine GERM-100-local (A_1) steps followed by (B_1):

[
oxed{
J_{12,m next}=B_1A_1^9.
}
]

The verifier checks the literal lower source contracts on an interior activation strip. Its determinant encloses one and

[
0.7071860460
<
operatorname{tr}J_{12,m next}
<
0.7071860461,
]

with

[
-3.4998878964
<
(operatorname{tr}J_{12,m next})^2-4det J_{12,m next}
<
-3.4998878963.
]

It is elliptic. This is a newly changed **twelfth source species beyond the completed GERM-102 formula window**, not an unhandled seventeenth return inside it. No exclusion above (L_{103}) is issued.

## 9. Stopping state

The GERM-103 verifier completed successfully. It checks the parent GERM-102 source geometry, all four new sixteenth formula cells, all 15 seventeenth source/chart cells, entry and endpoint faces, the chart junction, the next lower-level source guard, determinant enclosures, and independent endpoint arithmetic.

No eighteenth section or additional retained coordinate is used. Full earlier symbolic suites, the complete GERM-60 ambient reduction, and old large determinant inventories were not rerun. This is not Lean certification or canonical ratification.

```text
GERM-103: COMPLETE AS A SCOPED EXPERIMENTAL PASS
NEW EXCLUSION: 0<epsilon<=t15, epsilon=e-e102
SIXTEENTH FORMULAS: A0/A1/B0/B1 THROUGH THE FULL REMAINING GERM-102 WINDOW
SEVENTEENTH PROOF: 13 DISTINCT WORDS / 15 TESTS / TWO RATIONAL CHARTS
COMMON CONE FACTOR: 20
GERM-102 FORMULA WINDOW: CLOSED THROUGH z=tau14
EXPERIMENTAL ENDPOINT: log(3^616630565/(2^701561468*5^118769764))
NEXT TWELFTH WORD: GERM-100-LOCAL B1 A1^9; ELLIPTIC
GERM-104 / POST-z=TAU14 TWELFTH FINAL-VISIT TRANSFER: NOT EXECUTED
CANONICAL CURSOR: SZ-CROSS-COLLAR-3, UNCHANGED
RATIFICATION / PUBLIC PROMOTION: NONE
```
