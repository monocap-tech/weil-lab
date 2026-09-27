# SZ edge recurrence 35 — finite-defect transversality theorem

Date: 2026-09-26
Branch: sz-cross-collar
Status: UNRATIFIED RESIDUE / NF PASS
Canonical parent: SZ-CROSS-COLLAR-3
Immediate residue: series-34
Public promotion: forbidden

## Result

The post-p prime-channel problem is a finite transversality problem, but not an ordinary finite-dimensional pointwise determinant.

The correct state is a finite vector of L2 boundary fibers acted on by truncated translations.

For the whole chamber

log(50/9) < L <= log 6,

write

e = L - log(50/9),

h = log(81/80),

k = log(16/15).

Then

0 < e <= k+h,

and numerically

h = 0.0124225...,
k = 0.0645385....

The bulk state is

V(x) = (X(x), S(x))^T

with exact constant transfer matrix

M0 =
[ (Q-T)/R    E/R ]
[   -T        E  ],

det M0 = 1,

trace M0 = Theta = 1.9797928499....

The post-p gates add only the finite taps

S(x+k)

and

X(x-(k-h)).

The main theorem of this pass is that, after folding the moving lower and upper defect strips, these taps generate a finite operator algebra on the defect fibers. Therefore fixed-L injectivity reduces to finitely many constant matrix transversality tests for each boundary-ordering chamber.

No injectivity extension beyond the previously ratified experimental range is claimed here.

## 1. Correction to the four-scalar interpretation

Series-34 introduced the two-sheet state

W(t) = ( V(t), V(p+t) ),

0<t<e.

This is the correct finite sheet count, but it is not by itself a closed pointwise 4-by-4 recurrence.

The exact transfer contains values at shifted base arguments:

V(x+h)
=
M0 V(x)
+ 1_(x<alpha) c_plus S(x+k)
- 1_(x>k-h) c_minus X(x-(k-h)).

Thus a local value W(t) may depend on W at another base argument.

The load-bearing state is therefore not C^4 at one point. It is a finite vector of L2 fibers with partial translation operators between them.

This corrects any interpretation of series-34 as an ordinary 4-by-4 cocycle.

## 2. Truncated translation algebra

Let

D_e = L2(0,e).

For r>0 define the truncated forward and backward shifts

(T_r^+ phi)(t) = 1_(t+r<e) phi(t+r),

(T_r^- phi)(t) = 1_(t>r) phi(t-r).

The defect matching equations are finite linear combinations of:

- identity operators on D_e;
- T_h^+ and T_h^-;
- gated k-shifts T_k^+ and T_k^-;
- the fixed coefficient matrices inherited from M0 and the boundary P/J relations.

Thus the boundary matching object is a finite matrix over a truncated-translation algebra.

## 3. Finite depth of k-feedback

The outward chamber bound is

e <= k+h.

Since h<k,

e < 2k.

Therefore

(T_k^+)^2 = 0,

(T_k^-)^2 = 0

on D_e.

Equivalently, a source point inside the moving defect can be shifted by k and remain inside the same defect at most once.

If e<=k, there is no defect-to-defect k-feedback at all.

If k<e<=k+h, the only paired defect strip is

0<t<e-k,

paired with

k<t<e.

Its width satisfies

e-k <= h.

So even in the final subchamber the extra k-feedback occupies no more than one h-cell.

This disproves the operational dense-orbit picture suggested in series-32.

The irrationality of h/k is real, but the admissible boundary gates prevent arbitrary h/k words from acting inside the defect.

## 4. Finite depth of h-propagation

Also

e <= k+h < 7h.

Hence a pure h-chain inside the defect contains fewer than seven forward h-steps.

The bulk outside the defect has fixed length p-e with p=log(10/9), so its h-propagation depth is finite as well.

Thus every admissible boundary word consists of:

- finitely many h-steps;
- at most one defect-internal k-excursion;
- followed by finitely many h-steps.

There is no infinite transfer word inside one fixed boundary-ordering chamber.

## 5. Finite folding theorem

Collect all gate endpoints and all of their admissible h-preimages inside (0,e).

A sufficient breakpoint set is generated from

0,
e,
k,
e-k,
k-h,
alpha,

together with their translates by n*h that remain in (0,e), for the finitely many integers allowed by e<7h.

This produces a finite partition

(0,e) = I_1 union ... union I_N

up to null endpoints.

Refine once more by the corresponding upper-sheet endpoints p+I_j.

On each final atom I_j:

- every indicator in the exact P/J equations is constant;
- every admissible shifted argument lands in one fixed atom with the same local coordinate;
- every inadmissible shifted argument is zero or belongs to the already reconstructed bulk sheet.

Therefore, after identifying translated atoms by the obvious L2 isometries, the full boundary matching equations become

B_j z_j = 0

with a constant finite coefficient matrix B_j for each atom type.

The entries of B_j depend only on the exact Weil weights and on which gates are active, not on the local coordinate inside I_j.

Hence:

fixed-L boundary injectivity
is equivalent to
full column rank of finitely many constant matrices B_j.

This is the finite-defect transversality theorem.

## 6. Quantitative consequence of a successful rank test

Because the folding maps are L2 isometries, if every B_j has smallest singular value at least sigma_j>0, then the folded boundary operator has the fixed-L lower bound

||B_e W|| >= sigma_e ||W||,

where

sigma_e = min_j sigma_j > 0.

Thus the transfer framework naturally produces a quantitative fixed-scale boundary singular-value floor once transversality is verified.

This is stronger than mere algebraic injectivity of a pointwise recurrence.

However sigma_e may depend strongly on L and may collapse at ordering thresholds.

No uniform lower bound in L is proved.

## 7. Bulk symplectic structure

The constant bulk matrix satisfies

det M0 = 1

and

-2 < trace M0 < 2.

Hence M0 is elliptic and preserves a positive definite quadratic form after conjugation.

There is no bulk singularity.

Any loss of injectivity must therefore come from boundary defect matching, not from degeneration of the bulk transfer.

This sharply localizes the possible prime-channel resonance.

## 8. What is and is not proved

Proved in this pass:

1. the post-p transfer mechanism is finite-state at the level of L2 fibers;
2. the apparent h/k dense orbit does not occur operationally inside the defect;
3. the defect matching operator folds into finitely many constant matrix rank tests;
4. any successful rank test automatically gives a fixed-L singular-value floor for the folded boundary system;
5. the only possible failure is finite boundary transversality.

Not proved:

1. the complete list of B_j matrices for every e in (0,k+h];
2. their exact determinants/minors;
3. fixed-L injectivity for log(16/3)<L<=log6;
4. any uniform-in-L singular-value floor;
5. any shrinking-collar coercivity.

## 9. Status of the earlier positive window

The audit in series-34 invalidated the scalar proof used by series-33 beyond log(16/3).

Nothing in the present pass repairs that missing determinant.

Therefore the currently load-bearing experimental injectivity range remains

0 < L <= log(16/3).

Within that range, finite dimensionality of the regular zero family gives a fixed-scale arithmetic-delay singular-value floor.

## 10. General prime-channel injectivity theorem suggested by the chain

The reusable theorem template is now:

For any fixed finite active arithmetic-delay set and any boundary-ordering chamber, compact support plus the shortest delay reduce the source to finitely many boundary fibers. The interior equation induces a constant unimodular bulk transfer. Every new overlap threshold adds only finitely many translated boundary sheets. Support bounds make the resulting truncated-translation algebra finite-depth. After finite atom folding, fixed-L injectivity is equivalent to transversality of finitely many constant coefficient matrices.

This subsumes the scalar recurrences of series 27-31 as the one-sheet case and the post-p system as the first multi-sheet case.

What remains is to prove a chamber-independent nonvanishing principle for those finite boundary matrices using the exact arithmetic weights.

## 11. Shrinking-collar drilling status

Even a complete fixed-L prime-channel injectivity theorem would not yet advance the canonical cursor.

The missing drilling interface remains quantitative:

fixed-scale arithmetic-delay control
must be transferred to
the shrinking collar observation as epsilon -> 0.

No result here supplies a power-law lower bound for that transfer.

Therefore SZ-CROSS-COLLAR-3 remains fixed.

## Next frontier

Next target:

SZ-KERNEL-EDGE-GERM-36 / DEFECT MATRIX ENUMERATION

The next pass should explicitly enumerate the finite atom types in the two geometric cases

A. 0<e<=k,
B. k<e<=k+h,

derive the associated constant boundary matrices B_j, and test their exact minors with the Weil weights.

The strategic target is a weight-level transversality lemma reusable at later thresholds, not another support-threshold proof.

Canonical theorem cursor remains SZ-CROSS-COLLAR-3.

No public promotion and no canonical cursor movement are asserted.
