# SZ edge recurrence 38 — defect scattering extraction

Date: 2026-09-26
Branch: sz-cross-collar
Status: UNRATIFIED RESIDUE / NF PASS
Canonical parent: SZ-CROSS-COLLAR-3
Immediate residue: series-37
Public promotion: forbidden

## Objective

Extract the actual matched k-defect scattering map and test the complete family of monodromy words consisting of one matched defect excursion plus arbitrary admissible bulk propagation.

The result is positive:

every such single-scattering monodromy word is nonresonant for the exact Weil weights.

This does not yet prove global fixed-L injectivity, because complete boundary cycles may also contain endpoint or unmatched-defect scattering insertions.

## 1. Bulk data

Use the bulk state

V(x) = (X(x),S(x))^T

and the exact bulk transfer

V(x+h)=M0 V(x),

where

M0 =
[ (Q-T)/R    E/R ]
[   -T        E  ].

The exact identities are

det M0 = 1,

trace M0 = Theta = 1.9797928499....

Define the doubled pure-bulk transfer

B4 = diag(M0,M0).

## 2. Matched k-excursion

Let

e1 = (1,0)^T,
e2 = (0,1)^T,

and let the forward/backward tap columns from series-34 be

c_plus =
[ F/R ]
[ F   ],

c_minus =
[ Z/R ]
[ 0   ].

Consider a matched gate pair x and x+k for which:

V(x+h)
=
M0 V(x)
+
c_plus e2^T V(x+k),

and

V(x+k+h)
=
M0 V(x+k)
-
c_minus e1^T V(x+h).

On the paired state

W(x) =
( V(x), V(x+k) ),

this is

W(x+h) = K W(x),

with the matched defect scattering insertion

K =
[ M0,                     c_plus e2^T                       ]
[ -c_minus e1^T M0,       M0-(e1^T c_plus)c_minus e2^T    ].

This object is registered in the terminology file.

## 3. Exact unimodularity

K factors as

K
=
[ I, 0 ]
[ -c_minus e1^T, I ]

times

[ M0, c_plus e2^T ]
[ 0,  M0           ].

The first factor is a shear with determinant 1.

The second is block upper triangular with determinant

(det M0)^2 = 1.

Therefore

det K = 1.

Also e2^T c_minus = 0, so the rank-one correction to the lower-right block has zero trace. Hence

trace K = 2 trace M0 = 2 Theta.

Numerically,

K approximately equals

[  1.23933505   0.28692280   0            0.25284808 ]
[ -0.28692280   0.74045780   0            0.65252163 ]
[ -1.09215262  -0.25284808   1.23933505   0.06410275 ]
[  0            0           -0.28692280   0.74045780 ].

Its spectrum is approximately

1.61247708,
0.62016385,
0.86347238 + 0.50439612 i,
0.86347238 - 0.50439612 i.

Thus K itself has no eigenvalue 1.

## 4. Reciprocal characteristic polynomial

Direct symbolic reduction using det M0=1 gives a palindromic characteristic polynomial:

chi_K(z)
=
z^4
-
2 Theta z^3
+
Xi z^2
-
2 Theta z
+
1.

Numerically

Xi = 5.8556475749....

So the four eigenvalues occur in reciprocal pairs.

The two values of y=z+z^(-1) are approximately

2.23264093

and

1.72694477.

Hence one reciprocal pair is real hyperbolic and the other lies on the unit circle.

The defect scattering insertion is therefore mixed hyperbolic/elliptic, not a degenerate shear.

## 5. Exact nonresonance of K itself

Let

beta = B/A,
delta = D/A,
mu = beta^2,
G = sqrt(2).

A direct symbolic factorization gives

det(I-K)
=
H_minus H_plus / (delta^2 mu^4),

where

H_minus
=
G^3
-
G^2 beta
-
G delta^2
-
2 G mu^2
+
beta mu^2
+
2 delta mu^2,

H_plus
=
G^3
+
G^2 beta
-
G delta^2
-
2 G mu^2
-
beta mu^2
+
2 delta mu^2.

Use the exact rational logarithmic enclosures

1.5849625
<
log3/log2
<
1.5849626,

2.3219280
<
log5/log2
<
2.3219281.

These bounds are certified by direct integer-power comparison.

Together with rational square enclosures of width 10^(-10) for sqrt(2), sqrt(2/3), and sqrt(2/5), exact interval arithmetic gives

1.124634
<
H_minus
<
1.124695,

-0.958235
<
H_plus
<
-0.958174.

Therefore

det(I-K) < 0.

More precisely,

-0.063525
<
det(I-K)
<
-0.063523.

So the matched defect insertion itself is uniformly separated from resonance.

## 6. Single-scattering monodromy family

Any cycle containing exactly one matched defect insertion and otherwise only pure bulk propagation has, after cyclic permutation,

C_n = K B4^n

for some total number n of bulk h-steps.

Indeed, for a word

B4^m K B4^r,

the identity det(I-AB)=det(I-BA) reduces the resonance determinant to the same value with n=m+r:

det(I-B4^m K B4^r)
=
det(I-K B4^(m+r)).

Across the entire four-delay chamber, series-37 gives at most 15 bulk h-steps.

Thus it is enough to test

n=0,1,...,15.

## 7. Exact interval audit of all admissible n

Using the certified rational bounds

15849625/10^7
<
log3/log2
<
15849626/10^7,

23219280/10^7
<
log5/log2
<
23219281/10^7,

and rational square enclosures, exact outward interval matrix arithmetic gives:

n=0:
-0.063525 < det(I-C_n) < -0.063523

n=1:
-0.249269 < det(I-C_n) < -0.249254

n=2:
-0.535510 < det(I-C_n) < -0.535435

n=3:
-0.882972 < det(I-C_n) < -0.882703

n=4:
-1.238349 < det(I-C_n) < -1.237556

n=5:
-1.539161 < det(I-C_n) < -1.537106

n=6:
-1.719406 < det(I-C_n) < -1.714901

n=7:
-1.715763 < det(I-C_n) < -1.707059

n=8:
-1.473645 < det(I-C_n) < -1.458450

n=9:
-0.952636 < det(I-C_n) < -0.928304

n=10:
-0.130864 < det(I-C_n) < -0.094815

n=11:
0.992076 < det(I-C_n) < 1.041684

n=12:
2.393902 < det(I-C_n) < 2.457243

n=13:
4.030187 < det(I-C_n) < 4.104729

n=14:
5.835582 < det(I-C_n) < 5.917244

n=15:
7.724063 < det(I-C_n) < 7.815851.

Every interval excludes zero.

The smallest certified absolute margin occurs at n=0 and is greater than 0.0635.

Therefore:

every admissible single-matched-scattering bulk monodromy word is nonresonant.

## 8. Interpretation

The first genuine post-p overlap does not create a resonance merely by inserting one matched k-excursion into the elliptic bulk.

The defect insertion K is itself unimodular and nonresonant.

Moreover no amount of admissible pure bulk propagation before/after that single insertion can tune the return map to eigenvalue 1.

Thus any remaining boundary monodromy failure must contain at least one additional non-bulk ingredient, such as:

- endpoint closure scattering;
- an unmatched forward/backward gate;
- or the second independent cycle present in the paired-defect geometry.

This sharply reduces the global cycle library.

## 9. What this does not prove

This pass does not prove that every folded cycle is of the form K B4^n.

The complete folded boundary graph may contain endpoint scattering maps not yet extracted explicitly.

Case B may also require a two-cycle 4-state compatibility rather than a single return word.

Therefore fixed-L injectivity beyond the currently load-bearing range is not yet claimed.

## 10. Quantitative consequence

For the single-scattering family one has the uniform determinant margin

|det(I-C_n)| > 0.0635

for every admissible n.

Together with the local singular-value bounds from series-36 and bounded bulk powers, this gives a positive fixed-scale conditioning margin for every folded component whose only non-bulk event is one matched k-scattering insertion.

This is a genuine quantitative fixed-scale result.

It still does not imply shrinking-collar coercivity.

## 11. Status

Load-bearing fixed-L injectivity range remains

0 < L <= log(16/3).

The later series-33 extension remains non-load-bearing after the series-34 audit.

The canonical theorem cursor remains SZ-CROSS-COLLAR-3.

## Next frontier

Next target:

SZ-KERNEL-EDGE-GERM-39 / ENDPOINT SCATTERING CLOSURE

The next pass should extract the remaining endpoint/unmatched-defect scattering maps and determine whether every folded cycle factors into:

bulk powers,
the matched insertion K,
and a finite endpoint scattering library.

The target is then to enumerate the genuinely remaining return words and complete the weight-level monodromy nonresonance theorem.

No public promotion and no canonical cursor movement are asserted.
