# SZ edge recurrence 69 — overlapping-section control by a second exterior return

**Date:** 2026-09-28  
**Branch:** sz-cross-collar  
**Standing:** UNRATIFIED RESIDUE / ONE NF PASS / SCOPED POSITIVE RESULT  
**Canonical parent:** SZ-CROSS-COLLAR-3, unchanged  
**Immediate input:** GERM-68, retaining the pre-65 refold  
**Public promotion:** forbidden

## 0. Result and precise scope

The section-overlap word that defeated the GERM-68 cone chart can be absorbed into a longer legal return. A second fixed exterior section gives twelve complete words, all controlled by one new rational chart. The exact new source-equation statement is

```math
\boxed{3h-\kappa<e\le3h-\kappa+5\tau
\quad\Longrightarrow\quad x=0
\text{ in both scalar parity kernels},\qquad \tau=h-5\kappa.}
```

Combining this with the inherited coverage and GERM-60 reconstruction advances the experimental ambient endpoint to

```math
\boxed{L_{69}=\log(16/3)+3h-\kappa+5\tau
=\log\!\left(\frac{3^{577}}{2^{652}5^{112}}\right)
=1.710282643795708\ldots.}
```

The local three-layer formulas remain inherited through e=3h. The exclusion endpoint is strictly below 3h. No exclusion beyond L69, canonical ratification, full-form-domain persistence theorem, or RH proof is asserted.

## 1. Source custody and parameter conventions

Entry pin: `monocap-tech/weil-lab@54d94f4e26e82069f0bab1620063f63c6f70a7a6`. The live `sz-cross-collar` branch matched that pin at entry. Governance is `notes/SZ_CROSS_COLLAR_RATIFICATION_20260926.md`; the integration record is `notes/SZ_KERNEL_EDGE_PRE65_REFOLD_20260927.md`. The local source identities and injective reconstruction are inherited from `_recurrence67.md`, Sections 1-5 and 9; the immediate first-section construction is `_recurrence68.md`, Sections 2-4 and 8. Earlier ambient equivalence remains `_recurrence60.md` with its original scope.

The mounted GERM-68 note has Git blob `cfe6335618d5df79f449bf42e7eb3f1d8375dfa2`. The mounted GERM-68 verifier has blob `dd84bd79f00f955c4d26d80a495ac8f17291f0ed`, matching the file read from the entry commit. The new verifier checks byte hashes of that helper, the GERM-65 interval helper, and the GERM-67 output fixture before use. The fixture is a regression target, not the numerical input to the new coefficient bounds.

New definitions are registered in [GERM-69 terminology](../docs/TERMINOLOGY_GERM69.md). Companion artifacts are [the executable verifier](../tools/sz_overlapping_section_audit.py) and [its recorded output](_recurrence69_audit.json).

Retain

```math
h=\log(81/80),\quad k=\log(16/15),\quad
\kappa=k-5h,\quad\lambda=h-\kappa,\quad\tau=h-5\kappa,
```

```math
e=2h+\eta,\qquad \nu=\eta-\lambda,\qquad
\theta=\kappa-8\tau.
```

Here nu is a section-overlap width, not a physical prime coefficient. Exact prime-power comparison gives

```math
\boxed{0<\theta<\tau,\qquad8\tau<\kappa<9\tau.}             \tag{1}
```

In particular, `5tau<kappa-tau`, and

```math
0<\nu\le5\tau
\quad\Longrightarrow\quad
\lambda<\eta< h,\qquad2h<e<3h.
```

Thus the entire new interval lies inside the already-derived local three-layer formula range; no new local source regime is assumed.

For each external parity epsilon, the actual state remains

```math
W(t)=\binom{x(t)}{\varepsilon x(u-t)},\qquad u=k+e.
```

It is an L2 observation of the original scalar source, with its inherited reflection compatibility. No extra independent state coordinates or classical endpoint traces are introduced.

## 2. The first section after it overlaps the source overlap

Retain the original h-circle rotation and the GERM-68 section:

```math
R(t)=t+\kappa\pmod h,\qquad
\mathcal E=(\lambda,h),\qquad t=\lambda+z,\quad0<z<\kappa.
```

The first-return geometry of R to E does not depend on eta. It still gives

```math
\mathcal S(z)=z-\tau\pmod\kappa,
```

with five R-steps when z>tau and six when z<tau. What changes at eta>lambda is the source/target overlap status: the part of E inside the source overlap is exactly `0<z<nu`.

Write the inherited six-map names as

```math
P=T_{10}^+,\quad Q=T_{01}^-,\quad
E_+=T_{11}^+,\quad E_-=T_{11}^-.
```

Every point strictly between the initial and final E visit lies below lambda, hence inside `(0,eta)`. Consequently its internal steps are E+. The first wrap is Q or E- according to source status; the last step is P or E+ according to target status. This gives the five needed first-section matrices:

| S-step | Source / target section-overlap status | Original R-steps | Matrix |
| --- | --- | --- | --- |
| z>tau | outside / outside | 5 | `A1=P E_+^3 Q` |
| z<tau | outside / outside | 6 | `D1=P E_+^4 Q` |
| z>tau | outside / inside | 5 | `Q1=E_+^4 Q` |
| z<tau | inside / outside | 6 | `P1=P E_+^4 E_-` |
| z>tau | inside / inside | 5 | `E1=E_+^4 E_-` |

All products act rightmost first. The source-overlap wrap P1 is precisely the changed word from GERM-68; it is not discarded or replaced by the old Q-entry word.

There are no further types in the present range. For z>tau, S(z)=z-tau is smaller than z, so an inside-to-outside step is impossible. For z<tau, the target is larger than kappa-tau, hence outside the overlap by (1) and nu<=5tau. Thus an inside-to-inside wrap cannot occur here.

Let rho be the positive determinant ratio from GERM-67. The inherited identities give

```math
\det A_1=\det D_1=\det E_1=1,\qquad
\det P_1=\rho,\qquad\det Q_1=\rho^{-1}.                \tag{2}
```

The matrices are recalculated by small outward rational paired-source solves in the new verifier, with all six original map enclosures checked against the pinned GERM-67 boxes. The local mathematical derivation is inherited, not silently re-certified by interval overlap alone.

## 3. A second fixed section stays outside the overlap

For the S rotation, choose

```math
\mathcal F=(\kappa-\tau,\kappa),\qquad
z=\kappa-\tau+y,\quad0<y<\tau.
```

In the original h-circle this is simply `(h-tau,h)`. It is disjoint from the section overlap `(0,nu)` for every nu in the claimed range.

Put `kappa=8tau+theta`. Beginning at z, the orbit descends by tau until the next wrap. Its first return to F takes

```math
N(y)=\begin{cases}
8,&0<y<\tau-\theta,\\
9,&\tau-\theta<y<\tau.
\end{cases}                                               \tag{3}
```

To check this directly, write

```math
z_j=\kappa-(j+1)\tau+y\quad(0\le j<N),\qquad
q_y=z_{N-1}=\kappa-N\tau+y\in(0,\tau).
```

Every z_j with j>0 and j<N lies below kappa-tau. Every step before the last is a nonwrap S-step; the last maps q_y to `q_y+kappa-tau`, which belongs to F. No earlier F hit occurs.

In y coordinates the second induced map is therefore

```math
\mathcal S_2(y)=
\begin{cases}
y+\theta,&0<y<\tau-\theta,\\
y+\theta-\tau,&\tau-\theta<y<\tau.
\end{cases}                                               \tag{4}
```

The two images are `(theta,tau)` and `(0,theta)`. They tile `(0,tau)` up to endpoints. Thus S2 is invertible and Lebesgue-measure preserving. The proof uses this exact translation tiling, not an approximation to a return orbit.

## 4. Twelve legal words cover the full new interval

Because the z_j descend strictly before the final wrap, any visits to `(0,nu)` are consecutive at the end of that descent. Let s count them. If s=0, then `nu<q_y`. Otherwise

```math
q_y+(s-1)\tau<\nu<q_y+s\tau.                            \tag{5}
```

Since q_y>0 and nu<=5tau, the complete range is

```math
s\in\{0,1,2,3,4,5\},\qquad N\in\{8,9\}.
```

Thus twelve words suffice simultaneously over the parameter range. They are

```math
\boxed{
D_{0,N}=D_1A_1^{N-1},\qquad
D_{s,N}=P_1E_1^{s-1}Q_1A_1^{N-s-1}\quad(1\le s\le5).
}                                                        \tag{6}
```

For s>=1 the chronological order is ordinary S-steps, overlap entry, internal overlap steps, and overlap exit at the last wrap. All ordinary steps in (6) are forced by the first-return geometry. This is not arbitrary multiplication by favorable matrices.

Each word contains N S-steps, of which N-1 take five original R-steps and the final wrap takes six. Therefore the original R-return length is

```math
5N+1\in\{41,46\}.
```

Equation (2) proves `det D_(s,N)=1`. In particular, nonunit factors at overlap entry/exit are preserved and then cancel; no individual non-SL2 map is retyped as SL2.

The executable certifies every cell in (3)-(5) by exact rational polytope inequalities after normalizing tau=1 and putting `r=kappa/tau in (8,9)`. It checks each intermediate first-section point, source/target overlap bit, absence of an earlier F hit, and the full lift of each word to its 41 or 46 original R-step domains. This is finite word/domain certification, not sampled topology or a large orbit determinant.

At nu=5tau, exactly the s=5 words survive generically, for both N=8 and N=9. Their endpoint faces are checked separately. The remaining threshold seams are finitely many y values for each fixed parameter before their countable iterates are removed. No claim about an omitted parameter endpoint is inferred from the nullity of a seed seam.

## 5. One rational chart and a uniform expansion factor

Use

```math
C_2=\begin{pmatrix}1&1\\1&20\end{pmatrix},\qquad
C_2^{-1}=\frac1{19}\begin{pmatrix}20&-1\\-1&1\end{pmatrix}.
```

Define the positive representatives

```math
\widehat D_{s,N}=(-1)^N C_2^{-1}D_{s,N}C_2.
```

The outward rational audit proves that every entry of all twelve D-hat matrices is strictly positive. The following table weakens the successful bounds deliberately:

| s | N | Sign | Forward l1 factor | Backward opposite-sign l1 factor |
| --- | --- | --- | --- | --- |
| 0 | 8 | + | >6696.98 | >995.81 |
| 1 | 8 | + | >2316.29 | >523.67 |
| 2 | 8 | + | >712.04 | >222.15 |
| 3 | 8 | + | >188.47 | >82.29 |
| 4 | 8 | + | >38.21 | >27.14 |
| 5 | 8 | + | >2.535 | >5.826 |
| 0 | 9 | - | >19491.94 | >2898.38 |
| 1 | 9 | - | >6741.71 | >1524.18 |
| 2 | 9 | - | >2072.44 | >646.60 |
| 3 | 9 | - | >548.57 | >239.53 |
| 4 | 9 | - | >111.22 | >79.05 |
| 5 | 9 | - | >7.391 | >19.016 |

For a positive matrix `B=[[a0,b0],[c0,d0]]`, forward same-sign l1 expansion is bounded below by `min(a0+c0,b0+d0)`. If its positive determinant is delta, the inverse preserves the opposite-sign double cone with expansion at least `min(d0+c0,b0+a0)/delta`. The verifier evaluates these expressions using outward interval arithmetic and a directly computed positive determinant enclosure. It does not assume det=1 in order to divide in the numerical stage.

Consequently, on `C_+={XY>=0}` and `C_-={XY<=0}`,

```math
\boxed{
\|\widehat Dv\|_1\ge\frac52\|v\|_1\quad(v\in C_+),\qquad
\|\widehat D^{-1}v\|_1\ge\frac52\|v\|_1\quad(v\in C_-).
}                                                        \tag{7}
```

The actual transformed matrix is `(-1)^N D-hat`, not D-hat alone. The overall sign stays in the equation. Simultaneous negation preserves both double cones and the norm, so (7) and the associated cone invariance also hold for the actual signed matrices.

No claim is made that the earlier elliptic generators or short excursions individually expand. The certificate concerns only the complete legal words (6).

## 6. L2 exclusion on the second section

For the actual source, put

```math
U(y)=C_2^{-1}W(h-\tau+y),\qquad0<y<\tau.
```

Restrictions, translations, and the fixed invertible chart are bounded, so U is in L2. The source equations and the two exact inductions imply almost everywhere

```math
U(\mathcal S_2 y)=C_2^{-1}D_{s(y),N(y)}C_2U(y)
=(-1)^{N(y)}\widehat D_{s(y),N(y)}U(y).
```

Remove the source exceptional sets and their countably many needed affine/rotation preimages to obtain a common full-measure set for all iterations. No classical endpoint value of x is used.

For a real U, let `Y_+={U1 U2>=0}` and `Y_-={U1 U2<0}`. Forward double-cone invariance and (7) give

```math
(5/2)^{2n}\int_{Y_+}\|U(y)\|_1^2\,dy
\le\int_0^\tau\|U(y)\|_1^2\,dy.
```

The inequality follows by applying measure preservation of S2 to the iterated argument; the right side is finite and independent of n. Letting n increase proves U=0 almost everywhere on Y+. Backward cone invariance and the inverse inequality give the same result on Y-. Apply the real argument separately to real and imaginary parts for complex source profiles.

Thus W vanishes almost everywhere on the physical section `(h-tau,h)`. This argument does not infer pointwise boundedness along a dense orbit or use a heuristic Lyapunov exponent.

## 7. Reconstruction and experimental endpoint

Every z outside F reaches F under successive negative tau steps and the first wrap in at most eight S-steps, by `kappa<9tau`. The five first-section maps are invertible, so zero on F implies zero on all of E.

Every point of `(0,lambda)` reaches E after at most five successive +kappa steps, before an additional wrap; the inherited six-map return library is invertible. Hence W is zero on the full h-circle. The GERM-67 local reconstruction, with at most eight h-steps and bounded local maps/inverses in this formula range, propagates zero to the low head. Its middle and tail Schur formulas reconstruct zero on the whole scalar source interval.

This retains an injective, norm-controlled observation of actual source solutions. Surjectivity of arbitrary vector fields onto scalar sources is neither assumed nor needed.

Since

```math
3h-\kappa+5\tau=8h-26\kappa=138h-26k,
```

we have

```math
\exp L_{69}=(16/3)(81/80)^{138}(15/16)^{26}
=\frac{3^{577}}{2^{652}5^{112}}.
```

Together with the inherited GERM-63/65/66/67/68 coverage and GERM-60 equivalence,

```math
\boxed{\ker P_c=\{0\},\qquad
K_c^{\rm ps}=K_c\cap\ker P_c=\{0\},\qquad0<L\le L_{69}.}
```

The Kc statement retains its regular-kernel scope. The common expansion factor in this note is a bound for the induced source recurrence, not a new global uniform-in-L kernel gap. No full-form-domain null-persistence exclusion, selected-packet ownership result, or RH closure follows from this pass alone.

## 8. Exact stopping boundary: the sixth section-overlap visit

Above nu=5tau, another word becomes legal. Write

```math
\nu=5\tau+\zeta,\qquad0<\zeta<\theta.
```

On the N=9 strip where `0<q_y<zeta`, equivalently

```math
\tau-\theta<y<\tau-\theta+\zeta,
```

there are exactly six overlap positions. The new complete word is

```math
\boxed{D_{6,9}=P_1E_1^5Q_1A_1^2.}                       \tag{8}
```

The verifier checks this source-domain strip and its full lift. In the present chart it certifies

```math
C_2^{-1}D_{6,9}C_2\in
\begin{pmatrix}
(9.3131245687,9.3131245688)&(44.4055738957,44.4055738958)\\
(-0.9773326401,-0.9773326400)&(-4.5526092188,-4.5526092187)
\end{pmatrix}.
```

The two rows have opposite signs. Neither overall sign preserves the present same-sign double cone. The trace lies in `(4.7605153499,4.7605153500)`; this immediate new word is not being mislabeled elliptic. Its failure is a failure of this common chart/library, not evidence of a nonzero kernel or a no-go for an admissible-word cone field or further induction.

No exclusion beyond nu=5tau is asserted. The still-unresolved part of the existing local three-layer range is

```math
3h-\kappa+5\tau<e\le3h.
```

Its width is `kappa-5tau=0.000961349771634766...`. The full unresolved four-delay range remains

```math
\boxed{3h-\kappa+5\tau<e\le j,\qquad L_{69}<L\le\log6.}
```

Later coefficient/layer changes beyond e=3h remain outside this pass.

## 9. Execution receipt and audit limits

Run with assertions enabled:

```text
python tools/sz_overlapping_section_audit.py
```

The verifier completed with exit code zero. It recalculates the physical two-/three-layer maps by small outward rational solves, checks their containment in the pinned six-map boxes, certifies all twelve signed-cone products and both expansion bounds, proves the nested source-word geometry including every original h-circle step, and checks the endpoint and the first sixth-visit scope guard.

It also checks the exact prime-power inequalities (1) and the endpoint arithmetic. Interval consistency tests between two parenthesizations are regression checks; the ordered product identities follow from the explicit words and are not proved merely by overlapping numerical enclosures.

Executable SHA-256:

```text
0283a3412d0ef9d029e690693b472ad656602ca817e3d730d7c48234361602e4
```

Executable Git blob:

```text
429fb4994e5953c41f1372918789182b66701feb
```

Raw execution stdout SHA-256:

```text
3184b5c975c966aab8b1e1c61d192557bbe124460c489725583f723dd29716eb
```

The committed audit JSON is a whitespace-normalized serialization of the complete stdout JSON; no fields are removed. Its SHA-256 is `36dad32483727acbd9230457f4aa08b59a07d68ec46a93520cb1cba157edfb10`. The default verifier emits the indented form whose raw hash is recorded above.

The full parent symbolic suites and old large determinant programs were not rerun. This pass reuses their stated source derivations and performs the explicitly narrower rational recalculation and new nested-return certificate. This is a computational certificate accompanying a written source-domain and L2 proof, not Lean certification or canonical ratification.

## 10. Next individual target

```text
SZ-KERNEL-EDGE-GERM-70 / SIX-VISIT SECOND-SECTION CONTROL
```

Start from the existing three-layer formulas, the five first-section maps, and (8). Determine whether the newly legal sixth-visit word can be controlled by its forced neighboring words or a section-dependent chart. Preserve the twelve-word result where applicable. Do not rebuild the layer system, restart flat orbit determinants, or reopen the stopped screw shortcut.

```text
GERM-69: COMPLETE AS A SCOPED EXPERIMENTAL PASS
OVERLAPPING SECTION: CONTROLLED THROUGH nu=5tau
TWELVE NESTED WORDS: ONE SIGNED RATIONAL CONE CHART
EXPERIMENTAL ENDPOINT: L=log(3^577/(2^652*5^112))
THREE-LAYER LOCAL FORMULAS: STILL AVAILABLE THROUGH e=3h
SIXTH-VISIT WORD: NOT ABSORBED INTO THE CURRENT CONE LIBRARY
GERM-70: NOT EXECUTED
CANONICAL THEOREM CURSOR: SZ-CROSS-COLLAR-3, UNCHANGED
RATIFICATION / PUBLIC PROMOTION: NONE
```

This updates only the pending GERM-69 status. Historical notes and their standing remain unchanged.
