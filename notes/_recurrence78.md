# SZ edge recurrence 78 — eighth-return internal-visit control

**Date:** 2026-09-28  
**Branch:** sz-cross-collar  
**Standing:** UNRATIFIED RESIDUE / ONE NF PASS / SCOPED POSITIVE RESULT  
**Canonical parent:** SZ-CROSS-COLLAR-3, unchanged  
**Entry commit:** 8f8478a055b628f9cdcacd7fd6921cce438be4c1  
**Public promotion:** forbidden

## 0. Result and exact scope

The hyperbolic word that stopped GERM-77 is controlled by a wider rational chart. The same chart also controls the next two-step internal-visit word, so both subintervals are handled in one pass without another section or a change of retained state.

Retain `delta=e-e76`. The new source-equation result is
```math
\boxed{\psi_7<\delta\le2\psi_7
\quad\Longrightarrow\quad x=0\text{ in both scalar parity kernels}.}
```
Together with the inherited coverage and GERM-60 equivalence, the experimental ambient endpoint becomes
```math
\boxed{L_{78}=L_{76}+2\psi_7=L_{77}+\psi_7
=\log\!\left(\frac{3^{5434361}}{2^{6182852}5^{1046718}}\right)
=1.711212101598518046236589\ldots.}
```
The upper endpoint is included. No exclusion above L78 is proved. The four seventh-map formulas retain their larger scope `0<delta<chi7`; the underlying three-layer local formulas retain their inherited scope through e=3h. No canonical ratification, full-form-domain persistence theorem, selected-packet custody, global uniform norm gap, or RH closure is added.

## 1. Source custody and entry replay

The live branch matched the entry commit. Governance remains `notes/SZ_CROSS_COLLAR_RATIFICATION_20260926.md`; the pre-65 refold remains the integration record. GERM-73's correction of GERM-72 remains in force. The rejected ordinary-word assignments and factor 40 are not restored.

The exact GERM-77 verifier was checked against its repository Git blob and replayed with exit code zero. Its complete stdout matched the recorded SHA-256
```text
2f73a1078b12a53b5644baab46811fbbd5d1387469b7c88b32335f83a8acbfe7
```
byte for byte. This supplies the current entry replay, not ratification of its inherited dependencies.

The new verifier pins the GERM-77 helper and its transitive source stack. Physical matrices are freshly recomputed by the small outward rational paired-source solver on a 10^60 grid. GERM-71 matrix boxes are checked as regression targets, not used as rounded numerical inputs. Exact source derivations, original scalar reduction, and reconstruction remain inherited with their stated scopes.

Companion records are [GERM-78 terminology](../docs/TERMINOLOGY_GERM78.md), [the verifier](../tools/sz_eighth_return_internal_visit_audit.py), and [the execution receipt](_recurrence78_audit.json). The bundle includes complete output and all executable dependencies.

## 2. Retain the actual seventh maps and physical observation

GERM-77 establishes the four maps U0, U1, V0, V1 on `0<delta<chi7`. U is the nonwrapping negative-psi7 step, V is the wrap; the subscript is the source's interior bit relative to `(0,delta)`. Their exact determinants are one. The new pass rechecks their compositional source contracts on that entire formula range.

Retain
```math
2\psi_7<\chi_7<3\psi_7,\quad
\nu_8=\chi_7-2\psi_7,\quad
\sigma_8=3\psi_7-\chi_7,\quad
\nu_8+\sigma_8=\psi_7.
```
In particular `2psi7<chi7` keeps the whole claimed interval strictly inside the inherited seventh-map formula scope.

The physical pullback is still
```math
V_7(z)=W(t_0+z),\qquad
t_0=h-\beta+\gamma-\xi+2\eta_7,\qquad0<z<\chi_7.
```
The eighth section remains `K8=(0,psi7)`. No unqualified identification of physical and section coordinates is made.

## 3. Complete domain classification of the four eighth words

The first-return paths to K8 are unchanged. For `0<z<sigma8` the path is
```math
z,\quad z+\chi_7-\psi_7,\quad z+\nu_8,
```
with return time two. For `sigma8<z<psi7` it is
```math
z,\quad z+\chi_7-\psi_7,\quad z+\nu_8,\quad z-\sigma_8,
```
with return time three. All pre-final points after z lie above psi7, and the last lies inside K8. The image intervals are `(nu8,psi7)` and `(0,nu8)`. Thus the induced map is still
```math
S_8(z)=z+\nu_8\pmod{\psi_7},
```
an invertible Lebesgue-measure-preserving rotation.

Because `delta>psi7`, every initial source z is interior and uses V1. On the two-step branch, the sole intermediate source can use U0 or U1. On the three-step branch, the first intermediate source obeys the exact identity
```math
(z+\chi_7-\psi_7)-2\psi_7=z-\sigma_8>0.
```
Since `delta<=2psi7`, it always uses U0. Only the second intermediate source can change its bit. Therefore exactly four words suffice across the complete parameter interval:

| Word | Source conditions in addition to psi7<delta<=2psi7 | Matrix |
| --- | --- | --- |
| V1,U0 | z<sigma8 and z+chi7-psi7>delta | U0 V1 |
| V1,U1 | z<sigma8 and z+chi7-psi7<delta | U1 V1 |
| V1,U0,U0 | z>sigma8 and z+nu8>delta | U0^2 V1 |
| V1,U0,U1 | z>sigma8 and z+nu8<delta | U1 U0 V1 |

The two binary comparisons exhaust the two return branches. No word is selected merely from its endpoint bits. The mixed three-step word is exactly the GERM-77 stopping word.

The internal parameter junction is `delta=chi7-psi7`. Below it, the two-step word remains U0 V1 while the three-step branch splits. Above it, the three-step word is U1 U0 V1 while the two-step branch splits. Both are covered by the same library and chart, not separate traversal passes.

At `delta=2psi7`, only V1,U1 and V1,U0,U1 remain generically. Both faces are checked directly. The junction is likewise checked; threshold seeds and their countably many required preimages are null for each fixed parameter, but parameter endpoints are not discarded.

All four products have exact determinant one by the inherited atom determinant factors. Their original-step counts remain 257,302 for two-step returns and 353,997 for three-step returns. These are temporal products of 2-by-2 matrices, not matrices with that many coordinates.

## 4. One wider rational cone chart

Use
```math
C_{78}=\begin{pmatrix}1&5\\0&-40/3\end{pmatrix},\qquad
\widehat B=-C_{78}^{-1}BC_{78}.
```
The chart has determinant -40/3. Fresh outward rational calculation proves every entry of all four representatives strictly positive. All actual conjugates are negative representatives, so the minus sign remains in the physical recurrence.

| Chronological word | Forward lower factor | Backward lower factor |
| --- | --- | --- |
| V1,U0 | >18.0946049803 | >2.2359471573 |
| V1,U1 | >1.5781806165 | >1.7055391942 |
| V1,U0,U0 | >310.4019578362 | >38.2758713397 |
| V1,U0,U1 | >21.3440218133 | >29.6656288692 |

For positive `B=[[a,b],[c,d]]`, forward same-sign l1 expansion is at least `min(a+c,b+d)`. Its inverse preserves the opposite-sign double cone and expands it by at least `min(d+c,b+a)/det(B)`. The code uses the directly computed positive determinant enclosure in that division, not a silently imposed numerical normalization.

Thus, on `C+={XY>=0}` and `C-={XY<=0}`,
```math
\boxed{\|\widehat Bv\|_1\ge\tfrac32\|v\|_1\quad(v\in C_+),\qquad
\|\widehat B^{-1}v\|_1\ge\tfrac32\|v\|_1\quad(v\in C_-).}
```
The appropriate cones are invariant. Simultaneous negation preserves both double cones and the norm, so the actual negative conjugates obey the same estimates. These factors are per complete eighth return, not per original step or a comparison of normalized growth with GERM-77.

## 5. L2 exclusion and faithful reconstruction

For an actual scalar source, define
```math
Z(z)=C_{78}^{-1}W(t_0+z),\qquad0<z<\psi_7.
```
This is an L2 observation by bounded restriction, translation, and the fixed invertible chart. The source equations and domain-checked compositions imply `Z(S8 z)=-Bhat(z)Z(z)` almost everywhere. Work on the common full-measure set obtained by removing source exceptional sets and their countably many required affine/rotation preimages. No classical endpoint value is used.

For real Z let E+ be the set where its coordinate product is nonnegative and E- its complement. Forward cone invariance and measure preservation give
```math
(3/2)^{2n}\int_{E_+}\|Z(z)\|_1^2\,dz
\le\int_0^{\psi_7}\|Z(z)\|_1^2\,dz.
```
The right side is finite and independent of n, so Z vanishes on E+. Backward inverse-cone invariance gives the same result on E-. Apply the argument to real and imaginary parts for complex sources.

Every seventh-coordinate point above psi7 reaches K8 in at most two descending psi7 steps. The seventh maps are invertible throughout `delta<chi7`, so the full seventh field is zero. GERM-77's certified sixth-to-seventh towers cover the sixth circle; its finite invertible reconstruction then propagates zero through the lower sections, h-circle, low head, middle bands, and tail.

All observations and reconstructions concern actual source solutions. No surjectivity from arbitrary vector fields to scalar profiles and no pointwise boundedness along dense orbits is assumed.

## 6. Endpoint and inherited scope

The exact vector identity is
```math
\psi_7=-2396212\log2+2106127\log3-405663\log5
=502358h-96695k.
```
Consequently
```math
e_{78}=e_{76}+2\psi_7=1296216h-249498k,
```
and adding log(16/3) gives the prime-log vector `(-6182852,5434361,-1046718)`. This proves the exact L78 expression. Outward rational logarithm bounds check `L77<L78<log(16/3)+3h` and enclose the decimal displays without floating cancellation.

Combining the new strip with inherited coverage gives
```math
\boxed{\ker P_c=\{0\},\qquad K_c^{\rm ps}=K_c\cap\ker P_c=\{0\},
\qquad0<L\le L_{78}.}
```
The Kc conclusion retains regular-kernel scope. No global uniform-in-L gap, full-form-domain null-persistence theorem, selected-packet ownership result, or RH conclusion is added.

The remaining already-derived three-layer width is
```math
3h-e_{78}=0.0000318919688249599709728796\ldots.
```
The full unresolved four-delay range remains `L78<L<=log6`. The exact new increment over L77 is psi7, approximately `3.7729978241215485853e-8`.

## 7. Exact next boundary: the all-internal word

Above the endpoint write `delta=2psi7+a`, with `0<a<nu8`. On the nonempty source strip
```math
\sigma_8<z<\sigma_8+a,
```
both intermediate sources of a three-step return are now interior. Its chronological word and matrix are
```math
V_1,U_1,U_1,\qquad B_{\rm next}=U_1^2V_1.
```
The four seventh maps are already valid here, since `delta<chi7`; no new local scalar-state definition is required. The exact domain checker certifies the activation strip.

The new word has exact determinant one, and the rational audit gives
```math
1.0911385573<\operatorname{tr}B_{\rm next}<1.0911385574,
```
```math
-2.8094166488<(\operatorname{tr}B_{\rm next})^2-4\det B_{\rm next}
<-2.8094166487.
```
It is genuinely elliptic. Unlike the two hyperbolic words absorbed in this pass, it cannot simply be assigned a generator-wise expanding cone. This stops the present four-word argument, not every lawful regrouping, adapted cocycle argument, or section-dependent cone field. No nonzero kernel is constructed.

## 8. Execution and stopping state

The new verifier ran successfully with exit code zero. It freshly recalculates physical matrices, rechecks the four seventh-map composition contracts on their full scope, certifies all four new eighth words and both cone directions, checks the junction and upper-endpoint faces, and checks the next all-internal word. The entry GERM-77 replay was performed separately and matched its recorded complete stdout.

The full lower symbolic suites, complete GERM-60 ambient reduction, and old large determinant inventory were not rerun. Floating reconnaissance selected a candidate chart only; no floating sign or sampled topology is used in the certificate. The repository receipt records actual executable and output hashes. The bundle includes complete stdout and compact output, not just the receipt. This is not Lean certification or canonical ratification.

Next individual target:
```text
SZ-KERNEL-EDGE-GERM-79 / EIGHTH-RETURN ALL-INTERNAL CONTROL
```
Start from U1^2 V1 and its activation strip. Retain the valid seventh-map formula scope, physical translation, GERM-72 correction, and every intermediate domain. Seek lawful neighboring-word or section-dependent control without rebuilding the scalar layer system. Do not restore the rejected factor-40 argument or reopen the stopped screw route.

```text
GERM-78: COMPLETE AS A SCOPED EXPERIMENTAL PASS
NEW EXCLUSION: psi7<delta<=2psi7
EIGHTH SECTION: UNCHANGED; FOUR INTERNAL-VISIT WORDS
COMMON SIGNED RATIONAL CHART: FACTOR 3/2
EXPERIMENTAL ENDPOINT: L=log(3^5434361/(2^6182852*5^1046718))
FIRST ABOVE-SCOPE WORD: U1^2 V1, DETERMINANT ONE, ELLIPTIC
SEVENTH FORMULAS: STILL AVAILABLE THROUGH delta<chi7
THREE-LAYER FORMULAS: STILL AVAILABLE THROUGH e=3h
GERM-79: NOT EXECUTED
CANONICAL THEOREM CURSOR: SZ-CROSS-COLLAR-3, UNCHANGED
RATIFICATION / PUBLIC PROMOTION: NONE
```
