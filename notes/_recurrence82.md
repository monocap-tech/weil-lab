# SZ edge recurrence 82 — post-sigma8 ninth-map transfer and direct ninth exclusion

**Date:** 2026-09-28  
**Branch:** sz-cross-collar  
**Standing:** UNRATIFIED RESIDUE / ONE NF PASS / SCOPED POSITIVE RESULT  
**Canonical parent:** SZ-CROSS-COLLAR-3, unchanged  
**Entry commit:** d7da5057bc1f8d998037d51005fb67f6c6df6719  
**Public promotion:** forbidden

## 0. Result and exact scope

The changed ninth word B1 B0^2 A1 is included with its actual intermediate
source bits. A single signed rational chart controls all seven complete
ninth words throughout the remaining GERM-81 eighth-map window. No tenth
induction is used for this new interval, and no retained coordinate is added.

With t=e-e80, the new source-equation result is
```math
\boxed{\sigma_8<t\le\psi_7\quad\Longrightarrow\quad
x=0\text{ in both scalar parity kernels}.}
```
Combining with inherited coverage and GERM-60 equivalence gives the
experimental ambient endpoint
```math
\boxed{L_{82}=L_{80}+\psi_7=L_{81}+\nu_8
=\log\!\left(\frac{3^{1936158}}{2^{2202828}5^{372926}}\right)
=1.711212167401521129852679262098\ldots,}
```
where `nu8=psi7-sigma8=chi7-2psi7`. The increment is approximately
`2.80730248424006036538e-8`. The endpoint t=psi7 is included by direct source
checks, not a continuity inference. No exclusion above L82 is proved.
This is not closure of the larger three-layer range or full four-delay
problem, canonical ratification, full-form-domain persistence, selected-packet
custody, a global uniform norm gap, or RH.

## 1. Source custody and entry replay

The live branch matched the entry pin. Governance remains
`notes/SZ_CROSS_COLLAR_RATIFICATION_20260926.md`; the pre-65 refold remains
the integration record. GERM-73's correction of GERM-72 remains in force.
Neither the rejected ordinary words nor their factor 40 is used.

The mounted GERM-81 verifier matched its Git blob and SHA-256. Its separate
entry replay exited zero with stdout SHA-256
```text
01b29dab7256045bde981373094c0ae6ff10fedbacf8cea6964b54b4bb6eb90e
```
matching the recorded output byte for byte. This is not ratification of its
inherited dependencies.

The new verifier pins GERM-81 and its transitive helper bytes. Physical
matrices are freshly recomputed through the small paired-source outward
rational solver at grid 10^120, with 400 logarithm-series terms and explicit
remainder bounds. The GERM-71 boxes are regression targets, not rounded
numerical inputs. The original scalar equations, ambient equivalence, and
norm-controlled reconstruction remain inherited under their stated scopes.

Companion records: [terminology](../docs/TERMINOLOGY_GERM82.md),
[verifier](../tools/sz_post_sigma8_ninth_map_audit.py), and
[execution receipt](_recurrence82_audit.json). Complete output and executable
dependencies are included in the certificate bundle.

## 2. The actual ninth-word partition

All A_i, B_i, U_i, V_i below are **GERM-81-local**. Retain
```math
A_i=U_0V_i,\qquad B_i=U_0^2V_i,\qquad i=0,1,
```
on their proved range `0<t<=psi7`. The eighth rotation is negative-sigma8
translation on `(0,psi7)`. Its source bit is 1 exactly when that source is
below t. No seventh or eighth formula is changed within the present range.

For brevity write `sigma=sigma8`, `psi=psi7`, `rho=psi-3sigma`, and
`c=sigma-rho=c10`, so `3sigma<psi<4sigma`. The ninth section is unchanged:
`K9=(0,sigma)`. From y in K9, its first-return path is
```math
p_0=y,\qquad p_j=y+\psi-j\sigma\quad(1\le j\le n),
```
truncated after n steps, with n=3 for y<c and n=4 for y>c. More precisely,
`p0=y`, `pj=y+psi-j*sigma` for `1<=j<=n`, and the last point is
`q=pn` in `(0,sigma)`. Every pre-final point after y exceeds sigma, so these
are first returns. The target is y+rho for n=3, and y-c for n=4.

Because t>sigma, the initial source y always uses A1. Every later
pre-final source uses B0 or B1. Those sources descend in sigma increments;
the sources below t form a final consecutive run of length s. Thus
```math
\boxed{N_{s,n}=B_1^sB_0^{n-s-1}A_1,
\qquad n=3,4,\quad0\le s<n.}
```
Products act rightmost first. The complete word starts with A1, then takes
n-s-1 B0 steps, then s B1 steps. For s=0 its exact condition is
`t<q+sigma`. For s>0 the condition is
```math
q+s\sigma<t<q+(s+1)\sigma.
```
For s=n-1 the upper inequality is automatic from t<=psi and y>0, but it is
still checked. The cut y<c or y>c, the target range, and these comparisons
exhaust the possible words. There are exactly seven across the full interval,
not necessarily seven at each fixed parameter.

Every ninth cell is tested against the eighth-domain contract at **every**
intermediate source. Each output equals the next input as an exact affine
identity. The lower sixth, seventh, and eighth contracts are separately
rechecked on their full stated scopes. Thus endpoint bits are never used as
a substitute for intermediate source legality.

At t=2sigma only s=1 occurs generically on both return branches; at t=3sigma
only s=2 occurs. These junction faces are checked directly. At t=psi the
surviving words are
```math
N_{2,3}=B_1^2A_1,\qquad N_{3,4}=B_1^3A_1.
```
The inherited eighth A1/B1 endpoint faces and both new ninth endpoint faces
pass directly. At t=sigma the s=0 words reproduce the GERM-81 endpoint
Q and S by literal substitution; their lower faces are also checked.

## 3. Direct ninth dynamics and one chart

The ninth map is
```math
S_9(y)=\begin{cases}y+\rho,&0<y<c,\\y-c,&c<y<\sigma,\end{cases}
\qquad S_9(y)=y+\rho\pmod\sigma.
```
The images `(rho,sigma)` and `(0,rho)` tile the section. Hence S9 is invertible
and Lebesgue-measure preserving. The tower identity is `3c+4rho=psi`.
The physical field is still `W(t0+y)`, where
```math
t_0=h-\beta+\gamma-\xi+2\eta_7.
```

Use the constant rational chart
```math
C_{82}=\begin{pmatrix}1&-1\\-12/5&21/10\end{pmatrix},
\qquad\det C_{82}=-3/10.
```
The sign of the second column is intentional; the chart is not restricted
to columns whose first coordinates are both positive. Set
```math
\widehat N_{s,n}=\epsilon_{s,n}C_{82}^{-1}N_{s,n}C_{82},
\qquad \epsilon_{s,n}=\begin{cases}+1,&s=n-1,\\-1,&s<n-1.\end{cases}
```
Fresh outward rational arithmetic proves every entry of all seven
representatives strictly positive, with these certified lower bounds:

| s | n | Sign | Forward | Backward |
| --- | --- | --- | --- | --- |
| 0 | 3 | - | >18.3195707992 | >13.7512787550 |
| 1 | 3 | - | >98.8939893415 | >68.1494896679 |
| 2 | 3 | + | >31.9750564213 | >34.7500602785 |
| 0 | 4 | - | >3.8887760770 | >3.5598692789 |
| 1 | 4 | - | >117.7379717628 | >80.0936023511 |
| 2 | 4 | - | >635.0599571410 | >438.3575866658 |
| 3 | 4 | + | >205.3381249282 | >222.8330835644 |

Every product has exact determinant one by the inherited determinant
exponents. The numerical inverse estimate nevertheless divides by the
directly computed positive interval determinant. For positive
`M=[[a,b],[c,d]]`, the forward same-sign l1 factor is at least
`min(a+c,b+d)`, and the inverse preserves the opposite-sign double cone
with factor at least `min(d+c,b+a)/det(M)`.

Therefore, on `C+={XY>=0}` and `C-={XY<=0}`,
```math
\boxed{\|\widehat Nv\|_1\ge\tfrac72\|v\|_1\quad(v\in C_+),
\qquad\|\widehat N^{-1}v\|_1\ge\tfrac72\|v\|_1\quad(v\in C_-).}
```
The actual signs remain in the recurrence. Simultaneous negation preserves
both double cones and the norm. All seven actual matrices also have
certified positive discriminant; their hyperbolicity alone would not be
a common-cone proof, which is why the entry signs and both factors are checked.

These estimates apply per **complete ninth return**. Their original-step
counts are 965,296 and 1,319,293, verified from the literal source words.
The matrices remain 2-by-2. There is no tenth-return construction for this
new interval, no per-original-step factor claim, and no global norm-gap claim.

## 4. L2 exclusion and faithful reconstruction

For an actual scalar source define `Z(y)=C82^-1 W(t0+y)` on `(0,sigma)`.
This is in L2 by bounded restriction, translation, and the fixed chart.
Source equations and the domain-certified substitutions give
```math
Z(S_9y)=\epsilon_{s(y),n(y)}\widehat N_{s(y),n(y)}Z(y)
```
almost everywhere. Remove the inherited exceptional sets and their countably
many required affine/rotation preimages before iterating. No classical
endpoint trace is introduced.

For real Z let E+ be the set where its coordinate product is nonnegative,
and E- its complement. Forward cone invariance and measure preservation give
```math
(7/2)^{2m}\int_{E_+}\|Z(y)\|_1^2\,dy
\le\int_0^\sigma\|Z(y)\|_1^2\,dy.
```
The right side is finite and independent of m. Thus Z vanishes almost
everywhere on E+. The inverse-cone estimate gives the same conclusion on E-.
Apply the real argument separately to real and imaginary parts for complex
sources. No pointwise boundedness on a dense orbit is assumed.

Every eighth-coordinate point above sigma reaches K9 after at most three
negative-sigma steps, since psi<4sigma. The eighth maps are valid and
invertible through t=psi. Thus the entire eighth circle is zero. Every
seventh-coordinate point above psi reaches the eighth section after at most
two negative-psi steps. Its maps are still within t<chi since psi<chi.
GERM-81's rederived sixth atoms and first-return towers propagate zero to
the sixth circle; inherited finite lower-section reconstruction then covers
the h-circle, low head, middle bands, and tail. All these maps are on actual
scalar-source solutions, not arbitrary vector fields. Surjectivity from
vector cocycles to scalar sources is neither asserted nor needed.

## 5. Endpoint arithmetic and scope

The exact residual identity is
```math
\psi_7=502358h-96695k
=-2396212\log2+2106127\log3-405663\log5.
```
Consequently
```math
e_{82}=e_{80}+\psi_7=461817h-88891k,
```
and adding log(16/3) gives the vector `(-2202828,1936158,-372926)`.
Its difference from the GERM-81 vector is nu8. Rational logarithm enclosures
certify the positive increment and remaining width without floating cancellation.

Under the inherited ambient equivalence and coverage,
```math
\boxed{\ker P_c=\{0\},\quad K_c^{\rm ps}=K_c\cap\ker P_c=\{0\},
\qquad0<L\le L_{82}.}
```
The Kc conclusion retains regular-kernel scope. The remaining already-derived
three-layer width is
```math
3h-e_{82}=0.0000318261658218763548833727053067\ldots.
```
The full unresolved four-delay interval remains `L82<L<=log6`.
Neither larger interval is claimed closed.

## 6. Exact next source change: a new eighth branch

Above t=psi write `t=psi+eps`, with `0<eps<nu8`. On
```math
\sigma<z<\sigma+\varepsilon
```
the three-step eighth return has seventh sources
`z, z+chi-psi, z+chi-2psi`. Their bits are interior, exterior, interior.
Its exact chronological word and matrix are
```math
V_1,U_0,U_1,\qquad J_8=U_1U_0V_1.
```
These are GERM-81-local matrices, not earlier namesakes. The old B1 was
U0^2 V1. The seventh formulas are valid on the entire tested strip, so the
new audit licenses this change directly from seventh-domain contracts.

The new matrix has determinant one and rational bounds
```math
-2.4551989352<\operatorname{tr}J_8<-2.4551989351,
\qquad2.0280018112<(\operatorname{tr}J_8)^2-4\det J_8<2.0280018113.
```
It is hyperbolic. No cone impossibility or nonzero kernel is claimed.
The stopping reason is the changed eighth source branch beyond its completed
formula window, not an unhandled ninth word inside the proved range.
No new exclusion above t=psi is issued here.

## 7. Execution and stopping state

The final verifier exited zero. It freshly recalculates physical coefficients,
rechecks the lower sixth/seventh/eighth composition contracts and surviving
eighth endpoint faces, tests all seven ninth cells, all cone signs and both
factors, lower and upper endpoint faces, both integer-sigma junctions, the
next eighth branch, and exact endpoint vectors. The GERM-81 entry replay
matched its recorded output. The receipt supplies actual file and output
hashes; the bundle contains both complete output serializations.

An initial local run reached JSON serialization but failed because a summary
variable was overwritten by a list of affine margins. That output-variable
collision was repaired before the successful final execution; no certificate
is attributed to the failed run. Mathematical assertions were not removed.
Full lower symbolic suites, the full GERM-60 reduction, and the old large
determinant inventory were not rerun. Floating reconnaissance selected the
chart only; all certificate signs and domain tests are exact or outward rational.
This is not Lean certification or canonical ratification.

Next individual target:
```text
SZ-KERNEL-EDGE-GERM-83 / POST-PSI7 EIGHTH-MAP TRANSFER
```
Start from the GERM-81-local U1 U0 V1 and its exact source strip. Preserve
the completed t<=psi7 window, physical translations, the seventh formula
scope, all intermediate source contracts, the GERM-72 correction, and the
original three-layer endpoint. Do not restart flat determinants or reopen
the stopped screw route.

```text
GERM-82: COMPLETE AS A SCOPED EXPERIMENTAL PASS
NEW EXCLUSION: sigma8<t<=psi7, t=e-e80
NINTH SECTION: SEVEN COMPLETE WORDS, ONE SIGNED CHART, FACTOR 7/2
TENTH INDUCTION: NOT USED FOR THE NEW INTERVAL
EIGHTH FORMULA ENDPOINT t=psi7: INCLUDED BY DIRECT DOMAIN TESTS
EXPERIMENTAL ENDPOINT: L=log(3^1936158/(2^2202828*5^372926))
NEXT EIGHTH WORD: U1 U0 V1, GERM-81-LOCAL, HYPERBOLIC
THREE-LAYER LOCAL FORMULAS: STILL AVAILABLE THROUGH e=3h
GERM-83: NOT EXECUTED
CANONICAL THEOREM CURSOR: SZ-CROSS-COLLAR-3, UNCHANGED
RATIFICATION / PUBLIC PROMOTION: NONE
```
