# SZ edge recurrence 37 — monodromy cycle reduction

Date: 2026-09-26
Branch: sz-cross-collar
Status: UNRATIFIED RESIDUE / NF PASS
Canonical parent: SZ-CROSS-COLLAR-3
Immediate residue: series-36
Public promotion: forbidden

## Result

The finite folded boundary problem from series 35-36 reduces to a low-dimensional monodromy condition.

Case A: 0 < e <= k.
After eliminating all tree-like local atoms, each connected folded component has cycle rank at most one. Its remaining state is one bulk state V in C^2. Global rank loss occurs exactly when the 2-by-2 return map C_A has eigenvalue 1:

det(I-C_A)=0.

Case B: k < e <= k+h.
The single paired k-defect adds exactly one chord to the folded h-chain. After tree elimination, each connected component has cycle rank at most two. Cutting the two independent cycle edges leaves at most two bulk-state copies, hence a four-scalar monodromy state. Global rank loss occurs exactly when the corresponding return map C_B on C^4 has eigenvalue 1:

det(I-C_B)=0.

Thus the global boundary problem has been reduced from an L2 functional system to one 2-by-2 or 4-by-4 monodromy test per folded component.

No fixed-L injectivity theorem is claimed yet for the full post-p chamber.

## 1. Why the cycle rank is small

The folded graph has one ordered h-propagation spine.

Series 35 proved that admissible boundary words contain:

- finitely many h-steps;
- at most one defect-internal k-excursion;
- then finitely many h-steps.

The endpoint boundary matching closes the h-spine once.

Therefore:

- without a k-pair, the graph is a path plus one closure edge, so its first Betti number is at most 1;
- with the unique k-pair, one extra chord is added, so its first Betti number is at most 2.

All other vertices are attached trees.

Series 36 proves every local atom on those trees is invertible, so Gaussian/Schur elimination removes them without changing kernel dimension.

## 2. Monodromy factorization

Let B_e be one square folded boundary matrix after choosing one maximal square system on a connected component.

Choose a spanning tree of the folded graph and eliminate every tree vertex using the invertible atom library

M0, D0, P0, J0, T0, D1.

The remaining cycle variables satisfy

z = C_e z.

Hence

ker B_e is naturally isomorphic to ker(I-C_e).

At determinant level, up to the nonzero sign/permutation factor coming from the elimination ordering,

det B_e
=
(product of eliminated local atom determinants)
*
det(I-C_e).

Since every local atom determinant is nonzero by series 36, the only possible global singularity is

det(I-C_e)=0.

This is the exact monodromy reduction.

## 3. Pure bulk cycles are impossible

The bulk transfer matrix satisfies

det M0 = 1,

trace M0 = Theta = 1.9797928499....

Write its eigenvalues as

exp(+i theta), exp(-i theta).

Then

cos theta = Theta/2,

theta = 0.1422718154... .

Across the whole four-delay chamber,

u <= log(6/5).

With

h = log(81/80),

u/h < 14.677.

Thus any h-only propagation segment uses at most 15 transfer steps.

For 1 <= n <= 15,

0 < n theta < 2.135 < pi.

Therefore

det(I-M0^n)
=
2 - trace(M0^n)
=
2 - 2 cos(n theta)
>
0.

Because cos decreases on (0,pi),

det(I-M0^n)
>=
2 - 2 cos(theta)
=
2 - Theta
>
0.020.

Hence no folded component whose return map is a pure power of M0 can resonate.

Every unresolved monodromy cycle must contain at least one defect-scattering insertion.

## 4. Paired-defect Schur complement

In case B, write the paired defect block D1 in 2-by-2 block form

D1 =
[ D0  B ]
[ C   D0 ],

where

D0 =
[ G      delta ]
[ delta  G     ],

B =
[ 0  beta ]
[ 0   0   ],

C =
[ 0   0   ]
[ beta 0  ].

Eliminating the upper paired variables gives the effective lower Schur block

S1 = D0 - B D0^(-1) C.

Explicitly,

S1 =
[ G (G^2-beta^2-delta^2)/(G^2-delta^2)    delta ]
[ delta                                      G    ].

For the exact Weil weights S1 is positive definite.

Numerically,

S1 approximately equals

[ 16.5441   1.4685 ]
[  1.4685   1.4142 ],

with eigenvalues approximately

16.6853 and 1.2730.

Its determinant is approximately 21.2404.

Thus the paired k-defect remains strongly transverse even after one sheet is Schur-eliminated.

This does not by itself determine the global cycle return map, but it rules out a hidden local degeneracy introduced by the two-sheet reduction.

## 5. What remains in case A

Case A has no defect-internal k-pair.

After local elimination, there is at most one cycle.

Its return map has the form

C_A = L_A M0^n R_A

for one of finitely many admissible h-lengths n, where L_A and R_A are fixed boundary scattering maps assembled from D0, P0, J0 and T0 for the corresponding atom type.

By cyclicity of trace, the resonance determinant is

det(I-C_A)
=
1 - trace(C_A) + det(C_A).

All quantities are explicit rational expressions in the exact Weil weights once L_A,R_A are written.

The pure-bulk subcase L_A R_A = I is already excluded by Section 3.

The missing computation is therefore only the finite list of boundary scattering insertions, not a new source-level analysis.

## 6. What remains in case B

Case B contains one paired k-excursion.

After eliminating its tree attachments and, where convenient, applying the positive Schur block S1, every return word contains:

- a finite power of M0 before the k-excursion;
- one paired-defect scattering insertion;
- a finite power of M0 after it;
- the endpoint closure.

Because the graph has cycle rank at most two, one can cut two edges and encode all compatibility in one return map on at most C^4.

Thus case B requires one finite family of 4-by-4 determinants, not a functional determinant and not an infinite h/k lattice.

## 7. Pure-local determinant signs are not enough

Series 36 gave strong signs for every atom determinant.

That alone cannot settle monodromy.

Products of invertible local matrices may still acquire eigenvalue 1 after a closed return.

The elliptic bulk matrix makes this particularly clear: its powers rotate the invariant quadratic form rather than contract it.

Therefore the required weight-level theorem is a return-map transversality statement, not merely positivity of local minors.

## 8. Quantitative fixed-L consequence

If for a fixed L every monodromy determinant satisfies

|det(I-C_e)| >= eta_L > 0,

then, combining:

- the explicit local singular-value floors from series 36;
- the finite number of atom eliminations;
- the bounded powers of M0;

one obtains a fixed-L folded boundary estimate

||B_e z|| >= sigma_L ||z||

for some sigma_L>0.

Consequently the finite arithmetic-delay operator is injective on the corresponding folded source sector and has a fixed-scale singular-value floor there.

No uniform lower bound in L is obtained unless eta_L is controlled uniformly through the chamber.

## 9. Status of fixed-L injectivity

The load-bearing experimental range remains

0 < L <= log(16/3).

Series 33 remains non-load-bearing beyond that point after the series-34 audit.

This pass excludes:

- every local atom singularity;
- every pure-bulk monodromy resonance.

The sole remaining fixed-L obstruction is now:

defect-containing boundary monodromy.

## 10. General prime-channel theorem form

The common mechanism from series 27-37 is:

1. shortest-delay support geometry reduces the source to finitely many fibers;
2. the interior bulk carries a constant unimodular 2-state transfer;
3. new overlap thresholds add finitely many defect sheets;
4. local defect and overlap blocks are weight-level invertible;
5. finite support bounds the graph cycle rank;
6. tree elimination reduces injectivity to finitely many low-dimensional monodromy determinants.

This is the general prime-channel injectivity architecture suggested by the experiments.

The remaining task is not threshold-by-threshold source propagation. It is a finite weight-level monodromy nonresonance theorem.

## 11. Shrinking-collar status

Nothing in this pass advances the canonical cursor.

Even a complete fixed-L monodromy theorem would still need a quantitative bridge from the fixed-scale arithmetic-delay norm to the shrinking collar observation.

No power-law lower bound in epsilon is proved.

Canonical cursor remains SZ-CROSS-COLLAR-3.

## Next frontier

Next target:

SZ-KERNEL-EDGE-GERM-38 / DEFECT SCATTERING EXTRACTION

The next pass should explicitly compute the finite boundary scattering maps L_A,R_A in case A and the paired scattering insertion in case B.

Then:

- enumerate the finite admissible monodromy words;
- reduce det(I-C) to explicit rational/polynomial expressions in beta, delta, mu and G;
- test exact nonvanishing with outward rational bounds on log3/log2 and log5/log2.

No public promotion and no canonical cursor movement are asserted.
