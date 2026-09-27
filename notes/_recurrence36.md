# SZ edge recurrence 36 — defect matrix enumeration

Date: 2026-09-26
Branch: sz-cross-collar
Status: UNRATIFIED RESIDUE / NF PASS
Canonical parent: SZ-CROSS-COLLAR-3
Immediate residue: series-35
Public promotion: forbidden

## Objective

Enumerate the constant local matrices produced by the finite-folding theorem in the two post-p defect geometries

A. 0 < e <= k,
B. k < e <= k+h,

and test their exact minors with the Weil arithmetic weights.

The result is positive at the atomic level:

every local elimination block is uniformly nonsingular.

Therefore any failure of fixed-L injectivity in the post-p chamber cannot be caused by a local gate singularity. It must be a global boundary monodromy/transversality resonance assembled from invertible atoms.

No new fixed-L injectivity interval and no shrinking-collar result are claimed.

## 1. Constants

Use

beta = B/A,
gamma = C/A,
delta = D/A,
mu = beta^2,
G = 2 gamma = sqrt(2),

with

A = log2/sqrt(2),
B = log3/sqrt(3),
C = log2/2,
D = log5/sqrt(5).

Also

Delta = mu^2-G^2.

The exact numerical values are approximately

beta = 1.2941164627,
delta = 1.4685162686,
mu = 1.6747374191,
G = 1.4142135624,
Delta = 0.8047454230.

The bulk transfer matrix from series-34/35 is

M0 =
[ (Q-T)/R    E/R ]
[   -T        E  ],

with

det M0 = 1,

trace M0 = Theta = 1.9797928499....

Its smallest singular value is approximately 0.7812.

## 2. Case A: unpaired defect block

When

0 < e <= k,

there is no defect-internal backward k-feedback.

The two extreme boundary equations at one lower-defect point have local coefficient matrix

D0 =
[ G      delta ]
[ delta  G     ].

Its determinant is

det D0 = G^2-delta^2.

This is strictly negative.

Indeed

delta^2
=
(2/5) (log5/log2)^2.

Since

5^4 > 2^9,

log5/log2 > 9/4,

so

delta^2 > (2/5)(81/16) = 81/40.

As G^2=2,

delta^2-G^2 > 1/40.

Hence

det D0 < -1/40.

Thus D0 is uniformly invertible.

Numerically

det D0 = -0.1565400311,

sigma_min(D0) = 0.0543027062.

So the unpaired defect gate has no local rank loss.

## 3. P-overlap block

The P-overlap comparison solves for the pair consisting of the local S-value and the translated X(p+x)-value.

The coefficient block is

P0 =
[ mu   -G ]
[ -G   mu ].

Its determinant is

det P0 = mu^2-G^2 = Delta.

Since

log3/log2 > 3/2

from 9>8,

mu
=
(2/3)(log3/log2)^2
>
3/2.

Therefore

Delta > (3/2)^2 - 2 = 1/4.

Hence P0 is uniformly invertible.

Numerically

det P0 = 0.8047454230,

sigma_min(P0) = 0.2605238568.

Thus the P-overlap itself cannot create a resonance.

## 4. J-overlap block

The J-overlap first solves the translated X(j+x)-value and then the shifted S(x+h)-value.

With variables ordered as

(X(j+x), S(x+h)),

the coefficient block may be taken as

J0 =
[ mu   0  ]
[ -G   mu ].

Therefore

det J0 = mu^2 > 9/4.

Numerically

det J0 = 2.8047454230,

sigma_min(J0) = 1.1107890968.

So the J-overlap has a particularly strong local rank margin.

## 5. Terminal block

The old terminal relation has the form

S(x)
=
R^(-1) X(x)
-
(beta/delta) * gated S(x+k).

The coefficient of the local unknown S(x) is exactly 1.

Thus the terminal elimination block is the scalar matrix

T0 = [1].

There is no terminal local singularity.

Any terminal failure is necessarily a global matching resonance after propagation through the preceding transfer blocks.

## 6. Case B: paired k-defect block

Now assume

k < e <= k+h.

The only defect-internal k-pair is

0 < t < e-k

paired with

k < t+k < e.

Since

e-k <= h,

this paired region occupies at most one h-cell.

Fold t and t+k together and order the four local variables as

(X(t), S(t), X(t+k), S(t+k)).

The exact local coefficient matrix is

D1 =
[ G      delta   0      beta  ]
[ delta  G       0      0     ]
[ 0      0       G      delta ]
[ beta   0       delta  G     ].

This is the paired defect block registered in the terminology file.

Its determinant factors exactly as

det D1
=
-(-G^2 + G beta + delta^2)
 ( G^2 + G beta - delta^2).

Both factors are strictly positive.

For the first factor,

-G^2 + G beta + delta^2
=
(delta^2-G^2)+G beta.

The first term is greater than 1/40 by Section 2.

Also beta>1, hence G beta > sqrt(2) > 7/5.

Therefore

-G^2 + G beta + delta^2 > 57/40.

For the second factor, use

5^3 < 2^7,

so

log5/log2 < 7/3.

Hence

delta^2 < (2/5)(49/9) = 98/45,

and therefore

G^2-delta^2 > -8/45.

Again beta>1 and G beta > 7/5, so

G^2 + G beta - delta^2
>
7/5 - 8/45
=
11/9.

Thus

|det D1|
>
(57/40)(11/9)
=
627/360.

In particular D1 is uniformly invertible.

Numerically

det D1 = -3.3249700569,

sigma_min(D1) = 0.4565212256.

So the only defect-internal k-feedback pair is locally very far from singular.

## 7. Complete local atom list

After the finite folding of series-35, every local elimination step is built from the following constant atom types:

1. bulk propagation:
   M0, det = 1;

2. unpaired defect solve:
   D0, det < -1/40;

3. P-overlap solve:
   P0, det > 1/4;

4. J-overlap solve:
   J0, det > 9/4;

5. terminal local solve:
   T0, det = 1;

6. paired k-defect solve:
   D1, with |det D1| > 627/360.

Every local atom is therefore full rank with an explicit weight-level margin.

This statement is independent of the moving defect width e inside the two geometries.

## 8. Consequence for defect transversality

The finite-folding matrices B_j from series-35 are assembled by composing and coupling these local invertible atoms along the finite boundary graph.

Because every vertex block is nonsingular, a global B_j can lose rank only through a closed compatibility cycle.

Equivalently:

local gate singularity is excluded;

the only remaining failure mode is monodromy resonance.

This is a substantial simplification.

One no longer needs to inspect whether a new overlap threshold makes an individual elimination impossible. New thresholds only change the finite graph connecting already nonsingular atom types.

## 9. Quantitative fixed-scale implication

Suppose a given fixed-L folded boundary graph is globally transverse.

Then its smallest singular value is positive because it is a finite constant matrix assembled from the atoms above.

The explicit local determinant margins prevent any singular-value collapse from occurring at a single gate.

Any small global singular value must arise from near-cancellation around a complete boundary cycle.

Thus the next quantitative problem is global monodromy conditioning, not local defect conditioning.

No uniform lower bound in L is proved here.

## 10. Status of fixed-L injectivity

This pass does not itself prove global transversality of the folded boundary graph.

Therefore the load-bearing experimental injectivity range remains

0 < L <= log(16/3).

The later scalar extension claimed in series-33 remains non-load-bearing after the series-34 audit.

## 11. Prime-channel theorem extracted so far

The common mechanism from series 27-36 can now be stated more sharply:

Within any fixed active-delay and boundary-ordering chamber, the finite arithmetic-delay equation reduces to a finite graph of constant local atom matrices. For the first post-p chamber all atom types are weight-level nonsingular. Hence fixed-L injectivity is equivalent to exclusion of finitely many global monodromy resonances.

This is the first genuinely reusable statement that survives the overlap changes.

It replaces threshold-specific source elimination by:

finite atom library
+
finite graph
+
monodromy determinant.

## 12. Shrinking-collar status

Nothing here advances the canonical theorem cursor.

Even if all monodromy determinants are shown nonzero and fixed-L arithmetic-delay injectivity is proved globally, the drilling interface still requires a quantitative estimate transferring fixed-scale prime-channel control into the shrinking collar observation.

No such power-law or quasi-analytic transfer is proved.

Canonical cursor remains SZ-CROSS-COLLAR-3.

## Next frontier

Next target:

SZ-KERNEL-EDGE-GERM-37 / MONODROMY CYCLE REDUCTION

The next pass should:

1. enumerate the finite boundary cycles generated by the atom library in cases A and B;
2. compress each cycle to a product/Schur complement of M0, D0 or D1, P0, J0, and T0;
3. derive the resulting cycle determinant as a polynomial/rational expression in the exact Weil weights;
4. test whether all such cycle determinants have a common sign or admit an exact resonance;
5. if nonzero, recover fixed-L injectivity and a fixed-scale singular-value floor without returning to threshold-by-threshold proofs.

No public promotion and no canonical cursor movement are asserted.
