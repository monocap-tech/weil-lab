# SZ edge recurrence 68 — multi-visit control by a fixed exterior section

**Date:** 2026-09-27 (America/Los_Angeles)  
**Branch:** sz-cross-collar  
**Standing:** UNRATIFIED RESIDUE / ONE NF PASS / SCOPED POSITIVE RESULT  
**Canonical parent:** SZ-CROSS-COLLAR-3, unchanged  
**Immediate input:** GERM-67, retaining the pre-65 refold  
**Public promotion:** forbidden

## 0. Result and scope

The elliptic two-visit excursion from GERM-67 does not prevent a longer legal-return cone certificate. Inducing to one fixed exterior section includes the ordinary steps that must occur between successive visits to that section. One rational chart controls all nine resulting words, covering one through five overlap visits at once.

The new source-equation conclusion is

```math
\boxed{2h+\kappa<e\le3h-\kappa
\quad\Longrightarrow\quad x=0
\text{ in both scalar parity kernels}.}
```

Together with the inherited GERM-63/65/66/67 coverage and GERM-60 reconstruction, this advances the experimental ambient endpoint to

```math
\boxed{0<L\le L_{68}:=
\log\!\left(\frac{3^{32}}{2^{32}5^7}\right)
=\log\!\left(\frac{1853020188851841}{335544320000000}\right)
=1.708818072422557\ldots.}
```

The local three-layer formulas still have their inherited domain `2h<e<=3h`. Kernel exclusion is not claimed on `(3h-kappa,3h]` or beyond. The new interval is an unratified source-equation theorem, not canonical SZ advancement, a full-form-domain persistence theorem, or an RH proof.

## 1. Source custody and notation

Entry pin: `monocap-tech/weil-lab@1a2738cf539efb7d50644be1e47d64d94db66134`. The live branch was checked against this pin before execution. Governance remains `notes/SZ_CROSS_COLLAR_RATIFICATION_20260926.md`; the pre-65 refold remains the integration record. Immediate mathematical input is `_recurrence67.md`, especially Sections 1-5 and 9. Earlier source reductions are `_recurrence60.md`, `_recurrence61.md`, `_recurrence65.md`, and `_recurrence66.md` at the same entry pin.

The mounted GERM-67 proof has Git blob `685ed930d025e7796c36f205ee76224dc3d365aa`, matching the pinned source. New notation is registered in [GERM-68 terminology](../docs/TERMINOLOGY_GERM68.md). Companion files are [the executable verifier](../tools/sz_multivisit_section_audit.py) and [its successful output](_recurrence68_audit.json).

Retain

```math
e=2h+\eta,\quad h=\log(81/80),\quad k=\log(16/15),
\quad\kappa=k-5h,\quad\lambda=h-\kappa,
\quad\tau=h-5\kappa.
```

Thus `lambda=4kappa+tau`, and the inherited exact arithmetic gives `0<tau<kappa`, equivalently `5kappa<h<6kappa`. The new proof range is

```math
\kappa<\eta\le\lambda.
```

The coefficient symbols retain the GERM-67 meanings:

```math
\mu=\frac{\log3}{\sqrt3\log2},\quad
\beta=\sqrt{2/3}\frac{\log3}{\log2},\quad
 d=\frac{\log5}{\sqrt5\log2},\quad
b=\beta\mu,\quad a=b^2,\quad g=1-a,\quad\Delta=1-\mu^2.
```

For each external parity epsilon, the actual observation is

```math
W(t)=\binom{x(t)}{\varepsilon x(u-t)},\qquad u=k+e.
```

It is a bounded observation of the original L2 scalar source, not a freely supplied boundary jet.

## 2. Reuse the three-layer reduction, not another orbit assembler

GERM-67 establishes, in its entire three-layer formula domain, the necessary return equation

```math
W(Rt)=T(t)W(t),\qquad R(t)=t+\kappa\pmod h.
```

The six map types are labeled by whether the source and target lie in `I_eta=(0,eta)` and whether the step wraps around the h-circle. They are `00+`, `10+`, `11+`, `00-`, `01-`, `11-`; the other two bit patterns are forbidden by the interval ordering. Their exact source derivation, invertibility, and norm-controlled reconstruction are retained with their original scope.

For this pass abbreviate

```math
A=T_{00}^+,\qquad P=T_{10}^+,\qquad
Q=T_{01}^-,\qquad E_+=T_{11}^+.
```

From GERM-67, `det A=det E_+=1`, `det P=rho`, and `det Q=rho^{-1}` with `rho>0`. The short two-visit excursion `P E_+ Q` remains elliptic. The new argument never assumes expansion for that isolated block or for arbitrary words in the six generators.

The new verifier independently recomputes all six physical map enclosures from the small paired-source systems. In particular, with `f=d/(g Delta)` and `alpha=a/d`, it encodes the inherited source identities

```math
W_i=\binom{A_i}{f(D_i-\alpha D_{i-1})},\qquad
V_i=\binom{f(C_i-\alpha C_{i+1})}{B_i},
```

```math
C_i=\mu A_i+B_i,\quad D_i=A_i+\mu B_i,
\quad D_{-1}=0,\quad C_m=0,
```

and the paired rows

```math
A_i+aW_{i+1,2}-dW_{i,2}-\frac{ag}{d}fD_i=0,
```

```math
aV_{i,1}+B_{i+1}-dV_{i+1,1}-\frac{ag}{d}fC_{i+1}=0.
```

It solves the m=2 and m=3 systems with W_0 fixed, using outward rational Gaussian elimination with every pivot separated from zero. The final seed-to-bulk row is exactly GERM-67 equation (6). The resulting prefix, local, and bridge maps and their inverses retain a certified infinity-norm bound below 300. Every recomputed six-map enclosure lies inside the printed, pinned GERM-67 enclosure.

This is a fresh coefficient calculation and regression, not a replacement proof of the inherited source-domain reductions. It uses at most six scalar seed unknowns, not another large orbit determinant.

## 3. Choose a fixed section outside the overlap

Set

```math
\mathcal E=(\lambda,h).
```

Since `eta<=lambda`, this section is disjoint from I_eta up to endpoints. Parameterize it by

```math
t=\lambda+z,\qquad0<z<\kappa.
```

The first rotation step wraps to z, which lies in I_eta because `z<kappa<eta`. Subsequent positions, until return to E, are

```math
z,\ z+\kappa,\ z+2\kappa,\ldots.
```

Since `lambda=4kappa+tau`, the first-return time N is exactly

```math
N(z)=\begin{cases}
6,&0<z<\tau,\\
5,&\tau<z<\kappa.
\end{cases}
```

Indeed, for z>tau the point z+4kappa is the first point in E, while for z<tau the first is z+5kappa. Every preceding point lies below lambda and every displayed return point lies below h. These are exact inequalities, not a sampled return-time observation.

In the z coordinate, the induced map is

```math
\mathcal S(z)=
\begin{cases}
z+\kappa-\tau,&0<z<\tau,\\
z-\tau,&\tau<z<\kappa.
\end{cases}
```

Its images are `(kappa-tau,kappa)` and `(0,kappa-tau)`. They partition `(0,kappa)` up to endpoints. Therefore S is an invertible, Lebesgue-measure-preserving rotation by -tau on the kappa-circle. This conclusion follows directly from translation tiling; no unproved complete model of the higher-rank delay algebra is needed.

## 4. The legal multi-visit word

Let s be the number of consecutive overlap positions after the initial wrap. Off the finite threshold seams it is characterized by

```math
z+(s-1)\kappa<\eta<z+s\kappa.
```

The orbit enters I_eta by Q, takes s-1 internal E_+ steps, exits by P, and then takes ordinary A steps until the next E visit. Since E is outside I_eta, the exit must occur before or at that return. Consequently

```math
1\le s\le N-1,
```

and the complete list of possibilities is

```math
(N,s)=(5,1),(5,2),(5,3),(5,4),
(6,1),(6,2),(6,3),(6,4),(6,5).
```

The exact full-return matrix is

```math
\boxed{B_{s,N}=A^{N-s-1}P E_+^{s-1}Q.}                 \tag{1}
```

Products act rightmost first. Chronologically the word is

```text
01-, (s-1 copies of 11+), 10+, (N-s-1 copies of 00+).
```

Its total length is N and its determinant is one by the inherited factor identities. This is not an arbitrary padding of an elliptic excursion with convenient matrices: the A steps are forced by the first-return geometry.

The coefficient library is independent of eta. Only selection of a legal word changes. The verifier checks all nine word cells over exact rational polytopes with `1/6<kappa/h<1/5`, including every source/target overlap bit and the absence of an earlier E hit.

At the new endpoint `eta=lambda`, precisely the generic types `(s,N)=(4,5)` and `(5,6)` survive. Their endpoint faces are checked separately; the argument does not infer endpoint exclusion from continuity of a determinant or Lyapunov exponent. For each fixed eta, threshold equalities remove only finitely many z values before their countable iterates are excluded.

## 5. One rational cone chart for all nine blocks

Take

```math
C=\begin{pmatrix}1&1\\1/2&2\end{pmatrix},\qquad
C^{-1}=\begin{pmatrix}4/3&-2/3\\-1/3&2/3\end{pmatrix}.
```

Define

```math
\widehat B_{s,N}=\sigma_s C^{-1}B_{s,N}C,
\qquad
\sigma_s=\begin{cases}+1,&s=1,2,\\-1,&s=3,4,5.\end{cases}
```

Outward rational interval arithmetic proves that every entry of all nine B-hat matrices is strictly positive. Their actual determinants are one. The inverse bounds in the new executable nevertheless use directly computed positive determinant enclosures, so determinant normalization is not silently assumed by the numerical stage.

The following are deliberately weakened rational lower bounds from the successful audit:

| s | N | Overall sign sigma_s | Forward l1 factor | Backward opposite-sign l1 factor |
| --- | --- | --- | --- | --- |
| 1 | 5 | +1 | >140.43 | >143.20 |
| 2 | 5 | +1 | >21.32 | >22.16 |
| 3 | 5 | -1 | >1.276 | >1.315 |
| 4 | 5 | -1 | >2.70 | >1.81 |
| 1 | 6 | +1 | >479.96 | >489.22 |
| 2 | 6 | +1 | >73.00 | >74.78 |
| 3 | 6 | -1 | >4.04 | >7.24 |
| 4 | 6 | -1 | >8.78 | >9.53 |
| 5 | 6 | -1 | >3.56 | >2.46 |

For a positive matrix `B=[[a0,b0],[c0,d0]]` with positive determinant delta, the forward same-sign l1 factor is at least `min(a0+c0,b0+d0)`. The inverse preserves the opposite-sign cone and its factor is at least `min(d0+c0,b0+a0)/delta`. The certificate evaluates these expressions with outward enclosures.

Thus, on

```math
C_+=\{(u_1,u_2):u_1u_2\ge0\},\qquad
C_-=\{(u_1,u_2):u_1u_2\le0\},
```

all nine positive representatives obey

```math
\boxed{\|\widehat Bv\|_1\ge\tfrac54\|v\|_1\quad(v\in C_+),
\qquad
\|\widehat B^{-1}v\|_1\ge\tfrac54\|v\|_1\quad(v\in C_-).}    \tag{2}
```

The actual transformed recurrence contains `sigma_s B-hat`, not B-hat alone. The sign has NOT been deleted from the equation. Both double cones and the norm are invariant under simultaneous negation, so exactly the same forward/backward estimates and cone invariance hold for the actual signed matrices. This is why one chart can accommodate the negative full-return blocks.

The old elliptic excursion `P E_+ Q` still has trace in `(1.8106874868,1.8106874869)`. For two overlap visits the full return adds two or three compulsory ordinary steps. Equation (1), not an attempted expanding norm for that elliptic excursion, is what is certified.

## 6. L2 exclusion on the induced section

Set

```math
U(z)=C^{-1}W(\lambda+z),\qquad0<z<\kappa.
```

It belongs to L2 because restriction, translation, and the fixed invertible chart are bounded. The actual source equations imply almost everywhere

```math
U(\mathcal S z)=C^{-1}B_{s(z),N(z)}C\,U(z)
=\sigma_{s(z)}\widehat B_{s(z),N(z)}U(z).
```

Work on the common full-measure set obtained by removing the source-equation exceptional sets and their countably many required rotation/affine preimages. No value of x at a classical endpoint is used.

For real U, split its domain into `D_+={U_1U_2>=0}` and `D_-={U_1U_2<0}`. Forward double-cone invariance and (2) imply

```math
(5/4)^{2n}\int_{D_+}\|U(z)\|_1^2\,dz
\le\int_0^\kappa\|U(z)\|_1^2\,dz.
```

The inequality uses measure preservation of S; the right side is finite and independent of n. Letting n increase gives U=0 almost everywhere on D_+. Backward invariance and the inverse estimate give the same conclusion on D_-. Apply the real argument to real and imaginary parts for a complex-valued source; all matrices and C are real.

Therefore W vanishes almost everywhere on E.

Every point of `(0,lambda)` reaches E after at most five successive +kappa steps, before any additional wrap. The corresponding original six-map returns are invertible, so W vanishes on the full h-circle. No new independent coordinates or surjectivity from arbitrary vector fields to physical scalar sources are assumed.

GERM-67's finite local h-step reconstruction propagates this zero to the whole low head, and its licensed middle/tail Schur formulas reconstruct zero on the entire scalar source interval. The number of local h-steps is bounded by eight in the inherited formula domain. Hence

```math
\boxed{x=0\quad\text{for}\quad2h+\kappa<e\le3h-\kappa.}
```

## 7. Experimental endpoint and unchanged scope boundaries

Using `kappa=k-5h`,

```math
L_{68}=\log(16/3)+3h-\kappa=\log(16/3)+8h-k,
```

```math
\exp L_{68}=(16/3)(81/80)^8(15/16)
=\frac{3^{32}}{2^{32}5^7}.
```

Combining the new interval with the previous experimental coverage and the inherited ambient reconstruction gives

```math
\boxed{\ker P_c=\{0\},\qquad
K_c^{\rm ps}=K_c\cap\ker P_c=\{0\},\qquad0<L\le L_{68}.}
```

The Kc conclusion remains in the regular-kernel scope. The common cone constant here is a statement about this induced source recurrence, not a new global uniform-in-L kernel gap. No full-form-domain null-persistence exclusion, selected-packet custody theorem, or RH closure is inferred.

## 8. Exact boundary of the fixed-section proof

For `eta>lambda`, E itself intersects I_eta. Write `delta_eta=eta-lambda`. On the concrete small strip

```math
0<z<\delta_\eta<\tau,
```

the section point `lambda+z` is already inside the overlap. Its first wrap is therefore `11-`, not `01-`.

The exact inequality `kappa>2tau` is certified by prime-power comparison. It implies that this trajectory takes four further internal `11+` steps and then one `10+` exit to E. The changed full-return block is

```math
\boxed{B_{\rm changed}=P E_+^4T_{11}^-.}                  \tag{3}
```

The verifier checks this entire source-domain word directly. In the present rational chart its certified enclosure surrounds

```math
C^{-1}B_{\rm changed}C\approx
\begin{pmatrix}
-0.700160669&0.114185348\\
-1.899201386&-2.041386126
\end{pmatrix}.
```

The second column has opposite signs. Neither overall sign makes this map preserve the same-sign double cone. Thus the existing signed-quadrant certificate cannot be appended unchanged to the newly admitted word. This is a precise failure of this chart/section proof, not an assertion of a nonzero kernel, not a failure of the three-layer elimination, and not a no-go for a different section or a scheduler-dependent cone field.

The remaining part of the already-derived three-layer formula range is `(3h-kappa,3h]`. The full unresolved four-delay range is

```math
\boxed{3h-\kappa<e\le j,
\qquad L_{68}<L\le\log6.}
```

## 9. Execution receipt and audit limits

Run with assertions enabled:

```text
python tools/sz_multivisit_section_audit.py
```

The new verifier completed successfully with exit code zero. It recomputes the two-/three-layer physical maps by small outward rational solves, checks every pivot and local inverse, checks containment in the pinned six-map regression boxes, certifies all nine signed-cone matrices and both norm bounds, proves the first-return domain/image geometry by exact rational inequalities, and checks the new endpoint and changed-word scope guard.

Executable SHA-256:

```text
16517b40a62f46ec32e439a42fe70e6a52cf5d665138f0c93be0ed25a6c31bb7
```

Output SHA-256:

```text
1b51b84bd352e993ab2c416e1b02106819c045cb7b7845ba2501a19b4167824a
```

Direct dependency pins are checked by the executable: the GERM-65 interval helper and the GERM-67 output fixture. The fixture is a regression target, not the numerical input to the new block bounds; those are freshly calculated from the physical logarithm and square-root enclosures.

A full replay of the old GERM-67 symbolic suite was attempted with a 40-second limit and did not complete. It is not reported as a successful replay. The completed new audit is the explicitly narrower rational recalculation and return certificate described above. The old large determinant inventory was not rerun. This certificate accompanies the written source-domain and L2 proof; it is not Lean certification or canonical ratification.

## 10. Next individual target

```text
SZ-KERNEL-EDGE-GERM-69 / OVERLAPPING-SECTION RETURN CONTROL
```

Start from the existing three-layer formulas and (3). Reconcile source and target overlap within the section, or choose a section/cone field that absorbs the changed word while retaining the legal temporal order. Preserve the nine-block result where applicable. Do not rebuild the local layer system, restart flat orbit determinants, or reopen the stopped screw shortcut.

```text
GERM-68: COMPLETE AS A SCOPED EXPERIMENTAL PASS
MULTI-VISIT EXCLUSION: CLOSED THROUGH e=3h-kappa
NINE FULL-RETURN WORDS: ONE SIGNED RATIONAL CONE CHART
THREE-LAYER LOCAL FORMULAS: STILL AVAILABLE THROUGH e=3h
FIXED-SECTION PROOF ABOVE eta=lambda: NOT EXTENDED
GERM-69: NOT EXECUTED
CANONICAL THEOREM CURSOR: SZ-CROSS-COLLAR-3, UNCHANGED
RATIFICATION / PUBLIC PROMOTION: NONE
```

This updates only the pending GERM-68 status. Historical notes and their standing are unchanged.
