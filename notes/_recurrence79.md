# SZ edge recurrence 79 — all-internal eighth visits and ninth-return exclusion

**Date:** 2026-09-28  
**Branch:** sz-cross-collar  
**Standing:** UNRATIFIED RESIDUE / ONE NF PASS / SCOPED POSITIVE RESULT  
**Canonical parent:** SZ-CROSS-COLLAR-3, unchanged  
**Entry commit:** c0b870e1dc14bd8d8db85d64ff133a2a5ba1c4e5  
**Public promotion:** forbidden

## 0. Result and exact scope

The all-internal eighth return from GERM-78 remains elliptic. Its legal first returns to a smaller section include compulsory non-elliptic steps. Five such words admit one signed rational cone certificate, without enlarging the retained state.

Retain `delta=e-e76` and `sigma8=3psi7-chi7`. The new source-equation result is
```math
\boxed{2\psi_7<\delta\le3\psi_7-2\sigma_8
\quad\Longrightarrow\quad x=0\text{ in both scalar parity kernels}.}
```
With inherited coverage and GERM-60 equivalence, the experimental ambient endpoint is
```math
\boxed{L_{79}=L_{78}+\psi_7-2\sigma_8
=\log\!\left(\frac{2^{8965832}5^{1517855}}{3^{7880426}}\right)
=1.71121212001458948982231120\ldots.}
```
The upper endpoint is included. The exact increment over L78 is `psi7-2sigma8`, approximately `1.84160714435857214545e-8`. No exclusion beyond L79 is asserted.

The new three eighth-map formulas hold throughout `2psi7<delta<chi7`, strictly more than the exclusion interval proved here. The original three-layer formulas retain their inherited scope through e=3h. This is not canonical ratification, a full-form-domain persistence theorem, selected-packet custody, a global uniform norm gap, or RH closure.

## 1. Source custody and entry replay

The live branch matched the entry commit. Governance remains `notes/SZ_CROSS_COLLAR_RATIFICATION_20260926.md`; the pre-65 refold remains the integration record. GERM-73's correction of GERM-72 remains in force. Its rejected ordinary words and factor 40 are not used.

The mounted GERM-78 verifier matched its repository blob `c38295aa05e7cc1052ce989d7867477617a8c96d`. Its separate entry replay exited zero and produced SHA-256
```text
ffe68ffb19671811126db5a132b541d0a38dccffcc92c328ef4e9e7173cccfb0
```
matching its recorded stdout byte for byte. This is an executable entry check, not ratification of inherited mathematics.

The new verifier pins GERM-78 and the transitive helper bytes. It freshly recomputes the physical matrices through the small paired-source outward rational solver on a 10^60 grid. The recorded GERM-71 boxes are regression targets, not rounded numerical inputs. Original source identities, ambient equivalence, and local reconstruction remain inherited from GERM-60/61, 65–67, and the subsequent scoped reductions.

Companion records are [GERM-79 terminology](../docs/TERMINOLOGY_GERM79.md), [the verifier](../tools/sz_eighth_return_all_internal_audit.py), and [the execution receipt](_recurrence79_audit.json). The bundle contains complete stdout, compact output, and executable dependencies.

## 2. Three eighth maps on the full new formula range

Set
```math
a=\delta-2\psi_7,\quad
\nu_8=\chi_7-2\psi_7,\quad
\sigma_8=3\psi_7-\chi_7,\quad
\nu_8+\sigma_8=\psi_7.
```
The relevant formula range is `0<a<nu8`, equivalent to `2psi7<delta<chi7`. The eighth circle remains `(0,psi7)`, its map remains
```math
S_8(z)=z-\sigma_8\pmod{\psi_7},
```
and its physical observation remains `W(t0+z)`, with `t0=h-beta+gamma-xi+2eta7`.

Every initial source is interior and uses V1. The complete eighth partition is

| Source z | Chronological seventh word | Matrix |
| --- | --- | --- |
| `(0,sigma8)` | V1,U1 | `A=U1 V1` |
| `(sigma8,sigma8+a)` | V1,U1,U1 | `E=U1^2 V1` |
| `(sigma8+a,psi7)` | V1,U0,U1 | `D=U1 U0 V1` |

For a two-step return the intermediate point is `z+chi7-psi7<2psi7<delta`, so U1 is mandatory. For a three-step return, the second intermediate point is `z+nu8<psi7+nu8<2psi7<delta`, so it also uses U1. The first intermediate point is interior exactly when `z<sigma8+a`. These inequalities establish the complete partition, not merely a list of candidate words.

The verifier checks every seventh-map argument on all three cells. It also rechecks the four inherited seventh-map composition contracts on their original full formula scope. Each A, D, and E has exact determinant one by the inherited atom identities. E remains genuinely elliptic; A and D are not inserted as optional spectral padding.

## 3. Ninth section and exact return geometry

Exact prime-power tests establish
```math
3\sigma_8<\psi_7<4\sigma_8.
```
Define the new residual length and source cut
```math
\rho_9=\psi_7-3\sigma_8,\qquad
c_9=\sigma_8-\rho_9,\qquad0<\rho_9<\sigma_8.
```
The notation rho9 is distinct from the earlier determinant ratio rho.

Choose `K9=(0,sigma8)` in the eighth coordinate. From y in this section, the path is
```math
y,\quad y+\psi_7-\sigma_8,\quad y+\psi_7-2\sigma_8,
\quad y+\psi_7-3\sigma_8,
\quad [y+\psi_7-4\sigma_8].
```
The bracketed point is needed only for y>c9. The first return takes three eighth steps when `0<y<c9`, and four when `c9<y<sigma8`. All pre-final points after y lie strictly above sigma8; the final point q lies strictly below it.

The induced map is
```math
S_9(y)=\begin{cases}
y+\rho_9,&0<y<c_9,\\
y+\rho_9-\sigma_8,&c_9<y<\sigma_8,
\end{cases}
\qquad S_9(y)=y+\rho_9\pmod{\sigma_8}.
```
Its two images are `(rho9,sigma8)` and `(0,rho9)`, which tile K9 up to endpoints. Thus S9 is invertible and Lebesgue-measure preserving. The exact tower identity is `3c9+4rho9=psi7`.

## 4. Five complete legal words

The first eighth atom is always A. The later source positions descend strictly in sigma8 steps. Since E occupies `(sigma8,sigma8+a)`, all E visits form a final consecutive run.

Let s count those visits and n be the ninth return time. If s=0, `a<q`. If s>0,
```math
q+(s-1)\sigma_8<a<q+s\sigma_8.
```
The complete matrix is consequently
```math
B_{s,n}=E^sD^{n-s-1}A.
```
This pass covers
```math
0<a\le a_{\max}:=\psi_7-2\sigma_8=\sigma_8+\rho_9.
```
On the three-step branch q lies in `(rho9,sigma8)`. Two E visits would require `a>q+sigma8>rho9+sigma8`, outside the range. Thus s is 0 or 1. On the four-step branch q lies in `(0,rho9)`. Three E visits would require `a>q+2sigma8>amax`. Thus s is 0, 1, or 2. Exactly five words suffice:
```math
\boxed{(s,n)\in\{(0,3),(1,3),(0,4),(1,4),(2,4)\}.}
```
At a=amax only `(1,3)` and `(2,4)` occur generically. Both endpoint faces are checked directly. The internal junction a=sigma8 is also checked. Threshold seeds and their countably many required preimages are null for each fixed parameter; this does not license omitting a parameter endpoint.

The certificate uses typed composition: every ninth step substitutes its source into the proved eighth-domain contract and checks the exact affine target identity. The eighth contract itself checks all seventh arguments. The original lower contracts remain pinned dependencies. The written classification establishes completeness; exact rational polytope checks certify the resulting cells, not sampled orbit guesses.

The original rotation-step counts are 965,296 for three-step ninth returns and 1,319,293 for four-step returns. These remain words of 2-by-2 matrices, not matrices of those dimensions. All complete words have exact determinant one because every underlying atom has determinant one.

## 5. One signed rational cone chart

Use
```math
C_{79}=\begin{pmatrix}1&4\\-2&-23/2\end{pmatrix},\qquad
\widehat B_{s,n}=(-1)^{n+s}C_{79}^{-1}B_{s,n}C_{79}.
```
The chart determinant is -7/2. Fresh outward rational arithmetic proves all entries of all five representatives strictly positive.

| s | n | Sign | Forward lower factor | Backward lower factor |
| --- | --- | --- | --- | --- |
| 0 | 3 | - | >1150.2946190546 | >54.0531384220 |
| 1 | 3 | + | >50.3456672009 | >94.8569880197 |
| 0 | 4 | + | >47650.8050021155 | >2239.1357400190 |
| 1 | 4 | - | >2086.1700524493 | >3929.4626661197 |
| 2 | 4 | + | >27.1568272934 | >22.1051092849 |

For positive `B=[[a,b],[c,d]]`, forward same-sign l1 expansion is at least `min(a+c,b+d)`. Its inverse preserves the opposite-sign double cone, with factor at least `min(d+c,b+a)/det(B)`. The code divides by a directly computed positive determinant enclosure, not by a silently imposed numerical value of one.

Thus, with `C+={XY>=0}` and `C-={XY<=0}`,
```math
\boxed{\|\widehat Bv\|_1\ge20\|v\|_1\quad(v\in C_+),\qquad
\|\widehat B^{-1}v\|_1\ge20\|v\|_1\quad(v\in C_-).}
```
The actual sign remains in the recurrence. Both double cones and the norm are invariant under simultaneous negation. These estimates apply per complete ninth return, not per original step, not to E alone, and not as a comparison of normalized growth rates with earlier passes.

## 6. L2 exclusion and faithful reconstruction

For an actual scalar source define
```math
Z(y)=C_{79}^{-1}W(t_0+y),\qquad0<y<\sigma_8.
```
Restriction, translation, and the fixed invertible chart are bounded, hence Z is in L2. The source equations and domain-certified compositions imply the signed ninth-return equation almost everywhere. Remove source exceptional sets and their countably many required affine/rotation preimages to obtain a common full-measure iteration set. No classical endpoint traces are assumed.

For a real field let E+ be the set where its coordinate product is nonnegative and E- its complement. Forward cone invariance and measure preservation give
```math
20^{2m}\int_{E_+}\|Z(y)\|_1^2\,dy
\le\int_0^{\sigma_8}\|Z(y)\|_1^2\,dy.
```
The finite right side is independent of m, so Z vanishes almost everywhere on E+. The inverse estimate proves the same on E-. Apply the argument to real and imaginary parts for complex sources.

Every eighth-coordinate point above sigma8 reaches K9 after at most three descending sigma8 steps, since psi7<4sigma8. The eighth maps are invertible, so the entire eighth circle is zero. Every seventh-coordinate point above psi7 reaches the eighth section after at most two descending psi7 steps; the seventh maps remain valid and invertible because delta<chi7 throughout the new range.

The inherited sixth-to-seventh towers and finite lower-section reconstruction then cover the h-circle, low head, middle bands, and tail. All observations and reconstructions concern actual scalar-source solutions. Surjectivity from arbitrary vector cocycles and pointwise boundedness along dense orbits are not assumed.

## 7. Endpoint and inherited scope

The exact new increment has prime-log vector
```math
\psi_7-2\sigma_8
=15148684\log2-13314787\log3+2564573\log5.
```
Adding this to the GERM-78 endpoint gives `(8965832,-7880426,1517855)`. Independently,
```math
e_{79}=-1879656h+361801k,
```
so adding log(16/3) gives the same vector. Exact prime-power tests establish positivity of the increment and `L78<L79<log(16/3)+3h`. Outward rational logarithm bounds provide the displayed decimals without floating cancellation.

Combining with inherited coverage and the GERM-60 equivalence gives
```math
\boxed{\ker P_c=\{0\},\quad K_c^{\rm ps}=K_c\cap\ker P_c=\{0\},
\qquad0<L\le L_{79}.}
```
The Kc conclusion retains regular-kernel scope. No global uniform-in-L gap, full-form-domain null-persistence theorem, selected-packet ownership result, or RH conclusion is added.

The remaining already-derived three-layer width is
```math
3h-e_{79}=0.000031873552753516385251425177\ldots.
```
Within the narrower seventh-map formula window, the unexcluded width is exactly sigma8: `chi7-delta79=sigma8`. The full unresolved four-delay interval remains `L79<L<=log6`.

## 8. Exact next boundary: the two-internal-visit three-step word

Above a=amax write `a=amax+b`, with `0<b<c9`. On the nonempty strip `0<y<b`, the three-step ninth return now has two E visits. Its chronological word and matrix are
```math
A,E,E,\qquad B_{\rm next}=E^2A.
```
The exact domain checker certifies the activation strip. The eighth formulas are already valid there; no scalar layer system needs to be rebuilt.

The new word has exact determinant one, and rational bounds
```math
-0.5773206695<\operatorname{tr}B_{\rm next}<-0.5773206694,
```
```math
-3.6667008447<(\operatorname{tr}B_{\rm next})^2-4\det B_{\rm next}
<-3.6667008446.
```
It is genuinely elliptic. It cannot simply be appended as another individually expanding member of this common-cone library. This does not construct a nonzero kernel or rule out legal neighboring-word grouping, a changed section, or a section-dependent argument.

## 9. Execution and stopping state

The final new verifier ran successfully with exit code zero. It checks fresh physical-map recalculation, four seventh-map composition contracts, three eighth contracts over their full new formula scope, all five ninth-word cells and cone bounds, the internal junction and upper-endpoint faces, the next-word guard, determinant factors, and exact endpoint arithmetic. The separate GERM-78 entry replay matched its recorded stdout.

The full lower symbolic suites, complete GERM-60 ambient reduction, and old large determinant inventory were not rerun. Floating reconnaissance selected the candidate rational chart only; no floating sign or sampled topology is used in the certificate. The receipt records actual executable and output hashes; the bundle includes complete output and replay instructions. This is not Lean certification or canonical ratification.

Next individual target:
```text
SZ-KERNEL-EDGE-GERM-80 / NINTH-RETURN DOUBLE-INTERNAL CONTROL
```
Start from E^2 A and its activation strip. Retain the three eighth maps, their full formula scope, every intermediate domain, physical translations, and the GERM-72 correction. Do not restart flat determinants or reopen the stopped screw route.

```text
GERM-79: COMPLETE AS A SCOPED EXPERIMENTAL PASS
NEW EXCLUSION: 2psi7<delta<=3psi7-2sigma8
EIGHTH FORMULAS: THREE MAPS ON 2psi7<delta<chi7
NINTH SECTION: FIVE COMPLETE WORDS; SIGNED CHART; FACTOR 20
EXPERIMENTAL ENDPOINT: L=log(2^8965832*5^1517855/3^7880426)
FIRST ABOVE-SCOPE WORD: E^2 A, DETERMINANT ONE, ELLIPTIC
THREE-LAYER LOCAL FORMULAS: STILL AVAILABLE THROUGH e=3h
GERM-80: NOT EXECUTED
CANONICAL THEOREM CURSOR: SZ-CROSS-COLLAR-3, UNCHANGED
RATIFICATION / PUBLIC PROMOTION: NONE
```
