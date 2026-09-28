# SZ edge recurrence 83 — post-psi7 eighth-map transfer with the retained ninth cone

**Date:** 2026-09-28  
**Branch:** sz-cross-collar  
**Standing:** UNRATIFIED RESIDUE / ONE NF PASS / SCOPED POSITIVE RESULT  
**Canonical parent:** SZ-CROSS-COLLAR-3, unchanged  
**Entry commit:** d0d9a9258a5c33defcce9d3430ab4b628ebbfe99  
**Public promotion:** forbidden

## 0. Result and exact scope

The new eighth word U1 U0 V1 is incorporated with its actual intermediate seventh sources. The unchanged GERM-82 rational chart controls five new complete ninth words. No deeper section, new chart, or retained coordinate is needed for the new exclusion interval.

Retain `t=e-e80`. The new source-equation conclusion is
```math
\boxed{\psi_7<t\le2\psi_7-2\sigma_8
\quad\Longrightarrow\quad x=0\text{ in both scalar parity kernels}.}
```
Under the inherited ambient equivalence and coverage, the experimental endpoint becomes
```math
\boxed{L_{83}=L_{82}+\psi_7-2\sigma_8
=\log\!\left(\frac{2^{12945856}5^{2191647}}{3^{11378629}}\right)
=1.7112121858175925734384007165983356\ldots.}
```
The increment is approximately `1.84160714435857214545e-8`. The upper endpoint is checked directly. No exclusion above L83 is proved.

The new three eighth-map formulas have a larger domain, `psi7<t<=chi7-psi7`, including its directly checked formula endpoint. This must not be conflated with the smaller exclusion interval. The seventh formulas retain `0<t<chi7`, and the original three-layer local formulas retain their inherited scope through e=3h. No canonical ratification, full-form-domain persistence theorem, selected-packet custody, global uniform norm gap, or RH conclusion is asserted.

## 1. Custody, entry replay, and coefficient precision

The live branch matched the entry commit. Governance remains `notes/SZ_CROSS_COLLAR_RATIFICATION_20260926.md`; the pre-65 refold is retained. GERM-73's source-word correction to GERM-72 remains in force. Neither the rejected ordinary words nor the factor 40 is used.

The mounted GERM-82 verifier was checked against Git blob `c6b35a25fd47527ab00c7074f36ec040bc2dc41c` and SHA-256 `d1aef82e5dfc3673867f327b7fbcaff788f6c93f6cdbf099f38d10c8dc35e164`. Its entry replay exited zero and produced complete stdout SHA-256
```text
e5aca38ee3c63d6b96fed9e7da1cf17ddc0e01ab4befecd3f2762286aaebba15
```
matching the recorded output byte for byte. This is an executable entry check, not ratification of inherited mathematics.

The new executable pins the GERM-82 helper and its transitive bytes. It freshly recomputes physical matrices using the paired-source outward rational solver at grid 10^120, with 400 logarithm-series terms and explicit remainder bounds. GERM-71 matrix boxes are regression targets, not rounded numerical inputs. The original source equations, ambient equivalence, and bounded reconstruction remain inherited under their earlier scopes.

Companion records are [terminology](../docs/TERMINOLOGY_GERM83.md), [the verifier](../tools/sz_post_psi7_eighth_map_audit.py), and [the execution receipt](_recurrence83_audit.json). The bundle contains complete stdout, compact output, and executable dependencies.

## 2. Exact eighth-map transfer

All U_i and V_i below are **GERM-81-local**. The new A, D, E labels are **GERM-83-local**; they do not identify these matrices with older A/D/E namesakes.

Write
```math
\psi=\psi_7,\quad\chi=\chi_7,\quad\sigma=\sigma_8=3\psi-\chi,
\quad\nu=\nu_8=\psi-\sigma=\chi-2\psi,
```
```math
a=t-\psi,\quad\rho=\rho_9=\psi-3\sigma,
\quad c=c_{10}=\sigma-\rho.
```
The fixed ordering includes `3sigma<psi<4sigma`, hence `rho>0`, `c>0` and `nu>sigma`.

For the formula range `psi<t<=chi-psi`, equivalently `0<a<=nu`, the eighth section remains `(0,psi)`. Its seventh-coordinate first-return path is
```math
z,\quad z+\chi-\psi,\quad z+\chi-2\psi,
\quad[z+\chi-3\psi].
```
The bracketed point is needed only when z>sigma. Initial sources are always interior, because z<psi<t, so the first map is V1.

On the two-step branch z<sigma, the intermediate source obeys
```math
z+\chi-\psi>\chi-\psi\ge t.
```
It therefore uses U0 throughout this entire formula range, even at its upper endpoint.

On the three-step branch z>sigma, the first intermediate source satisfies
```math
z+\chi-\psi=2\psi+(z-\sigma)>2\psi>\chi-\psi\ge t.
```
It also uses U0. The second intermediate source is `z+nu`; it uses U1 precisely when `z+nu<t`, equivalently `z<sigma+a`.

Consequently the complete eighth partition is

| Eighth source z | Chronological seventh word | GERM-83-local matrix |
| --- | --- | --- |
| `(0,sigma)` | V1,U0 | A=U0 V1 |
| `(sigma,sigma+a)` | V1,U0,U1 | E=U1 U0 V1 |
| `(sigma+a,psi)` | V1,U0,U0 | D=U0^2 V1 |

All three matrices have exact determinant one. E is exactly the new GERM-82 stopping word; it has not been replaced by D. At a=nu, the D interval disappears and A/E survive, with their formula endpoint faces checked directly. All intermediate sources remain within the seventh formula scope because `chi-psi<chi`.

The eighth rotation remains `z -> z-sigma mod psi`. Its source field is the physical pullback `W(t0+z)`, with
```math
t_0=h-\beta+\gamma-\xi+2\eta_7.
```
The code rechecks both lower sixth and seventh composition contracts on their stated scopes, then proves these three eighth contracts by checking every intermediate seventh argument and the exact affine target identity.

## 3. Ninth section and five complete words

Use the unchanged ninth section `K9=(0,sigma)`. From y in K9 the eighth-coordinate positions are
```math
y,\quad y+\psi-\sigma,\quad y+\psi-2\sigma,
\quad y+\psi-3\sigma,\quad[y+\psi-4\sigma].
```
The return time is n=3 for y<c and n=4 for y>c. Every pre-final position after y exceeds sigma; the final point q lies below sigma. The induced map is
```math
S_9(y)=\begin{cases}y+\rho,&0<y<c,\\y-c,&c<y<\sigma,\end{cases}
\qquad S_9(y)=y+\rho\pmod\sigma.
```
Its images `(rho,sigma)` and `(0,rho)` tile the section. The identity `3c+4rho=psi` gives the full first-return tower length. Invertibility and Lebesgue-measure preservation are consequences of this exact geometry, not sampled dynamics.

The first eighth source always uses A. All later pre-return sources descend by sigma. Since E occupies `(sigma,sigma+a)`, E visits form a final consecutive run. If s counts them, their exact conditions are `a<q` for s=0, and
```math
q+(s-1)\sigma<a<q+s\sigma
```
for s>0. The chronological product is A, followed by n-s-1 D steps and s E steps:
```math
N_{s,n}=E^sD^{n-s-1}A.
```
For the exclusion range
```math
0<a\le a_{\max}:=\psi-2\sigma=\sigma+\rho,
```
only five words occur. On n=3, q>rho, so s=2 would require `a>q+sigma>amax`; only s=0,1 are allowed. On n=4, q is in `(0,rho)`, so s=3 would require `a>q+2sigma>amax`; only s=0,1,2 are allowed. Thus
```math
\boxed{(s,n)\in\{(0,3),(1,3),(0,4),(1,4),(2,4)\}.}
```
This proves completeness of the word library across the whole new interval. The ordinary D steps are forced by exterior intermediate sources; there is no favorable padding or reordering.

The source-domain checker substitutes every ninth step into its proved eighth contract and verifies the affine target identities. At a=amax the surviving words are `A,D,E` and `A,D,E,E`. Both endpoint faces are checked directly. The internal junction a=sigma is also checked. At a=0 the no-E words reproduce GERM-82's upper endpoint words by literal substitution: the new A/D equal the GERM-81 A1/B1 used there.

Threshold seeds and their countably many needed preimages are null for each fixed parameter. Parameter endpoints are not dismissed as null sets. The larger eighth formula window exceeds the new exclusion interval by exactly sigma, since `nu-amax=sigma>0`.

## 4. Retain the GERM-82 chart exactly

No new chart is needed:
```math
C_{83}=C_{82}=\begin{pmatrix}1&-1\\-12/5&21/10\end{pmatrix},
\qquad \det C_{82}=-3/10.
```
For the new ninth words use the sign rule
```math
\widehat N_{s,n}=(-1)^s C_{82}^{-1}N_{s,n}C_{82}.
```
Fresh outward rational arithmetic makes every entry of all five representatives strictly positive:

| s | n | Sign | Forward lower factor | Backward lower factor |
| --- | --- | --- | --- | --- |
| 0 | 3 | + | >31.9750564213 | >34.7500602785 |
| 1 | 3 | - | >13.6484374279 | >14.4962295658 |
| 0 | 4 | + | >205.3381249282 | >222.8330835644 |
| 1 | 4 | - | >89.9429607905 | >95.3474289513 |
| 2 | 4 | + | >28.5340023901 | >25.3240462214 |

The exact determinant-one identities are inherited through the literal source-word determinant exponents. Numerical inverse bounds nevertheless use directly computed positive interval determinants; they do not replace an uncertain numerical determinant by one.

For a positive matrix M=[[a,b],[c,d]], same-sign forward l1 growth is bounded below by `min(a+c,b+d)`. Its inverse preserves the opposite-sign double cone and grows there by at least `min(d+c,b+a)/det(M)`. Therefore
```math
\boxed{\|\widehat Nv\|_1\ge13\|v\|_1\quad(v\in C_+),\qquad
\|\widehat N^{-1}v\|_1\ge13\|v\|_1\quad(v\in C_-),}
```
where `C+={XY>=0}` and `C-={XY<=0}`. The actual signs remain in the recurrence. Simultaneous negation preserves both double cones and the norm. All five complete matrices also have certified positive discriminant, but hyperbolicity alone is not used as the common-cone proof.

A contains 257,302 original rotation steps; D and E each contain 353,997. Complete ninth words therefore contain 965,296 or 1,319,293 original steps. They are products of 2-by-2 matrices, not matrices of those dimensions. The factor 13 applies per complete ninth return, not per original step or as a global uniform norm gap. No tenth induction is used.

## 5. L2 exclusion and faithful reconstruction

For an actual scalar source define
```math
Z(y)=C_{82}^{-1}W(t_0+y),\qquad0<y<\sigma.
```
Restriction, translation, and a fixed invertible chart are bounded, so Z belongs to L2. The source equations and domain-certified products imply
```math
Z(S_9y)=(-1)^{s(y)}\widehat N_{s(y),n(y)}Z(y)
```
almost everywhere. Remove source exceptional sets and their countably many required affine/rotation preimages before iteration. No classical endpoint trace is introduced.

For a real field, let E+ be the set on which the product of its coordinates is nonnegative, and E- its complement. Forward cone invariance and measure preservation give
```math
13^{2m}\int_{E_+}\|Z(y)\|_1^2\,dy
\le\int_0^\sigma\|Z(y)\|_1^2\,dy.
```
The finite right side is independent of m, so Z vanishes almost everywhere on E+. Backward inverse-cone invariance gives the same conclusion on E-. Apply the argument separately to real and imaginary parts for complex profiles.

Every eighth-coordinate point above sigma reaches K9 after at most three descending sigma steps, since psi<4sigma. All three new eighth maps are invertible on the larger formula range, so zero propagates to the entire eighth circle. Every seventh-coordinate point above psi reaches the eighth section after at most two descending psi steps. The seventh maps remain valid because t<chi throughout the new interval. The inherited sixth-to-seventh towers and finite lower reconstruction then cover the h-circle, low head, middle bands, and tail.

All restrictions and reconstructions concern actual scalar-source solutions. No surjectivity from arbitrary vector fields and no pointwise boundedness along dense orbits are assumed.

## 6. Endpoint and remaining scope

The new increment has exact prime-log vector
```math
\psi_7-2\sigma_8=(15148684,-13314787,2564573).
```
Adding it to L82 gives `(12945856,-11378629,2191647)`. Independently,
```math
e_{83}=e_{80}+2\psi_7-2\sigma_8=-2714055h+522408k,
```
which gives the same vector after adding log(16/3). Outward rational logarithm bounds certify the positive increment, exact endpoint ordering, and decimal displays without floating cancellation.

Combining with inherited coverage and GERM-60 equivalence gives, within the same unratified experimental scope,
```math
\boxed{\ker P_c=\{0\},\qquad K_c^{\rm ps}=K_c\cap\ker P_c=\{0\},
\qquad0<L\le L_{83}.}
```
The Kc conclusion retains regular-kernel scope. No full-form-domain persistence theorem, selected-packet ownership statement, or RH conclusion is added.

The remaining already-derived three-layer width is
```math
3h-e_{83}=0.000031807749750432769161918205471671\ldots.
```
The full unresolved four-delay interval remains `L83<L<=log6`. Neither larger interval is claimed closed.

## 7. Exact stop: the second E visit in a three-step ninth return

Above a=amax, write `a=amax+b`, with `0<y<b<c`. On this source strip the three-step ninth path has q=y+rho and both pre-return D/E positions use E. Its chronological word and matrix are
```math
A,E,E,\qquad N_{\rm next}=E^2A.
```
This is a GERM-83-local matrix, not an earlier namesake. The eighth formulas already apply on this strip because `amax+b<nu`; no new scalar-state definition is required. Every intermediate source is checked against the new eighth contract.

The matrix has exact determinant one and rational enclosures
```math
0.3437490284<\operatorname{tr}N_{\rm next}<0.3437490285,
```
```math
-3.8818366055<(\operatorname{tr}N_{\rm next})^2-4\det N_{\rm next}
<-3.8818366054.
```
It is genuinely elliptic. It cannot simply be appended as another individually expanding matrix in the present common-cone library. This is a stopping point for this proof, not a nonzero-kernel construction or a no-go for lawful neighboring-word grouping, another section, or a section-dependent argument.

## 8. Execution and next individual target

The final new verifier ran successfully with exit code zero. It checks the fresh physical-map calculation, full inherited sixth and seventh composition contracts, three eighth source cells on their larger formula range, the entry and surviving formula endpoint faces, all five ninth-word cells and both cone directions, the internal junction and upper endpoint faces, the new elliptic-word strip, determinant factors, physical translation, and exact endpoint vectors.

The separate GERM-82 entry replay matched its recorded stdout. The execution receipt records actual executable and output hashes; the bundle includes both full output serializations and replay instructions. Full lower symbolic suites, the complete GERM-60 ambient reduction, and the old large determinant inventory were not rerun. No floating sign or sampled topology is used in the completed certificate. This is not Lean certification or canonical ratification.

Next individual target:
```text
SZ-KERNEL-EDGE-GERM-84 / POST-PSI7 NINTH DOUBLE-VISIT CONTROL
```
Start from the GERM-83-local E^2 A and its exact activation strip. Retain the larger eighth formula window, physical translation, GERM-82 chart where valid, every intermediate contract, GERM-72 correction, and the original three-layer endpoint. Do not restart flat determinants or reopen the stopped screw route.

```text
GERM-83: COMPLETE AS A SCOPED EXPERIMENTAL PASS
NEW EXCLUSION: psi7<t<=2psi7-2sigma8, t=e-e80
EIGHTH TRANSFER: THREE MAPS ON psi7<t<=chi7-psi7
NINTH SECTION: UNCHANGED; FIVE COMPLETE WORDS
RATIONAL CHART: EXACTLY THE GERM-82 CHART; SIGN RULE (-1)^s; FACTOR 13
TENTH INDUCTION / NEW RETAINED COORDINATES: NONE
EXPERIMENTAL ENDPOINT: L=log(2^12945856*5^2191647/3^11378629)
FIRST ABOVE-SCOPE WORD: GERM-83-LOCAL E^2 A; ELLIPTIC
THREE-LAYER LOCAL FORMULAS: STILL AVAILABLE THROUGH e=3h
GERM-84: NOT EXECUTED
CANONICAL THEOREM CURSOR: SZ-CROSS-COLLAR-3, UNCHANGED
RATIFICATION / PUBLIC PROMOTION: NONE
```
