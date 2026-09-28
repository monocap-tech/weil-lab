# SZ edge recurrence 64 — partial irrational rotation phase and full-cocycle threshold

Date: 2026-09-27
Branch: sz-cross-collar
Status: UNRATIFIED RESIDUE / NF PASS
Canonical parent: SZ-CROSS-COLLAR-3
Immediate residue: series-63
Public promotion: forbidden

## Objective

Continue beyond the one-scale multikappa closure of series-63.

Series-63 proves ambient four-delay prime-channel injectivity through

e <= lambda_ret,

where

kappa = k-5h,

lambda_ret = h-kappa = 6h-k.

It also identifies the second independent return

t <-> t+lambda_ret

once

e>lambda_ret.

The initial interpretation was that a genuine irrational cocycle begins immediately at that threshold.

That is too coarse.

The second return does become active there, but for

lambda_ret<e<h

its action on the fundamental kappa-residue circle is only partial. Every connected return component is still a finite path.

The genuinely infinite dense return orbit begins exactly at

e=h.

This pass proves that geometry exactly.

No new injectivity interval is claimed.

## 1. Constants

Retain

h=log(81/80),

k=log(16/15),

kappa=k-5h,

lambda_ret=h-kappa.

Series-63 proves

boxed:
4 kappa < lambda_ret < 5 kappa.

Define

boxed:
tau
=
lambda_ret-4kappa.

Then

boxed:
0<tau<kappa.

Also

boxed:
h=lambda_ret+kappa.

Numerically,

kappa
=
0.0024259211447856...,

lambda_ret
=
0.0099965988537715...,

tau
=
0.0002929142746290...,

h
=
0.0124225199985571....

The remaining chamber is

lambda_ret<e<=j,

j=log(9/8).

## 2. Exact domain of the new return

Series-63 derives

boxed:
t <-> t+lambda_ret

on

boxed:
0<t<e-lambda_ret.

Let

A_e
=
(0,e-lambda_ret).

This is the complete source interval from which the new return can originate at the lowest kappa level.

If

lambda_ret<e<h,

then

0<e-lambda_ret<kappa.

Thus A_e lies strictly inside one fundamental kappa cell.

Consequently no higher point

t+n kappa,
n>=1,

can itself belong to the new-return source interval.

Only the lowest representative of a kappa-residue class can initiate the lambda_ret-return.

## 3. Residue-circle action

Let

T_kappa
=
R/(kappa Z)

be the kappa-residue circle.

For

y in(0,kappa),

write the return target as

y+lambda_ret.

Since

lambda_ret
=
4kappa+tau,

the target has residue

boxed:
R_tau(y)
=
y+tau mod kappa.

More explicitly:

if

0<y<kappa-tau,

then

y+lambda_ret
=
(y+tau)+4kappa;

if

kappa-tau<y<kappa,

then

y+lambda_ret
=
(y+tau-kappa)+5kappa.

Thus the second return is an irrational circle rotation by tau, together with a level carry of four or five kappa steps.

## 4. Irrationality

In the prime-log basis

(log2,log3,log5),

series-61 gives

kappa=(24,-21,4).

Also

lambda_ret
=
h-kappa
=
(-28,25,-5).

Therefore

tau
=
lambda_ret-4kappa
=
(-124,109,-21).

Suppose

tau/kappa

were rational.

Then the two integer vectors

(-124,109,-21)

and

(24,-21,4)

would be rationally proportional.

The first coordinate would force one proportionality ratio, while the second gives a different one.

Therefore

boxed:
tau/kappa notin Q.

So

R_tau

is an irrational rotation of the kappa-circle.

## 5. Partial-return graph

For

lambda_ret<e<h,

define a graph on the residue circle by placing one undirected edge

boxed:
y <-> R_tau(y)

exactly when

boxed:
y in A_e=(0,e-lambda_ret).

The edge is undirected because the exact return path is reversible.

A vertex can have:

- one outgoing edge if y is in A_e;
- one incoming edge if R_tau^(-1)y is in A_e.

Hence every connected component has degree at most two.

Because R_tau has no periodic point, no component can be a finite cycle.

The only alternatives are:

- a finite path;
- a one-sided infinite path;
- a bi-infinite path.

## 6. Every component is finite for e<h

Take

lambda_ret<e<h.

Then A_e is a proper open subinterval of the residue circle.

Its complement contains a nonempty open interval.

Suppose one connected component were infinite.

Then, after choosing an orientation, it would contain an arbitrarily long orbit segment

y,
R_tau y,
R_tau^2 y,
...

whose internal vertices all belong to A_e.

A bi-infinite component would give an entire two-sided irrational rotation orbit contained in the closure of A_e.

But every irrational rotation orbit is dense in the whole circle.

That is impossible because the complement of A_e contains a nonempty open interval.

The same argument rules out one-sided infinite components.

Therefore

boxed:
every mixed-return component is a finite path
for
lambda_ret<e<h.

This is the partial mixed-return rotation registered in the terminology file.

## 7. Uniform finite path length for each fixed e<h

Fix one

e<h.

Let

B_e
=
T_kappa minus closure(A_e).

This contains a nonempty open interval.

Minimality of the irrational rotation implies that every residue orbit meets B_e.

Because the circle is compact, finitely many inverse images

B_e,
R_tau^(-1)B_e,
...,
R_tau^(-N)B_e

already cover the circle for some finite N=N(e).

Hence every forward orbit leaves A_e in at most N steps.

Applying the same statement to the inverse rotation gives a uniform backward bound.

Therefore:

boxed:
for each fixed e<h,
all connected partial-return paths have uniformly bounded finite length.

No bound uniform as

e up to h

is asserted.

Indeed the complement length is

h-e,

which tends to zero.

## 8. Why the finite template count explodes

Series-63 closes the chamber through

e=lambda_ret

with five one-scale kappa-chain templates.

Immediately above lambda_ret, one R_tau-link may join two such kappa-chain shells.

As e increases, a residue can remain inside the active interval A_e for more consecutive R_tau iterates.

Each such iterate appends another finite kappa-chain shell.

Therefore individual orbit matrices remain finite for every fixed

e<h,

but their possible dimensions are not bounded uniformly over the entire interval

lambda_ret<e<h.

This explains the direct orbit reconnaissance:

- just above lambda_ret, mixed orbits remain only modestly larger than the 372 template;
- closer to h, generic orbit sizes grow very rapidly;
- finite periodic kappa-template atomization becomes impractical even though every fixed-e component is still finite.

The difficulty is return-time growth, not yet an actually infinite component.

## 9. Exact threshold for an infinite irrational orbit

At

boxed:
e=h,

one has

e-lambda_ret
=
kappa.

Thus

A_e

fills the entire fundamental residue interval

(0,kappa)

up to endpoints.

Every generic residue therefore has its R_tau edge.

The return graph becomes the full irrational rotation graph.

Hence every generic component is

boxed:
{
R_tau^n y:
n in Z
},

which is infinite and dense in T_kappa.

Therefore

boxed:
e=h

is the exact full mixed-return cocycle threshold.

This sharpens the topology beyond the series-63 onset statement.

## 10. Above h

If

e>h,

then

e-lambda_ret>kappa.

In particular every lowest kappa-residue representative lies in the lambda_ret-return domain.

Therefore the full irrational rotation graph from Section 9 remains as a subgraph of the exact return geometry.

Additional higher-level lambda_ret returns may also become active.

Thus generic return components cannot become finite again.

The upper chamber

boxed:
h<=e<=j

must be treated as a genuine infinite irrational cocycle.

## 11. Corrected chamber architecture

The parity-recurrence frontier is now:

### A. Return-free

boxed:
0<e<=kappa.

Closed by series-62.

### B. Single-scale multikappa

boxed:
kappa<e<=lambda_ret.

Closed by series-63.

### C. Partial mixed-return rotation

boxed:
lambda_ret<e<h.

Every fixed-e component is finite, but the finite path lengths are not uniformly bounded as e approaches h.

No chamber-wide finite template library exists.

### D. Full irrational cocycle

boxed:
h<=e<=j.

Generic residue components are infinite and dense.

The coefficient-pattern threshold

e=p

still lies inside branch D because

p>h.

## 12. Consequence for the next proof architecture

The remaining chamber should not be attacked by one method.

The exact geometry suggests two separate targets.

### C1. Finite partial-rotation paths

For

lambda_ret<e<h,

derive a transfer/scattering map for one kappa-chain shell and one R_tau link.

Then prove nonresonance for an arbitrary finite concatenation.

A common invariant cone or uniform hyperbolicity statement would give a chamber-wide result without enumerating path lengths.

### D1. Full rotation cocycle

For

e>=h,

the same shell/link transfer becomes a matrix cocycle over the irrational rotation R_tau.

A positive proof would need:

- uniform hyperbolicity;
- a strict cone field;
- nonzero Lyapunov exponent incompatible with an L2 invariant section;
- or an equivalent spectral separation theorem.

The finite-path and infinite-cocycle problems should use the same local transfer matrices.

## 13. Reconnaissance on the shell transfer

Non-load-bearing Schur-complement reconnaissance on the already-certified parity orbit matrices indicates:

- the one-kappa shell reduces to an SL(2,R)-type hyperbolic transfer;
- the mixed R_tau link also reduces to an SL(2,R)-type hyperbolic scattering map;
- both parity signs appear related by diagonal sign conjugation;
- the numerically observed dominant projective directions are close.

Representative midpoint values give one kappa transfer with eigenvalue moduli approximately

boxed:
12.43
and
0.0804,

and one mixed-link transfer with eigenvalue moduli approximately

boxed:
15.58
and
0.0642.

These numbers are reconnaissance only.

They are not used in any theorem of this pass.

Their large separation suggests that a certified common-cone theorem is the natural next target.

## 14. Fixed-L status

This pass proves no new determinant or injectivity theorem.

Therefore the current load-bearing experimental ambient prime-channel range remains the series-63 interval

boxed:
0<L<=
log(
3^24/(2^24 5^5)
).

Equivalently,

boxed:
e<=lambda_ret.

On the regular kernel,

boxed:
K_c^{ps}=0

remains established through that same unratified residue range.

The canonical theorem cursor remains

boxed:
SZ-CROSS-COLLAR-3.

## Next frontier

Next target:

boxed:
SZ-KERNEL-EDGE-GERM-65 / MIXED-RETURN CONE TRANSFER.

The next pass should:

1. Schur-eliminate one generic kappa-chain shell to an exact 2-by-2 transfer;
2. Schur-eliminate one lambda_ret-link to its exact 2-by-2 scattering map;
3. certify both matrices by outward interval arithmetic from the existing logarithmic-ratio bounds;
4. seek one common invariant projective cone for both parity signs;
5. prove uniform expansion on that cone;
6. use it first to close all finite partial-rotation paths
   lambda_ret<e<h;
7. then test whether the same expansion excludes an L2 invariant section at
   e>=h.

A successful cone theorem could close both remaining return phases without any further orbit enumeration.

No public promotion and no canonical cursor movement are asserted.

## Pre-GERM-65 refold — additive handoff update, 2026-09-27

Before executing the next frontier above, read
[SZ kernel edge — pre-GERM-65 refold and integrated handoff](SZ_KERNEL_EDGE_PRE65_REFOLD_20260927.md).

That record pins the parallel return-cocycle work through RETURN-COCYCLE-5 and the screw-family regroup audit, reconciles them with series-63/64, and specifies the remaining source-state, shell/link, cone, endpoint, and L2 obligations. It supersedes stale imported status and routing statements, not the mathematical content of this historical pass.

The five-template series-63 coverage is retained. The existing lab assemblers are located; the fresh parallel 124/186 source reconstructions are additional scoped inputs, not a reason to repeat an unrelated finite-layer traversal. Bulk Chebyshev compression is not a substitute for deriving the actual return maps.

This addition is a refold only. GERM-64 remains the last completed experimental mathematical pass; GERM-65 has not been executed by this operation. The canonical theorem cursor remains SZ-CROSS-COLLAR-3. No new determinant, interval, ratification, or public promotion is asserted.
