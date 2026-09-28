# SZ edge recurrence 71 — second-section self-overlap and an exterior replacement section

**Date:** 2026-09-28  
**Branch:** sz-cross-collar  
**Standing:** UNRATIFIED RESIDUE / ONE NF PASS / SCOPED POSITIVE RESULT  
**Canonical parent:** SZ-CROSS-COLLAR-3, unchanged  
**Immediate input:** GERM-70, retaining the pre-65 refold  
**Public promotion:** forbidden

## 0. Result and precise scope

The missing inside-to-inside first-section wrap is now incorporated. The second-section cocycle again has six source/target overlap types, with no new independent source coordinate. An exterior replacement third section has seven complete return words controlled by one rational chart.

The new source-equation theorem is

```math
\boxed{3h-\tau<e\le3h-\theta
\quad\Longrightarrow\quad x=0\text{ in both scalar parity kernels},
\qquad\theta=\kappa-8\tau.}
```

Together with the inherited coverage and GERM-60 reconstruction, this gives the experimental ambient endpoint

```math
\boxed{0<L\le L_{71}:=\log(16/3)+3h-\theta
=\log\!\left(\frac{3^{904}}{2^{1024}5^{175}}\right)
=1.7111613866195986229\ldots.}
```

The retained local three-layer formulas remain available through e=3h. No exclusion on `(3h-theta,3h]` or beyond is proved here. This is an unratified source-equation result, not canonical ratification, a full-form-domain persistence theorem, selected-packet custody, or RH closure.

## 1. Source custody and the parameter change

Entry pin: `monocap-tech/weil-lab@dd94ef57114d520169965fd4b4d558143fed90d4`. The live branch matched this pin. Governance remains `notes/SZ_CROSS_COLLAR_RATIFICATION_20260926.md`; the pre-65 refold remains the integration record. Read `_recurrence67.md` for the local three-layer source reduction and reconstruction, `_recurrence68.md`/`_recurrence69.md` for the two nested section maps, and `_recurrence70.md`, especially its inside-to-inside wrap guard.

The mounted GERM-70 proof matches its pinned Git blob `41d05c57567925ca56015784ce1661b56b1d4fa0`. The new verifier checks the byte hashes of the GERM-69, GERM-68, and GERM-65 helpers and the GERM-67 output fixture before use. That fixture is a regression target, not the numerical source of new coefficients. The physical matrices are freshly recalculated by small outward rational paired-source solves. Their mathematical derivation and the ambient reduction retain their inherited standing.

New definitions are registered in [GERM-71 terminology](../docs/TERMINOLOGY_GERM71.md). Companion files are [the new verifier](../tools/sz_second_section_self_overlap_audit.py) and [its complete audit](_recurrence71_audit.json).

Retain

```math
h=\log(81/80),\quad k=\log(16/15),\quad
\kappa=k-5h,\quad\lambda=h-\kappa,\quad
\tau=h-5\kappa,\quad\theta=\kappa-8\tau.
```

The exact fixed inequalities, checked by integer prime-power comparison, are

```math
0<\theta,\qquad3\theta<\tau<4\theta.
```

Set

```math
\zeta=e-(3h-\tau),\quad
\eta=e-2h=h-\tau+\zeta,\quad
\nu=\eta-\lambda=\kappa-\tau+\zeta.
```

The new proof range is `0<zeta<=tau-theta`. It lies strictly within the retained three-layer formula range. The actual source observation remains

```math
W(t)=\binom{x(t)}{\varepsilon x(u-t)},\qquad u=k+e,
\qquad\varepsilon\in\{+1,-1\}.
```

This is the bounded L2 observation of the scalar source, with its inherited reflection compatibility, not an independent boundary jet. GERM-67 supplies the necessary h-circle equation `W(Rt)=T(t)W(t)`, where `R(t)=t+kappa mod h` and T is its original six-map library. This pass does not rederive that local system.

## 2. Incorporate the first inside-to-inside wrap

Use the parent abbreviations `P=T_10^+`, `Q=T_01^-`, and `E_+=T_11^+`, `E_-=T_11^-`. The first section is `(lambda,h)`, with coordinate `0<z<kappa` and induced map `S(z)=z-tau mod kappa`.

The first-section species needed in this strip are

```math
Q_1=E_+^4Q,\qquad E_1=E_+^4E_-,\qquad
P_1=P E_+^4E_-,\qquad J_1=E_+^5E_- .                 \tag{1}
```

Their chronological original words are

```text
Q1: 01-, 11+, 11+, 11+, 11+.
E1: 11-, 11+, 11+, 11+, 11+.
P1: 11-, 11+, 11+, 11+, 11+, 10+.
J1: 11-, 11+, 11+, 11+, 11+, 11+.
```

All products act rightmost first. J1 is exactly the missing GERM-70 species: its final target stays inside, so replacing its last 11+ by 10+ would change the source equation.

Let rho denote the positive inherited original entry/exit determinant ratio, as in GERM-67. Then `det Q1=rho^-1`, `det P1=rho`, and `det E1=det J1=1`. These factors are retained. They follow by multiplying the inherited determinant library, not by rounding computed determinants.

## 3. Six exact second-section types survive self-overlap

The second section F is physically `(h-tau,h)`. Write `t=h-tau+y`, `0<y<tau`. Its map is still

```math
S_2(y)=y+\theta\pmod\tau.                            \tag{2}
```

Its source-overlap interval is now exactly `0<y<zeta`; F is no longer entirely exterior. The second return uses eight first-section steps without wrap in (2), or nine with wrap.

To derive every word, start at `z0=kappa-tau+y`. Before the last first-section wrap,

```math
z_j=\kappa-(j+1)\tau+y,\qquad0\le j<N,\quad N=8\text{ or }9.
```

The intermediate points `j=1,...,N-1` are all below `kappa-tau`, hence inside `(0,nu)`. Only the source and final target depend on their overlap bits. The initial first-section step is Q1 or E1, depending on the source bit. The final step is P1 or J1, depending on the target bit. Every intervening step is E1.

The six second-section maps are therefore

| Type | Source/target bits | Exact matrix | Chronological first-section word |
| --- | --- | --- | --- |
| A2 = 00+ | exterior/exterior | `P1 E1^6 Q1` | Q1, six E1, P1 |
| P2 = 10+ | interior/exterior | `P1 E1^7` | seven E1, P1 |
| E2+ = 11+ | interior/interior | `J1 E1^7` | seven E1, J1 |
| D2 = 00- | exterior/exterior | `P1 E1^7 Q1` | Q1, seven E1, P1 |
| Q2 = 01- | exterior/interior | `J1 E1^7 Q1` | Q1, seven E1, J1 |
| E2- = 11- | interior/interior | `J1 E1^8` | eight E1, J1 |

The signs plus/minus specify nonwrap/wrap in (2). The other bit patterns, 01+ and 10-, are impossible by interval ordering. With `V(y)=W(h-tau+y)`, the exact necessary equation is

```math
V(S_2y)=T^{(2)}(y)V(y).                               \tag{3}
```

The determinant library is again

```math
1,\quad\rho,\quad1,\quad1,\quad\rho^{-1},\quad1.     \tag{4}
```

Every second nonwrap word contains 41 original R-steps; every wrap word contains 46. The verifier checks all six affine domain cells over `0<zeta<tau`, including every first-section point and every original R-step. Thus this is an exact reappearance of the six-type overlap structure at this particular scale. It is not yet an arbitrary-depth renormalization theorem.

## 4. Choose an exterior replacement third section

Unlike the bottom third section in GERM-70, use

```math
G_{\rm ext}=(\tau-\theta,\tau),\qquad
y=\tau-\theta+v,\quad0<v<\theta.                    \tag{5}
```

Physically this is `(h-theta,h)`. It stays outside `(0,zeta)` when `zeta<=tau-theta`.

Put `alpha=tau-3theta`. The first S2 step wraps to v. Following it, the positions are `v+theta`, `v+2theta`, and, if needed, `v+3theta`. The complete return time is

```math
\ell(v)=\begin{cases}4,&0<v<\alpha,\\3,&\alpha<v<\theta.\end{cases}
```

The pre-return points are below `tau-theta`; the last lies above it and below tau. In v coordinates the return is

```math
S_{3,\rm ext}(v)=
\begin{cases}v+\theta-\alpha,&0<v<\alpha,\\
v-\alpha,&\alpha<v<\theta.
\end{cases}                                           \tag{6}
```

The images are `(theta-alpha,theta)` and `(0,theta-alpha)`, which tile the section up to endpoints. Hence the induced map is an invertible Lebesgue-measure-preserving rotation by -alpha on the theta-circle.

The initial S2 step wraps and the rest do not. Thus one full return has `8ell+1` first-section steps and `41ell+5` original R-steps: 128 or 169. These are actual first returns; no matrices are added artificially to improve growth.

## 5. Seven complete words cover the whole new strip

Let s count the consecutive overlap positions after the first wrap. If s=0, `zeta<v`. Otherwise

```math
v+(s-1)\theta<\zeta<v+s\theta.
```

Since the section is exterior, the last point is outside and `0<=s<=ell-1`. The complete library consists of the three possibilities for ell=3 and the four for ell=4:

```math
\boxed{B_{0,\ell}=A_2^{\ell-1}D_2,\qquad
B_{s,\ell}=A_2^{\ell-s-1}P_2(E_2^+)^{s-1}Q_2
\quad(1\le s<\ell).}                                \tag{7}
```

Chronologically B0 begins with D2, not with A2. For s>0 the word begins with Q2, passes through the internal overlap steps, exits by P2, and finishes with the forced ordinary A2 steps. Formula (4) gives determinant one for every complete word.

Exact affine polytopes certify all seven word cells, absence of an earlier section hit, all source/target bits, and all lifted original R-step domains. The certificate uses the normalization `theta=1`, `3<tau/theta<4`, not sampled threshold positions.

At `zeta=tau-theta`, only `(s,ell)=(2,3)` and `(3,4)` survive generically. Their faces are checked separately. The open section and overlap merely touch, so the global section-separation margin may be zero; the actual source points remain strictly in their licensed intervals off finitely many threshold seams. Parameter endpoints are not discarded as if they were null seed sets.

## 6. One rational cone chart and expansion factor

Use

```math
C_{71}=\begin{pmatrix}1&1\\0&3\end{pmatrix},\qquad
C_{71}^{-1}=\begin{pmatrix}1&-1/3\\0&1/3\end{pmatrix}.
```

For every word in (7), define

```math
\widehat B_{s,\ell}=(-1)^{\ell+1}C_{71}^{-1}B_{s,\ell}C_{71}.
```

The outward rational audit proves every entry of all seven B-hat matrices strictly positive and their determinants positive. The following weakened lower bounds come from the successful audit:

| s | ell | Sign | Forward l1 factor | Backward opposite-sign l1 factor |
| --- | --- | --- | --- | --- |
| 0 | 3 | + | >10.890 | >4.190 |
| 1 | 3 | + | >5.972 | >3.005 |
| 2 | 3 | + | >2.667 | >3.067 |
| 0 | 4 | - | >20.638 | >7.323 |
| 1 | 4 | - | >11.703 | >4.409 |
| 2 | 4 | - | >6.127 | >3.127 |
| 3 | 4 | - | >2.550 | >2.537 |

For a positive matrix `B=[[a,b],[c,d]]` with positive determinant delta, the forward same-sign l1 factor is at least `min(a+c,b+d)`. Its inverse preserves the opposite-sign cone and has factor at least `min(d+c,b+a)/delta`. The code evaluates these expressions with outward bounds and the directly calculated positive determinant enclosure, rather than silently inserting det=1 into a numerical division.

Thus, for the double cones `C_+={XY>=0}` and `C_-={XY<=0}`,

```math
\boxed{\|\widehat Bz\|_1\ge\frac52\|z\|_1\quad(z\in C_+),
\qquad\|\widehat B^{-1}z\|_1\ge\frac52\|z\|_1\quad(z\in C_-).} \tag{8}
```

The forward and backward cones are preserved. The actual transformed equation still contains the overall sign `(-1)^(ell+1)`. Simultaneous negation preserves both double cones and the norm, so deleting that sign from the physical equation is neither necessary nor permitted.

The bounds are per complete return of 128 or 169 original steps. They do not assert expansion for every second-section generator. Floating exploratory calculations selected the candidate chart; none supplies a sign or inequality used in this certificate.

## 7. L2 exclusion and faithful reconstruction

For an actual scalar source define

```math
Z(v)=C_{71}^{-1}W(h-\theta+v),\qquad0<v<\theta.
```

Restriction, translation, and the fixed chart are bounded, so Z is in L2. The inherited source equations and the new exact inductions give

```math
Z(S_{3,\rm ext}v)=C_{71}^{-1}B_{s(v),\ell(v)}C_{71}Z(v)
=(-1)^{\ell(v)+1}\widehat B_{s(v),\ell(v)}Z(v)
```

almost everywhere. Remove the source exceptional sets and their countably many required affine/rotation preimages to obtain a common full-measure set for iteration. No classical boundary value of x is introduced.

For real Z, partition the section into `E_+={Z1 Z2>=0}` and `E_-={Z1 Z2<0}`. Forward cone invariance and (8), together with measure preservation, give

```math
(5/2)^{2n}\int_{E_+}\|Z(v)\|_1^2\,dv
\le\int_0^\theta\|Z(v)\|_1^2\,dv.
```

The right side is finite and independent of n; hence Z vanishes on E+. Apply the backward cone and inverse estimate to E- for the same conclusion. Real and imaginary parts obey the same real matrix equation, so complex source profiles are excluded as well.

Therefore W is zero on `(h-theta,h)`. Every y below `tau-theta` reaches G_ext in at most three successive +theta steps, without an intervening wrap. All six second-section maps are invertible, so W is zero on F. The parent geometry carries zero from F to the first section in at most eight S-steps, then to the h-circle in at most five R-steps. The inherited bounded three-layer reconstruction takes at most eight h-steps to cover the low head; its middle and tail Schur formulas then reconstruct zero on the full scalar source interval.

This remains an injective, norm-controlled observation on actual source solutions. Surjectivity from arbitrary vector fields to scalar sources is not asserted or needed. In particular, the proof never assumes pointwise boundedness of an L2 function along a dense orbit.

## 8. Endpoint arithmetic and inherited scope

Since

```math
\theta=\kappa-8\tau=41\kappa-8h=41k-213h,
\qquad3h-\theta=216h-41k,
```

we have

```math
\exp L_{71}=(16/3)(81/80)^{216}(15/16)^{41}
=\frac{3^{904}}{2^{1024}5^{175}}.
```

The verifier checks this rational identity independently through the exponential arguments of kappa and tau, and checks `L70<L71<log(16/3)+3h`.

Combining the new strip with the inherited GERM-63/65-70 coverage and the GERM-60 equivalence gives

```math
\boxed{\ker P_c=\{0\},\quad K_c^{\rm ps}=K_c\cap\ker P_c=\{0\},
\qquad0<L\le L_{71}.}
```

The Kc conclusion retains its regular-kernel scope. No full-form-domain null-persistence exclusion, selected-packet ownership theorem, or global uniform-in-L gap is added. The cone factor in (8) concerns this induced recurrence only.

## 9. Exact stop: the exterior replacement section becomes internal

Above the endpoint put

```math
\zeta=\tau-\theta+\epsilon_*,\qquad
0<v<\epsilon_*<\min(\alpha,\theta-\alpha).
```

This is a nonempty strip because `0<alpha<theta`. The section source `tau-theta+v` is now inside the overlap, as is its wrap target v. Its first S2 letter changes from 01- to 11-. The next two letters remain internal 11+, and the final 10+ exits to G_ext. The exact new complete word is

```math
\boxed{B_{\rm changed}=P_2(E_2^+)^2E_2^- .}           \tag{9}
```

The verifier checks its entire concrete domain and original-step lift. Its transformed enclosure is centered near

```math
C_{71}^{-1}B_{\rm changed}C_{71}\approx
\begin{pmatrix}-0.991559102&0.465882752\\
-1.099011617&-1.143803417\end{pmatrix}.
```

Neither overall sign makes it preserve the current same-sign double cone. Its determinant is rho, not one. The audit certifies

```math
\operatorname{tr}B_{\rm changed}\in(-2.1353625188,-2.1353625187),
\quad\det B_{\rm changed}\in(1.6461592457,1.6461592458),
```

```math
(\operatorname{tr}B_{\rm changed})^2-4\det B_{\rm changed}
\in(-2.0248638967,-2.0248638966).
```

Thus it is projectively elliptic despite its trace having absolute value greater than two. This does not assert bounded powers for the unnormalized matrix: its determinant is greater than one. Nor does it prohibit expansion in some adapted norm, a section-dependent chart, or further legal-word grouping. The actual proved failure is of the present signed-quadrant chart/library. No nonzero kernel is constructed.

The remaining part of the inherited local three-layer range is

```math
3h-\theta<e\le3h,
```

of width `theta=0.00008260694774438328444...`. The full unresolved four-delay range is still

```math
\boxed{3h-\theta<e\le j,\qquad L_{71}<L\le\log6.}
```

The six retyped second-section formulas have already been derived on `0<zeta<tau`; the next pass should not rederive the layer system or drop J1 when moving the section.

## 10. Execution receipt and audit limits

Run with assertions enabled:

```text
python tools/sz_second_section_self_overlap_audit.py
```

The verifier completed with exit code zero. It recalculates the physical maps by the pinned small paired-source rational solver, checks the parent regression boxes, certifies six retyped second-section domain cells, all seven signed-cone matrices and both growth bounds, every nested source-domain lift, the new endpoint faces, and the changed-word guard. It checks the determinant exponents of complete expanded words and the endpoint arithmetic.

The product identities follow from literal chronological word substitution. Intersections between enclosures from two parenthesizations are reported as regressions, not proofs of equality. The audit does not independently re-prove the inherited local symbolic identities or the full ambient source reduction.

Executable SHA-256:

```text
d0e725cc800aee9564bf79877d851c3c0d49299a4681ab9302ce80c7d3c1e8ad
```

Executable Git blob:

```text
fe616f9732b8c248c98fe17edcfce8ca81125d2e
```

Raw stdout SHA-256:

```text
e876db9bd3901a1f4d4df3abc35e281c25630320bc8664b126aad5bc967e7f31
```

The committed audit uses the lossless `GERM71-AUDIT-WORDS-1` encoding. Its `audit` field contains the complete stdout object, except that each repeated `original_word` array is represented by the marker `@expand:first_section_word`. Replace that marker by concatenating the corresponding `first_section_word` entries through the top-level `original_word_dictionary`. The exact decoded object equals the full raw stdout object, and its indented serialization reproduces the raw stdout hash above. This preserves every expanded word without manual repetition. The audit file SHA-256 is `f837da6405cce7a6aff2f67b381e00d9986dad4e41abf142b970dd21357d132b`.

Read-back detected a transcription mismatch in an initial expanded-word upload. The corrected lossless encoding was checked against the executed output before completion. The verifier and its successful mathematical bounds were unchanged.

The full parent symbolic suites and old large determinant programs were not rerun. This is an outward rational computational certificate accompanying the written source-domain and L2 proof, not Lean certification or canonical ratification.

## 11. Next individual target

```text
SZ-KERNEL-EDGE-GERM-72 / THIRD-SECTION SELF-OVERLAP CONTROL
```

Start from the six retyped second-section maps and (9). Preserve source/target overlap bits and determinant factors when the exterior replacement section becomes internal. Seek a legal-word or cone-field control on `(3h-theta,3h]`, keeping any movement beyond e=3h separate from the inherited formula scope. The exact recurrence of the six overlap types is useful structural input, not yet a theorem permitting unrestricted further induction. Do not restart flat determinants or reopen the stopped screw-family route.

```text
GERM-71: COMPLETE AS A SCOPED EXPERIMENTAL PASS
INSIDE-TO-INSIDE FIRST-SECTION WRAP: INCORPORATED
SELF-OVERLAP SECOND SECTION: SIX EXACT RETYPED MAPS
EXTERIOR REPLACEMENT THIRD SECTION: SEVEN WORDS, FACTOR 5/2
EXPERIMENTAL ENDPOINT: L=log(3^904/(2^1024*5^175))
THREE-LAYER FORMULAS: STILL AVAILABLE THROUGH e=3h
REMAINING THREE-LAYER EXCLUSION WIDTH: theta
GERM-72: NOT EXECUTED
CANONICAL THEOREM CURSOR: SZ-CROSS-COLLAR-3, UNCHANGED
RATIFICATION / PUBLIC PROMOTION: NONE
```

This updates only the pending GERM-71 status. Historical notes and their standing are unchanged.
