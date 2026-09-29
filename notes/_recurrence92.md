# SZ edge recurrence 92 — double-F20 nonwrap and direct eighth-return control

**Date:** 2026-09-28  
**Branch:** sz-cross-collar  
**Standing:** UNRATIFIED RESIDUE / ONE NF PASS / SCOPED POSITIVE RESULT  
**Canonical parent:** SZ-CROSS-COLLAR-3, unchanged  
**Entry commit:** 23c019e7e9caf103d5ccc3f8b6f38f0b9f8eceec  
**Public promotion:** forbidden

## 0. Result and exact scope

The elliptic double-F20 nonwrap U2 is retained. Its complete eighth returns with the legally required neighboring maps have a common signed rational cone. Three maps suffice; no ninth or deeper induction and no additional retained coordinate are needed.

Put b=e-e91=d-(eta7+psi7), with d=e-e90 as in GERM-91. The new source-equation result is

```math
\boxed{0<b\le\nu_8\quad\Longrightarrow\quad
x=0\text{ in both scalar parity kernels},\qquad\nu_8=\chi_7-2\psi_7.}
```

Under the inherited ambient equivalence and interval coverage,

```math
\boxed{L_{92}=L_{91}+\nu_8=L_{90}+2\chi_7
=\log\!\left(\frac{2^{2548608}5^{431461}}{3^{2240070}}\right)
=1.71121247800046510434740534245673741555\ldots.}
```

The increment is approximately 2.80730248424006036538e-8. The upper endpoint is checked directly. The larger GERM-91 sixth/seventh formula window still has width psi7 beyond this endpoint; it is not claimed closed. Neither the original three-layer endpoint e=3h nor the full four-delay endpoint L=log6 is reached. No canonical ratification, full-form-domain null-persistence theorem, selected-packet custody, or global uniform gap is added.

## 1. Custody and entry replay

The live branch matched the entry pin, and the repository was private. Authority remains notes/SZ_CROSS_COLLAR_RATIFICATION_20260926.md, canonical head SZ-CROSS-COLLAR-3. The pre-65 refold and GERM-72/GERM-87 correction records remain in force.

The mounted GERM-91 verifier matched SHA-256 909435197072a187936ec43799a2475bc6263b276d0f3f7c1c68fa307fcbef5a and Git blob e38b6def10d41a4ca488686acb089528d573453c. Its separate entry replay exited zero and reproduced stdout SHA-256

```text
dea727677e8573a6f3f5f589803e971ddc0448e047df430629d29b55738fee2b
```

byte for byte. All 44 entries in the inherited bundle manifest also matched. These are executable custody checks, not ratification of inherited mathematics.

The new verifier pins GERM-91 and uses its transitive helper bytes. It freshly recalculates physical coefficients through the small paired-source outward rational solver at grid 10^120, with 400 logarithm-series terms and explicit remainder bounds. GERM-71 matrix boxes are regression targets, not rounded proof inputs. Original source identities, ambient equivalence, and norm-controlled reconstruction retain their inherited scopes.

Companion records: [terminology](../docs/TERMINOLOGY_GERM92.md), [verifier](../tools/sz_seventh_double_f20_nonwrap_audit.py), and [execution receipt](_recurrence92_audit.json). The bundle contains complete stdout, compact output, the entry replay, fixtures, and executable dependencies.

## 2. Reduce the applicable seventh partition without changing its equations

All U1/U2/V3 in this note mean GERM-91-local seventh matrices. Set psi=psi7, chi=chi7, eta=eta7, sigma=3psi-chi, and nu=chi-2psi. The exact inequalities 2psi<chi<3psi imply sigma>0, nu>0, and sigma+nu=psi.

On the full remaining GERM-91 formula domain, write

```math
d=\eta+\psi+b,\qquad 0<b\le\chi-\psi.
```

For 0<z<psi, one has eta+z<d, so only V3 is possible. For psi<z<chi, the first-F threshold has already been crossed; U1 occurs when z>psi+b and U2 when z<psi+b. Thus the remaining seventh equation uses

| Seventh source | GERM-91-local map |
| --- | --- |
| (0,psi) | V3 |
| (psi,psi+b) | U2=E19 F20^2 |
| (psi+b,chi) | U1=E19 F20 E20 |

There is no omission of another legal seventh map. These are restrictions of the seven formulas proved in GERM-91, not new equations obtained from spectral data. The new verifier rechecks the parent sixth-to-fifth and seventh-to-sixth contracts, including their entry and formula-endpoint faces, then checks the three relevant restricted seventh cells.

The seventh map remains z -> z-psi modulo chi. The physical observation is W(t0+z), with t0=h-beta+gamma-xi+2eta7. No physical translation is suppressed.

## 3. Three complete eighth words through b=nu

Use K8=(0,psi). Its seventh-coordinate first-return path is

```math
z,\quad z+\chi-\psi,\quad z+\chi-2\psi,
\quad[z+\chi-3\psi].
```

The bracketed point occurs only for z>sigma. The return has two steps for z<sigma, three for z>sigma. After the first step the source is above psi; on the three-step branch the second intermediate source is also above psi. The final target is in (0,psi), so there is no omitted earlier return.

The initial map is always V3. Restrict now to 0<b<=nu. The first intermediate source is psi+z+nu, strictly above psi+b, so it always uses U1. On the three-step branch the second intermediate source is z+nu. It uses U2 exactly when

```math
z+\nu<\psi+b\quad\Longleftrightarrow\quad z<\sigma+b.
```

This proves the complete eighth partition:

| Eighth source | Chronological seventh word | GERM-92-local matrix |
| --- | --- | --- |
| (0,sigma) | V3,U1 | A=U1 V3 |
| (sigma,sigma+b) | V3,U1,U2 | E=U2 U1 V3 |
| (sigma+b,psi) | V3,U1,U1 | D=U1^2 V3 |

Products act rightmost first. In particular, the elliptic U2 is retained as the last factor in chronology for E, not replaced by U1. The neighboring U1 and V3 are forced by the actual source positions. No favorable padding or reordering is used.

At b=0 the surviving A/D products group the GERM-91 endpoint equations. At b=nu, sigma+b=psi: D disappears and A/E survive. Both endpoint faces pass directly against the parent seventh contracts. Only the named global parameter-bound margin vanishes identically on those faces; no open source-point inequality is dropped.

The induced map is

```math
S_8(z)=\begin{cases}z+\nu,&0<z<\sigma,\\z-\sigma,&\sigma<z<\psi,\end{cases}
\qquad S_8(z)=z-\sigma\pmod\psi.
```

Its images (nu,psi) and (0,nu) tile the section. The first-return tower identity is 2sigma+3nu=chi. Thus the map is invertible and Lebesgue-measure preserving, and its towers cover the seventh circle up to null boundaries. The exact verifier checks every intermediate seventh argument and affine output-to-input identity. Threshold seeds and their countably many required preimages are null for a fixed parameter; the parameter endpoint is audited separately.

## 4. One signed rational cone on the three complete returns

Use

```math
C_{92}=\begin{pmatrix}1&-3/2\\3/10&2\end{pmatrix},\qquad
\det C_{92}=49/20.
```

Take signs +1 for A/E and -1 for D. Fresh outward rational arithmetic proves every entry of the signed conjugates strictly positive, with the following certified lower factors:

| Matrix | Sign | Forward lower factor | Backward lower factor |
| --- | --- | ---: | ---: |
| A | + | >6.8122901796 | >5.6155293903 |
| D | - | >10.8450215151 | >11.4267368533 |
| E | + | >6.0515531638 | >5.6413316302 |

All three complete matrices have positive discriminant. That fact alone is not used as a common-cone proof. Positivity of the entries and both growth directions are separately certified. U2 itself retains negative discriminant; no individual expanding real cone for U2 is asserted.

For positive M=[[u,v],[w,z]], the same-sign forward l1 factor is at least min(u+w,v+z). The inverse preserves the opposite-sign double cone, with factor at least min(z+w,v+u)/det(M). The numerical division uses the directly computed positive interval determinant. Exact determinant-one identities follow separately from the literal source-word determinant exponents.

Consequently, for C+={XY>=0} and C-={XY<=0},

```math
\boxed{\|\widehat Mv\|_1\ge5\|v\|_1\ (v\in C_+),\qquad
\|\widehat M^{-1}v\|_1\ge5\|v\|_1\ (v\in C_-).}
```

The signs remain in the actual recurrence. Simultaneous negation preserves both double cones and the norm. The chart is fixed for every parameter and orbit point in the claimed interval, with no chart transition to account for.

A contains 257,302 original rotation steps; D/E each contain 353,997. These are temporal lengths of products of 2-by-2 matrices, not independent state coordinates. The factor 5 applies per complete eighth return, not per seventh map or original step. No ninth or deeper induction is used.

## 5. L2 exclusion and faithful reconstruction

For an actual scalar source let Z(z)=C92^-1 W(t0+z) on (0,psi). Bounded restriction, translation, and the fixed invertible chart preserve L2. The source equations and certified substitutions give the signed eighth recurrence almost everywhere. Remove the inherited exceptional sets and their countably many necessary affine/rotation preimages before iteration. No classical endpoint trace is used.

For real Z, let E+ be the subset where its coordinate product is nonnegative and E- its complement. Forward cone invariance and measure preservation give

```math
5^{2m}\int_{E_+}\|Z(z)\|_1^2\,dz\le\int_0^\psi\|Z(z)\|_1^2\,dz.
```

The finite right side is independent of m, so Z vanishes on E+. The backward inverse-cone estimate gives vanishing on E-. Real and imaginary parts satisfy the same real matrix equations, so complex scalar sources are excluded as well. No pointwise boundedness along dense orbits is assumed.

Every seventh-circle point above psi enters K8 after at most two negative-psi steps, since chi<3psi. The licensed seventh maps are invertible throughout the new interval, which stays strictly below the parent formula boundary. Thus vanishing propagates to the whole seventh circle. The inherited seventh first-return towers and invertible sixth atoms give vanishing on the sixth circle; the finite lower reconstruction covers the h-circle, head, middle bands, and tail. These operations concern actual scalar-source solutions; no surjectivity from arbitrary vector cocycles is assumed.

## 6. Endpoint arithmetic and distinct remaining obligations

Independently of accumulated decimals,

```math
e_{92}=e_{91}+\nu_8=e_{90}+2\chi_7=-534306h+102845k.
```

Adding log(16/3) gives (2548608,-2240070,431461) in the ordered prime-log basis. The increment vector is (6376236,-5604330,1079455). Outward rational logarithm bounds certify these identities, positivity, and all displayed decimals without floating cancellation.

Under the inherited ambient equivalence and coverage,

```math
\boxed{\ker P_c=\{0\},\quad K_c^{\rm ps}=K_c\cap\ker P_c=\{0\},
\qquad0<L\le L_{92}.}
```

The Kc statement retains regular-kernel scope. The remaining licensed sixth/seventh formula width is

```math
\omega-(\eta_7+\psi_7+\nu_8)=\psi_7
=0.00000003772997824121548585314779790099\ldots.
```

The larger remainder to e=3h is

```math
3h-e_{92}=0.00003151556687790186015729234706987238\ldots.
```

The full unresolved four-delay interval remains L92<L<=log6. Neither larger target is closed. The new three-map eighth formula window ends at b=nu8; the parent sixth/seventh formulas extend farther.

## 7. Exact next source change: the two-step eighth return

Beyond the endpoint write b=nu8+r. On 0<z<r<sigma8, the first intermediate seventh source is

```math
z+\chi_7-\psi_7=\psi_7+\nu_8+z<\psi_7+b.
```

It is now inside the U2 interval. The two-step chronological word changes from V3,U1 to V3,U2, with matrix

```math
J_{8,\mathrm{next}}=U_2V_3.
```

These are GERM-91-local seventh inputs. The final target z+nu8 remains below psi7 since z<sigma8. The checker licenses every intermediate seventh source and absence of an earlier section hit. The parent formula scope applies on the entire guard strip.

The new matrix has determinant one and certified

```math
-1.1875949973<\operatorname{tr}J_{8,\mathrm{next}}<-1.1875949972,
```

```math
-2.5896181226<(\operatorname{tr}J_{8,\mathrm{next}})^2-4\det J_{8,\mathrm{next}}<-2.5896181225.
```

It is elliptic and cannot simply be appended as an individually expanding member of the present real-cone library. This is not a nonzero-kernel construction or a no-go for lawful neighboring-word grouping, a different section, or a section-dependent argument. No exclusion beyond b=nu8 is issued.

## 8. Execution and stopping state

The final verifier exited zero. It checks fresh physical coefficients, the inherited sixth/seventh source contracts, their entry and formula-endpoint faces, the restricted seventh cells, all three new eighth cells, the entry and both new endpoint words, all three signed cone certificates, exact determinant factors, the next two-step word, and independent endpoint arithmetic. The GERM-91 entry replay matched its recorded stdout. The execution receipt records actual executable/output hashes and the separate clean-bundle replay.

Full lower symbolic suites, the complete GERM-60 ambient reduction, and old large determinant inventories were not rerun. Midpoint reconnaissance selected a rational chart only; all final coefficient signs and source inequalities are exact or outward rational. This is not Lean certification or canonical ratification.

Next individual target:

```text
SZ-KERNEL-EDGE-GERM-93 / POST-b=NU8 EIGHTH TWO-STEP TRANSFER
```

Start from the GERM-91-local U2 V3 and its source strip. Retain the larger sixth/seventh formula window, physical translation, every intermediate contract, GERM-72/GERM-87 corrections, and the original three-layer endpoint. Re-derive only changed maps; do not restart flat determinants or reopen the stopped screw route.

```text
GERM-92: COMPLETE AS A SCOPED EXPERIMENTAL PASS
NEW EXCLUSION: 0<b<=nu8, b=e-e91
ELLIPTIC U2: RETAINED IN ITS LEGAL COMPLETE EIGHTH RETURN
EIGHTH SECTION: THREE MAPS; ONE SIGNED RATIONAL CHART; FACTOR 5
NINTH OR DEEPER INDUCTION / NEW STATE COORDINATES: NONE
EXPERIMENTAL ENDPOINT: log(2^2548608*5^431461/3^2240070)
REMAINING PARENT SIXTH/SEVENTH FORMULA WIDTH: psi7
NEXT EIGHTH WORD: GERM-91-LOCAL U2 V3; ELLIPTIC
GERM-93: NOT EXECUTED
CANONICAL THEOREM CURSOR: SZ-CROSS-COLLAR-3, UNCHANGED
RATIFICATION / PUBLIC PROMOTION: NONE
```
