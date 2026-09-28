# SZ edge recurrence 70 — sixth-visit control and forced-neighbor continuation

**Date:** 2026-09-28  
**Branch:** sz-cross-collar  
**Standing:** UNRATIFIED RESIDUE / ONE NF PASS / SCOPED POSITIVE RESULT  
**Canonical parent:** SZ-CROSS-COLLAR-3, unchanged  
**Immediate input:** GERM-69, retaining the pre-65 refold  
**Public promotion:** forbidden

## 0. Result and precise scope

The first sixth-visit word is controlled by a wider rational cone chart. Once the elliptic sixth-visit nonwrap word becomes active, its forced neighboring steps give a third-section certificate. The same chart handles the ensuing seventh- and eighth-visit cases without separate local-layer passes.

The new source-equation statement is

```math
\boxed{3h-\kappa+5\tau<e\le3h-\tau
\quad\Longrightarrow\quad x=0\text{ in both scalar parity kernels}.}
```

Combining this with the inherited coverage and GERM-60 reconstruction gives the experimental ambient endpoint

```math
\boxed{0<L\le L_{70}:=\log(16/3)+3h-\tau
=\log\!\left(\frac{2^{116}5^{18}}{3^{98}}\right)
=1.710951079292712878\ldots.}
```

This is a scoped, unratified source-equation result. The inherited three-layer formulas remain available through e=3h, but exclusion is not proved here on `(3h-tau,3h]` or beyond. No canonical ratification, full-form-domain persistence theorem, selected-packet custody result, or RH proof is asserted.

## 1. Custody, retained equations, and parameters

Entry pin: `monocap-tech/weil-lab@8aff3f5bca9d887e4f11542594fe98ae3c09db6f`. The live branch matched that pin at entry. Governance remains `notes/SZ_CROSS_COLLAR_RATIFICATION_20260926.md`; integration remains `notes/SZ_KERNEL_EDGE_PRE65_REFOLD_20260927.md`. The source-level local reduction and injective reconstruction are inherited from `_recurrence67.md`, Sections 1-5 and 9. Immediate section identities are `_recurrence69.md`, Sections 2-4 and 8. GERM-60 remains the ambient equivalence dependency with its original scope.

The mounted GERM-69 note has Git blob `4a98e54e4deed49ef5632dc183cb5325a703209e`. The executable byte-pins its GERM-69/68/65 helper dependencies and the GERM-67 output fixture. The fixture is only a regression target: all physical coefficient bounds are recalculated from rational logarithm/square-root enclosures and small paired-source solves.

New notation is registered in [GERM-70 terminology](../docs/TERMINOLOGY_GERM70.md). Companion files are [the verifier](../tools/sz_six_visit_neighbor_audit.py) and [the complete recorded audit](_recurrence70_audit.json).

Retain

```math
h=\log(81/80),\quad k=\log(16/15),\quad\kappa=k-5h,
\quad\lambda=h-\kappa,\quad\tau=h-5\kappa,\quad\theta=\kappa-8\tau,
```

```math
e=2h+\eta,\qquad\nu=\eta-\lambda.
```

The new range is `5tau<nu<=kappa-tau`. Exact prime-power comparison sharpens the remainder bounds to

```math
\boxed{\frac\tau4<\theta<\frac\tau3.}                 \tag{1}
```

The actual source observation is still

```math
W(t)=\binom{x(t)}{\varepsilon x(u-t)},\qquad u=k+e.
```

It is a bounded observation of the original L2 scalar parity profile, with its inherited reflection compatibility. No classical endpoint trace or independent state coordinate is added. The necessary original circle recurrence is the GERM-67 six-map equation `W(Rt)=T(t)W(t)`, with `R(t)=t+kappa mod h` and the same source/target overlap bits. This note does not rederive those local matrices.

## 2. Extend the existing second-section word domains

The first section is `E=(lambda,h)`, with physical coordinate `t=lambda+z`. Its return map remains `S(z)=z-tau mod kappa`. GERM-69's five first-section matrices are

```math
A_1=P E_+^3Q,\quad D_1=P E_+^4Q,\quad
Q_1=E_+^4Q,\quad P_1=P E_+^4E_-,\quad E_1=E_+^4E_-.
```

Here `P=T_10^+`, `Q=T_01^-`, and `E_+=T_11^+`, `E_-=T_11^-`. All products act rightmost first.

These five types remain sufficient while `nu<=kappa-tau`. Nonwrap S-steps decrease z and cannot leave `(0,nu)`. A wrap target is strictly larger than kappa-tau, hence outside `(0,nu)` even at the new endpoint. The second exterior section `F=(kappa-tau,kappa)` is therefore still outside the overlap. Its physical interval is `(h-tau,h)`.

Use `z=kappa-tau+y`, `0<y<tau`. Its return is

```math
S_2(y)=y+\theta\pmod\tau,\qquad
N(y)=\begin{cases}8,&y<\tau-\theta,\\9,&y>\tau-\theta.\end{cases}
```

Write `q=S2(y)`. Before the final first-section wrap, the smallest z coordinate is exactly q, and successive preceding coordinates differ by tau. Thus the number s of section-overlap visits satisfies

```math
q+(s-1)\tau<\nu<q+s\tau.                             \tag{2}
```

The complete ordered word is still

```math
D_{s,N}=P_1E_1^{s-1}Q_1A_1^{N-s-1}.                  \tag{3}
```

The source cells now allow s through 8, but always s<=N-1. This is a domain extension of the ordered formula, not an assertion that arbitrary s,N or arbitrary word concatenations are legal. The new verifier checks every used word against each original h-circle source/target bit and first-section return domain.

The inherited determinant identities give `det D_(s,N)=1`: the P1/Q1 factors cancel, and the other factors have determinant one. The numerical bounds below nevertheless divide by directly computed positive determinant enclosures, rather than assuming exact normalization in interval arithmetic.

For convenience set

```math
U_s=D_{s,8}\ (s=5,6,7),\qquad V_s=D_{s,9}\ (s=5,6,7,8).
```

## 3. First sixth-visit strip: a wider chart suffices

First take

```math
5\tau<\nu\le5\tau+\theta.
```

Put zeta=nu-5tau. On the N=8 branch, q lies in `(theta,tau)`, so q>zeta and s=5. On the N=9 branch, q lies in `(0,theta)`, so s=6 when q<zeta and s=5 otherwise. Hence exactly three possible matrices suffice:

```math
U_5,\qquad V_5,\qquad V_6.
```

Use

```math
C_{\rm lo}=\begin{pmatrix}1&1/2\\-2&10\end{pmatrix}.
```

The rational audit proves that `C_lo^-1 U5 C_lo`, `-C_lo^-1 V5 C_lo`, and `C_lo^-1 V6 C_lo` are all strictly positive. Their forward same-sign and backward opposite-sign l1 factors are bounded below as follows (deliberately weakened from the recorded rational bounds):

| Word | Forward factor | Backward factor |
| --- | --- | --- |
| U5 | >1.840 | >2.534 |
| V5 | >4.951 | >7.993 |
| V6 | >3.460 | >1.705 |

Thus 3/2 is a common forward/backward expansion factor in this chart. The formerly problematic V6 is not elliptic; its expanding direction simply lay outside the old GERM-69 chart. At nu=5tau+theta the generic V5 branch disappears; U5 and V6 still obey the same certificate. This endpoint is checked directly.

Immediately above that strip, U6 becomes legal. It is genuinely elliptic: its determinant is one, its trace is between -1.9 and -1.7, and its discriminant is strictly negative. We do not append U6 to a generator-wise expanding cone. Its forced neighbors must be retained.

## 4. Third section: group the forced neighboring steps

For the remaining new range use

```math
5\tau+\theta\le\nu\le\kappa-\tau=7\tau+\theta.
```

Inside F's y circle, choose the third section

```math
G=(0,\theta),\qquad\alpha=\tau-3\theta.
```

Equation (1) gives `0<alpha<theta`. Physically G is `(h-tau,h-tau+theta)` and remains outside the source overlap throughout the claimed range.

Starting from y in G, the second-section positions increase by theta until the first wrap. The first return to G takes

```math
\ell(y)=\begin{cases}4,&0<y<\alpha,\\3,&\alpha<y<\theta.\end{cases}
```

Indeed, all pre-wrap positions other than y exceed theta and remain below tau. The last wraps into `(0,theta)`. Consequently

```math
S_3(y)=\begin{cases}
y+4\theta-\tau,&0<y<\alpha,\\
y+3\theta-\tau,&\alpha<y<\theta,
\end{cases}
\qquad S_3(y)=y-\alpha\pmod\theta.                    \tag{4}
```

The images are `(theta-alpha,theta)` and `(0,theta-alpha)`, which tile G up to endpoints. S3 is therefore invertible and Lebesgue-measure preserving.

Every pre-final S2 step is nonwrapping, so its second-section word has N=8. The final step wraps and has N=9. One complete third return therefore contains `8ell+1` first-section steps and `41ell+5` original R-steps: respectively 128 or 169 original rotation steps. No favorable padding is inserted; all these steps precede the actual first return to G.

## 5. Sixteen words, including all ensuing visit counts

Let q_j be the successive S2 targets during a third return. The nonfinal q_j increase strictly and lie in `(theta,tau)`. The final target q lies in `(0,theta)`. Applying (2) gives the following complete classification:

| Parameter band | Nonwrap visit counts | Final wrap count |
| --- | --- | --- |
| `[5tau+theta,6tau]` | An initial run of 6, then 5 | 6 |
| `[6tau,6tau+theta]` | All 6 | 6 or 7 |
| `[6tau+theta,7tau]` | An initial run of 7, then 6 | 7 |
| `[7tau,7tau+theta]` | All 7 | 7 or 8 |

The initial run may be empty or occupy every nonwrap step. At band boundaries the equality seams remove finitely many source points, not an entire parameter value. These bands exhaust the range; they do not introduce separate mathematical passes.

It follows that the complete library is

```math
\boxed{B_{b,m,\ell}=V_b U_{b-1}^{\ell-m-1}U_b^m,
\quad b\in\{6,7\},\quad\ell\in\{3,4\},
\quad0\le m\le\ell-1,}                              \tag{5}
```

plus

```math
\boxed{C_\ell=V_8 U_7^{\ell-1},\qquad\ell=3,4.}      \tag{6}
```

There are fourteen words in (5) and two in (6). The middle bands reuse the endpoint words of these families; they do not require extra matrices. For example, the second band uses `B_(6,ell-1,ell)` or `B_(7,0,ell)`.

The verifier checks the exact affine parameter cells for all sixteen words. It substitutes every S2 point into the parent word-domain calculation, lifting each complete return to all of its 128 or 169 original R-step source domains. It also verifies absence of an earlier G hit. No numerical orbit selection or large orbit determinant is used.

At nu=kappa-tau, only the two C_ell words survive generically. The open intervals F and the section overlap touch but do not intersect. The certificate allows equality only in that global separation margin; all actual source-point inequalities remain strict off the finite threshold seams. Both endpoint faces are checked directly.

## 6. One rational chart for the sixteen forced-neighbor words

Use

```math
C_{\rm hi}=\begin{pmatrix}1&1\\-13/8&2\end{pmatrix},
\qquad C_{\rm hi}^{-1}=\frac1{29}\begin{pmatrix}16&-8\\13&8\end{pmatrix}.
```

Positive representatives are obtained with the signs

```math
\sigma(B_{6,m,\ell})=(-1)^m,\qquad
\sigma(B_{7,m,\ell})=(-1)^{\ell+1},\qquad
\sigma(C_\ell)=(-1)^{\ell+1}.
```

For every word B in the library, the outward rational audit proves every entry of `sigma(B) C_hi^-1 B C_hi` strictly positive. It gives these weakened family-wise bounds:

| Family | Minimum forward factor | Minimum backward factor |
| --- | --- | --- |
| All B_(6,m,ell) | >1.959 | >1.698 |
| All B_(7,m,ell) | >1.494 | >7.809 |
| C3 and C4 | >3.289 | >5.017 |

The full individual enclosures are recorded in the audit. For any positive matrix `A=[[a,b],[c,d]]` with positive determinant delta, its same-sign l1 expansion is at least `min(a+c,b+d)`, and its inverse expands the opposite-sign cone by at least `min(d+c,b+a)/delta`. Both quantities are evaluated with outward bounds.

Thus all sixteen actual signed matrices obey

```math
\boxed{\|B'v\|_1\ge\frac75\|v\|_1\quad(v\in C_+),
\qquad\|(B')^{-1}v\|_1\ge\frac75\|v\|_1\quad(v\in C_-),} \tag{7}
```

where `B'=C_hi^-1 B C_hi`, `C_+={XY>=0}`, and `C_-={XY<=0}`. The associated forward/backward double cones are preserved. The actual overall signs are not deleted: simultaneous negation preserves both double cones and the norm.

The low parameter strip uses the same statement with chart C_lo and factor 3/2. These factors are per complete induced return, not per original R-step. In particular, (7) does not assert expansion for arbitrary iterates of the elliptic U6.

## 7. L2 exclusion and faithful reconstruction

Fix the parameter. On the low strip define `Z(y)=C_lo^-1 W(h-tau+y)` for `0<y<tau` and use S2. On the high strip use `Z(y)=C_hi^-1 W(h-tau+y)` for `0<y<theta` and use S3. Each is an L2 observation, and the necessary source recurrence gives the corresponding signed matrix equation almost everywhere.

Remove the source exceptional sets and their countably many relevant affine/rotation preimages, so the equations and their iterates hold on a common full-measure set. No classical boundary values of x are used.

For real Z, split the section into `E_+={Z1 Z2>=0}` and `E_-={Z1 Z2<0}`. If c is the relevant expansion factor, forward cone invariance gives

```math
c^{2n}\int_{E_+}\|Z(y)\|_1^2dy
\le\int_{\text{section}}\|Z(y)\|_1^2dy.
```

Measure preservation of S2 or S3 justifies the bound on the iterated argument. The right side is finite and independent of n. Backward cone invariance gives the same bound on E_- using inverse iterates. Letting n increase forces Z to vanish almost everywhere. Apply the argument to real and imaginary parts for complex profiles.

For the high strip, every point outside G reaches G at its first S2 wrap in at most four steps, by (1). All the used second-section maps are invertible, so zero on G propagates to all of F. On the low strip, zero on F was obtained directly.

The inherited finite return geometry then propagates zero from F to E in at most eight S-steps, and from E to the h-circle in at most five R-steps. GERM-67's bounded local reconstruction uses at most eight h-steps to cover the low head, after which its middle and tail Schur formulas reconstruct zero on the entire scalar profile interval.

Every reconstruction is on actual source solutions; surjectivity from arbitrary vector fields to scalar sources is unnecessary and is not assumed. This proves the stated exclusion with the inherited norm-controlled, injective observation. It does not assume pointwise boundedness on dense orbits or use a heuristic Lyapunov exponent.

## 8. Endpoint arithmetic and inherited scope

The exact arithmetic is

```math
3h-\tau=2h+5\kappa=5k-23h,
```

```math
\exp L_{70}=(16/3)(16/15)^5(80/81)^{23}
=\frac{2^{116}5^{18}}{3^{98}}.
```

The verifier independently checks this expression using the rational exponential arguments of kappa and tau, and checks strict ordering between the old endpoint, L70, and the e=3h endpoint.

Combining with GERM-69 and the earlier inherited coverage gives

```math
\boxed{\ker P_c=\{0\},\qquad K_c^{\rm ps}=K_c\cap\ker P_c=\{0\},
\qquad0<L\le L_{70}.}
```

The Kc conclusion keeps its regular-kernel scope. No full-form-domain null-persistence exclusion, selected-packet ownership theorem, or global uniform-in-L norm gap is added. The present cone constants are estimates for these induced source recurrences.

## 9. Exact stop: the second exterior section itself becomes internal

Above the new endpoint put

```math
\nu=\kappa-\tau+\zeta,\qquad0<\zeta<\theta.
```

For a first-section coordinate `0<z<zeta`, the wrap starts inside the overlap and its target `z+kappa-tau` also lies inside it. The original six-step word is now

```text
11-, 11+, 11+, 11+, 11+, 11+.
```

Equivalently, its matrix is

```math
\boxed{J_1=E_+^5E_-.}                                \tag{8}
```

The final 10+ exit in the old P1 word has become an internal 11+ step. The verifier checks the entire concrete source-domain strip for (8). This is the first missing first-section species, not a numerical failure of a matrix enclosure.

F now intersects the source overlap, so the outside-to-outside D_(s,N) formulas used here cannot simply be carried beyond nu=kappa-tau. The note does not assert that J1 fails every chart or that no further induction works. It records the precise new domain and word requiring treatment.

The remaining part of the already-derived three-layer range is

```math
3h-\tau<e\le3h,
```

of width exactly `tau=0.000292914274630127729...`. The full unresolved four-delay range remains

```math
\boxed{3h-\tau<e\le j,\qquad L_{70}<L\le\log6.}
```

No result above this endpoint is claimed.

## 10. Execution receipt and audit limits

Run with assertions enabled:

```text
python tools/sz_six_visit_neighbor_audit.py
```

The verifier completed successfully with exit code zero. It recalculates the physical maps through the pinned small paired-source solver, checks the inherited regression boxes, certifies three low-strip and sixteen third-return matrices with their forward/backward bounds, proves the exact nested source domains and endpoint faces, and checks the new inside-to-inside wrap guard and endpoint arithmetic.

The repeated product identities follow from the explicit chronological words. Enclosure overlap between different parenthesizations is reported only as a regression. The numerical audit does not independently re-prove the inherited local symbolic identities or the full GERM-60 ambient reduction.

Executable SHA-256:

```text
3bebf33464665ceef4b75a25ae8b30effc935a6ff19e6fbb40631d3325f003c8
```

Executable Git blob:

```text
cc69ccd60dee5c83b5c355c048fb190a1acd5196
```

Raw stdout SHA-256:

```text
67caebf1182b290347ac822db09f6c257086bf44ecef1816659794a67133c2c7
```

The committed audit is a compact serialization of the complete stdout JSON, with no fields removed. Its SHA-256 is `a826be1188b7e9d081c5aaca93bb2c3e9d6227e662f6763ad5c3edada5e445f9`. The executable records hashes of its expanded original words; those words are recoverable from the recorded second-section word sequences and pinned first-section definitions.

The full parent symbolic suites and old large determinant programs were not rerun. This is a rational computational certificate accompanying the written source-domain and L2 proof, not Lean certification or canonical ratification.

## 11. Next individual target

```text
SZ-KERNEL-EDGE-GERM-71 / SECOND-SECTION SELF-OVERLAP CONTROL
```

Start from (8), retaining the same three-layer local matrices. Incorporate the inside-to-inside first-section wrap and the now-internal part of F, then seek a valid section/word or cone-field certificate on the final `(3h-tau,3h]` portion. Keep any continuation beyond e=3h separate from the existing formula scope. Do not restart flat determinant enumeration or reopen the stopped screw-family route.

```text
GERM-70: COMPLETE AS A SCOPED EXPERIMENTAL PASS
SIXTH VISIT AND FORCED NEIGHBORS: CONTROLLED THROUGH nu=kappa-tau
LOW STRIP: THREE SECOND-SECTION WORDS, FACTOR 3/2
HIGH STRIP: SIXTEEN THIRD-SECTION WORDS, FACTOR 7/5
EXPERIMENTAL ENDPOINT: L=log(2^116*5^18/3^98)
THREE-LAYER LOCAL FORMULAS: STILL AVAILABLE THROUGH e=3h
SECOND-SECTION SELF-OVERLAP ABOVE THE ENDPOINT: OPEN
GERM-71: NOT EXECUTED
CANONICAL THEOREM CURSOR: SZ-CROSS-COLLAR-3, UNCHANGED
RATIFICATION / PUBLIC PROMOTION: NONE
```

This updates only the pending GERM-70 status. Historical notes and their standing remain unchanged.
