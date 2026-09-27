# SZ edge recurrence 39 — endpoint shear closure

Date: 2026-09-26
Branch: sz-cross-collar
Status: UNRATIFIED RESIDUE / NF PASS
Canonical parent: SZ-CROSS-COLLAR-3
Immediate residue: series-38
Public promotion: forbidden

## Objective

Extract the remaining unmatched endpoint/defect shear maps and determine how much of the residual monodromy library can be certified without re-entering source-level threshold arguments.

The result is positive for the complete one-excursion shear family:

- unmatched shears are explicit unimodular doubled-state transfers;
- every unmatched shear with at least one doubled bulk step is nonresonant by an exact factorization;
- every separated forward/backward one-k-excursion word with total admissible bulk length at most 15 is nonresonant by outward interval audit.

The only remaining endpoint issue is the zero-bulk unmatched-sheet closure and the genuinely coupled two-cycle boundary identification.

No new global fixed-L injectivity interval is claimed.

## 1. Unmatched defect shears

Use the doubled state

W = (V_low,V_high),

with

V=(X,S)^T,

bulk transfer

M0,

doubled bulk transfer

B4 = diag(M0,M0),

and exact tap columns

c_plus,
c_minus.

Let

e1=(1,0)^T,
e2=(0,1)^T.

Define

E_plus =
[ M0,                 c_plus e2^T ]
[ 0,                  I           ],

E_minus =
[ I,                   0           ]
[ -c_minus e1^T,       M0          ].

These are the unmatched defect shears registered in the terminology file.

They are exactly the forward-only and backward-only k-gate transfers when the companion sheet is carried but not simultaneously advanced.

Both are unimodular:

det E_plus = det M0 = 1,

det E_minus = det M0 = 1.

The matched defect scattering insertion from series-38 is

K = E_minus E_plus.

Thus a separated forward/backward one-k-excursion is not a new primitive object.

## 2. Unmatched-shear factorization

Consider

E_plus B4^n.

Because E_plus is block upper triangular,

E_plus B4^n
=
[ M0^(n+1),          c_plus e2^T M0^n ]
[ 0,                 M0^n              ].

Therefore

det(I-E_plus B4^n)
=
det(I-M0^(n+1))
*
det(I-M0^n).

Likewise

det(I-E_minus B4^n)
=
det(I-M0^n)
*
det(I-M0^(n+1)).

Series-37 proved

det(I-M0^r)>0

for every admissible pure bulk length

1<=r<=15.

Hence

det(I-E_plus B4^n)>0,

det(I-E_minus B4^n)>0

for every admissible

1<=n<=14.

The same conclusion holds at n=15 whenever the n+1 bulk power is still present in the actual folded word.

A coarse uniform bound follows from

det(I-M0^r) >= 2-Theta > 0.01.

Thus

det(I-E_plus B4^n),
det(I-E_minus B4^n)
>
10^(-4)

whenever both bulk factors have positive exponent.

## 3. Meaning of the n=0 zero

At n=0,

det(I-E_plus)=0,

det(I-E_minus)=0.

This is not evidence of a physical prime-channel resonance.

E_plus carries the upper sheet by the identity block.

E_minus carries the lower sheet by the identity block.

Therefore each unmatched shear alone has a fixed two-dimensional carried-sheet subspace.

A complete boundary cycle must close that carried sheet through an endpoint relation or through the companion shear.

Thus the n=0 zero is a bookkeeping degeneracy of an open doubled state.

It identifies exactly what endpoint data remain to be extracted.

## 4. Separated double-shear words

A balanced one-k-excursion with forward and backward gates separated by bulk propagation has one of the two forms

C_minus_plus(m,n)
=
E_minus B4^m E_plus B4^n,

or

C_plus_minus(m,n)
=
E_plus B4^m E_minus B4^n.

Cyclic determinant invariance removes arbitrary pure-bulk prefixes/suffixes; only the two internal bulk lengths matter.

Across the whole four-delay chamber, the total admissible number of h-steps is at most 15.

Therefore the finite audit domain is

m>=0,
n>=0,
m+n<=15.

There are

136

index pairs and two orientations, hence

272

return determinants.

## 5. Outward interval audit

Use the same certified logarithmic enclosures as series-38:

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

together with outward square-root interval arithmetic.

All 272 determinant intervals exclude zero.

The closest certified cases are:

orientation E_plus ... E_minus,
m=2, n=9:

0.01448
<
det(I-C)
<
0.05614;

orientation E_minus ... E_plus,
m=1, n=10:

0.01516
<
det(I-C)
<
0.05546;

orientation E_plus ... E_minus,
m=10, n=1:

0.01524
<
det(I-C)
<
0.05538;

orientation E_minus ... E_plus,
m=9, n=2:

0.01604
<
det(I-C)
<
0.05458.

Every other certified absolute determinant margin is larger.

Thus

|det(I-C)| > 0.0144

for every admissible separated double-shear word in the audit family.

The matched case m=n=0 reproduces series-38:

-0.063525
<
det(I-K)
<
-0.063523.

## 6. Consequence for one-excursion monodromy

The entire monodromy family with:

- at most one forward k-gate;
- at most one backward k-gate;
- arbitrary admissible pure bulk propagation between/around them;
- and no additional endpoint identification,

is now certified nonresonant whenever the doubled carried sheet is genuinely advanced/closed.

No tuning of the elliptic bulk lengths can create eigenvalue 1.

This extends the series-38 matched-scattering theorem to separated one-excursion scattering.

## 7. Remaining endpoint closure

What remains is now sharply typed.

An unmatched shear with zero bulk advance leaves one sheet fixed by construction.

To decide the actual boundary problem one must replace that carried identity sheet by the true endpoint boundary subspace supplied by the lower/upper defect equations.

Likewise, in the case-B two-cycle geometry, the two independently cut cycle states must be closed simultaneously rather than treated as a single balanced shear word.

Therefore the residual problem is not another bulk/defect scattering calculation.

It is endpoint subspace closure.

## 8. Status of finite-folding claims

The present calculations use only exact local transfer identities and the externally bounded number of bulk h-steps.

They do not require an infinite h/k orbit argument.

They also do not by themselves prove that every complete folded boundary component is one of the audited words.

That final identification remains part of endpoint closure.

## 9. Quantitative status

For the separated double-shear family the certified determinant floor

|det(I-C)| > 0.0144

is a genuine fixed-scale monodromy margin.

For unmatched shears with positive bulk advance, the exact product formula gives a positive margin from the pure-bulk determinant floor.

Combining these with the local atom singular-value bounds from series-36 gives fixed-scale conditioning for every component already reduced to one of these word types.

No uniform-in-L estimate for the complete boundary problem is yet claimed.

No shrinking-collar estimate follows.

## 10. Fixed-L injectivity status

The globally load-bearing experimental injectivity range remains

0 < L <= log(16/3).

The post-log(16/3) work now excludes:

- local atom singularity;
- pure bulk resonance;
- matched one-k scattering resonance;
- separated forward/backward one-k scattering resonance;
- unmatched shear resonance after positive doubled bulk advance.

The remaining obstruction is:

true endpoint subspace closure
and, in case B, simultaneous two-cycle closure.

## 11. General prime-channel architecture

The experimental chain now gives the following reusable decomposition:

bulk propagation:
M0;

unmatched gate primitives:
E_plus, E_minus;

matched gate primitive:
K = E_minus E_plus;

local boundary solves:
D0, D1, P0, J0, T0;

global obstruction:
closure of the carried endpoint subspaces.

Thus later arithmetic thresholds should enlarge the primitive scattering library but need not restart the source equation from scratch.

## Next frontier

Next target:

SZ-KERNEL-EDGE-GERM-40 / ENDPOINT SUBSPACE CLOSURE

The next pass should:

1. derive the exact lower and upper endpoint subspaces from the defect equations, rather than carrying an identity sheet;
2. replace the n=0 unmatched-shear bookkeeping zero by the true endpoint closure determinant;
3. identify whether every case-A boundary component is then completely covered by the certified one-excursion library;
4. derive the simultaneous closure matrix for the case-B two-cycle state.

A successful pass would leave only finitely many explicit endpoint closure determinants between the project and a full fixed-L four-delay prime-channel injectivity theorem.

Canonical theorem cursor remains SZ-CROSS-COLLAR-3.

No public promotion and no canonical cursor movement are asserted.
