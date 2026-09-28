# SZ edge recurrence 67 — three-layer transfer and induced isolated-overlap exclusion

**Date:** 2026-09-27 (America/Los_Angeles)  
**Branch:** sz-cross-collar  
**Standing:** UNRATIFIED RESIDUE / ONE NF PASS / SCOPED POSITIVE RESULT  
**Canonical parent:** SZ-CROSS-COLLAR-3, unchanged  
**Immediate input:** GERM-66, retaining the pre-65 refold  
**Public promotion:** forbidden

## 0. Result and precise scope

The three-layer feedback admits an exact, norm-controlled two-coordinate reduction. However, two new individual return matrices are elliptic, and the six-generator positive-cone proof from GERM-66 does not extend unchanged.

Inducing the rotation past an isolated overlap visit restores the cone argument and proves

```math
\boxed{2h<e\le2h+\kappa\ \Longrightarrow\ x=0
\text{ in both scalar parity kernels}.}
```

Together with the inherited GERM-63/65/66 coverage and GERM-60 reconstruction, the experimental ambient endpoint becomes

```math
\boxed{0<L\le\log\!\left(\frac{26214400}{4782969}\right)
=1.70124739471357\ldots.}
```

Two scopes must remain separate:

| Output | Scope |
| --- | --- |
| Exact three-layer local and return formulas | `2h<e<=3h` |
| New kernel-exclusion theorem | `2h<e<=2h+kappa` |

There is no exclusion claim for the rest of `(2h+kappa,3h]`, let alone the full remaining four-delay interval. This is a scoped experimental result, not canonical ratification or an RH proof.

Entry pin: `monocap-tech/weil-lab@a5c44833c5555323ee5f383479181706affbeaf6`. The entry branch was checked before work. Governance is `notes/SZ_CROSS_COLLAR_RATIFICATION_20260926.md`; inherited source reduction is in `_recurrence60.md`, `_recurrence61.md`, and the fully displayed system in `_recurrence65.md`/`_recurrence66.md`. The pre-65 refold remains the source-integration record.

The mounted GERM-66 note matches its repository blob `03639b1a3d01cca28ac8d92752cf7cb379601150`. The new verifier checks the byte hashes of its GERM-65 and GERM-66 helper dependencies. It reuses interval primitives and exact polytope operations; it does not rerun the old large determinant inventory.

New terms are in [GERM-67 terminology](../docs/TERMINOLOGY_GERM67.md). Companion files are [the executable verifier](../tools/sz_three_layer_induced_audit.py) and [its successful output](_recurrence67_audit.json).

## 1. Parameter domain and original source equations

Write

```math
e=2h+\eta,\quad0<\eta\le h,\quad
h=\log(81/80),\quad k=\log(16/15),\quad
\kappa=k-5h,\quad\lambda=h-\kappa,
```

```math
p=\log(10/9),\quad j=p+h,\quad q=\log(4/3),
\quad r=q+j,\quad s=q-k,\quad m_0=p+k,
```

```math
u=k+e,\quad v=m_0+e,\quad w=2q+e.
```

The length m_0 is written differently from the integer chain length m below. Exact prime-power comparisons certify

```math
5\kappa<h<6\kappa,\qquad k+3h<p,\qquad
3h<j-k,\qquad4h<k.
```

In particular, throughout the formula domain, `u<p`, `e<k-h`, `e<j-k`, and `e<k`. These inequalities are the source-domain guards, not numerical assumptions.

Retain

```math
\mu=\frac{\log3}{\sqrt3\log2},\quad
\beta=\sqrt{2/3}\frac{\log3}{\log2},\quad
 d=\frac{\log5}{\sqrt5\log2},\quad
b=\beta\mu,\quad a=b^2,\quad g=1-a,\quad\Delta=1-\mu^2.
```

The physical coefficient boxes have `0<mu<1`, `d>0`, `a>1`, `g<0`, and `Delta>0`. For each epsilon in `{+1,-1}`, the actual source is an L2 function on `(0,w)` satisfying almost everywhere

```math
\begin{array}{ll}
x(t)+\beta x(r+t)+d[x(s+t)-\varepsilon x(u-t)]=0,&0<t<u,\\
x(t)+\beta x(r+t)=0,&u<t<v,\\
x(t)=0,&v<t<q,\\
x(t)+\mu[x(t-q)-\varepsilon x(w-t)]=0,&q<t<w.
\end{array}
```

The GERM-65/66 tail and middle Schur eliminations remain licensed by the displayed guards. They reconstruct all values outside `(0,u)` from the low head: `x=0` on `(u,p)`, while

```math
x(p+z)=\begin{cases}
-b\varepsilon x(u-z),&0<z<k,\\
-\dfrac b\Delta[\mu x(z-k)+\varepsilon x(u-z)],&k<z<u.
\end{cases}
```

For `T(y)=x(q+y)`, the tail reconstruction is

```math
T(y)=\begin{cases}
-\dfrac\mu\Delta[x(y)+\varepsilon\mu x(e-y)],&0<y<e,\\
-\mu[x(y)-\varepsilon x(q+e-y)],&e<y<q,\\
\dfrac\mu\Delta[\mu x(z)+\varepsilon x(e-z)],&y=q+z,\ 0<z<e.
\end{cases}
```

Retain the actual observation

```math
W(t)=\binom{x(t)}{\varepsilon x(u-t)},\quad
J=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
W(u-t)=\varepsilon J W(t).
```

It is bounded on L2 and is not a classical boundary jet.

## 2. A reusable finite-layer bridge identity

The changed bridge row from GERM-66 takes the uniform form

```math
g x(k+z)=\frac d\Delta[\mu x(z)+\varepsilon x(e-z)]
-\mathbf1_{z<e-h}\frac a\Delta
[\mu x(z+h)+\varepsilon x(e-h-z)],\qquad0<z<e.       \tag{1}
```

The indicator denotes a source-domain split, not a distributional multiplication at its endpoint.

For a fundamental seed t in `(0,h)`, put

```math
m=\begin{cases}3,&0<t<\eta,\\2,&\eta<t<h,\end{cases}
\qquad z_i=t+ih\quad(0\le i<m).
```

Define the physical scalar values and combinations

```math
A_i=x(z_i),\quad B_i=\varepsilon x(e-z_i),\quad
C_i=\mu A_i+B_i,\quad D_i=A_i+\mu B_i,
```

and set `D_-1=0`, `C_m=0`. Let

```math
f=\frac d{g\Delta},\qquad\alpha=\frac ad,
\qquad W_i=W(z_i),\quad V_i=W(k+z_i).
```

Equation (1) and its reflected versions give exactly

```math
\boxed{W_i=\binom{A_i}{f(D_i-\alpha D_{i-1})},
\qquad V_i=\binom{f(C_i-\alpha C_{i+1})}{B_i}.}       \tag{2}
```

Thus the third layer is retained, not removed by setting its feedback to zero.

For every finite chain in (2), first replace the second input coordinate by

```math
fD_i=\sum_{j=0}^i\alpha^{i-j}W_{j,2},
```

apply the old two-by-two coefficient matrix

```math
K=\begin{pmatrix}-d/(g\mu)&1/\mu\\-1/\mu&g\Delta/(d\mu)\end{pmatrix},
```

to `(A_i,fD_i)`, and finally subtract alpha times the next first output coordinate. These are a lower triangular input shear, `diag(K,...,K)`, and an upper triangular output shear. Each shear has determinant one, as does K. In particular, the six-coordinate three-layer bridge has determinant one.

This algebraic shear identity is not yet a statement that six independent coordinates must be retained. The paired source rows supply additional constraints.

## 3. Paired source rows and the two-coordinate solve

For `0<=i<m-1`, the low first-cell row at z_i is

```math
R_i:=A_i+aW_{i+1,2}-dW_{i,2}
-\frac{ag}{d}fD_i=0.                                      \tag{3}
```

Its source provenance is the unsimplified row

```math
(\Delta-a)A_i+a\Delta W_{i+1,2}
-d\Delta W_{i,2}-a\mu B_i=0.
```

Substituting `D_i=A_i+mu B_i` and dividing by Delta gives (3).

The low source row at the reflected partner `e-z_(i+1)` is also in `(0,e)`. Reflection identifies its state pair with `epsilon J V_(i+1)` and `epsilon J V_i`. Its exact transformed equation is

```math
S_i:=aV_{i,1}+B_{i+1}-dV_{i+1,1}
-\frac{ag}{d}fC_{i+1}=0.                                  \tag{4}
```

Fix `W_0=(X,Y)^T`. Equation (2) then fixes

```math
A_0=X,\qquad B_0=\frac{Y/f-X}{\mu}.
```

For m=3, solve `(R_0,S_0,R_1,S_1)=0` for `(A_1,B_1,A_2,B_2)`. Denote that explicitly specified four-by-four coefficient matrix by Pi_3. Put

```math
\chi=2a+d^2-1,\quad
\Xi=\chi^2+g^2\mu^2-a^2d^2,\quad
\Psi=3\chi^2+g^2\mu^2-2a^2d^2.
```

The exact symbolic pivot is

```math
\boxed{\det\Pi_3=\frac{a^2d^2\Xi}{g^4\Delta^2}.}             \tag{5}
```

The outward rational audit proves Xi positive and

```math
19000<\det\Pi_3<20000.
```

Hence the three-layer source values are uniquely reconstructed from two retained coordinates. This is a source-level elimination, not a dimension guess.

The m=2 instance of (2)-(4) reproduces the GERM-66 N0, F, and K0 formulas exactly. The verifier checks these matrix identities symbolically; it does not merely compare dimensions or rounded determinants.

## 4. Final seed-to-bulk step and local maps

The last low source row, together with its upper first-cell companion, supplies `W_m=(X_m,Y_m)^T`:

```math
Y_m=-\frac{A_{m-1}}a+\frac daW_{m-1,2}
+\frac gd fD_{m-1},
```

```math
X_m=\frac gdY_m+\frac{ag}{d^2}fD_{m-1}.                    \tag{6}
```

For the companion, the reflected source coordinate is `u-z_m in (k-h,k)`. The fixed inequality `4h<k` licenses the required middle-band substitution. Equation (6) satisfies both original reduced rows exactly.

Define, by this explicit linear solve,

```math
W_i=L_{m,i}W_0,\quad L_{m,0}=I,\quad F_m=L_{m,m},
```

```math
N_{m,i}=L_{m,i+1}L_{m,i}^{-1},\qquad
V_i=K_{m,i}W_i,\qquad H_{m,i}=J N_{m,i}^{-1}J.
```

All matrices are fixed rational expressions in `a,d,mu`; no orbit length or sampled coefficient is part of their definition. The audit gives, approximately for orientation,

```math
(\det L_{3,0},\det L_{3,1},\det L_{3,2},\det L_{3,3})
\approx(1,\ 0.137569294,\ -0.636997325,\ -1.228578278).
```

Their interval enclosures exclude zero. The previous two-layer prefix determinants are also checked. Every prefix, local step, bridge, and its inverse has infinity norm below 300; the bulk map has the same bound. Upper maps inherit the bound by coordinate permutation.

Exact determinant identities are

```math
\det F_2=\frac{2g}{d^2},\qquad
\det F_3=\frac{g\Psi}{d^2\Xi},\qquad
\det K_{m,0}=\det L_{m,m-1}.                               \tag{7}
```

The bridge reflection identity is

```math
K_{m,m-1-i}=J K_{m,i}^{-1}J.
```

The bulk step remains the GERM-65 matrix

```math
M=\begin{pmatrix}(2a-1)/(da)&g/a\\-g/a&d/a\end{pmatrix},
\qquad\det M=1.
```

Its exact Cayley-Hamilton/Chebyshev compression remains available. No layer feedback map is replaced by a pure bulk power.

## 5. Complete local domains and six directed returns

The lower h-step intervals are

| Source interval | h-step |
| --- | --- |
| `(0,eta)` | N_(3,0) |
| `(eta,h)` | N_(2,0) |
| `(h,h+eta)` | N_(3,1) |
| `(h+eta,2h)` | N_(2,1) |
| `(2h,e)` | N_(3,2) |
| `(e,k-h)` | M |

The upper intervals, in increasing order, are

```text
(k-h,k-h+eta) : H_(3,2)
(k-h+eta,k)   : H_(2,1)
(k,k+eta)     : H_(3,1)
(k+eta,k+h)   : H_(2,0)
(k+h,u-h)    : H_(3,0).
```

These follow by reflecting the proved lower rules at `u-h-t` and cover the remaining h-steps up to `(0,u-h)`. At eta=h, the two-layer intervals disappear; the other formulas still apply directly.

Use the same h-circle rotation

```math
R(t)=t+\kappa\pmod h.
```

Let i indicate `t<eta`, j indicate `R(t)<eta`, and put `m_i=2+i`, `m_j=2+j`. Let omega=0 for a nonwrap and omega=1 for a wrap. Comparing the bridge from t with the h-ladder from R(t) to t+k gives

```math
\boxed{T_{ij}^{(\omega)}
=F_{m_j}^{-1}M^{-(4+\omega-m_j)}
J N_{m_i,m_i-1}J K_{m_i,0}.}                              \tag{8}
```

All products act rightmost first. The only types are `00+`, `10+`, `11+`, `00-`, `01-`, and `11-`. The chronological ladder words are

```text
00+ : N20 N21 M M H21
10+ : N20 N21 M M H32
11+ : N30 N31 N32 M H32
00- : N20 N21 M M M H21
01- : N30 N31 N32 M M H21
11- : N30 N31 N32 M M H32.
```

Here `Nmi` means N_(m,i), and similarly for H. The words are certified by exact rational polytope inequalities with `1/6<kappa/h<1/5`. The eta=h face is checked separately. No long-orbit enumeration or approximate topology choice is used.

The necessary source-section equation is `W(R(t))=T(t)W(t)`. Writing

```math
\rho=\frac{\Psi}{2\Xi}>0,
```

the six determinant values are

```math
1,\quad\rho,\quad1,\quad1,\quad\rho^{-1},\quad1.
```

This follows from (7): each return determinant is `det F_(m_i)/det F_(m_j)`. The two ordinary maps `T_00^+` and `T_00^-` are exactly the GERM-66 `11+` and `11-` maps.

## 6. Why the unmodified six-generator cone proof fails

The new matrices `T_11^+` and `T_11^-` have determinant one and strictly negative upper-right entries. The rational audit gives

```math
1.5730690723<\operatorname{tr}T_{11}^+<1.5730690724,
```

```math
1.3661018763<\operatorname{tr}T_{11}^-<1.3661018764.
```

Both discriminants `trace^2-4` are strictly negative. Thus they are elliptic real matrices, not hyperbolic matrices missed by numerical rounding.

In particular, they do not preserve the old positive quadrant. More generally, an elliptic real determinant-one matrix cannot have a nonzero invariant cone on which every iterate expands by one fixed factor greater than one: its distinct unit-modulus eigenvalues make all powers bounded in some norm, hence in every fixed finite-dimensional norm.

This rejects a generator-by-generator expansion proof for the complete three-layer library. It does **not** establish a nonzero kernel, rule out an admissible-word cone field, or decide the full three-layer chamber. The scheduler must now be used, not discarded.

## 7. Induce past an isolated overlap visit

Restrict the exclusion argument to

```math
0<\eta\le\kappa.
```

Let `I_eta=(0,eta)` be the overlap interval and `D_eta=(eta,h)` its complement up to endpoints. Since eta<=kappa and h>5kappa, a point of I_eta leaves it after one forward rotation step, and its predecessor is also outside. Thus overlap visits are isolated.

The first-return map S_eta to D_eta has exactly the following pieces:

| Source interval in D_eta | S_eta(t) | Return time | Matrix |
| --- | --- | --- | --- |
| `(eta,h-kappa)` | `t+kappa` | 1 | T_00^+ |
| `(h-kappa,h-kappa+eta)` | `t+2kappa-h` | 2 | T_10^+ T_01^- |
| `(h-kappa+eta,h)` | `t+kappa-h` | 1 | T_00^- |

Their respective images are

```math
(\eta+\kappa,h),\qquad(\kappa,\kappa+\eta),\qquad(\eta,\kappa).
```

They partition D_eta up to endpoints. Therefore S_eta is an invertible, Lebesgue-measure-preserving interval map, proved here directly by the translation tiling. At eta=kappa the third piece and its image are empty; the other two still partition D_eta. No continuity argument in e is needed.

The isolated excursion matrix is

```math
B_{\rm exc}=T_{10}^+T_{01}^-,\qquad\det B_{\rm exc}=1.
```

Although one factor has a negative entry, their product is strictly positive. Its certified narrow enclosure surrounds

```math
B_{\rm exc}\approx\begin{pmatrix}
3.151571057&0.165314829\\
5.663203704&0.614363921
\end{pmatrix}.
```

The reduction uses the actual temporal order of legal returns. It does not add equations or permit arbitrary reorderings of the maps.

## 8. Weighted cone certificate for the induced blocks

Use

```math
\|(X,Y)\|_*=|X|+\frac15|Y|,
\qquad C_+=\{XY\ge0\},\quad C_-=\{XY\le0\}.
```

For a positive determinant-one matrix `B=[[A,B12],[C,D]]`, the forward C+ factor is bounded below by

```math
\min(A+C/5,\ 5B_{12}+D),
```

and the backward C- factor for its inverse is bounded below by

```math
\min(D+C/5,\ 5B_{12}+A).
```

The rational audit supplies the following deliberately weakened bounds:

| Induced matrix | Forward factor | Backward factor |
| --- | --- | --- |
| T_00^+ | >3.06 | >1.47 |
| T_00^- | >3.01 | >1.68 |
| B_exc | >1.44 | >1.74 |

Every entry of all three matrices has a positive lower bound. Thus

```math
\boxed{\|Bz\|_*\ge\frac75\|z\|_*\quad(z\in C_+),\qquad
\|B^{-1}z\|_*\ge\frac75\|z\|_*\quad(z\in C_-).}             \tag{9}
```

The corresponding forward and backward cones are preserved. This is a certificate for the induced three-block library; it is not an assertion about every individual three-layer return matrix.

All coefficients and inequalities are enclosed using rational logarithmic series, integer-square bounds, and outward rational arithmetic. Rounded matrices in this note are explanatory, not load-bearing.

## 9. L2 exclusion and faithful reconstruction

Restrict the actual W to D_eta. It belongs to L2 and satisfies the induced return equation almost everywhere. Remove the source-equation exceptional sets and their countably many relevant affine/rotation preimages; no classical traces are introduced.

For a real state, let E+ be the subset where its coordinate product is nonnegative and E- where it is negative. Forward invariance and (9) give

```math
(7/5)^{2n}\int_{E_+}\|W(t)\|_*^2\,dt
\le\int_{D_\eta}\|W(t)\|_*^2\,dt.
```

Use measure preservation of S_eta. Backward invariance and the inverse bound give the identical estimate on E- with backward iterates. Letting n tend to infinity shows W=0 almost everywhere on D_eta. For a complex state, apply the real argument to its real and imaginary parts; all matrices are real.

For t in I_eta, `R(t)=t+kappa` lies in D_eta and

```math
W(R(t))=T_{10}^+W(t).
```

The determinant rho is nonzero, so W also vanishes on I_eta. Hence it is zero on the full h-circle almost everywhere.

The local h-step library propagates zero to every low-head point. At most eight h-steps are needed for `e<=3h`; all used local maps and inverses are bounded. The middle and tail formulas in Section 1 then reconstruct zero on the whole source interval `(0,w)`.

This gives an injective, norm-controlled observation of actual source solutions into the section. Surjectivity from arbitrary section fields to scalar sources is not asserted or required.

Consequently

```math
\boxed{2h<e\le2h+\kappa\ \Longrightarrow\ x=0
\text{ in both scalar parity kernels}.}
```

The argument does not assume pointwise boundedness along a dense orbit or infer L2 exclusion from a numerical Lyapunov exponent.

## 10. Experimental endpoint and inherited scope

Since `kappa=k-5h`,

```math
L_*=\log(16/3)+2h+\kappa=\log(16/3)+k-3h,
```

```math
\exp L_*=(16/3)(16/15)(80/81)^3=\frac{26214400}{4782969}.
```

Combine the new interval with the inherited GERM-63/65/66 coverage and GERM-60 equivalence:

```math
\boxed{\ker P_c=\{0\},\qquad
K_c^{\rm ps}=K_c\cap\ker P_c=\{0\},\qquad0<L\le L_*.}
```

The Kc conclusion retains its regular-kernel scope. No full-form-domain null-persistence exclusion, selected-packet ownership statement, global uniform gap, or RH closure is added.

## 11. Execution receipt

The verifier ran successfully with exit code zero. It checks the four-/six-coordinate shear identities, both parity conventions, all paired and terminal source rows, exact agreement with the GERM-66 two-layer interface, the three-layer pivot, prefix/bridge determinant and reflection identities, bounded local reconstruction, all six exact word domains, and the three induced weighted cone estimates. It explicitly checks the eta=kappa exclusion endpoint and the separate eta=h formula face.

Run with assertions enabled:

```text
python tools/sz_three_layer_induced_audit.py
```

Executed verifier SHA-256:

```text
7aa961486fa36e953c5237632d6ce31ce09e49f455ea30c610cd77ae0e67d746
```

Recorded output SHA-256:

```text
db2dcd27d30ca3199c444e449d7a2b93b674a7fe2b2d4cc764b38a9a863e0b09
```

The two dependency byte hashes are checked before use and included in the output. The old large determinant programs and the full inherited source-orbit regression suites were not rerun. The exact two-layer local regression performed here is narrower and explicitly identified.

This is a symbolic/rational certificate accompanying the written proof, not Lean certification or canonical ratification.

## 12. Exact stopping boundary and next individual target

At eta>kappa, consecutive overlap visits become possible. For example, when `kappa<eta<2kappa`, an entry into `(0,eta-kappa)` is followed by one internal `11+` step before exit. The new induced block is

```math
B_{\rm two}=T_{10}^+T_{11}^+T_{01}^-.
```

It has determinant one, a strictly negative upper-right entry, and certified trace

```math
1.8106874868<\operatorname{tr}B_{\rm two}<1.8106874869.
```

Thus the first newly admitted two-visit block is itself elliptic. It cannot be silently appended to the positive induced-block library. This is a specific obstruction to the present proof mechanism, not evidence of a nonzero kernel. Further induction over larger legal words, a scheduler-dependent cone field, or a different spectral argument remains possible.

The remaining four-delay interval is

```math
\boxed{2h+\kappa<e\le j,\qquad
\log(26214400/4782969)<L\le\log6.}
```

The exact local three-layer formulas are already available through e=3h. The next pass should use those formulas and the newly active two-visit word, rather than rederive the layer system or restart flat determinant enumeration.

Next individual target:

```text
SZ-KERNEL-EDGE-GERM-68 / MULTI-VISIT INDUCED RETURN CONTROL
```

```text
GERM-67: COMPLETE AS A SCOPED EXPERIMENTAL PASS
THREE-LAYER LOCAL FORMULAS: DERIVED THROUGH e=3h
ISOLATED-OVERLAP KERNEL EXCLUSION: CLOSED THROUGH e=2h+kappa
UNMODIFIED SIX-GENERATOR CONE PROOF: REJECTED
TWO-VISIT INDUCED BLOCK: EXACT ELLIPTIC OBSTRUCTION TO THE SAME CONE PROOF
GERM-68: NOT EXECUTED
CANONICAL THEOREM CURSOR: SZ-CROSS-COLLAR-3, UNCHANGED
RATIFICATION / PUBLIC PROMOTION: NONE
```

This updates only the pending GERM-67 status. Historical notes and their standing remain unchanged.
