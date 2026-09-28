# SZ edge recurrence 66 — post-h bridge-feedback transfer

**Date:** 2026-09-27 (America/Los_Angeles)  
**Branch:** sz-cross-collar  
**Status:** UNRATIFIED RESIDUE / ONE NF PASS / SCOPED POSITIVE RESULT  
**Canonical parent:** SZ-CROSS-COLLAR-3, unchanged  
**Immediate input:** GERM-65 and the pre-65 refold  
**Public promotion:** forbidden

## 0. Result and source custody

The new bridge feedback can be eliminated using its paired source rows. A larger independent state is not required in the first post-h overlap chamber. The resulting six-map return library proves

```math
\boxed{h<e\le 2h\ \Longrightarrow\ x=0\text{ in both scalar parity kernels}.}
```

With the inherited GERM-63/65 coverage and GERM-60 reconstruction, the experimental ambient endpoint becomes

```math
\boxed{0<L\le\log(2187/400)=1.6988214735687858528\ldots.}
```

No positive-width interval above e=2h is claimed. This is a scoped, unratified source-equation result, not a canonical SZ advancement or a proof of RH.

Entry repository pin: `monocap-tech/weil-lab@23005f480cdff4eb04ee460f4cd6cf60d9ebcf0e`.

Read the governance record `notes/SZ_CROSS_COLLAR_RATIFICATION_20260926.md`, the original scalar reduction in `_recurrence60.md` and `_recurrence61.md`, the pre-65 refold, and `_recurrence65.md` at that pin. This pass uses the exact source equations and reconstruction from GERM-65, its Section 12 changed bridge row, and its signed-quadrant L2 argument. It does not restart the finite determinant traversal or the stopped screw-family route.

New terms are registered in [GERM-66 terminology](../docs/TERMINOLOGY_GERM66.md). The executable certificate is [sz_post_h_bridge_feedback_audit.py](../tools/sz_post_h_bridge_feedback_audit.py), with [recorded output](_recurrence66_audit.json). Its interval primitives come from the pinned GERM-65 verifier, whose SHA-256 is checked before use. Neither the old large determinant programs nor the old source-orbit regressions are rerun by this pass.

## 1. Parameter range and inherited source equations

Write

```math
e=h+\eta,\quad 0<\eta\le h,\quad
h=\log(81/80),\quad k=\log(16/15),\quad
p=\log(10/9),\quad j=p+h,
```

```math
q=\log(4/3),\quad r=q+j,\quad s=q-k,\quad m=q-j=p+k,
\quad u=k+e,\quad v=m+e,\quad w=2q+e,
```

```math
\kappa=k-5h,\qquad\lambda=h-\kappa.
```

Here lambda means the return length lambda_ret. Exact prime-power comparisons certify

```math
5\kappa<h<6\kappa,\qquad k+2h<p,\qquad 2h<j-k,\qquad 3h<k.
```

Thus throughout this pass, `u<p`, `e<j-k`, `e<k-h`, and `e<k`. These inequalities license the tail/middle eliminations below, including at e=2h.

Use the coefficient conventions

```math
\mu=\frac{\log3}{\sqrt3\log2},\quad
\beta=\sqrt{2/3}\frac{\log3}{\log2},\quad
 d=\frac{\log5}{\sqrt5\log2},\quad
b=\beta\mu,\quad a=b^2,\quad g=1-a,\quad\Delta=1-\mu^2.
```

The rational audit verifies `0<mu<1`, `d>0`, `a>1`, `g<0`, and `Delta>0`. For either external parity epsilon, the source is `x in L2(0,w)` satisfying almost everywhere

```math
\begin{array}{ll}
x(t)+\beta x(r+t)+d[x(s+t)-\varepsilon x(u-t)]=0,&0<t<u,\\
x(t)+\beta x(r+t)=0,&u<t<v,\\
x(t)=0,&v<t<q,\\
x(t)+\mu[x(t-q)-\varepsilon x(w-t)]=0,&q<t<w.
\end{array}
```

## 2. Reuse the exact low-head reconstruction

The tail Schur determinant is Delta. With `T(y)=x(q+y)`, its exact solution remains

```math
T(y)=\begin{cases}
-\dfrac\mu\Delta[x(y)+\varepsilon\mu x(e-y)],&0<y<e,\\
-\mu[x(y)-\varepsilon x(q+e-y)],&e<y<q,\\
\dfrac\mu\Delta[\mu x(z)+\varepsilon x(e-z)],&y=q+z,\ 0<z<e.
\end{cases}
```

Since u<p and g is nonzero, the paired middle equations imply `x=0` on `(u,p)`. The remaining middle band is

```math
x(p+z)=\begin{cases}
-b\varepsilon x(u-z),&0<z<k,\\
-\dfrac b\Delta[\mu x(z-k)+\varepsilon x(u-z)],&k<z<u.
\end{cases}
```

Together with the dead strip, these formulas reconstruct the entire source from `(0,u)`. Nothing here requires a classical boundary trace. All substitutions are licensed by the fixed inequalities in Section 1.

Retain the actual observation

```math
W(t)=\begin{pmatrix}x(t)\\\varepsilon x(u-t)\end{pmatrix},
\qquad J=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad W(u-t)=\varepsilon J W(t).
```

It is bounded on L2. We do not identify it with an unproved P/J-state model.

## 3. Exact bridge feedback on the overlapping seed pair

For `0<z<eta`, the point `j+k+z=m+h+z` lies in `(m,v)`, not the dead strip. The source row at k+z becomes

```math
g x(k+z)=\frac d\Delta[\mu x(z)+\varepsilon x(e-z)]
-\frac a\Delta[\mu x(h+z)+\varepsilon x(\eta-z)].                 \tag{1}
```

For `eta<z<e`, the second bracket is absent. This remains valid at eta=h: the endpoint crossings have zero seed measure.

Set `f=d/(g Delta)` and `alpha=a/d`. For `0<t<eta`, use the four physical seed values

```math
A=x(t),\quad B=\varepsilon x(e-t),\quad
C=x(h+t),\quad D=\varepsilon x(\eta-t).
```

Let `W0=W(t)`, `W1=W(t+h)`, `V0=W(k+t)`, and `V1=W(k+h+t)`. Equation (1) and its reflected/unforced companions give exactly

```math
W_0=\binom{A}{f(A+\mu B)},\qquad
W_1=\binom{C}{f(C+\mu D)-\alpha W_{0,2}},
```

```math
V_1=\binom{f(\mu C+D)}D,\qquad
V_0=\binom{f(\mu A+B)-\alpha V_{1,1}}B.                         \tag{2}
```

In particular, applying the old K separately to both layers would discard nonzero feedback.

Let `P=diag(1,0)` and `Q=diag(0,1)`, local coordinate projectors, and retain the old coefficient matrix

```math
K=\begin{pmatrix}-d/(g\mu)&1/\mu\\-1/\mu&g\Delta/(d\mu)\end{pmatrix}.
```

The exact four-coordinate bridge is

```math
\binom{V_0}{V_1}=
\begin{pmatrix}K-\alpha^2PKQ&-\alpha PK\\\alpha KQ&K\end{pmatrix}
\binom{W_0}{W_1}.                                             \tag{3}
```

It factors as an input shear, `diag(K,K)`, and an output shear, and has determinant one. This four-coordinate representation is not yet the minimal retained state: two source rows have not been used.

## 4. The paired rows close the two-coordinate interface

Put

```math
\nu=d+ag/d,\qquad \ell=(-d-a/d,1)K,
```

```math
C_* =\begin{pmatrix}0&a\\\ell_1&\ell_2\end{pmatrix},\qquad
D_* =\begin{pmatrix}1&-\nu\\aK_{11}&aK_{12}+\alpha\ell_2\end{pmatrix}.
```

The reduced first-cell row at t gives

```math
W_{0,1}+aW_{1,2}-\nu W_{0,2}=0.                              \tag{4}
```

To see its source provenance, the unsimplified row is

```math
(\Delta-a)A+a\Delta W_{1,2}-d\Delta W_{0,2}-a\mu B=0.
```

Insert `B=(W0,2/f-A)/mu` from (2), and divide by Delta.

The same row at `eta-t` is also licensed because `0<eta-t<h`. Reflection identifies its input/output with `epsilon J V1` and `epsilon J V0`. Hence

```math
aV_{0,1}+V_{1,2}-\nu V_{1,1}=0.                              \tag{5}
```

Substitute (3) into (4)-(5). Since `nu+a alpha=d+a/d`, the resulting system is

```math
C_*W_1+D_*W_0=0.
```

The pivot is exact:

```math
\boxed{\det C_*=-\frac{a(2a+d^2-1)}{g\mu}>0.}
```

The rational enclosure places it above 10. Therefore

```math
\boxed{W(t+h)=N_0W(t),\qquad N_0=-C_*^{-1}D_*,\quad0<t<\eta.} \tag{6}
```

This is the promised two-port overlap reduction, derived from source rows rather than inferred from a matrix dimension. The physical seed values B and D are reconstructed from W0 and W1 by (2); all denominators are nonzero. The reduction is reversible for this local subsystem. We do not assert surjectivity from arbitrary cocycle fields to solutions of every original equation.

## 5. Second overlap step and corrected bridge maps

Keep the GERM-65 bulk and ordinary lower-gate coefficients

```math
M=\begin{pmatrix}(2a-1)/(da)&g/a\\-g/a&d/a\end{pmatrix},\qquad
N=\begin{pmatrix}-g/(da)&g(1/d^2+1/a)\\-1/a&\nu/a\end{pmatrix}.
```

Let `W2=W(t+2h)` for `0<t<eta`. The source row at h+t and its upper first-cell companion at `u-2h-t` give

```math
aW_{2,2}+W_{1,1}-\nu W_{1,2}-\frac{a^2g}{d^2}W_{0,2}=0,
```

```math
gW_{2,2}+\frac a\Delta(\mu D+W_{1,1})-dW_{2,1}=0.
```

Here `D=(W1,2+alpha W0,2-f W1,1)/(f mu)`; it must not be omitted. Simplifying yields

```math
W_2=NW_1+\binom{ag/d^3}{ag/d^2}W_{0,2}.
```

Define

```math
F=NN_0+\binom{ag/d^3}{ag/d^2}(0,1),\qquad N_1=FN_0^{-1},
```

```math
K_0=K-\alpha PK(N_0+\alpha Q),\qquad K_1=JK_0^{-1}J.
```

Then `F` is the exact two-step overlap gate; `N1` is its second h-step. Equation (3) gives the corrected bridge K0, and reflection gives K1. Symbolic algebra verifies

```math
\det K_0=\det N_0,\qquad
\det F=2g/d^2,\qquad
K(N_0+\alpha Q)N_0^{-1}=JK_0^{-1}J.                            \tag{7}
```

The rational audit proves

```math
-0.012<\det N_0<-0.011,
```

so all these inverses are licensed. For orientation only,

```math
N_0\approx\begin{pmatrix}0.749124&-0.387220\\-0.713077&0.352964\end{pmatrix},
\qquad
N_1\approx\begin{pmatrix}30.981309&31.597078\\31.170923&33.848734\end{pmatrix}.
```

The small determinant is explicitly enclosed; it is not silently treated as well conditioned. Every local gate/bridge used in this pass and its inverse has certified infinity norm below 300. Thus the elimination is norm controlled uniformly in eta within this chamber.

## 6. Complete local h-step and bridge domains

Set `H0=J N0^{-1}J`, `H=J N^{-1}J`, and `H1=J N1^{-1}J`. Reflection of the proven lower rules gives the upper rules. The middle first-cell row paired with its reflection gives M exactly as in GERM-65. The source domains are

| Source t interval | h-step matrix |
| --- | --- |
| `(0,eta)` | N0 |
| `(eta,h)` | N |
| `(h,e)` | N1 |
| `(e,k-h)` | M |
| `(k-h,k-h+eta)` | H1 |
| `(k-h+eta,k)` | H |
| `(k,k+eta)` | H0 |

These intervals cover `(0,u-h)` up to their endpoints. At eta=h, the ordinary N/H intervals are empty; the remaining rules still apply on open seed intervals. They do not require taking a limit of a spectral certificate.

The k-bridge domains are

| Source z interval | k-bridge matrix |
| --- | --- |
| `(0,eta)` | K0 |
| `(eta,h)` | K |
| `(h,e)` | K1 |

Bulk Chebyshev compression remains valid because `det M=1`. It is used only for the actual bulk powers in the words below; no feedback gate is replaced by a power of M.

## 7. Six return types, without orbit enumeration

Use the full h-circle section

```math
R(t)=t+\kappa\pmod h,\qquad 0<t<h.
```

Write `y=R(t)`. Let i indicate `t<eta` and j indicate `y<eta`. The plus sign denotes a nonwrap `+kappa`; minus denotes a wrap `-lambda`. Compare the k-bridge from t with the h-ladder from y to t+k. A nonwrap ladder has five steps, a wrap ladder six. The complete necessary return library is

| Type | Source/target overlap bits | Ladder product from y to t+k | Bridge from t | Return T |
| --- | --- | --- | --- | --- |
| `00+` | neither | `H M^3 N` | K | `N^{-1} M^{-3} H^{-1} K` |
| `10+` | source only | `H1 M^3 N` | K0 | `N^{-1} M^{-3} H1^{-1} K0` |
| `11+` | both | `H1 M^2 F` | K0 | `F^{-1} M^{-2} H1^{-1} K0` |
| `00-` | neither | `H M^4 N` | K | `N^{-1} M^{-4} H^{-1} K` |
| `01-` | target only | `H M^3 F` | K | `F^{-1} M^{-3} H^{-1} K` |
| `11-` | both | `H1 M^3 F` | K0 | `F^{-1} M^{-3} H1^{-1} K0` |

Products act rightmost first. The types `01+` and `10-` are impossible by the ordering of t and y. In every case

```math
\boxed{W(R(t))=T(t)W(t).}
```

This construction preserves the earlier two return matrices on their surviving domains. It adds four maps rather than rebuilding large finite orbit matrices.

The verifier checks every source interval in each word by exact rational polytope inequalities after normalizing h=1 and enclosing `kappa/h` between 1/6 and 1/5. This is a finite certificate of the six local word types, not a sampled orbit enumeration. It separately checks the eta=h face, where only the two `11` types remain.

Using (7), the return determinants are respectively

```math
1,\quad2,\quad1,\quad1,\quad1/2,\quad1.
```

In particular, the new library is not wholly SL2. The inverse-cone estimates below include these determinant factors explicitly.

## 8. Outward rational common-cone certificate

Exact rational atanh-series bounds for logarithms and integer-square bounds for square roots enclose the physical coefficients. All subsequent interval operations round outward. Every entry of all six return matrices has a strictly positive lower bound.

The two old matrices retain their GERM-65 enclosures. The four new matrices are approximately

```math
T_{10}^+\approx\begin{pmatrix}6.655933&1.193650\\4.754426&1.153125\end{pmatrix},
\quad
T_{11}^+\approx\begin{pmatrix}2.870520&0.444952\\3.169851&0.839720\end{pmatrix},
```

```math
T_{01}^-\approx\begin{pmatrix}5.445097&1.694813\\6.137105&2.002030\end{pmatrix},
\quad
T_{11}^-\approx\begin{pmatrix}3.255889&0.431381\\4.153924&0.857499\end{pmatrix}.
```

These rounded displays are not the certificate. The JSON contains outward interval endpoints. The following deliberately weaker rational lower bounds follow from that audit:

| Type | Forward l1 factor, same-sign cone | Backward l1 factor, opposite-sign cone |
| --- | --- | --- |
| `00+` | >5.50 | >8.77 |
| `10+` | >2.34 | >2.95 |
| `11+` | >1.28 | >3.31 |
| `00-` | >6.95 | >12.13 |
| `01-` | >3.69 | >14.27 |
| `11-` | >1.28 | >3.68 |

For a positive matrix `T=[[A,B],[C,D]]`, forward same-sign expansion is bounded below by `min(A+C,B+D)`. Since its audited determinant delta is positive,

```math
T^{-1}=\delta^{-1}\begin{pmatrix}D&-B\\-C&A\end{pmatrix}.
```

Backward opposite-sign expansion is bounded below by `min(D+C,B+A)/delta`. Thus the exact uniform certificate is

```math
\boxed{\|Tz\|_1\ge\tfrac54\|z\|_1\ (z\in C_+),\qquad
\|T^{-1}z\|_1\ge\tfrac54\|z\|_1\ (z\in C_-),}
```

where `C_+={XY>=0}` and `C_-={XY<=0}`. The positive cone is strictly preserved forward away from zero; the opposite-sign cone is preserved backward. This proves the necessary expansion for every legal product in this chamber, not merely individual numerical hyperbolicity.

## 9. L2 exclusion on the full circle

The actual W belongs to L2 on `(0,h)`. R is a measure-preserving rotation. On a common full-measure set, the source equations and all required translated/reflected instances hold. The finitely many threshold points and their countably many iterates do not require pointwise traces.

For a real W, split the circle into `E_+={W1 W2>=0}` and `E_-={W1 W2<0}`. Forward cone invariance on E+ gives

```math
(5/4)^{2n}\int_{E_+}\|W(t)\|_1^2dt
\le\int_0^h\|W(t)\|_1^2dt.
```

Backward cone invariance on E- gives the same inequality with backward iterates. The right side is finite and independent of n. Sending n to infinity gives W=0 almost everywhere on both sets.

Apply the same argument to the real and imaginary parts of a complex W. The matrices are real, so both parts satisfy the same necessary return equation. Therefore

```math
\boxed{W=0\text{ a.e. on }(0,h),\qquad h<e\le2h.}
```

No boundedness along an individual dense orbit, positive numerical Lyapunov exponent, or unsupported spectral-normalization assertion is used.

## 10. Injective reconstruction and experimental endpoint

Every point of `(0,u)` has a generic representative in `(0,h)` and is reached by at most seven h-steps. The local library in Section 6 covers all those steps; each has a bounded inverse and bounded coefficients. Consequently zero on the base circle propagates to zero on the whole low head. Section 2 then reconstructs zero on the middle band, dead strip, and tail.

This proves the stated source-equation theorem. It also supplies a norm-controlled, injective observation of actual source solutions into the two-coordinate section. Surjectivity from arbitrary vector fields is neither claimed nor needed.

Combine this with the GERM-65 interval and the inherited GERM-60 equivalence:

```math
L_{2h}=\log(16/3)+2\log(81/80)=\log(2187/400),
```

```math
\boxed{\ker P_c=\{0\},\qquad K_c^{\rm ps}=K_c\cap\ker P_c=\{0\},
\qquad0<L\le\log(2187/400).}
```

The Kc conclusion retains the regular-kernel scope. No uniform-in-L gap for the full problem, full-form-domain null-persistence exclusion, selected-packet custody theorem, or global RH result is added.

## 11. Execution receipt

The verifier ran successfully with exit code zero. Its checks comprise the four-coordinate shear identity, both parity source-row identities, the two-port pivot, second-step source rows, determinant/reflection identities, all six rational forward/backward cone bounds, local reconstruction norm bounds, and exact six-word domain inequalities including e=2h. It does not re-certify the whole inherited GERM-60 reduction or execute the old large determinants.

Run with assertions enabled:

```text
python tools/sz_post_h_bridge_feedback_audit.py
```

Executed verifier SHA-256:

```text
511b6cf1b6bf59e6133e47b6103dd2ea9960cfa41abe4491d6b7d56c17b6cd97
```

Expected Git blob of the executed verifier:

```text
fa953d55024c9a8d332fab2c08eb7456221070e5
```

Recorded JSON SHA-256:

```text
cb6be8b6e56a75b76fe41802c360432c6c56bd07c2332e163b14659efe371a1a
```

This is a symbolic/rational certificate accompanying a written proof, not Lean certification or canonical ratification.

## 12. Exact stop above 2h

The second seed layer in (2) used the absence of feedback in the bridge at k+h+t. If e>2h, that row changes on

```math
0<t<e-2h.
```

Within the same small-parameter coefficient regime, its exact replacement is

```math
g x(k+h+t)=\frac d\Delta[\mu x(h+t)+\varepsilon x(e-h-t)]
-\frac a\Delta[\mu x(2h+t)+\varepsilon x(e-2h-t)].               \tag{8}
```

For example this row is licensed for `2h<e<min(3h,p-k,j-k)` on the displayed source strip. The final bracket is a third seed layer and was absent from V1 in (2). Therefore the present four-coordinate shear and the ensuing N0/N1/K0 reduction cannot be carried beyond 2h unchanged. Equation (8) is a scope audit, not a solution of the next chamber.

The remaining four-delay interval is

```math
\boxed{2h<e\le j,\qquad\log(2187/400)<L\le\log6.}
```

Its logarithmic width is `j-2h=log(800/729)`. The later coefficient changes, including e=p, remain unresolved.

Next individual target:

```text
SZ-KERNEL-EDGE-GERM-67 / POST-2h THREE-LAYER TRANSFER
```

Start from (8). Seek a reusable source-level layer-elimination rule, preserving the present directed cone mechanism wherever its hypotheses remain valid. Do not restart flat determinant enumeration, assume the state remains two-dimensional, or reopen the stopped screw shortcut.

```text
GERM-66: COMPLETE AS A SCOPED EXPERIMENTAL PASS
POST-h TWO-LAYER CHAMBER h<e<=2h: CLOSED
EXPERIMENTAL ENDPOINT: L=log(2187/400)
POSITIVE-WIDTH CHAMBER ABOVE e=2h: OPEN
GERM-67: NOT EXECUTED
CANONICAL THEOREM CURSOR: SZ-CROSS-COLLAR-3, UNCHANGED
RATIFICATION / PUBLIC PROMOTION: NONE
```

This updates only the pending GERM-66 status in the earlier handoff; historical notes and their standing remain unchanged.
