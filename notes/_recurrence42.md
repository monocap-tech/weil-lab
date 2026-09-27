# SZ edge recurrence 42 — three-sheet atomization

Date: 2026-09-27
Branch: sz-cross-collar
Status: UNRATIFIED RESIDUE / NF PASS
Canonical parent: SZ-CROSS-COLLAR-3
Immediate residue: series-41
Public promotion: forbidden

## Objective

Construct the globally complete finite k-sheet transfer for the four-delay chamber

log(50/9) < L <= log 6

and identify the exact remaining nonlocal term.

The result is structural:

- at most three k-sheets are ever needed;
- the homogeneous local transfer is one universal r-sheet scattering block K_r with r=1,2,3;
- all K_r are exactly unimodular;
- the only external nonlocality after k-sheet stacking is one rank-one causal lag X(x-(k-h));
- the new r=3 block is itself strongly nonresonant, including true gate-free endpoint closure with all admissible bulk powers.

This is the first globally complete local atom library for the four-delay chamber.

It is not yet a complete global injectivity theorem because the rank-one causal lag still couples different h-residue fibers.

## 1. Arithmetic geometry

Set

h = log(81/80),

k = log(16/15),

p = log(10/9),

u = L-log5,

alpha = u-k,

zeta = u-2k.

Across the chamber,

p < u <= log(6/5),

and

u < 3k.

Therefore no coordinate x+3k can remain inside the head support.

Also

alpha <= log(9/8) < 2k,

so no point carrying the forward k-gate can generate a third forward k-jump.

The third sheet appears exactly when

zeta > 0,

equivalently

u>2k.

In terms of the moving post-p width

e=u-p,

this threshold is

e > e0,

where

e0 = 2k-p = log(128/125).

## 2. Three k-sheets

For an absolute base coordinate x, define

V0(x)=V(x),

V1(x)=V(x+k),

V2(x)=V(x+2k),

where

V=(X,S)^T.

A sheet is omitted whenever its argument lies outside the support.

The active sheet count is therefore

r(x)
=
1
+
1_(x<alpha)
+
1_(x<zeta).

Thus:

r=3 on 0<x<zeta when zeta>0;

r=2 on max(0,zeta)<x<alpha;

r=1 on alpha<x<u.

The sheet boundaries are monotone in L.

## 3. Coupling blocks

Let

e1=(1,0)^T,

e2=(0,1)^T.

Use the exact bulk transfer M0 from series 34:

V(x+h)=M0 V(x)

when all taps are absent.

The forward k-coupling block is

C_plus = c_plus e2^T.

The backward coupling block simplifies exactly to

C_minus = c_minus e1^T
        = eta e1 e1^T,

where

eta = beta/delta.

Using

log3/log2 < 8/5,

log5/log2 > 23/10,

one obtains

eta^2
<
1280/1587
<
81/100.

Hence

0 < eta < 9/10.

## 4. Universal r-sheet scattering block

For r active sheets, define the homogeneous sheet update sequentially by

Y0
=
M0 V0
+
C_plus V1

when r>=2, and Y0=M0V0 when r=1.

For 1<=m<r-1,

Ym
=
M0 Vm
+
C_plus V_(m+1)
-
C_minus Y_(m-1).

For the last sheet,

Y_(r-1)
=
M0 V_(r-1)
-
C_minus Y_(r-2).

This defines the r-sheet scattering block K_r.

Equivalently,

K_r = L_r U_r,

where U_r is block upper bidiagonal with

M0

on every diagonal block and

C_plus

on every superdiagonal block, while L_r is unit block lower bidiagonal with

-C_minus

on every subdiagonal block.

Therefore

det K_r
=
(det M0)^r
=
1.

The cases are:

K_1=M0;

K_2 is exactly the matched defect scattering insertion K from series 38;

K_3 is the new three-sheet scattering block registered in the terminology file.

## 5. Exact causal lag injection

The full transfer has one additional backward term on the first sheet when

x>k-h.

Set

lambda = k-h.

The external past value is

xi(x)=X(x-lambda).

The first sheet receives

-eta e1 xi.

Because each subsequent sheet subtracts

C_minus = eta e1e1^T

times the previous updated sheet, the same past scalar propagates through the active stack with geometric coefficients.

For r active sheets,

W_r(x+h)
=
K_r W_r(x)
+
epsilon(x) b_r xi(x),

where

epsilon(x)=1_(x>lambda),

and

b_r
=
(
-eta e1,
+eta^2 e1,
-eta^3 e1,
...,
(-1)^r eta^r e1
)^T

truncated after r blocks.

This is the causal lag injection registered in the terminology file.

Thus the only external nonlocality left after finite k-sheet closure is one scalar causal lag.

## 6. The explicit K3 block

Numerically the exact K3 block is approximately

[ 1.23933505   0.28692280   0            0.25284808   0            0          ]
[-0.28692280   0.74045780   0            0.65252163   0            0          ]
[-1.09215262  -0.25284808   1.23933505   0.06410275   0            0.25284808 ]
[ 0            0           -0.28692280   0.74045780   0            0.65252163 ]
[ 0            0           -1.09215262  -0.25284808   1.23933505   0.06410275 ]
[ 0            0            0            0           -0.28692280   0.74045780 ].

Its determinant is exactly 1.

Using the same certified outward rational logarithmic enclosures as series 38-41,

1.5849625
<
log3/log2
<
1.5849626,

2.3219280
<
log5/log2
<
2.3219281,

one obtains

0.0470727
<
det(I-K3)
<
0.0470739.

Hence K3 itself has no eigenvalue 1.

Its numerical smallest singular value is approximately 0.38959.

## 7. True endpoint closure of K3

Use the exact entrance and terminal graph lines

v_in=(1,R)^T,

ell_out=(R^(-1),-1).

For three sheets define

J_in^(3)
=
diag(v_in,v_in,v_in)

as a 6-by-3 injection, and

L_out^(3)
=
diag(ell_out,ell_out,ell_out)

as a 3-by-6 endpoint test.

The true endpoint closure matrix is

C_end^(3)(A)
=
L_out^(3) A J_in^(3).

For A=K3,

0.874794
<
det C_end^(3)(K3)
<
0.874823.

Thus the new three-sheet scattering atom is strongly endpoint-transverse.

## 8. K3 plus admissible bulk propagation

Let

B6
=
diag(M0,M0,M0).

Audit

A_n
=
K3 B6^n,

0<=n<=15.

Every outward determinant interval for

det C_end^(3)(A_n)

excludes zero.

The smallest absolute certified margin occurs at n=1:

-0.703159
<
det C_end^(3)(K3 B6)
<
-0.703123.

At n=0 the determinant is greater than 0.87479.

At n=2 it is greater than 4.21369.

For n>=3 the absolute values grow rapidly.

Therefore

|det C_end^(3)(K3 B6^n)|
>
0.7031

for every admissible n.

The genuinely new three-sheet homogeneous scattering event cannot create an endpoint-line resonance.

## 9. Sheet-drop atoms

When x+h crosses one of the sheet boundaries

zeta

or

alpha,

the active sheet count drops from

3 to 2

or from

2 to 1.

No new coefficient matrix is needed.

One applies the corresponding K_r relation and imposes zero on the output coordinates whose arguments have just left the support.

Since K_r is invertible, this is a boundary projection/constraint, not a local singularity.

Thus sheet creation/destruction does not enlarge the atom library beyond

K_1,K_2,K_3

plus the causal lag row.

## 10. Finite atom partition

A globally sufficient atom partition is obtained by starting from the structural breakpoints

0,

zeta,

alpha,

lambda=k-h,

u,

and closing this finite set under the admissible preimages of

x -> x+h

and

x -> x-lambda

that remain inside (0,u).

This closure is finite.

Indeed

u/h < 15,

and

u/lambda < 4.

Therefore an admissible dependency word contains fewer than 15 forward h-steps and fewer than 4 causal-lag steps before leaving the support.

On every resulting open atom:

- the active sheet count r is fixed;
- the causal-lag indicator epsilon is fixed;
- every shifted argument lands in one fixed atom or outside the support;
- the constant homogeneous coefficient block is one of K_1,K_2,K_3;
- the only off-atom forcing is the rank-one causal lag b_r e1^T.

This is the complete local atomization theorem for the four-delay chamber.

## 11. Arithmetic chamber changes

The third sheet appears at

e=e0=log(128/125).

Its width is

zeta=e-e0.

As e increases, the h-chain combinatorics change only when sheet/gate breakpoints or their bounded h/lambda preimages cross.

A useful primary family of thresholds is

e=e0+m h,

for the finitely many integers m for which the value lies in

0<e<=k+h.

Additional ordering changes involving the causal gate occur only when the same sheet boundaries cross a translate of

lambda=k-h.

Thus the parameter chamber decomposition is finite.

There is no irrational threshold cascade.

## 12. Scope corrections to series 35-41

The following statements survive:

- the transfer mechanism is finite-state at the L2-fiber level;
- all previously audited one- and two-sheet scattering subfamilies remain valid;
- terminal endpoint closure is always gate-free;
- no infinite operational h/k lattice is required.

The correct globally complete state is now:

at most three k-sheets
+
one scalar causal lag.

The two-sheet state is not globally complete.

The cycle-rank claims made before the three-sheet repair should not be used as global theorems.

## 13. Fixed-L injectivity status

This pass proves that the new three-sheet homogeneous atom is nonresonant and endpoint-transverse.

It does not yet eliminate the causal lag coupling between distinct atoms.

Therefore no new globally complete fixed-L injectivity interval is claimed.

The load-bearing continuous range remains

0 < L <= log(16/3).

## 14. Quantitative status

New fixed-scale margins in this pass include:

three-sheet local resonance:
det(I-K3) > 0.04707;

three-sheet endpoint closure:
absolute determinant > 0.87479;

three-sheet plus admissible bulk endpoint closure:
absolute determinant > 0.7031.

Also

eta<9/10

for the sole causal lag coefficient.

These are fixed-scale arithmetic-delay estimates.

They do not imply shrinking-collar coercivity.

## 15. General transfer theorem extracted

The experimental prime-channel mechanism can now be stated in a form naturally extensible to later thresholds.

For a fixed active-delay chamber:

1. choose the shortest newly active arithmetic gap k;
2. stack all k-translates that fit in the support;
3. the homogeneous local transfer is an r-sheet block K_r=L_r U_r;
4. det K_r=(det M0)^r;
5. forward k-couplings are absorbed in U_r;
6. matched backward k-couplings are absorbed in L_r;
7. only causal taps that leave the stacked sheet family remain as delayed forcing;
8. compact support bounds both the sheet count and the lag depth.

The four-delay chamber has r<=3 and one rank-one causal lag.

This is the first globally complete local prime-channel transfer theorem in the GERM chain.

## Next frontier

Next target:

SZ-KERNEL-EDGE-GERM-43 / CAUSAL-LAG CLOSURE

The next pass should attack the sole remaining global ingredient:

X(x-(k-h)).

Priority:

1. fold the causal lag into the finite atom graph generated in Section 10;
2. determine whether its coefficient eta<9/10 gives a triangular/contraction elimination;
3. if contraction is insufficient, enumerate the finite causal-history return words;
4. combine them with K_1,K_2,K_3 endpoint transversality.

A successful pass would produce the first globally complete fixed-L four-delay prime-channel injectivity theorem.

Canonical theorem cursor remains SZ-CROSS-COLLAR-3.

No public promotion and no canonical cursor movement are asserted.
