# SZ edge recurrence 73 — repaired source words and fourth-section elliptic-visit control

**Date:** 2026-09-28  
**Branch:** sz-cross-collar  
**Standing:** UNRATIFIED RESIDUE / ONE NF PASS / CORRECTION AND SCOPED POSITIVE RESULT  
**Canonical parent:** SZ-CROSS-COLLAR-3, unchanged  
**Entry commit:** e7ea1faf0a4c77439523b480b6d3f0c650c2bf99  
**Public promotion:** forbidden

## 0. Result, with a necessary correction

The entry source-domain audit found an error in GERM-72. Its ordinary third-section words ignored internal overlap visits. Their factor-40 calculation therefore did not certify the actual recurrence. Read [the additive correction](_recurrence72_correction.md) before using that record.

This pass re-establishes the GERM-72 interval with the correct source words and a factor 5/2, then controls the elliptic-visit continuation by nine longer legal returns with a factor 2. Its combined source-equation conclusion is
```math
\boxed{3h-\theta<e\le3h-\alpha
\ \Longrightarrow\ x=0\text{ in both scalar parity kernels},\qquad
\alpha=\tau-3\theta.}
```
The genuinely new part beyond the repaired interval is
```math
3h-\theta+\gamma<e\le3h-\alpha.
```
Together with the inherited GERM-63/65–71 coverage and GERM-60 reconstruction, the experimental ambient endpoint is
```math
\boxed{
L_{73}=\log(16/3)+3h-\alpha
=\log\!\left(\frac{2^{3164}5^{534}}{3^{2777}}\right)
=1.7111989001359460283\ldots.}
```
There is no reliance on the erroneous GERM-72 word assignment. Its interval is recovered by the present proof, not assumed. No claim is made above L73 or beyond the inherited three-layer formula scope e<=3h.

## 1. Source custody, notation, and exact arithmetic

The live branch matched the entry pin before this NF pass. Governance is `notes/SZ_CROSS_COLLAR_RATIFICATION_20260926.md`; the pre-65 refold remains the integration record. The original source equations and ambient equivalence are inherited from GERM-60/61. The two-coordinate observation, three-layer reduction, and reconstruction are inherited from GERM-65–67. The six self-overlap second-section maps and their domain rules are inherited from GERM-71, whose formula scope includes the new parameters here. These are unratified dependencies, not newly ratified conclusions.

The new executable pins the GERM-71/69/68/65 helper bytes and the GERM-67/71 audit fixtures. It freshly recalculates the physical matrices by the small outward rational source solver and verifies containment in the GERM-71 boxes. The GERM-72 wrapper is neither a source-domain proof nor a dependency of this new certificate.

New notation is in [GERM-73 terminology](../docs/TERMINOLOGY_GERM73.md). Keep the residual lengths distinct from older prime coefficients:
```math
\begin{gathered}
h=\log(81/80),\quad k=\log(16/15),\quad
\kappa=k-5h,\quad\tau=h-5\kappa,\\
\theta=\kappa-8\tau,\quad
\alpha=\tau-3\theta,\quad
\beta=\theta-\alpha,\quad
\gamma=\alpha-\beta.
\end{gathered}
```
Here beta and gamma denote residual lengths only. Exact prime-power comparisons give
```math
\gamma>0,\qquad49\gamma<10\beta<50\gamma.
```
Consequently
```math
\theta=2\beta+\gamma,\quad
\alpha=\beta+\gamma,\quad
\tau=7\beta+4\gamma,\quad
0<\gamma<\beta<\alpha<\theta.
```
Write `e=3h-theta+epsilon`. The combined range of this pass is `0<epsilon<=beta`.

Let W be the actual GERM-65 scalar-source observation. Define the theta-section pullback
```math
V(v)=W(h-\theta+v),\qquad0<v<\theta.
```
All translations of the physical state will be kept explicitly. These are bounded L2 observations, not classical boundary jets.

## 2. Repair the third-section source words

The third-section map is
```math
S_3(v)=v-\alpha\pmod\theta.
```
In the second-section coordinate its starting point is `tau-theta+v`; the overlap width there is `zeta=tau-theta+epsilon`. After the first wrap, the intermediate points are `v`, `v+theta`, and, on the four-step branch, `v+2theta`.

All those intermediate points are inside the overlap in the present range. Even an exterior-to-exterior complete return therefore has internal visits. The exact four-type library through epsilon=beta is:

| Type | Source interval | Chronological second-section word | Matrix |
| --- | --- | --- | --- |
| A3 | `alpha+epsilon<v<theta` | `01-,11+,10+` | `P2 E2+ Q2` |
| Q3 | `alpha<v<alpha+epsilon` | `01-,11+,11+` | `(E2+)^2 Q2` |
| P3 | `0<v<epsilon` | `11-,11+,11+,10+` | `P2 (E2+)^2 E2-` |
| D3 | `epsilon<v<alpha` | `01-,11+,11+,10+` | `P2 (E2+)^2 Q2` |

Products act rightmost first. Plus/minus in these words refer to the second-section rotation, not the sign of a matrix. At epsilon=beta the A3 source interval is empty; all remaining actual source intervals are still licensed.

The executable checks these cells and every underlying original rotation step using the GERM-71 affine lift. It also supplies exact counterexamples to the old A3/D3 assignments. At `epsilon=gamma/2`, `v=3theta/4` gives overlap bits `0,1,1,0`, while `v=alpha/2` gives `0,1,1,1,0`. Thus the old all-exterior words are not legal at those points.

The determinant factors remain
```math
\det A_3=\det D_3=1,\qquad
\det Q_3=\rho^{-1},\qquad
\det P_3=\rho>0.
```
Their derivation is literal multiplication of the inherited library, not a floating determinant inference.

## 3. Fourth-section geometry and repaired GERM-72 interval

Retain the section `H=(alpha,theta)`. It is exterior for epsilon<=beta because beta<alpha. Write `v=alpha+w`, so `0<w<beta`. Physically the observation is `W(h-beta+w)`.

The first return is
```math
S_4(w)=w-\gamma\pmod\beta.
```
For `gamma<w<beta` its path is
```math
\alpha+w,\quad w,\quad w+\beta,
```
and for `0<w<gamma` it is
```math
\alpha+w,\quad w,\quad w+\beta,\quad w+2\beta.
```
The intermediate points stay below alpha and the last lies in H. The coordinate images `(0,beta-gamma)` and `(beta-gamma,beta)` tile the fourth circle, proving invertibility and preservation of Lebesgue measure.

The complete fourth-return library is:
```math
\mathcal A=D_3A_3,\quad
\mathcal O=D_3^2A_3,\quad
\mathcal J=D_3P_3Q_3,\quad
\mathcal E=P_3Q_3.
```

| Word | Domain |
| --- | --- |
| A | `max(epsilon,gamma)<w<beta` |
| O | `epsilon<w<gamma` |
| J | `0<w<min(epsilon,gamma)` |
| E | `gamma<w<epsilon` |

These are domains of complete returns, not independently selectable generators. All four matrices have determinant one.

For `0<epsilon<=gamma`, only A,O,J occur. The correct chart is
```math
C_{\rm repair}=\begin{pmatrix}1&1\\1&3\end{pmatrix}.
```
Fresh outward rational tests give:

| Word | Overall sign of positive representative | Forward lower bound | Backward lower bound |
| --- | --- | --- | --- |
| A | -1 | >8.4665 | >6.3410 |
| O | +1 | >24.5464 | >18.9019 |
| J | +1 | >2.5466 | >3.0671 |

Thus the common factor is 5/2 in both cone directions. The GERM-72 factor 40 is withdrawn: its old chart sends the corrected J matrix to a matrix with positive first row and negative second row. No overall sign fixes that cone failure.

The measure-preserving L2 argument in Section 6, applied here to the whole fourth circle and the repair chart, recovers the full old interval including epsilon=gamma. The O interval disappears at that endpoint; A and J are checked directly. The old theorem's interval is now justified by this replacement proof, not by the old calculation.

For epsilon>gamma, E becomes active. Its discriminant remains negative; it is not relabeled expanding. The next induction incorporates its forced neighboring steps.

## 4. A fifth section groups every legal elliptic visit in the new range

Assume `gamma<epsilon<=beta`. Use `K=(0,gamma)` inside the fourth circle, with coordinate z. Physically K is `(h-beta,h-beta+gamma)`.

Put `xi=5gamma-beta`. The exact arithmetic gives `0<xi<gamma`. Starting at z, the first fourth-step is always J, and the subsequent positions descend:
```math
z,\quad z+\beta-\gamma,\quad z+\beta-2\gamma,\quad\ldots,\quad
q=z+\beta-N\gamma.
```
The first return to K has
```math
N(z)=
\begin{cases}
4,&0<z<\xi,\\
5,&\xi<z<\gamma.
\end{cases}
```
Every pre-final position after z is above gamma; q lies in `(0,gamma)`. There is no earlier hit. The return map is
```math
S_5(z)=z+(\beta-4\gamma)\pmod\gamma.
```
Its two images `(beta-4gamma,gamma)` and `(0,beta-4gamma)` tile K. This proves measure preservation directly.

Among the N-1 descending intermediate positions, the ones below epsilon form a final consecutive run. Let s count them. For s=0, `epsilon<q+gamma`; for s>0,
```math
q+s\gamma<\varepsilon<q+(s+1)\gamma.
```
There are exactly nine possible words:
```math
\boxed{
\mathcal B_{s,N}=
\mathcal E^s\mathcal A^{N-s-1}\mathcal J,\qquad
N\in\{4,5\},\quad0\le s<N.}
```
Chronologically the word is J, then ordinary A steps, then s elliptic E steps. Every A step is forced by a pre-return source point above epsilon. No favorable padding or reordering is permitted.

Each complete word has determinant one. Its expansion contains `2N+1` third-section steps and `297N+169` original rotation steps: 1,357 or 1,654. These are long words of fixed 2-by-2 matrices, not matrices of those dimensions.

At epsilon=beta, only `(s,N)=(3,4)` and `(4,5)` remain generically. Both endpoint faces are checked directly. Endpoint equality of a parameter is not discarded as a null seed set.

## 5. One rational cone chart for all nine complete words

Use
```math
C_5=\begin{pmatrix}1&-1\\6&-10\end{pmatrix}.
```
The negative first entry of its second column is intentional. Restricting both columns to positive first coordinates would miss this common projective cone.

Define
```math
\sigma_{s,N}=
\begin{cases}
(-1)^{N+1},&s=0,1,\\
-(-1)^{N+1},&s\ge2.
\end{cases}
```
Every matrix `sigma_(s,N) C5^-1 B_(s,N) C5` has strictly positive entries under outward rational enclosure. The following deliberately weakened bounds are all certified:

| s | N | Sign | Forward factor | Backward factor |
| --- | --- | --- | --- | --- |
| 0 | 4 | - | >2247.57 | >1680.94 |
| 1 | 4 | - | >131.33 | >63.66 |
| 2 | 4 | + | >6.648 | >4.430 |
| 3 | 4 | + | >2.834 | >2.464 |
| 0 | 5 | + | >20444.12 | >15289.94 |
| 1 | 5 | + | >1194.37 | >579.03 |
| 2 | 5 | - | >62.047 | >40.620 |
| 3 | 5 | - | >24.071 | >21.738 |
| 4 | 5 | - | >2.177 | >2.438 |

For positive `B=[[a,b],[c,d]]`, the same-sign forward l1 factor is at least `min(a+c,b+d)`. The inverse expands the opposite-sign double cone by at least `min(d+c,b+a)/det(B)`. The code uses a directly computed positive interval determinant in that division. It does not silently set a numerically uncertain determinant to one.

Consequently every actual signed transformed word satisfies
```math
\boxed{
\|B'z\|_1\ge2\|z\|_1\quad(z\in C_+),\qquad
\|(B')^{-1}z\|_1\ge2\|z\|_1\quad(z\in C_-),}
```
where `C+={XY>=0}`, `C-={XY<=0}`, and `B'=C5^-1 B C5`. These cones are preserved forward and backward respectively. Overall signs remain in the recurrence: simultaneous negation preserves both double cones and the norm.

The factor is per complete fifth return, not per original rotation step, and not for arbitrary repetitions of the elliptic E matrix.

## 6. L2 exclusion and faithful reconstruction

On K define
```math
Z(z)=C_5^{-1}W(h-\beta+z),\qquad0<z<\gamma.
```
It is an L2 observation. The source equations and exact inductions imply the signed transformed return equation almost everywhere. Remove the inherited exceptional sets and their countably many necessary affine/rotation preimages to obtain a common full-measure set for iteration; no classical endpoint traces are assumed.

For a real state, let `K+={Z1 Z2>=0}` and `K-={Z1 Z2<0}`. Forward cone invariance and measure preservation give
```math
2^{2n}\int_{K_+}\|Z(z)\|_1^2\,dz
\le\int_0^\gamma\|Z(z)\|_1^2\,dz.
```
The right side is finite and independent of n. Hence Z vanishes almost everywhere on K+. Backward inverse expansion gives the identical conclusion on K-. Real and imaginary parts obey the same real matrix equation, so complex profiles are excluded as well.

For the repaired `epsilon<=gamma` strip, use the same argument on the full fourth circle with the repair chart and factor 5/2.

For the new strip, any point outside K reaches K after at most four successive negative-gamma fourth steps, before any wrap. Those maps are invertible, so zero on K gives zero throughout H. Every point below H reaches H after at most two S3 steps, using the certified four-type library. Thus the entire physical theta-section is zero.

The inherited six second-section maps then propagate zero to the second section, the first section, and the h-circle. GERM-67's bounded local reconstruction covers the low head and its middle/tail Schur formulas reconstruct the original source. All observations and reconstructions are on actual source solutions; surjectivity from arbitrary vector fields is neither assumed nor needed.

This proves the repaired and new source-exclusion intervals. It does not infer bounded values of an L2 function along an individual dense orbit.

## 7. Exact endpoint and stopping interface

The arithmetic identity is
```math
\alpha=665h-128k,\qquad
3h-\alpha=128k-662h.
```
Therefore
```math
\exp L_{73}=(16/3)(16/15)^{128}(80/81)^{662}
=\frac{2^{3164}5^{534}}{3^{2777}}.
```
The executable independently checks this rational identity and strict ordering between L71, the exact repaired L72, L73, and the e=3h endpoint. Combining with the inherited ambient equivalence yields
```math
\boxed{
\ker P_c=\{0\},\qquad K_c^{\rm ps}=K_c\cap\ker P_c=\{0\},
\qquad0<L\le L_{73}.}
```
The Kc statement retains regular-kernel scope. There is no new full-form-domain null-persistence theorem, selected-packet ownership theorem, global uniform-in-L gap, or RH closure.

Immediately above epsilon=beta put `epsilon=beta+delta`, with `0<v<delta<gamma`. A third-section wrap now starts and ends inside the overlap. Its exact second-section word is
```text
11-, 11+, 11+, 11+
```
and its matrix is
```math
I_3=(E_2^+)^3E_2^-.
```
The new audit checks this concrete strip and its original-step lift. This species was absent from the four-type library. The current four-type and fifth-word formulas must not be continued unchanged across it. No claim is made that the new word is impossible to control.

The remaining already-derived three-layer range is
```math
3h-\alpha<e\le3h,
```
of width `alpha=0.000045093431396977875669...`. The full remaining four-delay range is still `L73<L<=log6`; continuation past e=3h requires its own formula audit.

## 8. Execution receipt and limits

Run with assertions enabled:
```text
python tools/sz_fourth_section_elliptic_visit_audit.py
```
The final verifier was executed successfully with exit code zero. It checks the two GERM-72 source-word counterexamples, four corrected third-map cells, all fourth-word cells, the repaired three cone bounds, all nine new cone bounds, the source lifts of all complete words, both repair endpoint faces, both new endpoint faces, and the next internal-wrap guard.

The nine new word cells contain 83,776 affine margin expressions, each tested exactly on its rational polytope vertices. The code separately checks every lifted source/target bit and absence of an earlier section hit. Floating reconnaissance selected the charts; no floating sign or sampled topology is used in the certificate.

Executed verifier SHA-256:
```text
1b36e699415e0ebf2a93946161745e5f8297132e7ab1c6f2930a73a19bbb483f
```
Expected verifier Git blob:
```text
4fee37c9870b0f2f8220fefe04fa98085b15868b
```
Full indented stdout SHA-256:
```text
4aeeeb665bb5741122870da76762d8bf3bb9a5d282d85bf7f48874808b337df4
```
Full compact audit SHA-256:
```text
cd8602405239d16b4a66e1cd8198bd08d3766bd31bbbe9010051f18a13e33be5
```
The repository [audit file](_recurrence73_audit.json) is explicitly an execution receipt with lower bounds and full-output hashes, not a claim to contain every stdout field. Running the pinned verifier reproduces the complete JSON; both complete serializations are included in the downloadable certificate bundle.

The original GERM-72 wrapper, full parent symbolic suites, old large determinant inventory, and full GERM-60 reduction were not rerun. The completed work is the stated fresh physical-map recalculation, exact domain audit, new cone certificate, and written L2 proof. It is not Lean certification or canonical ratification.

## 9. Next individual target

```text
SZ-KERNEL-EDGE-GERM-74 / FOURTH-SECTION INTERNAL-WRAP CONTROL
```
Start from the newly active I3 species, preserving the corrected source-word library and explicit physical coordinates. Do not restore the rejected GERM-72 factor-40 argument, re-enumerate flat orbit determinants, or reopen the stopped screw shortcut.

```text
GERM-73: COMPLETE AS A SCOPED EXPERIMENTAL PASS
GERM-72 ORDINARY WORDS AND FACTOR 40: SUPERSEDED / NOT VALID SOURCE CERTIFICATES
GERM-72 INTERVAL: RE-ESTABLISHED WITH CORRECT WORDS, FACTOR 5/2
ELLIPTIC-VISIT CONTINUATION: NINE LEGAL FIFTH RETURNS, FACTOR 2
EXPERIMENTAL ENDPOINT: L=log(2^3164*5^534/3^2777)
THREE-LAYER LOCAL FORMULAS: STILL AVAILABLE THROUGH e=3h
GERM-74: NOT EXECUTED
CANONICAL THEOREM CURSOR: SZ-CROSS-COLLAR-3, UNCHANGED
RATIFICATION / PUBLIC PROMOTION: NONE
```
