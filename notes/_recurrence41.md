# SZ edge recurrence 41 — terminal-gate exclusion and three-sheet closure

Date: 2026-09-27
Branch: sz-cross-collar
Status: UNRATIFIED RESIDUE / NF PASS
Canonical parent: SZ-CROSS-COLLAR-3
Immediate residue: series-40
Public promotion: forbidden

## Objective

Close the gated-endpoint question from series-40 and audit whether the one-excursion scattering library is globally complete.

The result has two parts:

1. the terminal k-gate is actually absent throughout the four-delay post-p chamber, so every true terminal endpoint is gate-free;
2. the one-excursion library from series 38-40 is not globally exhaustive, because the forward k-gate may fire twice on distinct h-steps.

The correct globally complete bookkeeping uses three k-sheets, not two.

No new global fixed-L injectivity interval is claimed in this pass.

## 1. Terminal gate exclusion

Recall

h = log(81/80),

k = log(16/15),

u = L-log5,

alpha = u-k.

The old terminal strip from series-34 is

u-h < x < p.

The translated terminal term would be active only if

x < alpha = u-k.

But

k > h,

because

16/15 > 81/80.

Therefore

u-h > u-k = alpha.

Hence every x in the terminal strip satisfies

x > alpha.

So the terminal gate indicator is identically zero.

Therefore the exact terminal relation throughout the four-delay post-p chamber is always

S(x) = R^(-1) X(x).

The gated endpoint row registered in series-40 is a formally valid algebraic row, but it is not operationally realized in this chamber.

This removes the endpoint obstruction identified at the end of series-40.

## 2. Endpoint graph closure is always gate-free

The physical endpoint subspaces are therefore exactly

L_in = span((1,R)^T),

L_out = span((1,R^(-1))^T).

There is no post-p four-delay chamber in which the terminal endpoint requires an additional S(x+k) coordinate.

Thus every actual endpoint-connected component must close against the gate-free graph line L_out.

## 3. Broad one-shear endpoint audit

Let

B4 = diag(M0,M0),

and let E_plus,E_minus be the unmatched shears from series-39.

For every orientation sigma in {+,-} and every pair

a,b >= 0,

a+b <= 15,

test the true endpoint-line closure matrix

C_end(B4^a E_sigma B4^b)
=
L_out^(2)
B4^a E_sigma B4^b
J_in^(2),

where J_in^(2) injects both incoming endpoint lines and L_out^(2) tests both outgoing endpoint lines.

There are 136 index pairs and two orientations, hence 272 matrices.

Using the certified rational logarithmic enclosures from series 38-40 and outward interval matrix arithmetic, all 272 determinant intervals exclude zero.

The smallest certified absolute margin is

|det C_end| > 0.4257.

Thus no one-shear endpoint path can resonate.

## 4. Broad opposite-orientation two-shear endpoint audit

Now consider both orientations

B4^a E_minus B4^b E_plus B4^c,

B4^a E_plus B4^b E_minus B4^c,

with

a,b,c >= 0,

a+b+c <= 15.

There are

C(18,3)=816

bulk triples per orientation, hence 1632 endpoint closure matrices.

All 1632 outward determinant intervals exclude zero.

The closest cases are

orientation + -,
(a,b,c)=(0,0,1)

and

orientation + -,
(a,b,c)=(1,0,0),

with

0.009049430466
<
det C_end
<
0.009049430469.

Hence

|det C_end| > 0.00904

through this complete opposite-orientation two-shear audit family.

## 5. Same-orientation two-shear endpoint audit

Because global forward-gate repetition is possible, also audit

B4^a E_plus B4^b E_plus B4^c

and

B4^a E_minus B4^b E_minus B4^c

over the same bulk simplex.

All 1632 determinant intervals exclude zero.

The smallest certified absolute margin is

|det C_end| > 1.089.

Therefore two repeated same-orientation shear events do not create an endpoint-line resonance either.

These audits are intentionally broader than the physically realized word set.

## 6. Why one-excursion completeness fails

The earlier one-excursion interpretation used the defect bound

e <= k+h.

That correctly limits k-feedback inside the moving defect.

It does not imply that the forward k-gate fires only once globally.

The forward gate in the exact transfer is active for

x < alpha.

Across the chamber,

alpha = u-k.

Since

u <= log(6/5),

one has

alpha <= log(6/5)-log(16/15)
      = log(9/8)
      = j.

Now

j < 2k,

because

9/8 < (16/15)^2

is equivalent to

2025 < 2048.

Therefore a forward k-chain may have the form

x
-> x+k
-> x+2k,

but no third forward jump can remain inside the active forward-gate region.

So the correct global k-depth is two, not one.

## 7. Three-sheet head bound

The total head width satisfies

u <= log(6/5).

Also

log(6/5) < 3 log(16/15),

because

6/5 < (16/15)^3.

Hence

u < 3k.

Therefore every head point lies in one of at most three k-cells:

I0 = (0,k),

I1 = (k,2k),

I2 = (2k,u).

The third interval is omitted when 2k>=u.

This gives the globally complete three-sheet boundary state registered in the terminology file.

Each sheet carries the two-component bulk state V=(X,S), so the global fiber count is at most six scalar L2 components.

## 8. Nature of the three-sheet transfer

The three-sheet state is finite at the L2-fiber level, but it is not one constant pointwise 6-by-6 matrix.

The reason is the backward tap

X(x-(k-h)).

It shifts the base coordinate by k-h rather than simply changing a k-sheet at fixed coordinate.

Thus the correct global object is a finite matrix over truncated translations acting on the three-sheet Hilbert direct sum.

All k-shifts move only between adjacent sheets.

All h-propagation has bounded length because

u/h < 15.

Hence the apparent irrational h/k lattice is still operationally finite for fixed L.

But the atomization must include all three sheets and all admissible h-preimages of the sheet boundaries.

## 9. Scope correction to series 35-40

The following earlier results remain valid as stated for the subfamilies they actually analyze:

- local atom invertibility from series-36;
- pure-bulk nonresonance from series-37;
- matched one-excursion nonresonance from series-38;
- separated one-excursion nonresonance from series-39;
- gate-free endpoint graph nonresonance from series-40.

The following global completeness claims require correction:

- the two-sheet state is not globally complete;
- the claim that there is at most one k-excursion globally is not established;
- the cycle-rank-at-most-two statement from series-37 is therefore not load-bearing as a global graph theorem;
- the gated terminal endpoint from series-40 never occurs in the four-delay post-p chamber.

The corrected global statement is:

the post-p chamber closes on at most three k-sheets with finite h-depth.

## 10. Fixed-L injectivity status

This pass does not yet enumerate every three-sheet atom pattern.

Therefore no new full fixed-L injectivity theorem is claimed for the post-log(16/3) region.

The load-bearing continuous positive range remains

0 < L <= log(16/3).

Separately, the one- and two-shear endpoint families now have explicit nonresonance margins, but this is not yet a completeness theorem.

## 11. Quantitative status

Certified fixed-scale endpoint margins obtained or retained in this chain include:

pure bulk endpoint closure:
absolute determinant > 0.4968;

zero-bulk unmatched endpoint closure:
determinant > 15/196;

matched gate-free endpoint closure:
absolute determinant > 0.04245;

one-shear endpoint family:
absolute determinant > 0.4257;

opposite two-shear endpoint family:
absolute determinant > 0.00904;

same-orientation two-shear endpoint family:
absolute determinant > 1.089.

These margins are fixed-scale arithmetic-delay statements only.

No shrinking-collar estimate follows.

## 12. Strategic consequence

The prime-channel mechanism remains finite and reusable.

The state enlargement sequence is now clear:

one-sheet scalar recurrence
->
two-component bulk state
->
two-sheet one-excursion state
->
globally complete three-sheet finite-translation state.

Later arithmetic thresholds should be handled by enlarging the finite sheet state when the support width crosses another multiple of the new delay, not by restarting the source equation.

## Next frontier

Next target:

SZ-KERNEL-EDGE-GERM-42 / THREE-SHEET ATOMIZATION

The next pass should:

1. partition the three k-cells by the exact forward/backward gate thresholds and their h-preimages;
2. derive the finite constant atom matrices on every resulting interval;
3. identify the actual finite graph and its true cycle rank;
4. test whether the existing one/two-shear audits already cover all graph words;
5. otherwise enumerate the genuinely new three-sheet words.

The target is a globally complete fixed-L transfer theorem for the four-delay chamber.

Canonical theorem cursor remains SZ-CROSS-COLLAR-3.

No public promotion and no canonical cursor movement are asserted.
